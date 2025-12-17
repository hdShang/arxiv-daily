---
layout: default
title: SPACE: Noise Contrastive Estimation Stabilizes Self-Play Fine-Tuning for Large Language Models
---

# SPACE: Noise Contrastive Estimation Stabilizes Self-Play Fine-Tuning for Large Language Models

**arXiv**: [2512.07175v1](https://arxiv.org/abs/2512.07175) | [PDF](https://arxiv.org/pdf/2512.07175.pdf)

**作者**: Yibo Wang, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Lijun Zhang

---

## 💡 一句话要点

**提出SPACE方法，通过噪声对比估计稳定自博弈微调，解决目标退化问题**

**关键词**: `自博弈微调` `噪声对比估计` `大语言模型` `稳定收敛` `分布对齐`

## 📋 核心要点

1. 现有自博弈微调方法基于奖励差距，忽略绝对值，导致目标退化与不稳定演化
2. SPACE将合成样本视为辅助，以二元分类区分真实样本，独立优化绝对奖励值
3. 实验显示SPACE在多种任务上显著提升性能，优于监督微调与差距方法，确保稳定收敛

## 📄 摘要（原文）

> Self-play fine-tuning has demonstrated promising abilities in adapting large language models (LLMs) to downstream tasks with limited real-world data. The basic principle is to iteratively refine the model with real samples and synthetic ones generated from itself. However, the existing methods primarily focus on the relative gaps between the rewards for two types of data, neglecting their absolute values. Through theoretical analysis, we identify that the gap-based methods suffer from unstable evolution, due to the potentially degenerated objectives. To address this limitation, we introduce a novel self-play fine-tuning method, namely Self-PlAy via Noise Contrastive Estimation (SPACE), which leverages noise contrastive estimation to capture the real-world data distribution. Specifically, SPACE treats synthetic samples as auxiliary components, and discriminates them from the real ones in a binary classification manner. As a result, SPACE independently optimizes the absolute reward values for each type of data, ensuring a consistently meaningful objective and thereby avoiding the instability issue. Theoretically, we show that the optimal solution of the objective in SPACE aligns with the underlying distribution of real-world data, and SPACE guarantees a provably stable convergence to the optimal distribution. Empirically, we show that SPACE significantly improves the performance of LLMs over various tasks, and outperforms supervised fine-tuning that employs much more real-world samples. Compared to gap-based self-play fine-tuning methods, SPACE exhibits remarkable superiority and stable evolution.

