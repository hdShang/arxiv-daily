---
layout: default
title: PolySet: Restoring the Statistical Ensemble Nature of Polymers for Machine Learning
---

# PolySet: Restoring the Statistical Ensemble Nature of Polymers for Machine Learning

**arXiv**: [2512.13186v1](https://arxiv.org/abs/2512.13186) | [PDF](https://arxiv.org/pdf/2512.13186.pdf)

**作者**: Khalid Ferji

---

## 💡 一句话要点

**提出PolySet框架，通过加权链集合表示聚合物，以解决机器学习中聚合物统计性质缺失的问题。**

**关键词**: `聚合物机器学习` `统计集合表示` `加权链集合` `摩尔质量分布` `尾部敏感性质` `均聚物建模`

## 📋 核心要点

1. 核心问题：现有机器学习模型将聚合物视为单一分子图，忽略真实材料中链长分布的统计集合性质，限制模型捕捉聚合物行为的能力。
2. 方法要点：PolySet将聚合物表示为从摩尔质量分布采样的有限加权链集合，编码独立于化学细节，适用于任何分子表示，以均聚物为例使用最小语言模型展示。
3. 实验或效果：PolySet保留高阶分布矩（如Mz、Mz+1），使机器学习模型能学习尾部敏感性质，显著提高稳定性和准确性。

## 📄 摘要（原文）

> Machine-learning (ML) models in polymer science typically treat a polymer as a single, perfectly defined molecular graph, even though real materials consist of stochastic ensembles of chains with distributed lengths. This mismatch between physical reality and digital representation limits the ability of current models to capture polymer behaviour. Here we introduce PolySet, a framework that represents a polymer as a finite, weighted ensemble of chains sampled from an assumed molar-mass distribution. This ensemble-based encoding is independent of chemical detail, compatible with any molecular representation and illustrated here in the homopolymer case using a minimal language model. We show that PolySet retains higher-order distributional moments (such as Mz, Mz+1), enabling ML models to learn tail-sensitive properties with greatly improved stability and accuracy. By explicitly acknowledging the statistical nature of polymer matter, PolySet establishes a physically grounded foundation for future polymer machine learning, naturally extensible to copolymers, block architectures, and other complex topologies.

