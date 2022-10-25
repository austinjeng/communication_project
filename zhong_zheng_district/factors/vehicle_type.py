from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager

matplotlib.rcParams['font.family'] = ['Heiti TC']


def draw_pie_chart(dict: dict):
    x = dict.values()
    l = dict.keys()
    new_l = [f'{k}({v})' for k, v in dict.items()]
    plt.pie(x, labels=new_l, radius=0.8, autopct='%.1f%%',
            pctdistance=0.7, labeldistance=1.5)
    plt.legend(loc='upper left')
    plt.show()


def get_vehicle_type_count(fileLocation: str):
    data = pd.read_csv(fileLocation)
    l = data['車種'].tolist()
    c = Counter(l)
    c = dict(c)

    car = ['B01', 'B02', 'B03']
    bike = ['C01', 'C02', 'C03', 'C04', 'C05']

    dict1 = {k: v for k, v in c.items() if k in car or k in bike}
    b_sum = int(0)
    c_sum = int(0)
    for k, v in dict1.items():
        if ('B' in k):
            b_sum += v
        if ('C' in k):
            c_sum += v

    dict_final = {'小客車': b_sum, '機車': c_sum}

    return dict_final


if __name__ == '__main__':
    draw_pie_chart(get_vehicle_type_count(
        'zhong_zheng_district/zz_106_to_110.csv'))

'''
B01 B02 B03 -> 小客車
C01 C02 C03 C04 C05 -> 機車
'''
