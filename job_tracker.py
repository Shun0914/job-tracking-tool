# Streamlitアプリにブロックフィルタリング機能を追加し、分析機能を強化
import streamlit as st
import pandas as pd

# 修正後のExcelファイルのパスを更新（"転職活動_最終版.xlsx" を使用）
final_file_path = "転職活動_最終版.xlsx"

# 最新のデータを読み込む
df_final = pd.read_excel(final_file_path, sheet_name="2025")

# 必要なカラムを選択
columns_to_keep = ["企業名", "ジャンル", "職種名", "業界", "応募日", "ステータス", "ブロック"]
df_final = df_final[columns_to_keep]

# ブロックごとのフィルタリング機能を追加
st.title("📊 転職活動 進捗管理")

# ブロックフィルター（選択式）
selected_block = st.selectbox("📌 表示するブロックを選択", sorted(df_final["ブロック"].unique()))
filtered_df = df_final[df_final["ブロック"] == selected_block]

# 応募企業リスト（選択したブロックのみ表示）
st.subheader(f"📝 ブロック {selected_block} の応募企業リスト")
edited_df = st.data_editor(filtered_df, key="editable_table")

# データを保存するボタン
if st.button("💾 データを保存"):
    try:
        with pd.ExcelWriter(final_file_path, engine='xlsxwriter') as writer:
            df_final.to_excel(writer, sheet_name="2025", index=False)
        st.success("✅ データを保存しました！")
    except Exception as e:
        st.error(f"❌ データの保存に失敗しました: {e}")

# 応募結果の詳細分析（職種ごと・業界ごと・ブロックごと）
st.subheader("📈 応募状況の分析")

# ブロックごとの応募数
st.bar_chart(df_final["ブロック"].value_counts())

# 職種ごとの応募数
st.bar_chart(df_final["ジャンル"].value_counts())

# 業界ごとの応募数
st.bar_chart(df_final["業界"].value_counts())

# 書類通過率の分析（業界別・職種別）
if "ステータス" in df_final.columns:
    success_df = df_final.copy()
    success_df["書類通過フラグ"] = success_df["ステータス"].apply(lambda x: 1 if x in ["書類通過", "一次面接", "二次面接", "最終面接", "内定"] else 0)

    # 業界ごとに集計
    industry_stats = success_df.groupby("業界").agg(
        応募数=("企業名", "count"),
        書類通過数=("書類通過フラグ", "sum")
    )
    industry_stats["通過率 (%)"] = (industry_stats["書類通過数"] / industry_stats["応募数"]) * 100
    st.subheader("📊 業界別 書類通過率")
    st.bar_chart(industry_stats["通過率 (%)"])

    # 職種ごとに集計
    role_stats = success_df.groupby("ジャンル").agg(
        応募数=("企業名", "count"),
        書類通過数=("書類通過フラグ", "sum")
    )
    role_stats["通過率 (%)"] = (role_stats["書類通過数"] / role_stats["応募数"]) * 100
    st.subheader("📊 職種別 書類通過率")
    st.bar_chart(role_stats["通過率 (%)"])

# ブロックごとの通過率
block_stats = success_df.groupby("ブロック").agg(
    応募数=("企業名", "count"),
    書類通過数=("書類通過フラグ", "sum")
)
block_stats["通過率 (%)"] = (block_stats["書類通過数"] / block_stats["応募数"]) * 100

st.subheader("📊 ブロック別 書類通過率")
st.bar_chart(block_stats["通過率 (%)"])

# Streamlitアプリの修正完了！