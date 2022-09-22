import numpy as np
import pandas as pd
import time

base_list = [1, 5, 10, 100]  # 基分类器数目列表


# StandardScaler 标准化
def standard_scaler(data):
    return (data - np.mean(data, axis=0)) / np.std(data, axis=0)


# MinMaxScaler 标准化
def minmax_scaler(data):
    return (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))


del_list = []


# 数据预处理
def pre_process(data):
    for col in range(data.shape[1]):
        if (data[:, col] == 0).sum() / data.shape[0] >= 0.95:
            del_list.append(col)
    data = np.delete(data, del_list, axis=1)
    return data


# K 折交叉验证，本实验中默认 10 折
class KFold:
    def __init__(self, n_splits=10):
        self.n_splits = n_splits  # 折数

    def split(self, data, label, k):
        """
        :param data: 训练数据
        :param label: 训练标签
        :param k: 第 k 折

        :returns : train_data, test_data, train_label, test_label
        """
        k_size = len(data) // self.n_splits
        fold_index = np.zeros(len(data))
        fold_index[k * k_size: (k + 1) * k_size] = 1
        # 划分训练集和测试集
        train_index, test_index = (fold_index == 0), (fold_index == 1)
        train_data, test_data = data[train_index], data[test_index]
        # 划分训练标签和测试标签
        train_label, test_label = label[train_index], label[test_index]
        return train_data, test_data, train_label, test_label


KFOLD = 10  # 10 折交叉验证
kf = KFold(n_splits=KFOLD)


# 单层决策树（决策树桩）基分类器
class DecisionTreeStump:
    def __init__(self, n_steps=60):
        self.error = 0  # 最小加权错误率
        self.best_v = 0  # 选定特征的最优阈值
        self.best_axis = None  # 最佳特征索引
        self.direct = None  # 阈值符号，positive 为正向，negative 为反向
        self.clf_result = None
        self.n_steps = n_steps  # 迭代次数，默认为 50
        self.M, self.N = None, None

    # 初始化参数
    def init_args(self, data):
        self.M, self.N = data.shape
        self.error = float('inf')  # 初始化错误率为无穷大

    # 求解根据特征 features 的分类阈值、分类误差、分类结果
    def best_threshold(self, features, labels, weights):
        best_err = float('inf')  # 当前错误率，初始化为无穷大
        best_v = float('-inf')  # 当前阈值
        best_direct = None  # 当前阈值符号
        cmp_array = None  # 当前结果
        features_min, features_max = features.min(), features.max()
        step_size = (features_max - features_min) / self.n_steps  # 设置步长
        for step in range(-1, self.n_steps + 1):
            v = features_min + step_size * float(step)
            cmp_array_pos = np.where(features >= v, 1, -1)  # 误分类计算，假定不小于 cur_v 的为 1
            weight_err_pos = np.sum((cmp_array_pos != labels) * weights)
            if min(weight_err_pos, 1 - weight_err_pos) < best_err:
                best_v = v  # 阈值更新
                if weight_err_pos < 0.5:
                    best_err = weight_err_pos
                    best_direct = 'positive'
                    cmp_array = cmp_array_pos
                else:
                    best_err = 1 - weight_err_pos
                    best_direct = 'negative'
                    cmp_array = -cmp_array_pos  # 反转
        return best_v, best_direct, best_err, cmp_array

    def fit(self, train_data, train_label, weights):
        """
        :param train_data: 训练数据
        :param train_label: 训练标签
        :param weights: 样本权重

        :return: None
        """
        self.init_args(train_data)
        # 选择误差最小的特征维度
        for col in range(self.N):
            features = train_data[:, col]  # 第 col 列特征
            cur_v, cur_direct, cur_err, cmp_array = self.best_threshold(features, train_label, weights)
            if cur_err < self.error:
                self.error = cur_err
                self.best_v = cur_v
                self.direct = cur_direct
                self.best_axis = col
                self.clf_result = cmp_array
            if self.error == 0.0:
                break

    def predict(self, test):
        """
        :param test: 测试数据
        :return: 预测结果，类型为 numpy.ndarray
        """
        if self.direct == 'positive':
            return np.where(test[:, self.best_axis] > self.best_v, 1, -1)
        else:
            return np.where(test[:, self.best_axis] > self.best_v, -1, 1)


# 对数几率回归基分类器
class LogisticRegression:
    def __init__(self, n_iters=200, learning_rate=1.0):
        self.n_iters = n_iters  # 迭代次数
        self.lr = learning_rate  # 学习率
        self.threshold = 0.4  # 分界阈值
        self.error = 0.0  # 错误率
        self.clf_result = None
        self.M, self.N = None, None
        self.theta = None  # 权重

    def init_args(self, data):
        self.M, self.N = data.shape
        self.theta = np.ones(self.N)  # 初始化权重 theta

    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))

    def fit(self, train_data, train_label, weights):
        """
        :param train_data: 训练数据
        :param train_label: 训练标签
        :param weights: 样本权重

        :return: None
        """
        train_data = np.insert(train_data, 0, 1, 1)  # 在数据集的第 0 列增加一列 1
        self.init_args(train_data)
        label = np.where(train_label == -1, 0, 1)  # 将标签为 -1 的改为 0
        # 梯度下降算法
        for k in range(self.n_iters):
            # z = w * T + b
            z = np.dot(train_data, self.theta)
            # h = sigmoid(z)
            h = self.sigmoid(z)
            # 计算梯度 gradient
            g = np.dot((weights.T * (h.T - label.T)).T, train_data)
            if np.linalg.norm(g) <= 1e-3:  # 梯度足够小时可视为达到极值点
                break
            self.theta -= g * self.lr * (0.9 ** (k * 10.0 / self.n_iters))
        # 计算误分率
        self.clf_result = np.where(self.sigmoid(np.inner(self.theta, train_data)) >= self.threshold, 1, -1)
        self.error = np.sum((self.clf_result != train_label) * weights)
        self.error = min(self.error, 1 - self.error)  # 将错误率大于 0.5 的情况进行反转

    def predict(self, test):
        """
        :param test: 测试数据
        :return: 预测结果，类型为 numpy.ndarray
        """
        test = np.insert(test, 0, 1, 1)
        return np.where(self.sigmoid(np.inner(self.theta, test)) >= self.threshold, 1, -1)


# AdaBoost 算法
class AdaBoost:
    def __init__(self, base=0, n_estimator=5):
        self.clf_kind = base  # 基分类器种类
        self.base_num = n_estimator  # 基分类器数量
        self.X, self.Y = None, None  # 训练集、训练标签
        self.M, self.N = None, None  # 训练集大小
        self.clf_sets = []  # 弱分类器集合
        self.clf_num = 0  # 弱分类器数量
        self.alphas = []  # 系数 alpha
        self.weights = None  # 样本权重

    # 初始化参数
    def init_args(self, datasets, labels):
        self.X = datasets  # 训练集
        self.Y = labels  # 训练标签
        self.M, self.N = datasets.shape  # 初始化 M, N
        self.weights = np.ones(self.M) / self.M  # 初始化权重为 1 / M

    # 计算 alpha
    def _alpha(self, error):
        return 0.5 * np.log((1 - error) / error)

    # 权值更新并规范化
    def _w(self, a, clf):
        self.weights *= np.exp(-1 * a * self.Y * clf)
        sum_of_weights = sum(self.weights)
        self.weights /= sum_of_weights  # 归一化权重

    # 计算在训练集上的准确率
    def accuracy(self, features, labels):
        res = np.zeros(self.M)  # 预测结果
        for idx in range(self.clf_num):
            weak_clf = self.clf_sets[idx]  # 单个弱分类器
            res += self.alphas[idx] * weak_clf.predict(features)  # 记录加权结果
        res_array = np.where(res > 0, 1, -1)  # 预测结果
        return np.sum(res_array == labels) / self.M  # 计算准确率

    def fit(self, x_file, y_file):
        # 读取训练数据并转换为 numpy.ndarray
        data = np.array(pd.read_csv(x_file, header=None))
        # data = np.genfromtxt(x_file, delimiter=',', dtype=np.float32)

        # 对于逻辑回归，进行数据预处理删除 0 的个数过多的列
        if self.clf_kind == 0:
            data = pre_process(data)

        data = standard_scaler(data)  # 数据标准化
        # 读取训练标签并转换为 numpy.ndarray
        label = np.genfromtxt(y_file, delimiter=',', dtype=int)
        label = np.where(label == 0, -1, label)  # 将标签为 0 的改为 -1

        # 记录分类效果最好的分类器
        best_clf_sets = None
        best_alphas = None
        best_acc = -1.0

        # 分别以 1、5、10、100 作为基分类器数目进行训练
        for base_num in base_list:
            st_time = time.time()
            print("base_num = %d" % base_num)
            self.base_num = base_num
            # 10 折交叉验证开始
            k_size = len(data) // KFOLD
            for i in range(KFOLD):
                print(i + 1)
                train_data, test_data, train_label, test_label = kf.split(data, label, i)
                self.init_args(train_data, train_label)
                # 训练模型
                for epoch in range(self.base_num):
                    if self.clf_kind == 0:  # 基分类器为逻辑回归
                        classifier = LogisticRegression()
                    else:  # 基分类器为决策树桩
                        classifier = DecisionTreeStump()
                    classifier.fit(train_data, train_label, self.weights)
                    # print("error: %f" % classifier.error)
                    # 若分类器比随机猜测效果还差则终止
                    if classifier.error > 0.5:
                        self.clf_num = len(self.clf_sets)
                        break
                    # 若误差对权重更新的影响很有限也终止
                    if 0.5 - classifier.error <= 1e-4:
                        self.clf_num = len(self.clf_sets)
                        break
                    a = self._alpha(classifier.error)  # 计算系数
                    self.alphas.append(a)
                    self.clf_sets.append(classifier)  # 记录分类器
                    # cur_accuracy = self.accuracy(train_data, train_label)
                    # print("迭代次数：%d 准确率：%f" % (epoch + 1, cur_accuracy))
                    # 修改权值
                    self._w(a, classifier.clf_result)
                    # 输出 10 折交叉验证结果
                    out = self.test(test_data).reshape(1, -1)
                    cur_acc = np.sum(out == test_label) / len(out)
                    out = np.insert(out, 0, np.arange(i * k_size + 1, (i + 1) * k_size + 1), axis=0)
                    out = [[row[j] for row in out] for j in range(k_size)]
                    np.savetxt("experiments/base%d_fold%d.csv" % (self.base_num, i + 1), out, fmt='%d', delimiter=',')
                    # 在 10 折交叉验证过程中记录最好的分类模型
                    if best_acc < cur_acc:
                        best_acc = cur_acc
                        best_clf_sets = self.clf_sets
                        best_alphas = self.alphas
            ed_time = time.time()
            print("Training time of base_num %d: %.3f s" % (self.base_num, ed_time - st_time))
            # 10 折交叉验证结束
        # 选择最好的模型作为预测测试数据的模型
        self.clf_sets = best_clf_sets
        self.alphas = best_alphas

    def test(self, test):
        res = np.zeros(len(test))
        for idx in range(len(self.clf_sets)):
            classifier = self.clf_sets[idx]
            res += self.alphas[idx] * classifier.predict(test)
        return np.where(res > 0, 1, 0)

    def predict(self, x_file):
        test_data = np.array(pd.read_csv(x_file, header=None))
        if self.clf_kind == 0:
            test_data = np.delete(test_data, del_list, axis=1)
        test_data = standard_scaler(test_data)
        return self.test(test_data)
