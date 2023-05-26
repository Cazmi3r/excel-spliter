import pandas as pd

input = "input.xlsx"

df_dic = pd.read_excel(input, sheet_name=None)

for sheet in df_dic:
    df = df_dic[sheet]
    
    # removes the last row. pandas was adding a sum as the last row
    df.drop(df.tail(1).index,inplace=True)
    df.to_excel(f"{sheet}.xlsx", index=False)
    