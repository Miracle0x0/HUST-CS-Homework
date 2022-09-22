import numpy as np
import pandas as pd


class Adaboost():
    def __init__(self, base):
        '''
        :param base: 基分类器编号 0 代表对数几率回归 1 代表决策树桩
        在此函数中对模型相关参数进行初始化，如后续还需要使用参数请赋初始值
        '''

    def fit(self, x_file, y_file):
        '''
        在此函数中训练模型
        :param x_file:训练数据(data.csv)
        :param y_file:训练数据标记(targets.csv)
        '''

    def predict(self, x_file):
        '''
        :param x_file:测试集文件夹(后缀为csv)
        :return: 训练模型对测试集的预测标记
        '''


