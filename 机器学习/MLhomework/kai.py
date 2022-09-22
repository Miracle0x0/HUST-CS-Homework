import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
kf=KFold(n_splits=10)
basenum=[1,5,10,100]


class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=100, fit_intercept=True):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.err = 1.0

    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    def fit(self, X, y, sample_weight):
        # 添加偏置b
        if self.fit_intercept:
            X = self.__add_intercept(X)
        # 初始化theta(w)
        self.theta = np.zeros(X.shape[1])
        # z=wT+b
        z = np.dot(X, self.theta)
        # h=sigmoid(z)
        h = self.__sigmoid(z)
        # 梯度下降算法开始，迭代次数为num-iter次
        for i in range(self.num_iter):
            # 计算梯度
            gradient = (sample_weight.T * (h.T - y.T)).T.dot(X)
            # 更新theta
            self.theta -= self.lr * gradient
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            loss = self.__loss(h, y)

        y_p = []
        for p in h:
            y_p.append(1 if p > 0.5 else -1)
        self.err = np.sum((y_p != y) * sample_weight)
        # print("error:")
        # print(self.err)
        return self

    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        return self.__sigmoid(np.dot(X, self.theta))

    def predict(self, X):
        return self.predict_prob(X).round()


class DecisionTreeClassifierWithWeight:
    def __init__(self):
        self.best_err = 1  # 最小的加权错误率
        self.best_fea_id = 0  # 最优特征id
        self.best_thres = 0  # 选定特征的最优阈值
        self.best_op = 1  # 阈值符号，其中 1: >, 0: <

    def fit(self, X, y, sample_weight=None):
        if sample_weight is None:
            sample_weight = np.ones(len(X)) / len(X)
        n = X.shape[1]
        numSteps = 35.0  # 将一列特征值分为numSteps个块
        for i in range(n):
            feature = X[:, i]  # 选定特征列
            rangeMin = feature.min()  # 特征值最小值
            rangeMax = feature.max()  # 特征值最大值
            stepSize = (rangeMax - rangeMin) / numSteps  # 计算步长
            for j in range(-1, int(numSteps) + 1):
                thres = (rangeMin + float(j) * stepSize)
                # fea_unique = np.sort(np.unique(feature))  # 将所有特征值从小到大排序
                # for j in range(len(fea_unique)-1):
                #     thres = (fea_unique[j] + fea_unique[j+1]) / 2  # 逐一设定可能阈值
                for op in (0, 1):
                    y_ = 2 * (feature >= thres) - 1 if op == 1 else 2 * (feature < thres) - 1  # 判断何种符号为最优
                    err = np.sum((y_ != y) * sample_weight)
                    if err < self.best_err:  # 当前参数组合可以获得更低错误率，更新最优参数
                        self.best_err = err
                        self.best_op = op
                        self.best_fea_id = i
                        self.best_thres = thres
        return self

    def predict(self, X):
        feature = X[:, self.best_fea_id]
        return 2 * (feature >= self.best_thres) - 1 if self.best_op == 1 else 2 * (feature < self.best_thres) - 1

    def score(self, X, y, sample_weight=None):
        y_pre = self.predict(X)
        if sample_weight is not None:
            return np.sum((y_pre == y) * sample_weight)
        return np.mean(y_pre == y)


class AdaBoostClassifier_Logistic:
    def __init__(self, n_estimators):
        self.n_estimators = n_estimators
        self.estimators = []
        self.alphas = []

    def fit(self, X, y):
        sample_weight = np.ones(len(X)) / len(X)  # 初始化样本权重为 1/N
        for _ in range(self.n_estimators):
            dtc = LogisticRegression().fit(X, y, sample_weight)  # 训练弱学习器
            alpha = 1/2 * np.log((1-dtc.err)/dtc.err)  # 权重系数
            y_pred = dtc.predict(X)
            sample_weight *= np.exp(-alpha*y_pred*y)  # 更新迭代样本权重
            sample_weight /= np.sum(sample_weight)  # 样本权重归一化
            self.estimators.append(dtc)
            self.alphas.append(alpha)
        return self

    def predict(self, X):
        y_pred = np.empty((len(X), self.n_estimators))  # 预测结果二维数组，其中每一列代表一个弱学习器的预测结果
        for i in range(self.n_estimators):
            y_pred[:, i] = self.estimators[i].predict(X)
        y_pred = y_pred * np.array(self.alphas)  # 将预测结果与训练权重乘积作为集成预测结果
        return 2*(np.sum(y_pred, axis=1)>0)-1  # 以0为阈值，判断并映射为-1和1

    def score(self, X, y):
        y_pred = self.predict(X)
        return np.mean(y_pred==y)


class AdaBoostClassifier_DecisionTree:
    def __init__(self, n_estimators):
        self.n_estimators = n_estimators
        self.estimators = []
        self.alphas = []

    def fit(self, X, y):
        sample_weight = np.ones(len(X)) / len(X)  # 初始化样本权重为 1/N
        for _ in range(self.n_estimators):
            dtc = DecisionTreeClassifierWithWeight().fit(X, y, sample_weight)  # 训练弱学习器
            alpha = 1/2 * np.log((1-dtc.best_err)/dtc.best_err)  # 权重系数
            y_pred = dtc.predict(X)
            sample_weight *= np.exp(-alpha*y_pred*y)  # 更新迭代样本权重
            sample_weight /= np.sum(sample_weight)  # 样本权重归一化
            self.estimators.append(dtc)
            self.alphas.append(alpha)
        return self

    def predict(self, X):
        y_pred = np.empty((len(X), self.n_estimators))  # 预测结果二维数组，其中每一列代表一个弱学习器的预测结果
        for i in range(self.n_estimators):
            y_pred[:, i] = self.estimators[i].predict(X)
        y_pred = y_pred * np.array(self.alphas)  # 将预测结果与训练权重乘积作为集成预测结果
        return 2*(np.sum(y_pred, axis=1)>0)-1  # 以0为阈值，判断并映射为-1和1

    def score(self, X, y):
        y_pred = self.predict(X)
        return np.mean(y_pred==y)


class Adaboost:
    def __init__(self, base):
        self.base = base
        self.clf = []

    def fit(self, data_filename, targets_filename):
        data = pd.read_csv(data_filename, header=None)
        X = np.array(data)
        with open(targets_filename) as f:
            reader = csv.reader(f)
            col = []  # 创建存储列数据的空列表
            for row in reader:  # 遍历文件中的每一行
                data = float(row[0])  # 将索引1处即第二列的字符串数据转换为数字
                col.append(data)  # 将数据存储到列表中
        y = np.array(col)
        y = 2 * y - 1  # 将0/1取值映射为-1/1取值
        if self.base == 0:  # 对数几率回归
            print("正在生成文件......（大约需要30秒）")
            X_scalar = StandardScaler()
            X = X_scalar.fit_transform(X)
            for baseclf in basenum:
                i = 1
                for train_i, test_i in kf.split(X):
                    self.clf = AdaBoostClassifier_Logistic(baseclf).fit(X[train_i], y[train_i])
                    y_pre = self.clf.predict(X[test_i])
                    y_pre = (y_pre + 1) / 2
                    dataframe = pd.DataFrame({'Id': test_i + 1, 'target': y_pre})
                    dataframe.to_csv("experiments/base" + str(baseclf) + "_fold" + str(i) + ".csv", index=False,
                                     sep=',')
                    i = i + 1
            print("文件生成完毕")
        elif self.base == 1:  # 决策树桩
            print("正在生成文件......（大约需要1分50秒）")
            for baseclf in basenum:
                i = 1
                for train_i, test_i in kf.split(X):
                    self.clf = AdaBoostClassifier_DecisionTree(baseclf).fit(X[train_i], y[train_i])
                    y_pre = self.clf.predict(X[test_i])
                    y_pre = (y_pre + 1) / 2
                    dataframe = pd.DataFrame({'Id': test_i + 1, 'target': y_pre})
                    dataframe.to_csv("experiments/base" + str(baseclf) + "_fold" + str(i) + ".csv", index=False,
                                     sep=',')
                    i = i + 1
            print("文件生成完毕")
        return self

    def predict(self, test_filename):
        data = pd.read_csv(test_filename, header=None)
        X = np.array(data)
        if self.base == 0:
            X_scalar = StandardScaler()
            X = X_scalar.fit_transform(X)
        test_result = self.clf.predict(X)
        return test_result


