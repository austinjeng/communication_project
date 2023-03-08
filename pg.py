import pandas as pd

data = pd.read_csv('temp.csv', encoding='UTF-8')
# data.reset_index(inplace=True)
# data.to_csv('temp.csv', index=False, index_label=False)
data.drop(data.index[64]).to_csv('temp.csv', index=False, index_label=False)
print(data)
