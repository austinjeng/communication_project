from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np

matplotlib.rcParams['font.family'] = ['Heiti TC']


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


def draw_road_bar_plot(l: list):
    x = np.array(1, len(l) + 1)
    # plt.bar(x, height)
    # plt.xticks(np.arange(1, len(d) + 1), tick_label)
    # plt.tick_params(axis='x', labelsize=7)
    # plt.xlabel("路名")
    # plt.ylabel('事故數量')
    # plt.show()


def main():
    data = pd.read_csv('metadata/taipei_vehicle_total.csv')

    car_data = data[['年底別', '汽車/小客車計']]
    bike_data = data[['年底別', '機車/合計']]

    # When using loc/iloc, the part before the comma is the rows you want,
    # and the part after the comma is the columns you want to select.
    taipie_car_count = car_data.loc[car_data['年底別']
                                    == '110年', '汽車/小客車計'].tolist()[0]
    taipei_bike_count = bike_data.loc[bike_data['年底別']
                                      == '110年', '機車/合計'].tolist()[0]

    zz_car_and_bike_dict = get_vehicle_type_count(
        'zhong_zheng_district/zz_106_to_110.csv')
    zz_car_count = zz_car_and_bike_dict['小客車']
    zz_bike_count = zz_car_and_bike_dict['機車']


if __name__ == '__main__':
    main()

'''
B01 B02 B03 -> 小客車
C01 C02 C03 C04 C05 -> 機車
'''
