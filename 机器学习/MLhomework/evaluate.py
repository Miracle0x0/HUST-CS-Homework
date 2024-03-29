import numpy as np
target = np.genfromtxt('targets.csv')
base_list = [1, 5, 10, 100]
from main import Adaboost
test1=Adaboost(base=1)
test1.fit("data.csv","targets.csv")
testy1=test1.predict("data.csv")
for base_num in base_list:
    acc = []
    for i in range(1, 11):
        fold = np.genfromtxt('experiments/base%d_fold%d.csv' % (base_num, i), delimiter=',', dtype=np.int)
        accuracy = sum(target[fold[:, 0] - 1] == fold[:, 1]) / fold.shape[0]
        acc.append(accuracy)

    print(np.array(acc).mean())
