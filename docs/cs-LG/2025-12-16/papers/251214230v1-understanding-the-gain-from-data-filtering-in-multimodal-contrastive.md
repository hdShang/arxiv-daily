---
layout: default
title: Understanding the Gain from Data Filtering in Multimodal Contrastive Learning
---

# Understanding the Gain from Data Filtering in Multimodal Contrastive Learning

**arXiv**: [2512.14230v1](https://arxiv.org/abs/2512.14230) | [PDF](https://arxiv.org/pdf/2512.14230.pdf)

**作者**: Divyansh Pareek, Sewoong Oh, Simon S. Du

**分类**: cs.LG, stat.ML

**发布日期**: 2025-12-16

**备注**: 40 pages, 8 figures, 1 table. This work is accepted to the Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025

---

## 💡 一句话要点

**提出基于教师模型的数据过滤方法，以提升多模态对比学习在噪声数据下的性能。**

**关键词**: `多模态对比学习` `数据过滤` `教师模型` `噪声数据` `理论分析` `表示学习` `双模态数据`

## 📋 核心要点

1. 核心问题：互联网规模多模态数据集中存在大量噪声和不匹配样本，影响对比学习性能。
2. 方法要点：提出基于教师模型的过滤方法，利用预训练模型评估数据质量，筛选高质量样本。
3. 实验或效果：理论证明过滤能显著降低误差，在η较大时误差上界为1/√(ηn)，η较小时为1/√n。

## 📝 摘要（中文）

现代多模态表示学习的成功依赖于互联网规模的数据集。由于大量原始网络数据质量较低，数据筛选已成为训练流程中的关键步骤。使用训练模型进行过滤（即基于教师的过滤）已成为一种成功的解决方案，它利用预训练模型计算质量分数。为了解释基于教师的过滤在经验上的成功，我们在标准双模态数据生成模型下刻画了过滤后对比学习的性能。设η∈(0,1]为n个配对样本中模态正确匹配的数据比例，我们利用线性对比学习设置来展示数据过滤的可证明益处：(i) 无过滤时的误差上界和下界为1/(η√n)，(ii) 在η较大时，基于教师过滤的误差上界为1/√(ηn)，在η较小时为1/√n。

## 🔬 方法详解

论文采用线性对比学习框架，核心方法为基于教师模型的数据过滤。整体框架包括：在标准双模态数据生成模型下，利用预训练教师模型计算每个样本的质量分数，根据分数筛选出高质量数据用于后续对比学习训练。关键技术创新点在于理论分析了过滤对误差的影响，证明了过滤能改善学习性能。与现有方法的主要区别在于，该方法不仅提供经验解决方案，还通过理论推导量化了过滤的益处，为数据筛选提供了理论依据。

## 📊 实验亮点

理论结果表明，无过滤时误差界为1/(η√n)，而基于教师过滤后，在η较大时误差上界降至1/√(ηn)，η较小时降至1/√n，显著提升了学习效率。

## 🎯 应用场景

该研究可应用于多模态表示学习领域，如视觉-语言模型训练、跨模态检索和生成任务，通过有效过滤噪声数据提升模型鲁棒性和性能，具有实际价值。

## 📄 摘要（原文）

> The success of modern multimodal representation learning relies on internet-scale datasets. Due to the low quality of a large fraction of raw web data, data curation has become a critical step in the training pipeline. Filtering using a trained model (i.e., teacher-based filtering) has emerged as a successful solution, leveraging a pre-trained model to compute quality scores. To explain the empirical success of teacher-based filtering, we characterize the performance of filtered contrastive learning under the standard bimodal data generation model. Denoting $η\in(0,1]$ as the fraction of data with correctly matched modalities among $n$ paired samples, we utilize a linear contrastive learning setup to show a provable benefit of data filtering: $(i)$ the error without filtering is upper and lower bounded by $\frac{1}{η\sqrt{n}}$, and $(ii)$ the error with teacher-based filtering is upper bounded by $\frac{1}{\sqrt{ηn}}$ in the large $η$ regime, and by $\frac{1}{\sqrt{n}}$ in the small $η$ regime.

