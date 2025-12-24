---
layout: default
title: "Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents"
---

# Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21252" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21252v1</a>
  <a href="https://arxiv.org/pdf/2506.21252.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21252v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21252v1', 'Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyi Men, Zhuoran Jin, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-26

**备注**: ACL 2025 Main

---

## 💡 一句话要点

**提出Agent-RewardBench以解决多模态智能体奖励建模问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态智能体` `奖励建模` `基准评估` `自我修正` `决策优化` `现实场景` `深度学习`

## 📋 核心要点

1. 现有多模态智能体缺乏外部反馈，导致自我修正和泛化能力不足。
2. 提出Agent-RewardBench基准，旨在评估多模态大型语言模型的奖励建模能力，涵盖感知、规划和安全等多个维度。
3. 实验结果显示，当前最先进的多模态模型在奖励建模任务中表现有限，强调了专门训练的必要性。

## 📝 摘要（中文）

随着多模态大型语言模型（MLLMs）的进步，多模态智能体在网页导航和具身智能等现实任务中展现出潜力。然而，由于缺乏外部反馈，这些智能体在自我修正和泛化方面面临挑战。使用奖励模型作为外部反馈是一种有前景的方法，但尚无明确的选择标准。因此，迫切需要建立一个针对智能体的奖励基准。为此，我们提出了Agent-RewardBench，这是一个旨在评估MLLMs奖励建模能力的基准。该基准具有三个关键特征：多维度和现实场景评估、逐步奖励评估以及适当的难度和高质量的数据采样。实验表明，即使是最先进的多模态模型表现有限，强调了在智能体奖励建模方面进行专门训练的必要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态智能体在缺乏外部反馈情况下的奖励建模问题。现有方法未能有效选择适合智能体的奖励模型，导致智能体在自我修正和泛化方面的能力不足。

**核心思路**：论文提出Agent-RewardBench基准，通过多维度评估和逐步奖励评估来提升智能体的奖励建模能力。这样的设计能够更细致地分析智能体在任务执行过程中的表现。

**技术框架**：整体架构包括三个主要模块：多维度评估模块，逐步奖励评估模块，以及数据采样与验证模块。多维度评估涵盖感知、规划和安全等场景，逐步奖励评估则关注任务执行的每一步。

**关键创新**：最重要的技术创新点在于引入了逐步奖励评估机制，使得对智能体能力的评估更加细致和全面。这与现有方法的整体评估方式形成了鲜明对比。

**关键设计**：在数据采样方面，论文从10个多样化模型中进行精心抽样，并通过人工验证确保数据的完整性。同时，难度控制策略被应用于任务设计，以保持挑战性并促进智能体的学习。

## 📊 实验亮点

实验结果表明，即使是当前最先进的多模态模型在Agent-RewardBench基准上表现有限，强调了在奖励建模方面进行专门训练的必要性。这一发现为未来的研究方向提供了重要的指导。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟助手等多模态智能体的开发。通过提升奖励建模能力，Agent-RewardBench能够帮助智能体在复杂的现实环境中更好地进行决策和自我优化，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> As Multimodal Large Language Models (MLLMs) advance, multimodal agents show promise in real-world tasks like web navigation and embodied intelligence. However, due to limitations in a lack of external feedback, these agents struggle with self-correction and generalization. A promising approach is to use reward models as external feedback, but there is no clear on how to select reward models for agents. Thus, there is an urgent need to build a reward bench targeted at agents. To address these challenges, we propose Agent-RewardBench, a benchmark designed to evaluate reward modeling ability in MLLMs. The benchmark is characterized by three key features: (1) Multiple dimensions and real-world agent scenarios evaluation. It covers perception, planning, and safety with 7 scenarios; (2) Step-level reward evaluation. It allows for the assessment of agent capabilities at the individual steps of a task, providing a more granular view of performance during the planning process; and (3) Appropriately difficulty and high-quality. We carefully sample from 10 diverse models, difficulty control to maintain task challenges, and manual verification to ensure the integrity of the data. Experiments demonstrate that even state-of-the-art multimodal models show limited performance, highlighting the need for specialized training in agent reward modeling. Code is available at github.

