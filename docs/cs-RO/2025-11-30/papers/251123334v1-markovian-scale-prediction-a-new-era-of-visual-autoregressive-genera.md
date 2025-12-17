---
layout: default
title: Markovian Scale Prediction: A New Era of Visual Autoregressive Generation
---

# Markovian Scale Prediction: A New Era of Visual Autoregressive Generation

**arXiv**: [2511.23334v1](https://arxiv.org/abs/2511.23334) | [PDF](https://arxiv.org/pdf/2511.23334.pdf)

**作者**: Yu Zhang, Jingyi Liu, Yiwei Shi, Qi Zhang, Duoqian Miao, Changwei Wang, Longbing Cao

---

## 💡 一句话要点

**提出Markov-VAR以解决视觉自回归生成中全上下文依赖的计算效率问题**

**关键词**: `视觉自回归生成` `马尔可夫过程` `尺度预测` `计算效率优化` `图像生成`

## 📋 核心要点

1. 核心问题：全上下文依赖导致计算效率低下和内存开销大，限制VAR的实用性和可扩展性。
2. 方法要点：将VAR重构为非全上下文马尔可夫过程，通过滑动窗口压缩历史信息为紧凑向量，实现马尔可夫尺度预测。
3. 实验或效果：在ImageNet上，Markov-VAR降低FID 10.5%（256×256），减少峰值内存消耗83.8%（1024×1024）。

## 📄 摘要（原文）

> Visual AutoRegressive modeling (VAR) based on next-scale prediction has revitalized autoregressive visual generation. Although its full-context dependency, i.e., modeling all previous scales for next-scale prediction, facilitates more stable and comprehensive representation learning by leveraging complete information flow, the resulting computational inefficiency and substantial overhead severely hinder VAR's practicality and scalability. This motivates us to develop a new VAR model with better performance and efficiency without full-context dependency. To address this, we reformulate VAR as a non-full-context Markov process, proposing Markov-VAR. It is achieved via Markovian Scale Prediction: we treat each scale as a Markov state and introduce a sliding window that compresses certain previous scales into a compact history vector to compensate for historical information loss owing to non-full-context dependency. Integrating the history vector with the Markov state yields a representative dynamic state that evolves under a Markov process. Extensive experiments demonstrate that Markov-VAR is extremely simple yet highly effective: Compared to VAR on ImageNet, Markov-VAR reduces FID by 10.5% (256 $\times$ 256) and decreases peak memory consumption by 83.8% (1024 $\times$ 1024). We believe that Markov-VAR can serve as a foundation for future research on visual autoregressive generation and other downstream tasks.

