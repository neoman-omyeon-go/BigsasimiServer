import pandas as pd
import os


def search_list(ctx:str):
    df = pd.read_csv('./etcetera/food.csv')
    data = df[df['식품명'].str.contains(ctx)]
    top10 = data.head(10)
    selected_columns = ['식품명', '에너지', '단백질', '지방', '탄수화물', '나트륨']
    selected_data = top10[selected_columns]
    dict_list = selected_data.to_dict(orient='records')
    return dict_list
