---
layout: default
title: MicroEvoEval: A Systematic Evaluation Framework for Image-Based Microstructure Evolution Prediction
---

# MicroEvoEval: A Systematic Evaluation Framework for Image-Based Microstructure Evolution Prediction

**arXiv**: [2511.08955v1](https://arxiv.org/abs/2511.08955) | [PDF](https://arxiv.org/pdf/2511.08955.pdf)

**作者**: Qinyi Zhang, Duanyu Feng, Ronghui Han, Yangshuai Wang, Hao Wang

---

## 💡 一句话要点

**提出MicroEvoEval基准框架以系统评估图像基微观结构演化预测模型**

**关键词**: `微观结构演化预测` `深度学习基准` `物理保真度评估` `计算效率优化` `图像序列预测`

## 📋 核心要点

1. 核心问题：微观结构演化模拟缺乏标准化基准，现有研究忽视物理保真度和误差传播分析
2. 方法要点：构建首个综合基准，评估14种模型，涵盖领域专用和通用架构
3. 实验或效果：现代架构如VMamba在长期稳定性和计算效率上表现优越

## 📄 摘要（原文）

> Simulating microstructure evolution (MicroEvo) is vital for materials design but demands high numerical accuracy, efficiency, and physical fidelity. Although recent studies on deep learning (DL) offer a promising alternative to traditional solvers, the field lacks standardized benchmarks. Existing studies are flawed due to a lack of comparing specialized MicroEvo DL models with state-of-the-art spatio-temporal architectures, an overemphasis on numerical accuracy over physical fidelity, and a failure to analyze error propagation over time. To address these gaps, we introduce MicroEvoEval, the first comprehensive benchmark for image-based microstructure evolution prediction. We evaluate 14 models, encompassing both domain-specific and general-purpose architectures, across four representative MicroEvo tasks with datasets specifically structured for both short- and long-term assessment. Our multi-faceted evaluation framework goes beyond numerical accuracy and computational cost, incorporating a curated set of structure-preserving metrics to assess physical fidelity. Our extensive evaluations yield several key insights. Notably, we find that modern architectures (e.g., VMamba), not only achieve superior long-term stability and physical fidelity but also operate with an order-of-magnitude greater computational efficiency. The results highlight the necessity of holistic evaluation and identify these modern architectures as a highly promising direction for developing efficient and reliable surrogate models in data-driven materials science.

