---
layout: default
title: Generalization Beyond Benchmarks: Evaluating Learnable Protein-Ligand Scoring Functions on Unseen Targets
---

# Generalization Beyond Benchmarks: Evaluating Learnable Protein-Ligand Scoring Functions on Unseen Targets

**arXiv**: [2512.05386v1](https://arxiv.org/abs/2512.05386) | [PDF](https://arxiv.org/pdf/2512.05386.pdf)

**作者**: Jakub Kopko, David Graber, Saltuk Mustafa Eyrilmez, Stanislav Mazurenko, David Bednar, Jiri Sedlar, Josef Sivic

---

## 💡 一句话要点

**评估可学习蛋白-配体评分函数在新靶点上的泛化能力，揭示基准测试局限性并探索改进方法**

**关键词**: `蛋白-配体评分函数` `泛化能力评估` `自监督预训练` `分子设计` `机器学习可靠性` `新靶点预测`

## 📋 核心要点

1. 核心问题：机器学习评分函数在标准基准上表现良好，但泛化到新蛋白靶点的能力仍面临挑战
2. 方法要点：通过模拟有限结构数据的靶点分割评估泛化能力，并研究大规模自监督预训练和简单数据利用方法
3. 实验或效果：发现常用基准不能反映真实泛化挑战，初步证据显示自监督预训练有潜力，并提供实用设计指导

## 📄 摘要（原文）

> As machine learning becomes increasingly central to molecular design, it is vital to ensure the reliability of learnable protein-ligand scoring functions on novel protein targets. While many scoring functions perform well on standard benchmarks, their ability to generalize beyond training data remains a significant challenge. In this work, we evaluate the generalization capability of state-of-the-art scoring functions on dataset splits that simulate evaluation on targets with a limited number of known structures and experimental affinity measurements. Our analysis reveals that the commonly used benchmarks do not reflect the true challenge of generalizing to novel targets. We also investigate whether large-scale self-supervised pretraining can bridge this generalization gap and we provide preliminary evidence of its potential. Furthermore, we probe the efficacy of simple methods that leverage limited test-target data to improve scoring function performance. Our findings underscore the need for more rigorous evaluation protocols and offer practical guidance for designing scoring functions with predictive power extending to novel protein targets.

