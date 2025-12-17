---
layout: default
title: EmbodiedBrain: Expanding Performance Boundaries of Task Planning for Embodied Intelligence
---

# EmbodiedBrain: Expanding Performance Boundaries of Task Planning for Embodied Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20578" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20578v1</a>
  <a href="https://arxiv.org/pdf/2510.20578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20578v1" onclick="toggleFavorite(this, '2510.20578v1', 'EmbodiedBrain: Expanding Performance Boundaries of Task Planning for Embodied Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ding Zou, Feifan Wang, Mengyu Ge, Siyuan Fan, Zongbing Zhang, Wei Chen, Lingfeng Wang, Zhongyou Hu, Wenrui Yan, Zhengwei Gao, Hao Wang, Weizhao Jin, Yu Zhang, Hainan Zhao, Mingliang Zhang, Xianxian Xi, Yaru Zhang, Wenyuan Li, Zhengguang Gao, Yurui Zhu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-23

**🔗 代码/项目**: [PROJECT_PAGE](https://zterobot.github.io/EmbodiedBrain.github.io)

---

## 💡 一句话要点

**EmbodiedBrain：通过Step-GRPO提升具身智能任务规划性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `任务规划` `视觉-语言模型` `强化学习` `长时程任务` `策略优化` `生成奖励模型`

## 📋 核心要点

1. 现有具身智能体依赖的LLM/MLLM在模型设计、实时性与性能平衡、评估指标真实性等方面存在局限。
2. EmbodiedBrain通过智能体对齐的数据结构和Step-GRPO训练方法，提升长时程任务规划能力。
3. 实验表明，EmbodiedBrain在通用、规划和端到端模拟基准测试中均优于现有方法，达到SOTA水平。

## 📝 摘要（中文）

为了实现通用人工智能（AGI），具身AI智能体需要在物理环境中具备强大的空间感知、有效的任务规划和自适应执行能力。然而，目前用于具身任务的大型语言模型（LLM）和多模态LLM（MLLM）存在模型设计与智能体需求脱节、实时延迟与性能之间的权衡、以及使用非真实的离线评估指标等关键限制。为了解决这些挑战，我们提出了EmbodiedBrain，一个参数规模分别为7B和32B的新型视觉-语言基础模型。我们的框架具有与智能体对齐的数据结构，并采用强大的训练方法，该方法集成了大规模监督微调（SFT）和步增强组相对策略优化（Step-GRPO），通过将先前的步骤作为引导前体来提高长时程任务的成功率。此外，我们还整合了一个全面的奖励系统，包括在基础设施层面加速的生成奖励模型（GRM），以提高训练效率。为了实现彻底的验证，我们建立了一个包含通用、规划和端到端模拟基准的三部分评估系统，重点是提出并开源了一个新的、具有挑战性的模拟环境。实验结果表明，EmbodiedBrain在所有指标上都取得了优异的性能，为具身基础模型建立了新的最先进水平。为了为下一代通用具身智能体铺平道路，我们开源了所有数据、模型权重和评估方法，可在https://zterobot.github.io/EmbodiedBrain.github.io上获取。

## 🔬 方法详解

**问题定义**：现有的大型语言模型和多模态大型语言模型在应用于具身智能任务时，存在着模型设计与智能体实际需求不匹配的问题。具体来说，这些模型往往难以兼顾实时性和高性能，并且依赖于非真实的离线评估指标，导致在真实物理环境中的表现不佳。因此，如何设计一个能够有效进行空间感知、任务规划和自适应执行的具身智能体，是本文要解决的核心问题。

**核心思路**：EmbodiedBrain的核心思路是构建一个与智能体对齐的视觉-语言基础模型，并通过一种新颖的训练方法来提升其长时程任务规划能力。这种方法的核心在于将先前的步骤作为引导前体，从而更好地利用历史信息，提高任务的成功率。此外，通过引入生成奖励模型（GRM）来加速训练过程，进一步提升模型的效率。

**技术框架**：EmbodiedBrain的整体框架包含以下几个主要模块：1) 一个视觉-语言基础模型，负责处理输入的多模态信息；2) 一个与智能体对齐的数据结构，用于更好地表示和处理具身任务相关的数据；3) 一个Step-GRPO训练模块，用于提升模型的长时程任务规划能力；4) 一个生成奖励模型（GRM），用于加速训练过程。整个流程是，首先通过视觉-语言模型处理环境信息，然后利用Step-GRPO进行策略优化，最后通过GRM进行奖励反馈，不断迭代提升模型性能。

**关键创新**：EmbodiedBrain最重要的技术创新点在于Step-Augumented Group Relative Policy Optimization (Step-GRPO) 方法。与传统的策略优化方法不同，Step-GRPO将先前的步骤作为引导前体，从而更好地利用历史信息，提高长时程任务的成功率。这种方法能够有效地解决传统方法在长时程任务中容易出现的梯度消失和奖励稀疏问题。

**关键设计**：在Step-GRPO中，关键的设计包括如何选择和利用先前的步骤作为引导前体，以及如何设计损失函数来优化策略。此外，生成奖励模型（GRM）的设计也至关重要，它需要能够准确地评估智能体的行为，并提供有效的奖励信号。具体的参数设置和网络结构细节在论文中有更详细的描述。

## 📊 实验亮点

EmbodiedBrain在各项评估指标上均取得了显著的性能提升，尤其是在长时程任务规划方面。实验结果表明，EmbodiedBrain在通用、规划和端到端模拟基准测试中均优于现有方法，并建立了新的SOTA。具体的性能数据和对比基线可在论文的实验部分找到。

## 🎯 应用场景

EmbodiedBrain的研究成果可广泛应用于机器人导航、家庭服务机器人、自动驾驶、智能制造等领域。通过提升具身智能体的任务规划和执行能力，可以实现更智能、更自主的机器人系统，从而提高生产效率、改善生活质量。未来，该研究有望推动通用人工智能的发展，使机器人能够更好地理解和适应复杂多变的环境。

## 📄 摘要（原文）

> The realization of Artificial General Intelligence (AGI) necessitates Embodied AI agents capable of robust spatial perception, effective task planning, and adaptive execution in physical environments. However, current large language models (LLMs) and multimodal LLMs (MLLMs) for embodied tasks suffer from key limitations, including a significant gap between model design and agent requirements, an unavoidable trade-off between real-time latency and performance, and the use of unauthentic, offline evaluation metrics. To address these challenges, we propose EmbodiedBrain, a novel vision-language foundation model available in both 7B and 32B parameter sizes. Our framework features an agent-aligned data structure and employs a powerful training methodology that integrates large-scale Supervised Fine-Tuning (SFT) with Step-Augumented Group Relative Policy Optimization (Step-GRPO), which boosts long-horizon task success by integrating preceding steps as Guided Precursors. Furthermore, we incorporate a comprehensive reward system, including a Generative Reward Model (GRM) accelerated at the infrastructure level, to improve training efficiency. For enable thorough validation, we establish a three-part evaluation system encompassing General, Planning, and End-to-End Simulation Benchmarks, highlighted by the proposal and open-sourcing of a novel, challenging simulation environment. Experimental results demonstrate that EmbodiedBrain achieves superior performance across all metrics, establishing a new state-of-the-art for embodied foundation models. Towards paving the way for the next generation of generalist embodied agents, we open-source all of our data, model weight, and evaluating methods, which are available at https://zterobot.github.io/EmbodiedBrain.github.io.

