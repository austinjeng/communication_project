import pandas
df = pandas.read_csv('110_A1_traffic_accident.csv')
print(type(df['發生地點']))
print(df['發生地點'].str.contains('台北市', regex=False))

df2 = df[df['發生地點'].str.contains('臺北市', regex=False)]
df2.to_csv('output.csv')