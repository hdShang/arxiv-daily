---
layout: default
title: SEAL: Semantic-Aware Hierarchical Learning for Generalized Category Discovery
---

# SEAL: Semantic-Aware Hierarchical Learning for Generalized Category Discovery

**arXiv**: [2510.18740v1](https://arxiv.org/abs/2510.18740) | [PDF](https://arxiv.org/pdf/2510.18740.pdf)

**作者**: Zhenqi He, Yuanpei Liu, Kai Han

---

## 💡 一句话要点

**提出SEAL框架以解决广义类别发现中的语义层次利用问题**

**关键词**: `广义类别发现` `语义层次学习` `软对比学习` `跨粒度一致性` `细粒度分类`

## 📋 核心要点

1. 核心问题：广义类别发现旨在对部分标注数据集中的未知和已知类图像进行分类
2. 方法要点：利用自然层次结构进行语义感知的层次学习和软负样本对比学习
3. 实验或效果：在细粒度基准上实现SOTA性能，并展示在粗粒度数据集上的泛化能力

## 📄 摘要（原文）

> This paper investigates the problem of Generalized Category Discovery (GCD).
> Given a partially labelled dataset, GCD aims to categorize all unlabelled
> images, regardless of whether they belong to known or unknown classes. Existing
> approaches typically depend on either single-level semantics or manually
> designed abstract hierarchies, which limit their generalizability and
> scalability. To address these limitations, we introduce a SEmantic-aware
> hierArchical Learning framework (SEAL), guided by naturally occurring and
> easily accessible hierarchical structures. Within SEAL, we propose a
> Hierarchical Semantic-Guided Soft Contrastive Learning approach that exploits
> hierarchical similarity to generate informative soft negatives, addressing the
> limitations of conventional contrastive losses that treat all negatives
> equally. Furthermore, a Cross-Granularity Consistency (CGC) module is designed
> to align the predictions from different levels of granularity. SEAL
> consistently achieves state-of-the-art performance on fine-grained benchmarks,
> including the SSB benchmark, Oxford-Pet, and the Herbarium19 dataset, and
> further demonstrates generalization on coarse-grained datasets. Project page:
> https://visual-ai.github.io/seal/

