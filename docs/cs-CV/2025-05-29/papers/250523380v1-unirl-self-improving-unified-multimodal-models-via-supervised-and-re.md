---
layout: default
title: "UniRL: Self-Improving Unified Multimodal Models via Supervised and Reinforcement Learning"
---

# UniRL: Self-Improving Unified Multimodal Models via Supervised and Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23380" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23380v1</a>
  <a href="https://arxiv.org/pdf/2505.23380.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23380v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23380v1', 'UniRL: Self-Improving Unified Multimodal Models via Supervised and Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijia Mao, Zhenheng Yang, Mike Zheng Shou

**分类**: cs.CV

**发布日期**: 2025-05-29

**🔗 代码/项目**: [GITHUB](https://github.com/showlab/UniRL)

---

## 💡 一句话要点

**提出UniRL以解决多模态模型后训练数据依赖问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `自我生成` `后训练` `监督学习` `强化学习` `生成与理解` `数据依赖` `模型优化`

## 📋 核心要点

1. 现有的多模态模型在预训练阶段依赖大量外部数据，计算成本高，且后训练方法通常受限于特定任务。
2. UniRL通过自我生成图像作为训练数据，消除了对外部数据的依赖，并实现生成与理解任务的相互促进。
3. 在Show-o和Janus模型上进行评估，UniRL分别取得了0.77和0.65的GenEval得分，显示出显著的性能提升。

## 📝 摘要（中文）

统一多模态大语言模型如Show-o和Janus在生成和理解任务上表现出色，但通常依赖于大规模数据集，并在预训练阶段需要大量计算。此外，现有的后训练方法往往依赖外部数据或仅限于特定任务的定制。本文提出了UniRL，一种自我改进的后训练方法，能够在每次迭代中生成图像并将其作为训练数据，而无需依赖任何外部图像数据。该方法使得生成和理解任务相互促进，生成的图像用于理解，理解结果则用于监督生成。我们探索了监督微调(SFT)和组相对策略优化(GRPO)来优化模型。UniRL具有三个主要优势：不需要外部图像数据、提高了任务性能并减少生成与理解之间的不平衡、仅需在后训练阶段增加少量训练步骤。我们在Show-o和Janus上评估UniRL，分别取得了0.77和0.65的GenEval得分。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态模型在后训练阶段对外部数据的依赖问题，现有方法在灵活性和通用性上存在不足。

**核心思路**：UniRL的核心思想是通过模型自我生成图像，利用生成的图像作为训练数据，避免了对外部图像数据的需求，同时促进生成与理解任务的相互提升。

**技术框架**：UniRL的整体架构包括生成模块和理解模块，生成模块负责从提示生成图像，理解模块则利用生成的图像进行理解任务，二者通过反馈机制相互优化。

**关键创新**：UniRL的主要创新在于其自我生成数据的能力，使得模型在训练过程中不断自我改进，区别于传统方法依赖外部数据的局限性。

**关键设计**：在模型训练中，采用了监督微调(SFT)和组相对策略优化(GRPO)作为优化策略，确保生成与理解任务的平衡，并通过少量额外训练步骤实现高效的后训练。

## 📊 实验亮点

在实验中，UniRL在Show-o和Janus模型上分别取得了0.77和0.65的GenEval得分，显示出显著的性能提升。这一结果表明，UniRL不仅提高了单一任务的表现，还有效地减少了生成与理解之间的性能不平衡。

## 🎯 应用场景

UniRL的研究成果在多个领域具有广泛的应用潜力，包括智能助手、自动内容生成、教育技术等。通过减少对外部数据的依赖，UniRL能够在资源有限的环境中实现高效的多模态学习，推动相关技术的普及与发展。

## 📄 摘要（原文）

> Unified multimodal large language models such as Show-o and Janus have achieved strong performance across both generation and understanding tasks. However, these models typically rely on large-scale datasets and require substantial computation during the pretraining stage. In addition, several post-training methods have been proposed, but they often depend on external data or are limited to task-specific customization. In this work, we introduce UniRL, a self-improving post-training approach. Our approach enables the model to generate images from prompts and use them as training data in each iteration, without relying on any external image data. Moreover, it enables the two tasks to enhance each other: the generated images are used for understanding, and the understanding results are used to supervise generation. We explore supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO) to optimize the models. UniRL offers three key advantages: (1) it requires no external image data, as all training samples are generated by the model itself during training; (2) it not only improves individual task performance, but also reduces the imbalance between generation and understanding; and (3) it requires only several additional training steps during the post-training stage. We evaluate UniRL on top of Show-o and Janus, achieving a GenEval score of 0.77 for Show-o and 0.65 for Janus. Code and models will be released in https://github.com/showlab/UniRL.

