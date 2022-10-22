import pandas as pd
import matplotlib.font_manager
import matplotlib.pyplot as plt
import numpy as np
from glob import glob


matplotlib.rcParams['font.family'] = ['Heiti TC']

road_dict = {'guiyang': '貴陽街1段', 'zhonghua': '中華路1段', 'bo_ai': '博愛路', 'yanping_south': '延平南路',
             'aiguo_west': '愛國西路', 'taoyuan': '桃源街', 'baoqing': '寶慶路', 'hengyang': '衡陽路',
             'chongqing_south': '重慶南路1段'}


# retun a list of fileName ending with csv
datas = glob('zhong_zheng_district/roads/*.csv')


# return a dictionary with accident count on each road in road_dict
def get_accident_count(l: list):
    data_dict = dict()

    count = 0
    road_name = 'N/A'
    for csv_file in datas:
        # shape is a tuple indicating the rows and columns
        total_accident = pd.read_csv(datas[count]).shape[0]
        for k, v in road_dict.items():
            if k in csv_file:
                road_name = v
                break
        data_dict.update({str(road_name): int(total_accident)})
        count += 1

    return data_dict


def draw_road_bar_plot(d: dict):
    x = np.arange(1, len(d) + 1)

    # he code is sorting each item by the second item in the tuple, whereas normally it would initially sort
    # by the first item in the tuple, then break ties with the second item.
    d = dict(sorted(d.items(), key=lambda item: item[1]))

    tick_label = [k for k, v in d.items()]
    height = [v for k, v in d.items()]
    plt.bar(x, height)
    plt.xticks(np.arange(1, len(d) + 1), tick_label)
    plt.tick_params(axis='x', labelsize=7)
    plt.xlabel("路名")
    plt.ylabel('事故數量')
    plt.show()


draw_road_bar_plot(get_accident_count(datas))
