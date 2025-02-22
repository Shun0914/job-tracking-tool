import os
import pandas as pd

# 現在のスクリプトのディレクトリ（extract.py がある場所）
script_dir = os.path.dirname(os.path.abspath(__file__))

# 企業フォルダの保存先（転職/企業フォルダ/）
base_path = os.path.join(script_dir, "企業フォルダ")
os.makedirs(base_path, exist_ok=True)  # 企業フォルダを作成

# Excelファイルのパス
excel_path = os.path.join(script_dir, "転職活動.xlsx")

# Excelを読み込む
xls = pd.ExcelFile(excel_path)
company_list = xls.parse("企業リスト")["企業名"].dropna().tolist()

# 企業ごとのフォルダとファイルを作成
for company in company_list:
    company_path = os.path.join(base_path, company)
    os.makedirs(company_path, exist_ok=True)  # 企業フォルダ作成
    
    # ファイルのパス
    docx_path = os.path.join(company_path, f"職務経歴書_{company}.docx")
    pages_path = os.path.join(company_path, f"履歴書_{company}.pages")
    txt_path = os.path.join(company_path, "募集要項.txt")

    # 空のファイルを作成
    for path in [docx_path, pages_path, txt_path]:
        with open(path, 'w') as f:
            pass

print(f"企業フォルダを {base_path} に作成しました。")
