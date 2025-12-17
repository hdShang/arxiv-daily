---
layout: default
title: Asymptotic analysis of shallow and deep forgetting in replay with Neural Collapse
---

# Asymptotic analysis of shallow and deep forgetting in replay with Neural Collapse

**arXiv**: [2512.07400v1](https://arxiv.org/abs/2512.07400) | [PDF](https://arxiv.org/pdf/2512.07400.pdf)

**作者**: Giulia Lanzillotta, Damiano Meier, Thomas Hofmann

---

## 💡 一句话要点

**扩展神经坍缩框架分析经验回放中浅层与深层遗忘的不对称性**

**关键词**: `持续学习` `经验回放` `神经坍缩` `遗忘分析` `特征几何` `统计伪影`

## 📋 核心要点

1. 持续学习中神经网络常保留过去任务的线性可分表示，但输出预测失败，定义为浅层与深层遗忘的差距。
2. 揭示经验回放中不对称性：小缓冲区可锚定特征几何防止深层遗忘，但缓解浅层遗忘需更大容量。
3. 扩展神经坍缩框架至序列设置，证明非零回放分数渐近保证线性可分性，而小缓冲区导致统计伪影。

## 📄 摘要（原文）

> A persistent paradox in continual learning (CL) is that neural networks often retain linearly separable representations of past tasks even when their output predictions fail. We formalize this distinction as the gap between deep feature-space and shallow classifier-level forgetting. We reveal a critical asymmetry in Experience Replay: while minimal buffers successfully anchor feature geometry and prevent deep forgetting, mitigating shallow forgetting typically requires substantially larger buffer capacities. To explain this, we extend the Neural Collapse framework to the sequential setting. We characterize deep forgetting as a geometric drift toward out-of-distribution subspaces and prove that any non-zero replay fraction asymptotically guarantees the retention of linear separability. Conversely, we identify that the "strong collapse" induced by small buffers leads to rank-deficient covariances and inflated class means, effectively blinding the classifier to true population boundaries. By unifying CL with out-of-distribution detection, our work challenges the prevailing reliance on large buffers, suggesting that explicitly correcting these statistical artifacts could unlock robust performance with minimal replay.

