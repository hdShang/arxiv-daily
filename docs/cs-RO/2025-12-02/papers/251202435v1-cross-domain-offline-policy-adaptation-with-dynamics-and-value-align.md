---
layout: default
title: Cross-Domain Offline Policy Adaptation with Dynamics- and Value-Aligned Data Filtering
---

# Cross-Domain Offline Policy Adaptation with Dynamics- and Value-Aligned Data Filtering

**arXiv**: [2512.02435v1](https://arxiv.org/abs/2512.02435) | [PDF](https://arxiv.org/pdf/2512.02435.pdf)

**作者**: Zhongjian Qiao, Rui Yang, Jiafei Lyu, Chenjia Bai, Xiu Li, Zhuoran Yang, Siyang Gao, Shuang Qiu

---

## 💡 一句话要点

**提出DVDF方法，通过动态与价值对齐的数据筛选，提升跨域离线强化学习的策略性能。**

**关键词**: `跨域离线强化学习` `动态对齐` `价值对齐` `数据筛选` `策略适应` `低数据设置`

## 📋 核心要点

1. 核心问题：跨域离线强化学习中，源域与目标域动态不匹配，仅合并数据可能导致性能下降。
2. 方法要点：设计DVDF方法，选择性共享源域中动态与价值对齐的高质量样本，优化策略学习。
3. 实验或效果：在多种动态偏移设置和低数据场景下，DVDF优于现有基线，表现稳定且优异。

## 📄 摘要（原文）

> Cross-Domain Offline Reinforcement Learning aims to train an agent deployed in the target environment, leveraging both a limited target domain dataset and a source domain dataset with (possibly) sufficient data coverage. Due to the underlying dynamics misalignment between the source and target domain, simply merging the data from two datasets may incur inferior performance. Recent advances address this issue by selectively sharing source domain samples that exhibit dynamics alignment with the target domain. However, these approaches focus solely on dynamics alignment and overlook \textit{value alignment}, i.e., selecting high-quality, high-value samples from the source domain. In this paper, we first demonstrate that both dynamics alignment and value alignment are essential for policy learning, by examining the limitations of the current theoretical framework for cross-domain RL and establishing a concrete sub-optimality gap of a policy trained on the source domain and evaluated on the target domain. Motivated by the theoretical insights, we propose to selectively share those source domain samples with both high dynamics and value alignment and present our \textbf{\underline{D}}ynamics- and \textbf{\underline{V}}alue-aligned \textbf{\underline{D}}ata \textbf{\underline{F}}iltering (DVDF) method. We design a range of dynamics shift settings, including kinematic and morphology shifts, and evaluate DVDF on various tasks and datasets, as well as in challenging extremely low-data settings where the target domain dataset contains only 5,000 transitions. Extensive experiments demonstrate that DVDF consistently outperforms prior strong baselines and delivers exceptional performance across multiple tasks and datasets.

