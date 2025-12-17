---
layout: default
title: PRISM: Periodic Representation with multIscale and Similarity graph Modelling for enhanced crystal structure property prediction
---

# PRISM: Periodic Representation with multIscale and Similarity graph Modelling for enhanced crystal structure property prediction

**arXiv**: [2511.20362v1](https://arxiv.org/abs/2511.20362) | [PDF](https://arxiv.org/pdf/2511.20362.pdf)

**作者**: Àlex Solé, Albert Mosella-Montoro, Joan Cardona, Daniel Aravena, Silvia Gómez-Coca, Eliseo Ruiz, Javier Ruiz-Hidalgo

---

## 💡 一句话要点

**提出PRISM框架以解决晶体结构预测中周期性边界和多尺度交互的挑战**

**关键词**: `晶体结构预测` `图神经网络` `周期性边界条件` `多尺度表示` `专家模块`

## 📋 核心要点

1. 核心问题：晶体结构具有周期性边界和多尺度交互，现有图学习方法常忽略这些特性
2. 方法要点：PRISM集成多尺度表示和周期性特征编码，使用专家模块处理不同结构化学方面
3. 实验或效果：在多个基准测试中，PRISM提升了晶体属性预测的准确率，优于现有方法

## 📄 摘要（原文）

> Crystal structures are characterised by repeating atomic patterns within unit cells across three-dimensional space, posing unique challenges for graph-based representation learning. Current methods often overlook essential periodic boundary conditions and multiscale interactions inherent to crystalline structures. In this paper, we introduce PRISM, a graph neural network framework that explicitly integrates multiscale representations and periodic feature encoding by employing a set of expert modules, each specialised in encoding distinct structural and chemical aspects of periodic systems. Extensive experiments across crystal structure-based benchmarks demonstrate that PRISM improves state-of-the-art predictive accuracy, significantly enhancing crystal property prediction.

