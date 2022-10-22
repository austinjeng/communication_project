import pandas as pd
import matplotlib.font_manager
import matplotlib.pyplot as plt
import numpy as np


matplotlib.rcParams['font.family'] = ['Heiti TC']


def get_age_interval_count(fileLocation):
    data = pd.read_csv(fileLocation)

    age_data = data['年齡']
    age_data_cleansed = age_data[~age_data.isnull()]

    counts, bins = np.histogram(age_data_cleansed, bins=8, range=(20, 100))
    return counts


def draw_age_bar_plot(counts: list):
    x = np.arange(1, 9)
    label_1 = [x for x in np.arange(20, 100, 10)]
    label_2 = [x for x in np.arange(30, 110, 10)]

    tick_label = [f'{x}~{y}歲' for x, y in zip(label_1, label_2)]
    plt.bar(x, counts, tick_label=tick_label)
    plt.xlabel("年齡層分佈區間")
    plt.ylabel('人數')
    plt.show()


draw_age_bar_plot(get_age_interval_count(
    'zhong_zheng_district/zz_106_to_110.csv'))
