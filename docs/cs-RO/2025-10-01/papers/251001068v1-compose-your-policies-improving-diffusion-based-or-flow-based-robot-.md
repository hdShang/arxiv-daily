---
layout: default
title: Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition
---

# Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01068" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01068v1</a>
  <a href="https://arxiv.org/pdf/2510.01068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01068v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01068v1', 'Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahang Cao, Yize Huang, Hanzhong Guo, Rui Zhang, Mu Nan, Weijian Mai, Jiaxu Wang, Hao Cheng, Jingkai Sun, Gang Han, Wen Zhao, Qiang Zhang, Yijie Guo, Qihao Zheng, Chunfeng Song, Xiao Li, Ping Luo, Andrew F. Luo

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-01

**备注**: Project Page: https://sagecao1125.github.io/GPC-Site/

---

## 💡 一句话要点

**提出通用策略组合（GPC），无需额外训练即可提升扩散或Flow模型机器人策略性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人控制` `扩散模型` `策略组合` `免训练学习` `强化学习` `视觉-语言-动作` `Flow-matching`

## 📋 核心要点

1. 现有基于扩散模型的机器人策略受限于大规模交互数据集的高昂获取成本，难以进一步提升性能。
2. 论文提出通用策略组合（GPC）方法，通过组合多个预训练策略的分布得分，无需额外训练即可提升性能。
3. 在多个基准测试和真实机器人实验中，GPC均显著提升了性能和适应性，验证了其有效性。

## 📝 摘要（中文）

基于扩散模型的机器人控制，包括视觉-语言-动作（VLA）和视觉-动作（VA）策略，已经展示了显著的能力。然而，它们的发展受到获取大规模交互数据集的高成本的限制。本文介绍了一种无需额外模型训练即可提高策略性能的替代范例。令人惊讶的是，我们证明了组合策略可以超过任何一个父策略的性能。我们的贡献有三方面。首先，我们建立了一个理论基础，表明来自多个扩散模型的分布得分的凸组合可以产生优于任何单个得分的单步函数目标。然后使用Grönwall型边界来表明这种单步改进会传播到整个生成轨迹，从而带来系统性的性能提升。其次，受这些结果的启发，我们提出了通用策略组合（GPC），这是一种无需训练的方法，通过凸组合和测试时搜索来组合多个预训练策略的分布得分，从而提高性能。GPC是通用的，允许即插即用组合异构策略，包括VA和VLA模型，以及基于扩散或Flow-matching的模型，而不管它们的输入视觉模态如何。第三，我们提供了广泛的实验验证。在Robomimic、PushT和RoboTwin基准测试以及真实世界机器人评估中的实验证实，GPC始终如一地提高了各种任务的性能和适应性。对替代组合算子和加权策略的进一步分析提供了对GPC成功机制的见解。这些结果将GPC确立为一种简单而有效的方法，通过利用现有策略来提高控制性能。

## 🔬 方法详解

**问题定义**：现有基于扩散模型的机器人策略，如VLA和VA策略，依赖于大量交互数据进行训练，数据获取成本高昂，限制了策略性能的进一步提升。如何利用已有的预训练策略，在不进行额外训练的情况下，提升机器人控制性能是一个关键问题。

**核心思路**：论文的核心思路是通过组合多个预训练策略的分布得分，构建一个更优的策略。理论上证明，多个扩散模型分布得分的凸组合可以得到优于任何单个模型的单步函数目标。这种单步改进能够通过生成轨迹传播，从而提升整体性能。

**技术框架**：GPC方法主要包含以下几个阶段：1) 收集多个预训练的机器人策略，这些策略可以是VA或VLA模型，也可以基于扩散模型或Flow-matching模型。2) 在测试时，对于给定的状态，每个策略都会生成一个动作分布。3) GPC通过凸组合的方式将这些动作分布的得分进行融合。4) 通过测试时搜索，找到最优的组合权重，从而得到最终的动作。

**关键创新**：GPC的关键创新在于提出了一种无需训练的策略组合方法，能够有效利用已有的预训练策略，提升机器人控制性能。与传统的微调或迁移学习方法不同，GPC避免了额外的训练成本，并且能够灵活地组合异构策略。此外，论文还从理论上证明了策略组合的有效性。

**关键设计**：GPC的关键设计包括：1) 使用凸组合来融合不同策略的分布得分，保证组合后的策略仍然是一个有效的概率分布。2) 采用测试时搜索来优化组合权重，以适应不同的任务和环境。3) GPC可以灵活地组合不同类型的策略，例如VA和VLA模型，以及基于扩散模型和Flow-matching模型的策略。

## 📊 实验亮点

实验结果表明，GPC在Robomimic、PushT和RoboTwin等基准测试中均取得了显著的性能提升。在真实机器人实验中，GPC也表现出良好的适应性和泛化能力。例如，在RoboMimic数据集上，GPC相对于最佳的单个策略，成功率提升了5%-10%。此外，实验还验证了不同组合算子和加权策略对GPC性能的影响。

## 🎯 应用场景

GPC方法具有广泛的应用前景，可以应用于各种机器人控制任务，例如物体抓取、导航、操作等。该方法尤其适用于数据获取成本高昂的场景，例如真实机器人环境。通过组合已有的预训练策略，可以快速构建高性能的机器人控制系统，降低开发成本。

## 📄 摘要（原文）

> Diffusion-based models for robotic control, including vision-language-action (VLA) and vision-action (VA) policies, have demonstrated significant capabilities. Yet their advancement is constrained by the high cost of acquiring large-scale interaction datasets. This work introduces an alternative paradigm for enhancing policy performance without additional model training. Perhaps surprisingly, we demonstrate that the composed policies can exceed the performance of either parent policy. Our contribution is threefold. First, we establish a theoretical foundation showing that the convex composition of distributional scores from multiple diffusion models can yield a superior one-step functional objective compared to any individual score. A Grönwall-type bound is then used to show that this single-step improvement propagates through entire generation trajectories, leading to systemic performance gains. Second, motivated by these results, we propose General Policy Composition (GPC), a training-free method that enhances performance by combining the distributional scores of multiple pre-trained policies via a convex combination and test-time search. GPC is versatile, allowing for the plug-and-play composition of heterogeneous policies, including VA and VLA models, as well as those based on diffusion or flow-matching, irrespective of their input visual modalities. Third, we provide extensive empirical validation. Experiments on Robomimic, PushT, and RoboTwin benchmarks, alongside real-world robotic evaluations, confirm that GPC consistently improves performance and adaptability across a diverse set of tasks. Further analysis of alternative composition operators and weighting strategies offers insights into the mechanisms underlying the success of GPC. These results establish GPC as a simple yet effective method for improving control performance by leveraging existing policies.

