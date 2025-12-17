---
layout: default
title: DiRe: Diversity-promoting Regularization for Dataset Condensation
---

# DiRe: Diversity-promoting Regularization for Dataset Condensation

**arXiv**: [2512.13083v1](https://arxiv.org/abs/2512.13083) | [PDF](https://arxiv.org/pdf/2512.13083.pdf)

**作者**: Saumyaranjan Mohanty, Aravind Reddy, Konda Reddy Mopuri

---

## 💡 一句话要点

**提出多样性正则化器DiRe以提升数据集压缩中的合成数据集多样性**

**关键词**: `数据集压缩` `多样性正则化` `余弦相似度` `欧氏距离` `合成数据集` `泛化性能`

## 📋 核心要点

1. 核心问题：现有数据集压缩方法合成数据集冗余度高，缺乏多样性。
2. 方法要点：设计基于余弦相似度和欧氏距离的多样性正则化器，可即插即用于多种先进压缩方法。
3. 实验或效果：在CIFAR-10至ImageNet-1K等基准数据集上，提升压缩方法的泛化性能和多样性指标。

## 📄 摘要（原文）

> In Dataset Condensation, the goal is to synthesize a small dataset that replicates the training utility of a large original dataset. Existing condensation methods synthesize datasets with significant redundancy, so there is a dire need to reduce redundancy and improve the diversity of the synthesized datasets. To tackle this, we propose an intuitive Diversity Regularizer (DiRe) composed of cosine similarity and Euclidean distance, which can be applied off-the-shelf to various state-of-the-art condensation methods. Through extensive experiments, we demonstrate that the addition of our regularizer improves state-of-the-art condensation methods on various benchmark datasets from CIFAR-10 to ImageNet-1K with respect to generalization and diversity metrics.

