# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('taipei_A1_A2_accidents/taipei_106_to_110.csv')

df.to_excel('output1.xlsx', index=False, index_label=False)
