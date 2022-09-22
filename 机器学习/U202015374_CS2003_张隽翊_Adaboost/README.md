# 提交文件说明

[TOC]

## 一、文件结构

- `main.py`：实验代码
- `Word 文档`：实验报告 Word 版本
- `PDF 文档`：实验报告 PDF 版本

## 二、代码结构

> 主要有三个大类（DecisionTreeStump、LogisticRegression 和 AdaBoost）和一个小类（KFold），以及若干用于数据统计和处理的函数。

- `DecisionTreeStump`
  - `init_args`：初始化参数
  - `best_threshold`：用于 `fit` 函数中，根据某一维特征求解
  - `fit`：拟合函数
  - `predict`：预测函数
- `LogisticRegression`
  - `init_args`：初始化参数
  - `sigmoid`：对数几率函数
  - `fit`：拟合函数
  - `predict`：预测函数

- `AdaBoost`
  - `init_args`：初始化参数
  - `_alpha`：计算 alpha
  - `_w`：更新权值并归一化
  - `accuracy`：计算在训练集上的准确率
  - `fit`：拟合函数
  - `predict`：测试函数
  - `test`：辅助测试