---
layout: default
title: Challenges in 3D Data Synthesis for Training Neural Networks on Topological Features
---

# Challenges in 3D Data Synthesis for Training Neural Networks on Topological Features

**arXiv**: [2511.04972v1](https://arxiv.org/abs/2511.04972) | [PDF](https://arxiv.org/pdf/2511.04972.pdf)

**作者**: Dylan Peek, Matthew P. Skerritt, Siddharth Pritam, Stephan Chalup

---

## 💡 一句话要点

**提出基于排斥表面算法的3D数据合成方法，以解决拓扑数据分析中标注数据缺乏的问题。**

**关键词**: `拓扑数据分析` `3D数据合成` `神经网络估计器` `亏格估计` `卷积变换器`

## 📋 核心要点

1. 核心问题：拓扑数据分析中缺乏标注3D数据，阻碍神经网络估计器发展。
2. 方法要点：使用排斥表面算法生成可控拓扑不变量的标注3D数据集。
3. 实验或效果：训练卷积变换器网络估计亏格，变形增加时精度下降。

## 📄 摘要（原文）

> Topological Data Analysis (TDA) involves techniques of analyzing the
> underlying structure and connectivity of data. However, traditional methods
> like persistent homology can be computationally demanding, motivating the
> development of neural network-based estimators capable of reducing
> computational overhead and inference time. A key barrier to advancing these
> methods is the lack of labeled 3D data with class distributions and diversity
> tailored specifically for supervised learning in TDA tasks. To address this, we
> introduce a novel approach for systematically generating labeled 3D datasets
> using the Repulsive Surface algorithm, allowing control over topological
> invariants, such as hole count. The resulting dataset offers varied geometry
> with topological labeling, making it suitable for training and benchmarking
> neural network estimators. This paper uses a synthetic 3D dataset to train a
> genus estimator network, created using a 3D convolutional transformer
> architecture. An observed decrease in accuracy as deformations increase
> highlights the role of not just topological complexity, but also geometric
> complexity, when training generalized estimators. This dataset fills a gap in
> labeled 3D datasets and generation for training and evaluating models and
> techniques for TDA.

