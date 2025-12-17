---
layout: default
title: Mosaic Pruning: A Hierarchical Framework for Generalizable Pruning of Mixture-of-Experts Models
---

# Mosaic Pruning: A Hierarchical Framework for Generalizable Pruning of Mixture-of-Experts Models

**arXiv**: [2511.19822v1](https://arxiv.org/abs/2511.19822) | [PDF](https://arxiv.org/pdf/2511.19822.pdf)

**作者**: Wentao Hu, Mingkuan Zhao, Shuangyong Song, Xiaoyan Zhu, Xin Lai, Jiayin Wang

---

## 💡 一句话要点

**提出Mosaic Pruning以解决稀疏专家模型剪枝的泛化性问题**

**关键词**: `稀疏专家模型` `模型剪枝` `泛化性` `聚类选择` `激活变异性评分`

## 📋 核心要点

1. 稀疏专家模型剪枝后跨域性能严重下降，需重复剪枝
2. 通过聚类选择构建功能互补专家集，提升模型泛化能力
3. 实验显示在通用和专用任务上性能显著优于现有方法

## 📄 摘要（原文）

> Sparse Mixture-of-Experts (SMoE) architectures have enabled a new frontier in scaling Large Language Models (LLMs), offering superior performance by activating only a fraction of their total parameters during inference. However, their practical deployment is severely hampered by substantial static memory overhead, as all experts must be loaded into memory. Existing post-training pruning methods, while reducing model size, often derive their pruning criteria from a single, general-purpose corpus. This leads to a critical limitation: a catastrophic performance degradation when the pruned model is applied to other domains, necessitating a costly re-pruning for each new domain. To address this generalization gap, we introduce Mosaic Pruning (MoP). The core idea of MoP is to construct a functionally comprehensive set of experts through a structured ``cluster-then-select" process. This process leverages a similarity metric that captures expert performance across different task domains to functionally cluster the experts, and subsequently selects the most representative expert from each cluster based on our proposed Activation Variability Score. Unlike methods that optimize for a single corpus, our proposed Mosaic Pruning ensures that the pruned model retains a functionally complementary set of experts, much like the tiles of a mosaic that together form a complete picture of the original model's capabilities, enabling it to handle diverse downstream tasks.Extensive experiments on various MoE models demonstrate the superiority of our approach. MoP significantly outperforms prior work, achieving a 7.24\% gain on general tasks and 8.92\% on specialized tasks like math reasoning and code generation.

