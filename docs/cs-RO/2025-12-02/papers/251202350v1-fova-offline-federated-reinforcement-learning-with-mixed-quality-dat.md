---
layout: default
title: FOVA: Offline Federated Reinforcement Learning with Mixed-Quality Data
---

# FOVA: Offline Federated Reinforcement Learning with Mixed-Quality Data

**arXiv**: [2512.02350v1](https://arxiv.org/abs/2512.02350) | [PDF](https://arxiv.org/pdf/2512.02350.pdf)

**作者**: Nan Qiao, Sheng Yue, Ju Ren, Yaoxue Zhang

---

## 💡 一句话要点

**提出FOVA框架以解决离线联邦强化学习中混合质量数据导致的性能下降问题**

**关键词**: `离线联邦强化学习` `混合质量数据` `投票机制` `优势加权回归` `策略改进`

## 📋 核心要点

1. 核心问题：现有离线联邦强化学习方法在混合质量数据（即客户端策略质量不一）下性能显著下降
2. 方法要点：引入投票机制识别高回报动作，基于优势加权回归构建一致训练目标
3. 实验或效果：理论分析证明策略改进，实验显示在基准测试中优于现有基线

## 📄 摘要（原文）

> Offline Federated Reinforcement Learning (FRL), a marriage of federated learning and offline reinforcement learning, has attracted increasing interest recently. Albeit with some advancement, we find that the performance of most existing offline FRL methods drops dramatically when provided with mixed-quality data, that is, the logging behaviors (offline data) are collected by policies with varying qualities across clients. To overcome this limitation, this paper introduces a new vote-based offline FRL framework, named FOVA. It exploits a \emph{vote mechanism} to identify high-return actions during local policy evaluation, alleviating the negative effect of low-quality behaviors from diverse local learning policies. Besides, building on advantage-weighted regression (AWR), we construct consistent local and global training objectives, significantly enhancing the efficiency and stability of FOVA. Further, we conduct an extensive theoretical analysis and rigorously show that the policy learned by FOVA enjoys strict policy improvement over the behavioral policy. Extensive experiments corroborate the significant performance gains of our proposed algorithm over existing baselines on widely used benchmarks.

