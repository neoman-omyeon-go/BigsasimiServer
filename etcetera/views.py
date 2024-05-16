from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
import os

from utils.apihelper import FJR


def search_list(ctx:str) -> list:
    # print(os.getcwd())
    df = pd.read_csv('./etcetera/food.csv')
    data = df[df['식품명'].str.contains(ctx)]
    top10 = data.head(10)
    selected_columns = ['식품명', '에너지', '단백질', '지방', '탄수화물', '나트륨', '콜레스테롤', '총당류']
    selected_data = top10[selected_columns]
    dict_list = selected_data.to_dict(orient='records')
    return dict_list


class SearchList(APIView):
    def get(self, request):
        item = request.GET.get("item",None)
        if item:
            result = dict()
            a = search_list(item)
            result["len"] = a.__len__()
            result["items"] = a

            return FJR(msg="succeed get item", data=result)
        else:
            return FJR(error="error", msg="wrong item keyword", status=status.HTTP_400_BAD_REQUEST)
