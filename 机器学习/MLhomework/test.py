# 训练模型
    def fit(self, x_file, y_file):
        data = np.genfromtxt(x_file, delimiter=',', dtype=np.float32)
        data = self.standardscaler(data)  # 数据标准化
        data = self.minmaxscaler(data)
        label = np.genfromtxt(y_file, delimiter=',', dtype=int)
        label = np.where(label == 0, -1, 1)  # 将标签为0的改为-1
        best_clf_sets, best_alpha, best_acc = None, None, -1
        # 4种基分类器数目
        base_list = [1, 5, 10, 100]
        for j in range(4):
            print('base_num=', base_list[j])
            self.base_num = base_list[j]
            kfold = 10
            kfold_size = len(data) // kfold
            # 10折交叉验证
            for i in range(kfold):
                # print(i + 1)
                foldindex = np.zeros(len(data))
                foldindex[i * kfold_size:(i + 1) * kfold_size] = 1
                trainindex = foldindex == 0
                testindex = foldindex == 1
                train_data = data[trainindex]  # 第i折的训练数据
                train_label = label[trainindex]  # 第i折的训练标签
                test_data = data[testindex]  # 第i折的测试数据
                test_label = label[testindex]  # 第i折的测试标签
                self.init_args(train_data, train_label)  # 初始化参数
                # 训练模型
                if self.base_kind == 1:  # 基分类器为决策树桩时
                    for epoch in range(self.base_num):
                        stump = Treestump()
                        stump.fit(train_data, train_label, self.weights)
                        # 若基分类器比随机猜测还差则中止算法
                        if stump.error >= 0.5:
                            break
                        # 计算G(x)系数a
                        a = self._alpha(stump.error)
                        self.alpha.append(a)
                        # 记录分类器
                        self.clf_sets.append(stump)
                        # # 计算当前Adaboost的准确率
                        # clf_accuracy = self.accuracy(train_data, train_label)
                        # print('迭代次数：', epoch + 1, '准确率：', clf_accuracy)
                        # 权值更新
                        self._w(a, stump.clf_result)
                        # 归一化权重
                        self._Z()
                else:  # 基分类器为逻辑回归时
                    for epoch in range(self.base_num):
                        lr = LogisticRegression(n_iters=500, learning_rate=10)
                        lr.fit(train_data, train_label, self.weights)
                        if 0.5 - lr.error < 0.001:
                            break
                        a = self._alpha(lr.error)
                        self.alpha.append(a)
                        self.clf_sets.append(lr)
                        # clf_accuracy = self.accuracy(train_data, train_label)
                        # print('迭代次数：', epoch + 1, '准确率：', clf_accuracy)
                        self._w(a, lr.clf_result)
                        self._Z()
                # 输出10折测试集的预测结果
                out = self.test(test_data)
                acc = sum(np.where(out == test_label, 1, 0)) / len(out)
                out = np.insert(out.reshape(1, -1), 0, np.arange(i * kfold_size + 1, i * kfold_size + kfold_size + 1),
                                axis=0)
                out = [[row[j] for row in out] for j in range(kfold_size)]
                np.savetxt('experiments/base%d_fold%d.csv' % (self.base_num, i + 1), out, fmt='%d', delimiter=',')
                # 10折过程中，记录最好的模型
                if best_acc < acc:
                    best_acc = acc
                    best_clf_sets = self.clf_sets
                    best_alpha = self.alpha
        # 训练结束后，选择最好的模型作为预测测试数据的模型
        self.clf_sets = best_clf_sets
        self.alpha = best_alpha
        print(len(self.clf_sets))
