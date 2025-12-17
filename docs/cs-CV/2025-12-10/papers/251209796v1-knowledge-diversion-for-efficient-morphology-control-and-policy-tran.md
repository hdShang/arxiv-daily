---
layout: default
title: Knowledge Diversion for Efficient Morphology Control and Policy Transfer
---

# Knowledge Diversion for Efficient Morphology Control and Policy Transfer

**arXiv**: [2512.09796v1](https://arxiv.org/abs/2512.09796) | [PDF](https://arxiv.org/pdf/2512.09796.pdf)

**作者**: Fu Feng, Ruixiao Shi, Yucheng Xie, Jianlu Shen, Jing Wang, Xin Geng

---

## 💡 一句话要点

**提出DivMorph，通过知识分流实现高效形态控制和策略迁移**

**关键词**: `通用形态控制` `知识分流` `Transformer控制器` `策略迁移` `模块化训练`

## 📋 核心要点

1. 核心问题：通用形态控制中Transformer控制器计算成本高，跨任务泛化能力有限
2. 方法要点：利用SVD分解权重为因子单元，通过动态软门控分离共享和特定知识
3. 实验或效果：在跨任务迁移中样本效率提升3倍，单智能体部署模型大小减少17倍

## 📄 摘要（原文）

> Universal morphology control aims to learn a universal policy that generalizes across heterogeneous agent morphologies, with Transformer-based controllers emerging as a popular choice. However, such architectures incur substantial computational costs, resulting in high deployment overhead, and existing methods exhibit limited cross-task generalization, necessitating training from scratch for each new task. To this end, we propose \textbf{DivMorph}, a modular training paradigm that leverages knowledge diversion to learn decomposable controllers. DivMorph factorizes randomly initialized Transformer weights into factor units via SVD prior to training and employs dynamic soft gating to modulate these units based on task and morphology embeddings, separating them into shared \textit{learngenes} and morphology- and task-specific \textit{tailors}, thereby achieving knowledge disentanglement. By selectively activating relevant components, DivMorph enables scalable and efficient policy deployment while supporting effective policy transfer to novel tasks. Extensive experiments demonstrate that DivMorph achieves state-of-the-art performance, achieving a 3$\times$ improvement in sample efficiency over direct finetuning for cross-task transfer and a 17$\times$ reduction in model size for single-agent deployment.

