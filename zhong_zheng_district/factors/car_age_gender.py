from collections import Counter
import pandas as pd

# 匯入所有“汽車”事故，分離出男女性別車禍次數，匯出兩個CSV

# 資料內性別欄位有[1,2]以外的需要清理 『 3 無或物(動物、堆置物)4 肇事逃逸尚未查獲 』


def cleanse_gender(file_location: str):
    df = pd.read_csv(file_location)

    df = df[(df.性別 == 1) | (df.性別 == 2)]
    df.to_csv(file_location, index=False, index_label=False)


def seperate_gender(file_location: str):
    data = pd.read_csv(file_location)
    check = [1, 2]

    for i in range(len(data['性別'])):
        if data['性別'][i] != 1 and data['性別'][i] != 2:
            print(data['性別'][i])

    male_data = data[data['性別'] == int(1)]
    female_data = data[data['性別'] == int(2)]
    male_data.to_csv('male_car_accidents.csv', index=False, index_label=False)
    female_data.to_csv('female_car_accidents.csv',
                       index=False, index_label=False)

    # 表格大小確認
    data_size = data.shape
    male_data_size = male_data.shape
    female_data_size = female_data.shape
    print(data_size, male_data_size, female_data_size)

    if (male_data_size[0] + female_data_size[0] != data_size[0]):
        print("Numbers dont match!")
    return


def get_all_cars(fileLocation: str):
    data = pd.read_csv(fileLocation)
    car = ['B01', 'B02', 'B03']

    data = data[data['車種'].isin(car)]
    # data['車種'] = "---" + data['車種'].astype(str) + "---"
    print('function "get_all_cars" succesfully finished!')
    return data


def get_age_distribution(file_location: str):
    df = pd.read_csv(file_location)

    age_distribution = {"18-29": 0, "30-39": 0, '40-49': 0,
                        '50-59': 0, '60-69': 0, '70-79': 0, '80UP': 0}


def main():
    # output = get_all_cars(
    #     'taipei_A1_A2_accidents/taipei_101_to_108.csv')
    # output.to_csv('vehicle_is_car.csv', index=False, index_label=False)
    # cleanse_gender('vehicle_is_car.csv')
    seperate_gender('vehicle_is_car.csv')
    pass


if __name__ == "__main__":
    main()
