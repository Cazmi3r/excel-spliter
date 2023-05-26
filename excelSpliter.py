import pandas as pd

def excel_split(input_path, output_path):
    df_dic = pd.read_excel(input_path, sheet_name=None)
    for sheet in df_dic:
        file_name = output_path / f"{sheet}.xlsx"
        df_dic[sheet].to_excel(file_name, index=False)