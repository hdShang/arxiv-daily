---
layout: default
title: Ensemble Performance Through the Lens of Linear Independence of Classifier Votes in Data Streams
---

# Ensemble Performance Through the Lens of Linear Independence of Classifier Votes in Data Streams

**arXiv**: [2511.21465v1](https://arxiv.org/abs/2511.21465) | [PDF](https://arxiv.org/pdf/2511.21465.pdf)

**作者**: Enes Bektas, Fazli Can

---

## 💡 一句话要点

**提出基于分类器投票线性独立性的理论框架，以优化数据流集成学习性能**

**关键词**: `集成学习` `数据流分类` `线性独立性` `加权多数投票` `理论框架` `性能饱和`

## 📋 核心要点

1. 研究集成学习中分类器数量与性能的权衡，避免计算低效和收益递减
2. 通过线性独立性和加权多数投票模型，推导理论框架估计最优集成规模
3. 在真实和合成数据集上验证理论，OzaBagging性能饱和，GOOWE可能不稳定

## 📄 摘要（原文）

> Ensemble learning improves classification performance by combining multiple base classifiers. While increasing the number of classifiers generally enhances accuracy, excessively large ensembles can lead to computational inefficiency and diminishing returns. This paper investigates the relationship between ensemble size and performance through the lens of linear independence among classifier votes in data streams. We propose that ensembles composed of linearly independent classifiers maximize representational capacity, particularly under a geometric model. We then generalize the importance of linear independence to the weighted majority voting problem. By modeling the probability of achieving linear independence among classifier outputs, we derive a theoretical framework that explains the trade-off between ensemble size and accuracy. Our analysis leads to a theoretical estimate of the ensemble size required to achieve a user-specified probability of linear independence. We validate our theory through experiments on both real-world and synthetic datasets using two ensemble methods, OzaBagging and GOOWE. Our results confirm that this theoretical estimate effectively identifies the point of performance saturation for robust ensembles like OzaBagging. Conversely, for complex weighting schemes like GOOWE, our framework reveals that high theoretical diversity can trigger algorithmic instability. Our implementation is publicly available to support reproducibility and future research.

