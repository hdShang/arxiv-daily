---
layout: default
title: Data Augmentation Techniques to Reverse-Engineer Neural Network Weights from Input-Output Queries
---

# Data Augmentation Techniques to Reverse-Engineer Neural Network Weights from Input-Output Queries

**arXiv**: [2511.20312v1](https://arxiv.org/abs/2511.20312) | [PDF](https://arxiv.org/pdf/2511.20312.pdf)

**作者**: Alexander Beiser, Flavio Martinelli, Wulfram Gerstner, Johanni Brea

---

## 💡 一句话要点

**提出定制数据增强技术以在参数多于训练数据时恢复神经网络权重**

**关键词**: `神经网络权重恢复` `数据增强` `教师-学生设置` `表示空间采样` `过拟合缓解`

## 📋 核心要点

1. 核心问题：教师网络参数多于训练数据时，学生网络过拟合查询，无法对齐权重。
2. 方法要点：设计新数据增强技术，优化教师隐藏层表示空间的采样。
3. 实验效果：扩展可恢复网络规模，参数比训练数据点多达100倍。

## 📄 摘要（原文）

> Network weights can be reverse-engineered given enough informative samples of a network's input-output function. In a teacher-student setup, this translates into collecting a dataset of the teacher mapping -- querying the teacher -- and fitting a student to imitate such mapping. A sensible choice of queries is the dataset the teacher is trained on. But current methods fail when the teacher parameters are more numerous than the training data, because the student overfits to the queries instead of aligning its parameters to the teacher. In this work, we explore augmentation techniques to best sample the input-output mapping of a teacher network, with the goal of eliciting a rich set of representations from the teacher hidden layers. We discover that standard augmentations such as rotation, flipping, and adding noise, bring little to no improvement to the identification problem. We design new data augmentation techniques tailored to better sample the representational space of the network's hidden layers. With our augmentations we extend the state-of-the-art range of recoverable network sizes. To test their scalability, we show that we can recover networks of up to 100 times more parameters than training data-points.

