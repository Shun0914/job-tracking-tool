🚀 転職活動管理 & 最適化ツール

このプロジェクトは、転職活動を データドリブンで管理 & 最適化 するためのツールです。
Python & Streamlit を活用し、企業リスト管理・レジュメ作成・スクレイピング・進捗分析を効率化します。

📌 主な機能

✅ 応募企業の管理 & 転職進捗トラッキング (job_tracker.py)
✅ 企業ごとの職務経歴書を自動生成 & 整理 (resume.py)
✅ フォルダ自動作成 & データ整理 (extract.py)
✅ Webスクレイピングで募集要項を自動取得 (job_description.py)
✅ 企業リストの要約 & 分析 (summary.py)

📂 プロジェクト構成

job-tracking-tool/
│── README.md               # この説明書
│── requirement.txt        # 必要なライブラリ一覧
│── job_tracker.py        # 転職管理アプリ（Streamlit）
│── job_description.py   # スクレイピングで募集要項を取得
│── resume.py            # 企業ごとに職務経歴書をコピー
│── extract.py           # 企業フォルダを自動作成
│── summary.py           # 企業リストの要約 & 分析
│── company/             # データフォルダ（企業リスト & レジュメ保存）
│   ├── sample_jobs.xlsx  # サンプル企業リスト（個人情報なし）

🚀 セットアップ方法

🔹 1. 必要なライブラリをインストール

pip install -r requirement.txt

🔹 2. 転職管理アプリを実行（Streamlit）

streamlit run job_tracker.py

🔹 3. Webスクレイピングで募集要項を取得

python job_description.py

🔹 4. 企業ごとの職務経歴書を整理

python resume.py

🔹 5. 企業リストを要約 & 分析

python summary.py

📊 期待できる効果

✅ 無駄な応募を減らし、より通過率の高い企業を狙える！
✅ データを活用して、転職活動を戦略的に進められる！
✅ 面接の傾向分析や意思決定の最適化ができる！

🔥 このツールを使って、効率的に転職活動を進めましょう！ 🚀
