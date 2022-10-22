import pandas as pd

df = pd.read_csv('taipei_A1_A2_accidents/106.csv')

df2 = df[df['區序'].str.contains('中正')]
df2.to_csv('output.csv')
print(df2)