---
layout: default
title: Comprehensive Evaluation of Rule-Based, Machine Learning, and Deep Learning in Human Estimation Using Radio Wave Sensing: Accuracy, Spatial Generalization, and Output Granularity Trade-offs
---

# Comprehensive Evaluation of Rule-Based, Machine Learning, and Deep Learning in Human Estimation Using Radio Wave Sensing: Accuracy, Spatial Generalization, and Output Granularity Trade-offs

**arXiv**: [2512.13031v1](https://arxiv.org/abs/2512.13031) | [PDF](https://arxiv.org/pdf/2512.13031.pdf)

**作者**: Tomoya Tanaka, Tomonori Ikeda, Ryo Yonemoto

---

## 💡 一句话要点

**比较基于规则、机器学习和深度学习在无线电波人体估计中的性能，揭示空间泛化与输出粒度权衡**

**关键词**: `无线电波感知` `人体估计` `空间泛化` `输出粒度` `FMCW MIMO雷达` `模型比较`

## 📋 核心要点

1. 核心问题：评估不同方法在无线电波人体估计中的准确性、空间泛化能力和输出粒度权衡
2. 方法要点：系统比较基于规则、传统机器学习和深度学习模型，使用FMCW MIMO雷达在两种室内布局中测试
3. 实验或效果：深度学习在训练环境精度最高，但空间泛化差；基于规则方法泛化强但输出粒度粗

## 📄 摘要（原文）

> This study presents the first comprehensive comparison of rule-based methods, traditional machine learning models, and deep learning models in radio wave sensing with frequency modulated continuous wave multiple input multiple output radar. We systematically evaluated five approaches in two indoor environments with distinct layouts: a rule-based connected component method; three traditional machine learning models, namely k-nearest neighbors, random forest, and support vector machine; and a deep learning model combining a convolutional neural network and long short term memory. In the training environment, the convolutional neural network long short term memory model achieved the highest accuracy, while traditional machine learning models provided moderate performance. In a new layout, however, all learning based methods showed significant degradation, whereas the rule-based method remained stable. Notably, for binary detection of presence versus absence of people, all models consistently achieved high accuracy across layouts. These results demonstrate that high capacity models can produce fine grained outputs with high accuracy in the same environment, but they are vulnerable to domain shift. In contrast, rule-based methods cannot provide fine grained outputs but exhibit robustness against domain shift. Moreover, regardless of the model type, a clear trade off was revealed between spatial generalization performance and output granularity.

