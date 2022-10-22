import pandas as pd

df110 = pd.read_csv('zhong_zheng_district/zz_110.csv')
df109 = pd.read_csv('taipei_A1_A2_accidents/109.csv')
df108 = pd.read_csv('taipei_A1_A2_accidents/108.csv')
df107 = pd.read_csv('taipei_A1_A2_accidents/107.csv')
df106 = pd.read_csv('taipei_A1_A2_accidents/106.csv')

df_all = df110.append(df109).append(df108).append(df107).append(df106)

df_all.to_csv('taipei_A1_A2_accidents/taipei_106_to_110.csv',
              index_label=False, index=False)
