---
layout: default
title: Jigsaw-R1: A Study of Rule-based Visual Reinforcement Learning with Jigsaw Puzzles
---

# Jigsaw-R1: A Study of Rule-based Visual Reinforcement Learning with Jigsaw Puzzles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23590" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23590v3</a>
  <a href="https://arxiv.org/pdf/2505.23590.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23590v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23590v3', 'Jigsaw-R1: A Study of Rule-based Visual Reinforcement Learning with Jigsaw Puzzles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zifu Wang, Junyi Zhu, Bo Tang, Zhiyu Li, Feiyu Xiong, Jiaqian Yu, Matthew B. Blaschko

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-05-29 (更新: 2025-10-11)

**备注**: TMLR 2025

**🔗 代码/项目**: [GITHUB](https://github.com/zifuwanggg/Jigsaw-R1)

---

## 💡 一句话要点

**提出基于规则的视觉强化学习方法以解决多模态学习挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉强化学习` `多模态学习` `拼图任务` `模型泛化` `复杂推理` `监督微调` `决策能力`

## 📋 核心要点

1. 现有方法在多模态学习中面临感知密集型任务的挑战，尤其是规则基础的视觉强化学习尚未得到充分研究。
2. 本研究通过拼图作为实验框架，探索基于规则的视觉强化学习，揭示了其在复杂决策中的有效性和泛化能力。
3. 实验结果显示，MLLMs在拼图任务中经过训练后能显著提高准确率，并在其他视觉任务中实现泛化，RL的表现优于传统的SFT方法。

## 📝 摘要（中文）

本研究探讨了基于规则的视觉强化学习（RL）在多模态大语言模型（MLLMs）中的应用，特别是在感知密集型任务中的挑战。通过使用拼图作为实验框架，我们发现MLLMs在简单拼图上初始表现接近随机猜测，但经过微调后能够实现接近完美的准确率，并能推广到复杂的未见配置。此外，拼图训练能够促进对其他视觉任务的泛化，且复杂推理模式在训练和任务难度增加时频率上升。我们的研究表明，RL在泛化能力上优于监督微调（SFT），初始的SFT冷启动阶段可能会阻碍后续的RL优化。

## 🔬 方法详解

**问题定义**：本研究旨在解决基于规则的视觉强化学习在多模态大语言模型中的应用挑战，尤其是在感知密集型任务中的表现不足。现有方法在处理复杂决策时常常依赖于直接回答，而忽视了推理过程。

**核心思路**：论文提出使用拼图作为结构化实验框架，通过调整难度和提供明确的真实答案，来研究MLLMs在视觉任务中的学习和泛化能力。这样的设计使得研究能够在控制变量的情况下深入探讨模型的推理能力。

**技术框架**：整体架构包括数据准备、模型训练和评估三个主要阶段。首先，构建拼图数据集并设置不同难度；其次，使用强化学习算法对模型进行训练；最后，通过评估模型在不同任务上的表现来验证其泛化能力。

**关键创新**：本研究的创新点在于揭示了复杂推理模式的存在是预先存在的，而非在训练过程中自发产生。与现有方法相比，强调了在视觉任务中RL的有效性，尤其是在泛化能力方面。

**关键设计**：在模型训练中，采用了特定的损失函数以优化拼图重组的准确性，并设计了适应不同任务配置的训练策略，确保模型能够在多样化的视觉任务中表现出色。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，经过训练的MLLMs在简单拼图任务上的准确率从接近随机猜测提升至接近完美。此外，研究表明，RL在泛化能力上优于监督微调，且初始的SFT冷启动阶段可能会对后续的RL优化产生负面影响。

## 🎯 应用场景

该研究的潜在应用领域包括教育、游戏设计和机器人视觉等。通过提高多模态学习模型在视觉任务中的表现，能够推动智能系统在复杂环境中的决策能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The application of rule-based reinforcement learning (RL) to multimodal large language models (MLLMs) introduces unique challenges and potential deviations from findings in text-only domains, particularly for perception-heavy tasks. This paper provides a comprehensive study of rule-based visual RL, using jigsaw puzzles as a structured experimental framework. Jigsaw puzzles offer inherent ground truth, adjustable difficulty, and demand complex decision-making, making them ideal for this study. Our research reveals several key findings: \textit{Firstly,} we find that MLLMs, initially performing near to random guessing on the simplest jigsaw puzzles, achieve near-perfect accuracy and generalize to complex, unseen configurations through fine-tuning. \textit{Secondly,} training on jigsaw puzzles can induce generalization to other visual tasks, with effectiveness tied to specific task configurations. \textit{Thirdly,} MLLMs can learn and generalize with or without explicit reasoning, though open-source models often favor direct answering. Consequently, even when trained for step-by-step reasoning, they can ignore the thinking process in deriving the final answer. \textit{Fourthly,} we observe that complex reasoning patterns appear to be pre-existing rather than emergent, with their frequency increasing alongside training and task difficulty. \textit{Finally,} our results demonstrate that RL exhibits more effective generalization than Supervised Fine-Tuning (SFT), and an initial SFT cold start phase can hinder subsequent RL optimization. Although these observations are based on jigsaw puzzles and may vary across other visual tasks, this research contributes a valuable piece of jigsaw to the larger puzzle of collective understanding rule-based visual RL and its potential in multimodal learning. The code is available at: https://github.com/zifuwanggg/Jigsaw-R1

