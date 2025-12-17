---
layout: default
title: Improving Slow Transfer Predictions: Generative Methods Compared
---

# Improving Slow Transfer Predictions: Generative Methods Compared

**arXiv**: [2512.14522v1](https://arxiv.org/abs/2512.14522) | [PDF](https://arxiv.org/pdf/2512.14522.pdf)

**作者**: Jacob Taegon Kim, Alex Sim, Kesheng Wu, Jinoh Kim

**分类**: cs.LG, cs.DC, cs.NI

**发布日期**: 2025-12-16

**DOI**: [10.1109/ICNC64010.2025.10994006](https://doi.org/10.1109/ICNC64010.2025.10994006)

---

## 💡 一句话要点

**比较生成方法以解决科学计算网络中数据转移预测的类别不平衡问题**

**关键词**: `数据转移预测` `类别不平衡` `生成方法` `过采样` `科学计算网络` `性能监控` `机器学习模型` `CTGAN`

## 📋 核心要点

1. 核心问题：机器学习模型在科学计算网络数据转移预测中面临类别不平衡，导致预测准确性受限。
2. 方法要点：比较传统过采样与生成方法如CTGAN，调整训练数据不平衡比例以评估增强策略效果。
3. 实验或效果：增强策略在低不平衡时可能提升性能，但高不平衡下改进有限，CTGAN未显著优于分层采样。

## 📝 摘要（中文）

监控数据转移性能是科学计算网络中的关键任务。通过在通信阶段早期预测性能，可以识别潜在缓慢的转移并选择性监控，从而优化网络使用和整体性能。在此背景下，提高机器学习模型预测能力的一个关键瓶颈是类别不平衡问题。本项目专注于解决类别不平衡问题以增强性能预测的准确性。在本研究中，我们分析和比较了多种增强策略，包括传统的过采样方法和生成技术。此外，我们调整训练数据集中的类别不平衡比例以评估其对模型性能的影响。虽然增强可能改善性能，但随着不平衡比例增加，性能并未显著提升。我们得出结论，即使是最先进的技术如CTGAN，也未显著优于简单的分层采样。

## 🔬 方法详解

论文采用比较分析框架，核心方法包括传统过采样和生成技术如CTGAN，用于处理数据转移预测中的类别不平衡。关键技术创新点在于系统评估不同增强策略在不平衡比例变化下的效果，而非提出新模型。与现有方法的主要区别在于直接对比生成方法与简单采样，强调实际应用中的性能瓶颈，而非理论优化。整体框架基于实验驱动，通过调整训练数据集的不平衡比例来量化增强策略的贡献。

## 📊 实验亮点

最重要的实验结果显示，增强策略在类别不平衡比例较低时可能改善预测性能，但随着比例增加，性能提升不显著；CTGAN等先进生成方法未超越简单分层采样，表明类别不平衡问题在此场景下具有挑战性。

## 🎯 应用场景

该研究可应用于科学计算网络中的性能监控和优化，帮助识别缓慢数据转移以提升网络效率，潜在价值在于指导实际部署中的类别不平衡处理策略。

## 📄 摘要（原文）

> Monitoring data transfer performance is a crucial task in scientific computing networks. By predicting performance early in the communication phase, potentially sluggish transfers can be identified and selectively monitored, optimizing network usage and overall performance. A key bottleneck to improving the predictive power of machine learning (ML) models in this context is the issue of class imbalance. This project focuses on addressing the class imbalance problem to enhance the accuracy of performance predictions. In this study, we analyze and compare various augmentation strategies, including traditional oversampling methods and generative techniques. Additionally, we adjust the class imbalance ratios in training datasets to evaluate their impact on model performance. While augmentation may improve performance, as the imbalance ratio increases, the performance does not significantly improve. We conclude that even the most advanced technique, such as CTGAN, does not significantly improve over simple stratified sampling.

