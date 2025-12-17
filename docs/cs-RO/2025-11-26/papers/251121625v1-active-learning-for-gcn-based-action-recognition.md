---
layout: default
title: Active Learning for GCN-based Action Recognition
---

# Active Learning for GCN-based Action Recognition

**arXiv**: [2511.21625v1](https://arxiv.org/abs/2511.21625) | [PDF](https://arxiv.org/pdf/2511.21625.pdf)

**作者**: Hichem Sahbi

---

## 💡 一句话要点

**提出标签高效GCN模型，通过主动学习解决骨架动作识别中标注数据稀缺问题。**

**关键词**: `主动学习` `图卷积网络` `骨架动作识别` `标签效率` `对抗策略`

## 📋 核心要点

1. 核心问题：GCN在骨架动作识别中依赖大量标注数据，但实际场景中数据稀缺。
2. 方法要点：开发对抗性采集函数选择信息样本，并引入双向稳定GCN架构。
3. 实验或效果：在多个基准测试中，模型相比先前工作实现显著性能提升。

## 📄 摘要（原文）

> Despite the notable success of graph convolutional networks (GCNs) in skeleton-based action recognition, their performance often depends on large volumes of labeled data, which are frequently scarce in practical settings. To address this limitation, we propose a novel label-efficient GCN model. Our work makes two primary contributions. First, we develop a novel acquisition function that employs an adversarial strategy to identify a compact set of informative exemplars for labeling. This selection process balances representativeness, diversity, and uncertainty. Second, we introduce bidirectional and stable GCN architectures. These enhanced networks facilitate a more effective mapping between the ambient and latent data spaces, enabling a better understanding of the learned exemplar distribution. Extensive evaluations on two challenging skeleton-based action recognition benchmarks reveal significant improvements achieved by our label-efficient GCNs compared to prior work.

