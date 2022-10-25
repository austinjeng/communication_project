import pandas as pd
import matplotlib.font_manager
from collections import Counter
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = ['Heiti TC']


def get_gender_count(file_location: str):
    df = pd.read_csv(file_location)
    weather_list = (df['性別']).tolist()

    c = Counter(weather_list)
    counter_dict = dict(c)

    parsed_dict = {k: v for k, v in counter_dict.items() if k in [
        1, 2]}  # 1是男性 2是女性

    parsed_dict['男性'] = parsed_dict.pop(1)
    parsed_dict['女性'] = parsed_dict.pop(2)

    return parsed_dict


def draw_pie_chart(dict: dict):
    x = dict.values()
    l = dict.keys()
    new_l = [f'{k}({v})' for k, v in dict.items()]
    plt.pie(x, labels=new_l, radius=0.8, autopct='%.1f%%',
            pctdistance=0.7, labeldistance=1.5)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    draw_pie_chart(get_gender_count('zhong_zheng_district/zz_106_to_110.csv'))
