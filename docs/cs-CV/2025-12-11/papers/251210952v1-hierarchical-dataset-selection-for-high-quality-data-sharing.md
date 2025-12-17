---
layout: default
title: Hierarchical Dataset Selection for High-Quality Data Sharing
---

# Hierarchical Dataset Selection for High-Quality Data Sharing

**arXiv**: [2512.10952v1](https://arxiv.org/abs/2512.10952) | [PDF](https://arxiv.org/pdf/2512.10952.pdf)

**作者**: Xiaona Zhou, Yingyan Zeng, Ran Jin, Ismini Lourentzou

---

## 💡 一句话要点

**提出DaSH方法以解决异构数据池中高效选择高质量数据集的问题**

**关键词**: `数据集选择` `层次化建模` `多源学习` `资源约束优化` `异构数据池`

## 📋 核心要点

1. 核心问题：现有方法忽略数据集间差异，难以在资源约束下选择整体数据集提升下游性能
2. 方法要点：DaSH通过层次化建模数据集和组级效用，从有限观测中实现高效泛化
3. 实验或效果：在Digit-Five和DomainNet基准上，DaSH准确率提升达26.2%，且探索步骤显著减少

## 📄 摘要（原文）

> The success of modern machine learning hinges on access to high-quality training data. In many real-world scenarios, such as acquiring data from public repositories or sharing across institutions, data is naturally organized into discrete datasets that vary in relevance, quality, and utility. Selecting which repositories or institutions to search for useful datasets, and which datasets to incorporate into model training are therefore critical decisions, yet most existing methods select individual samples and treat all data as equally relevant, ignoring differences between datasets and their sources. In this work, we formalize the task of dataset selection: selecting entire datasets from a large, heterogeneous pool to improve downstream performance under resource constraints. We propose Dataset Selection via Hierarchies (DaSH), a dataset selection method that models utility at both dataset and group (e.g., collections, institutions) levels, enabling efficient generalization from limited observations. Across two public benchmarks (Digit-Five and DomainNet), DaSH outperforms state-of-the-art data selection baselines by up to 26.2% in accuracy, while requiring significantly fewer exploration steps. Ablations show DaSH is robust to low-resource settings and lack of relevant datasets, making it suitable for scalable and adaptive dataset selection in practical multi-source learning workflows.

