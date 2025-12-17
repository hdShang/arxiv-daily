---
layout: default
title: GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation
---

# GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27210" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27210v1</a>
  <a href="https://arxiv.org/pdf/2510.27210.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27210v1" onclick="toggleFavorite(this, '2510.27210v1', 'GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Liu, Chongyu Wang, Rongjie Li, Yingchen Yu, Xuming He, Bai Song

**分类**: cs.AI, cs.CV

**发布日期**: 2025-10-31

**备注**: Published in NeurIPS 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://leon022.github.io/GUI-Rise)

---

## 💡 一句话要点

**GUI-Rise：提出一种融合结构化推理和历史总结的GUI导航框架，提升跨领域泛化能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI导航` `多模态大语言模型` `结构化推理` `历史总结` `强化学习` `Chain-of-Thought` `跨领域泛化`

## 📋 核心要点

1. 现有GUI导航代理在跨领域泛化能力和历史信息有效利用方面存在不足，限制了其应用范围。
2. GUI-Rise框架通过结构化推理生成Chain-of-Thought分析，指导动作预测和历史总结，提升决策质量。
3. 实验表明，GUI-Rise在标准基准上取得了最先进的结果，尤其是在领域外场景中表现出强大的泛化能力。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在GUI导航代理方面取得了进展，但现有方法在跨领域泛化和有效利用历史信息方面存在局限性。本文提出了一种推理增强框架，该框架系统地整合了结构化推理、动作预测和历史总结。结构化推理组件生成连贯的Chain-of-Thought分析，结合了进度估计和决策推理，为即时动作预测和未来步骤的紧凑历史总结提供信息。基于此框架，我们通过在伪标签轨迹上进行监督微调和使用群体相对策略优化（GRPO）进行强化学习，训练了一个GUI代理，名为GUI-Rise。该框架采用专门的奖励，包括一个历史感知目标，直接将总结质量与后续动作表现联系起来。在标准基准上的全面评估表明，在相同的训练数据条件下，该方法取得了最先进的结果，尤其是在领域外场景中表现出色。这些发现验证了我们的框架在各种GUI导航任务中保持稳健的推理和泛化能力。

## 🔬 方法详解

**问题定义**：现有基于多模态大型语言模型的GUI导航代理在跨领域泛化能力和历史信息利用方面存在不足。它们难以有效地处理不同类型的GUI界面，并且无法充分利用历史交互信息来指导未来的动作决策，导致性能下降。

**核心思路**：GUI-Rise的核心思路是引入结构化推理和历史总结机制，增强代理的决策能力和泛化能力。通过结构化推理，代理可以更清晰地理解当前任务的状态和目标，并生成连贯的Chain-of-Thought分析。通过历史总结，代理可以将过去的关键信息压缩成紧凑的表示，以便在未来的决策中使用。

**技术框架**：GUI-Rise框架包含三个主要组件：结构化推理、动作预测和历史总结。首先，结构化推理组件接收GUI界面图像和历史信息作为输入，生成Chain-of-Thought分析，包括进度估计和决策推理。然后，动作预测组件基于Chain-of-Thought分析预测下一步的动作。同时，历史总结组件将Chain-of-Thought分析压缩成紧凑的历史摘要，用于指导未来的推理和动作预测。整个框架通过监督微调和强化学习进行训练。

**关键创新**：GUI-Rise的关键创新在于将结构化推理和历史总结相结合，形成一个闭环的反馈机制。结构化推理不仅指导动作预测，还用于生成历史摘要，而历史摘要又反过来影响未来的推理过程。这种设计使得代理能够更好地理解任务状态、利用历史信息，并做出更明智的决策。

**关键设计**：GUI-Rise使用Chain-of-Thought提示工程来引导结构化推理。在训练过程中，使用伪标签轨迹进行监督微调，并使用群体相对策略优化（GRPO）进行强化学习。特别地，设计了一个历史感知奖励函数，将历史摘要的质量与后续动作的表现直接联系起来，鼓励代理生成更有用的历史摘要。

## 📊 实验亮点

GUI-Rise在标准GUI导航基准测试中取得了最先进的结果，尤其是在领域外场景中表现出色。在相同的训练数据条件下，GUI-Rise的性能显著优于现有方法，验证了其框架的有效性和泛化能力。实验结果表明，结构化推理和历史总结机制能够有效提升GUI导航代理的性能。

## 🎯 应用场景

GUI-Rise具有广泛的应用前景，可用于自动化软件测试、用户界面自动化、辅助技术等领域。它可以帮助用户更高效地完成各种GUI导航任务，提高工作效率和用户体验。未来，该技术有望应用于更复杂的交互式系统中，例如虚拟助手和机器人。

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have advanced GUI navigation agents, current approaches face limitations in cross-domain generalization and effective history utilization. We present a reasoning-enhanced framework that systematically integrates structured reasoning, action prediction, and history summarization. The structured reasoning component generates coherent Chain-of-Thought analyses combining progress estimation and decision reasoning, which inform both immediate action predictions and compact history summaries for future steps. Based on this framework, we train a GUI agent, \textbf{GUI-Rise}, through supervised fine-tuning on pseudo-labeled trajectories and reinforcement learning with Group Relative Policy Optimization (GRPO). This framework employs specialized rewards, including a history-aware objective, directly linking summary quality to subsequent action performance. Comprehensive evaluations on standard benchmarks demonstrate state-of-the-art results under identical training data conditions, with particularly strong performance in out-of-domain scenarios. These findings validate our framework's ability to maintain robust reasoning and generalization across diverse GUI navigation tasks. Code is available at https://leon022.github.io/GUI-Rise.

