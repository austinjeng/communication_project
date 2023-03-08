import pandas as pd

# df110 = pd.read_csv('zhong_zheng_district/zz_110.csv')
# df109 = pd.read_csv('taipei_A1_A2_accidents/109.csv')
df108 = pd.read_csv('taipei_A1_A2_accidents/108.csv')
df107 = pd.read_csv('taipei_A1_A2_accidents/107.csv')
df106 = pd.read_csv('taipei_A1_A2_accidents/106.csv')
df105 = pd.read_csv('taipei_A1_A2_accidents/105.csv')
df104 = pd.read_csv('taipei_A1_A2_accidents/104.csv')
df103 = pd.read_csv('taipei_A1_A2_accidents/103.csv')
df102 = pd.read_csv('taipei_A1_A2_accidents/102.csv')
df101 = pd.read_csv('taipei_A1_A2_accidents/101.csv')

df_all = df108.append(df107).append(df106).append(
    df105).append(df104).append(df103).append(df102).append(df101)

df_all.to_csv('taipei_A1_A2_accidents/taipei_101_to_108.csv',
              index_label=False, index=False)
