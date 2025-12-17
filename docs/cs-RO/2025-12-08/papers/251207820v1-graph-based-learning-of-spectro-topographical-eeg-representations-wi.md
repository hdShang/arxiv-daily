---
layout: default
title: Graph-Based Learning of Spectro-Topographical EEG Representations with Gradient Alignment for Brain-Computer Interfaces
---

# Graph-Based Learning of Spectro-Topographical EEG Representations with Gradient Alignment for Brain-Computer Interfaces

**arXiv**: [2512.07820v1](https://arxiv.org/abs/2512.07820) | [PDF](https://arxiv.org/pdf/2512.07820.pdf)

**作者**: Prithila Angkan, Amin Jalali, Paul Hungler, Ali Etemad

---

## 💡 一句话要点

**提出基于图卷积网络与梯度对齐的脑电表征学习方法，用于脑机接口任务。**

**关键词**: `脑机接口` `图卷积网络` `脑电表征学习` `梯度对齐` `多域信息融合`

## 📋 核心要点

1. 核心问题：脑电信号具有时间动态性和个体敏感性，导致类间可分性低。
2. 方法要点：融合频域地形图和时频谱图，结合中心损失和成对差异损失，并采用梯度对齐策略。
3. 实验或效果：在三个公开脑电数据集上验证有效性，并通过消融研究分析组件影响。

## 📄 摘要（原文）

> We present a novel graph-based learning of EEG representations with gradient alignment (GEEGA) that leverages multi-domain information to learn EEG representations for brain-computer interfaces. Our model leverages graph convolutional networks to fuse embeddings from frequency-based topographical maps and time-frequency spectrograms, capturing inter-domain relationships. GEEGA addresses the challenge of achieving high inter-class separability, which arises from the temporally dynamic and subject-sensitive nature of EEG signals by incorporating the center loss and pairwise difference loss. Additionally, GEEGA incorporates a gradient alignment strategy to resolve conflicts between gradients from different domains and the fused embeddings, ensuring that discrepancies, where gradients point in conflicting directions, are aligned toward a unified optimization direction. We validate the efficacy of our method through extensive experiments on three publicly available EEG datasets: BCI-2a, CL-Drive and CLARE. Comprehensive ablation studies further highlight the impact of various components of our model.

