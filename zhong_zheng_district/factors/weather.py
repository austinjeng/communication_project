from tracemalloc import start
import pandas as pd
import matplotlib.font_manager
from collections import Counter
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = ['Heiti TC']

weather_dict = {"1.0": "暴雨", "2.0": '強風', '3.0': '風沙',
                '4.0': '霧或煙', '5.0': '雪', '6.0': '雨', '7.0': '陰', '8.0': '晴'}


def getWeatherCount(file_location):
    df = pd.read_csv(file_location)
    weather_list = df['天候'].tolist()
    index = 0
    for i in weather_list:
        weather_list[index] = weather_dict.get(str(i))
        index += 1
    c = Counter(weather_list)
    c = dict(c)
    print(c)

    return c


def draw_pie_chart(dict: dict):
    x = dict.values()
    l = dict.keys()
    new_l = [f'{k}({v})' for k, v in dict.items()]
    plt.pie(x, labels=new_l, radius=0.8, autopct='%.1f%%',
            pctdistance=0.7, labeldistance=1.2, startangle=27)
    plt.legend(loc='upper left')
    plt.show()


def cleanse(dict: dict):
    sum = 0
    for i in dict.values():
        sum += i

    cleansed_dict = {k: v for k, v in dict.items() if v > sum/500}
    return cleansed_dict


def f(file_location):
    draw_pie_chart(cleanse(getWeatherCount(file_location)))


f("zhong_zheng_district/zz_106_to_110.csv")
