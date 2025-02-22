import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

# スクリプトのディレクトリ
script_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(script_dir, "企業フォルダ")

# Excelファイルのパス
excel_path = os.path.join(script_dir, "転職活動.xlsx")

# Excelを読み込む
xls = pd.ExcelFile(excel_path)
df = xls.parse("2025")  # 2025年の転職活動データ
urls = df[["企業名", "職種名", "リンク"]].dropna().values.tolist()  # 企業名、職種、URLのリスト

# スクレイピングして募集要項を取得
for company, job_title, url in urls:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生

        # 文字化け対策（ページのエンコーディングを自動検出）
        response.encoding = response.apparent_encoding

        # HTMLを解析
        soup = BeautifulSoup(response.text, "html.parser")

        # Talentio系の対応（ページ内のjob descriptionがどこにあるか試す）
        if "talentio.com" in url:
            job_description_section = soup.find("div", class_="job_description")  # クラス名は仮
            job_description = job_description_section.get_text("\n", strip=True) if job_description_section else "募集要項が見つかりません"
        else:
            # 他のページはページ全体のテキストを取得
            job_description = soup.get_text("\n", strip=True)

        # 企業フォルダのパス
        company_path = os.path.join(base_path, company)
        os.makedirs(company_path, exist_ok=True)

        # ファイルに職種ごとに追加保存
        job_desc_path = os.path.join(company_path, "募集要項.txt")
        with open(job_desc_path, "a", encoding="utf-8") as f:
            f.write(f"職種: {job_title}\n")
            f.write(f"URL: {url}\n")
            f.write("=" * 50 + "\n")
            f.write(job_description + "\n\n")

        print(f"✅ {company} - {job_title} の募集要項を保存しました！")

    except requests.RequestException as e:
        print(f"❌ {company} - {job_title} のスクレイピングに失敗: {e}")

print("🎯 すべての企業の募集要項取得が完了しました。")