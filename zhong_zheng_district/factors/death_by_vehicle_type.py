from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager

matplotlib.rcParams['font.family'] = ['Heiti TC']


def get_death_count_by_vehicle_type():
    data = pd.read_csv('taipei_A1_A2_accidents/taipei_106_to_110.csv')
    d = data[(data['受傷程度'] == 1.0) | (data['受傷程度'] == 5.0)]
    #print(d[['車種', '受傷程度']])
    # print(d.shape)

    d.to_csv('temp.csv', index=False, index_label=False)


def get_vehicle_type_count(fileLocation: str):
    data = pd.read_csv(fileLocation)

    car_identifier = ['B01', 'B02', 'B03']
    bike_identifier = ['C01', 'C02', 'C03', 'C04', 'C05']

    data = data[['受傷程度', '車種']]
    cars = data[data['車種'].isin(car_identifier)]
    bikes = data[data['車種'].isin(bike_identifier)]
    cars_A1 = cars[cars['受傷程度'] == 1.0]
    cars_A2 = cars[cars['受傷程度'] == 5.0]
    bikes_A1 = bikes[bikes['受傷程度'] == 1.0]
    bikes_A2 = bikes[bikes['受傷程度'] == 5.0]
    print(f'''carA1 count is {cars_A1.shape[0]}\n
        carA2 count is {cars_A2.shape[0]}\n
        bikeA1 count is {bikes_A1.shape[0]}
        bikeA2 count is {bikes_A2.shape[0]}''')
    return [cars_A1.shape[0], cars_A2.shape[0], bikes_A1.shape[0], bikes_A2.shape[0]]


def draw_stack_bar_chart(l: list):
    labels = ['汽車', '機車']
    car = [l[0], l[2]]
    bike = [l[1], l[3]]
    width = 0.7       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, car, width, label='A1')
    ax.bar(labels, bike, width, bottom=car, label='A2')

    ax.set_ylabel('事件數量')
    ax.set_title('台北市106-110年汽機車A1/A2事故數量')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    draw_stack_bar_chart(get_vehicle_type_count(
        'taipei_A1_A2_accidents/taipei_106_to_110.csv'))


'''
B01 B02 B03 -> 小客車
C01 C02 C03 C04 C05 -> 機車
'''
