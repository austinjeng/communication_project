
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd

matplotlib.rcParams['font.family'] = ['Heiti TC']

data = pd.read_csv('metadata/taipei_vehicle_total.csv')

car_data = data[['年底別', '汽車/小客車計']]
bike_data = data[['年底別', '機車/合計']]

# When using loc/iloc, the part before the comma is the rows you want,
# and the part after the comma is the columns you want to select.
car_count = car_data.loc[car_data['年底別'] == '110年', '汽車/小客車計'].tolist()
bike_count = bike_data.loc[bike_data['年底別'] == '110年', '機車/合計'].tolist()


def draw_pie_chart():
    x = [car_count[0], bike_count[0]]
    l = [f'汽車/小客車計({car_count[0]})', f'機車/合計({bike_count[0]})']
    plt.pie(x, labels=l, radius=0.8, autopct='%.1f%%',
            pctdistance=0.7, labeldistance=1.2, startangle=27)
    plt.legend()
    plt.show()


draw_pie_chart()
