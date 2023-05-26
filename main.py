import pandas as pd

input = "input.xlsx"

df_dic = pd.read_excel(input, sheet_name=None)

for sheet in df_dic:
    df_dic[sheet].to_excel(f"{sheet}.xlsx", index=False)