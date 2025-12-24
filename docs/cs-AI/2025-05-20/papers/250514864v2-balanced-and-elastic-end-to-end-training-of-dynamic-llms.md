---
layout: default
title: Balanced and Elastic End-to-end Training of Dynamic LLMs
---

# Balanced and Elastic End-to-end Training of Dynamic LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14864" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14864v2</a>
  <a href="https://arxiv.org/pdf/2505.14864.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14864v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14864v2', 'Balanced and Elastic End-to-end Training of Dynamic LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamed Wahib, Muhammed Abdullah Soyturk, Didem Unat

**分类**: cs.DC, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-09-14)

**DOI**: [10.1145/3712285.3759775](https://doi.org/10.1145/3712285.3759775)

---

## 💡 一句话要点

**提出DynMo以解决大规模动态LLM训练中的负载不均问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态负载均衡` `大型语言模型` `分布式训练` `计算效率` `动态调整`

## 📋 核心要点

1. 现有方法在大规模分布式训练中常导致工作负载不均，影响训练效率。
2. 提出DynMo，通过动态负载均衡技术自适应地平衡计算负载，提升训练效率。
3. 实验结果显示，DynMo在多种场景下显著加速了动态GPT模型的训练，提升幅度高达4.52倍。

## 📝 摘要（中文）

为了减少大型语言模型的计算和内存开销，已有多种方法被提出，包括专家混合模型、逐步剪枝、动态冻结层、动态稀疏注意机制、早期退出和深度混合等。然而，这些方法在大规模分布式训练中常常导致工作负载不均，限制了它们的实际应用。本文提出了一种自主动态负载均衡解决方案DynMo，能够有效减少工作负载不均，并在管道并行训练中自适应地平衡计算负载。DynMo支持单节点多GPU系统和多节点GPU集群，能够在不牺牲训练吞吐量的情况下，将计算动态整合到更少的工作节点上。与静态分布式训练解决方案相比，DynMo在多种情况下显著加速了动态GPT模型的端到端训练。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型训练中的工作负载不均问题，现有方法在大规模分布式训练中效率低下，难以应用于实际场景。

**核心思路**：DynMo通过动态负载均衡技术，自动调整计算负载，确保各工作节点的计算量均衡，从而提升整体训练效率。

**技术框架**：DynMo的整体架构包括负载监测模块、动态调整模块和任务分配模块，能够实时监控各节点的负载情况，并根据需要调整计算任务的分配。

**关键创新**：DynMo的核心创新在于其自主动态负载均衡能力，能够在不牺牲训练吞吐量的情况下，将计算整合到更少的工作节点上，与传统静态方法相比，显著提升了训练效率。

**关键设计**：DynMo在设计中考虑了多种参数设置，包括负载监测频率、任务分配策略等，确保在不同训练场景下均能高效运行。

## 📊 实验亮点

实验结果表明，DynMo在多种动态LLM训练场景下显著提升了训练速度，具体表现为在专家混合模型中加速1.23倍，参数剪枝加速3.18倍，层冻结加速2.23倍，稀疏注意加速4.02倍，早期退出加速4.52倍，深度混合加速1.17倍，显示出其优越的性能。

## 🎯 应用场景

该研究的潜在应用领域包括大规模语言模型的训练和部署，尤其是在需要高效计算资源管理的场景中，如云计算平台和高性能计算集群。DynMo的动态负载均衡能力将为实际应用提供更高的训练效率和资源利用率，推动AI模型的快速迭代和应用落地。

## 📄 摘要（原文）

> To reduce the computational and memory overhead of Large Language Models, various approaches have been proposed. These include a) Mixture of Experts (MoEs), where token routing affects compute balance; b) gradual pruning of model parameters; c) dynamically freezing layers; d) dynamic sparse attention mechanisms; e) early exit of tokens as they pass through model layers; and f) Mixture of Depths (MoDs), where tokens bypass certain blocks. While these approaches are effective in reducing overall computation, they often introduce significant workload imbalance across workers. In many cases, this imbalance is severe enough to render the techniques impractical for large-scale distributed training, limiting their applicability to toy models due to poor efficiency.
>   We propose an autonomous dynamic load balancing solution, DynMo, which provably achieves maximum reduction in workload imbalance and adaptively equalizes compute loads across workers in pipeline-parallel training. In addition, DynMo dynamically consolidates computation onto fewer workers without sacrificing training throughput, allowing idle workers to be released back to the job manager. DynMo supports both single-node multi-GPU systems and multi-node GPU clusters, and can be used in practical deployment. Compared to static distributed training solutions such as Megatron-LM and DeepSpeed, DynMo accelerates the end-to-end training of dynamic GPT models by up to 1.23x for MoEs, 3.18x for parameter pruning, 2.23x for layer freezing, 4.02x for sparse attention, 4.52x for early exit, and 1.17x for MoDs.

