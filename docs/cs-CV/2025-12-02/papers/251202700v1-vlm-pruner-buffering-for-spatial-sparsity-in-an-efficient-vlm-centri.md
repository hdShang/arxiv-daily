---
layout: default
title: VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm
---

# VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm

**arXiv**: [2512.02700v1](https://arxiv.org/abs/2512.02700) | [PDF](https://arxiv.org/pdf/2512.02700.pdf)

**作者**: Zhenkai Wu, Xiaowen Ma, Zhenliang Ni, Dengming Zhang, Han Shu, Xin Jiang, Xinghao Chen

---

## 💡 一句话要点

**提出VLM-Pruner以解决视觉语言模型在移动设备部署中的计算成本问题**

**关键词**: `视觉语言模型` `令牌剪枝` `空间稀疏性` `计算效率` `移动部署`

## 📋 核心要点

1. 核心问题：视觉语言模型视觉令牌数量大导致计算成本高，现有剪枝方法忽视令牌间冗余和空间关系，导致保留令牌稀疏或重复
2. 方法要点：采用离心令牌剪枝范式平衡冗余和空间稀疏性，设计缓冲空间稀疏性准则延迟选择远距离令牌，并行贪婪策略高效选择令牌
3. 实验或效果：在五种视觉语言模型上以88.9%剪枝率优于基线，实现端到端推理加速

## 📄 摘要（原文）

> Vision-language models (VLMs) excel at image understanding tasks, but the large number of visual tokens imposes significant computational costs, hindering deployment on mobile devices. Many pruning methods rely solely on token importance and thus overlook inter-token redundancy, retaining numerous duplicated tokens and wasting capacity. Although some redundancy-aware approaches have been proposed, they often ignore the spatial relationships among visual tokens. This can lead to overly sparse selections of retained tokens that fail to adequately cover the regions of target objects. To address these limitations, we propose VLM-Pruner, a training-free token pruning algorithm that explicitly balances redundancy and spatial sparsity. We introduce a centrifugal token pruning paradigm that enables near-to-far selection while prioritizing the preservation of fine-grained object details. Moreover, we design a Buffering for Spatial Sparsity (BSS) criterion that defers the selection of spatially distant tokens. We further adopt a parallel greedy strategy to conduct token selection efficiently. To mitigate information loss from pruning, we selectively fuse salient information from the discarded tokens into the retained ones. Comprehensive comparisons demonstrate that VLM-Pruner consistently outperforms strong baselines across five VLMs with an 88.9\% pruning rate, while delivering an end-to-end inference speedup.

