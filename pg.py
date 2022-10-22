import numpy as np

label_1 = [x for x in np.arange(20, 100, 10)]
label_2 = [x for x in np.arange(30, 110, 10)]

l = list()

l = [f'{x}~{y} ' for x, y in zip(label_1, label_2)]
print(l)
