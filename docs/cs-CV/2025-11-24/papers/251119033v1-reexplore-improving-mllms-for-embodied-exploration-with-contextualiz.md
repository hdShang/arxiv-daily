---
layout: default
title: ReEXplore: Improving MLLMs for Embodied Exploration with Contextualized Retrospective Experience Replay
---

# ReEXplore: Improving MLLMs for Embodied Exploration with Contextualized Retrospective Experience Replay

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19033" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19033v1</a>
  <a href="https://arxiv.org/pdf/2511.19033.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19033v1" onclick="toggleFavorite(this, '2511.19033v1', 'ReEXplore: Improving MLLMs for Embodied Exploration with Contextualized Retrospective Experience Replay')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gengyuan Zhang, Mingcong Ding, Jingpei Wu, Ruotong Liao, Volker Tresp

**分类**: cs.CV

**发布日期**: 2025-11-24

**备注**: 8 main pages plus 13 pages Appendix

---

## 💡 一句话要点

**ReEXplore：利用情境化回顾经验回放改进MLLM在具身探索中的性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `具身探索` `多模态大语言模型` `经验回放` `分层决策` `机器人导航`

## 📋 核心要点

1. 现有基于MLLM的具身智能体依赖于预训练知识，缺乏对新环境的适应性，且训练成本高昂。
2. ReEXplore通过回顾性经验回放注入提炼的抽象经验，并采用分层前沿选择策略，提升探索效率。
3. 实验表明，ReEXplore在多个具身探索基准测试中，成功率和导航效率均显著优于现有MLLM基线。

## 📝 摘要（中文）

具身探索是一个目标驱动的过程，它要求具身智能体具备精细的感知和知识增强的决策能力。尽管最近的研究尝试利用MLLM进行探索，因为它们具有强大的感知和推理能力，但我们发现基于MLLM的具身智能体在探索新环境时仍然不尽如人意：（i）它们依赖于深刻但陈旧的预训练知识；（ii）基于训练的方法，如模仿学习或强化学习，对于具有稀疏结果奖励的长时程任务来说成本高昂；（iii）基于前沿的探索产生了一个巨大的、视觉上细微的动作空间，这使得MLLM难以做出可靠的决策。我们提出了ReEXplore，这是一个无需训练的框架，它在推理时执行回顾性经验回放，以注入提炼的、抽象的经验，并进行分层前沿选择，将前沿排序分解为由粗到精的决策。我们的方法能够实现稳健、可追溯和高效的探索。在多个具身探索基准测试中，ReEXplore在开源骨干网络下，在成功率和导航效率方面都比强大的MLLM基线提高了高达3倍的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决基于MLLM的具身智能体在未知环境中探索效率低下的问题。现有方法依赖于预训练知识，难以适应新环境；模仿学习和强化学习等训练方法成本高昂；基于前沿的探索产生庞大且细微的动作空间，导致决策困难。

**核心思路**：ReEXplore的核心思路是通过回顾性经验回放，将智能体过去探索的经验提炼成抽象知识，并在推理时注入，从而增强智能体对环境的理解和适应能力。同时，采用分层前沿选择策略，将复杂的动作空间分解为由粗到精的决策过程，降低决策难度。

**技术框架**：ReEXplore框架主要包含两个模块：回顾性经验回放和分层前沿选择。回顾性经验回放模块负责从历史经验中提取关键信息，并将其转化为抽象的知识表示。分层前沿选择模块则将前沿探索任务分解为多个层级，首先进行粗略的选择，然后逐步细化，最终确定最佳的探索方向。整个过程无需训练，可以在推理阶段直接应用。

**关键创新**：ReEXplore的关键创新在于将回顾性经验回放和分层前沿选择相结合，从而实现了高效、稳健且可追溯的具身探索。与现有方法相比，ReEXplore无需训练，能够更好地适应新环境，并且能够提供更清晰的决策过程。

**关键设计**：回顾性经验回放模块使用MLLM对历史经验进行编码和提炼，提取关键的视觉和语义信息。分层前沿选择模块采用多层感知机（MLP）对前沿进行排序，并根据排序结果选择最佳的探索方向。具体参数设置和损失函数等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

ReEXplore在多个具身探索基准测试中取得了显著的性能提升，成功率和导航效率均提高了高达3倍。该方法在开源骨干网络下进行了验证，表明其具有良好的通用性和可扩展性。实验结果表明，ReEXplore能够有效解决MLLM在具身探索中面临的挑战，并为未来的研究提供了新的思路。

## 🎯 应用场景

ReEXplore可应用于机器人导航、自动驾驶、搜索救援等领域。该研究能够提升智能体在未知环境中的探索效率和适应能力，降低对训练数据的依赖，具有重要的实际应用价值和广阔的未来发展前景。例如，在灾难救援场景中，机器人可以利用ReEXplore快速探索受灾区域，寻找幸存者。

## 📄 摘要（原文）

> Embodied exploration is a target-driven process that requires embodied agents to possess fine-grained perception and knowledge-enhanced decision making. While recent attempts leverage MLLMs for exploration due to their strong perceptual and reasoning abilities, we find that MLLM-based embodied agents remain suboptimal in exploring new environments: (i) they rely on profound but stale pre-trained knowledge, (ii) training-based approaches such as imitation learning or reinforcement learning are expensive for long-horizon tasks with sparse outcome rewards, and (iii) frontier-based exploration yields a large, visually nuanced action space that is difficult for MLLMs to make reliable decisions. We address these challenges with ReEXplore, a training-free framework that performs retrospective experience replay to inject distilled, abstract experience at inference time, and hierarchical frontier selection to decompose frontier ranking into coarse-to-fine decisions. Our approach enables robust, traceable, and efficient exploration. Across multiple embodied exploration benchmarks, ReEXplore yields great improvements over strong MLLM baselines, up to 3x higher performance in both success rate and in navigation efficiency under open-source backbones.

