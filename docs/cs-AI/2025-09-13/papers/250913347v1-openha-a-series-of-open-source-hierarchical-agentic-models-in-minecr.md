---
layout: default
title: "OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft"
---

# OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13347" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13347v1</a>
  <a href="https://arxiv.org/pdf/2509.13347.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13347v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13347v1', 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihao Wang, Muyao Li, Kaichen He, Xiangyu Wang, Zhancun Mu, Anji Liu, Yitao Liang

**分类**: cs.AI

**发布日期**: 2025-09-13

**🔗 代码/项目**: [GITHUB](https://github.com/CraftJarvis/OpenHA)

---

## 💡 一句话要点

**提出Chain of Action框架，解决Minecraft中通用智能体动作空间选择难题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Minecraft` `分层智能体` `动作空间` `视觉-语言-动作模型` `通用人工智能` `Chain of Action` `开放世界`

## 📋 核心要点

1. 现有端到端智能体面临动作空间选择难题，缺乏通用最优解，严重限制了智能体的泛化能力。
2. 提出Chain of Action (CoA) 框架，将高层规划和低层控制统一在单个VLA模型中，实现动作空间的灵活切换。
3. 实验表明，基于CoA训练的All-in-One智能体在多样任务中表现出色，超越了专门的基线模型，达到新的SOTA。

## 📝 摘要（中文）

本文针对开发具有能力的端到端可训练智能体中动作空间选择这一关键但未解决的挑战，首先对开放世界Minecraft中视觉-语言-动作（VLA）或分层智能体模型中突出的抽象动作空间和分词器进行了大规模、系统的比较。分析表明，没有单一的动作空间是普遍最优的；相反，最有效的抽象高度依赖于任务，这给构建通用智能体带来了困境。为了解决这个问题，我们引入了Chain of Action（CoA），这是一个新颖的框架，它在单个整体VLA模型中统一了高层规划和低层控制。CoA将抽象动作视为中间推理步骤，类似于思维链，指导最终可执行动作的生成，而不是将其视为单独策略的命令。此外，我们证明了使用CoA范式在各种动作空间混合上训练的All-in-One智能体学习到更鲁棒和泛化的策略。这种统一的智能体实现了新的最先进水平，提高了整体任务成功率，超过了强大的、专门的基线。为了促进可重复的研究，我们发布了OpenHA（开放分层智能体）套件，其中包括我们超过800个不同任务的综合基准、精选数据集、源代码以及所有预训练模型检查点，网址为https://github.com/CraftJarvis/OpenHA。

## 🔬 方法详解

**问题定义**：现有端到端可训练智能体在开放世界Minecraft中面临动作空间选择的难题。不同的任务需要不同的抽象动作空间，没有一种动作空间能够适用于所有任务。这使得构建通用智能体变得非常困难，因为需要针对不同的任务设计不同的策略，或者使用复杂的策略切换机制。现有方法难以兼顾效率和泛化性。

**核心思路**：论文的核心思路是将抽象动作视为中间推理步骤，类似于思维链（Chain of Thought）。通过将高层规划和低层控制统一在一个VLA模型中，使得智能体能够根据当前的任务和环境，动态地选择合适的动作空间，并生成最终的可执行动作。这样，智能体就可以在不同的任务之间进行灵活的切换，从而提高其泛化能力。

**技术框架**：OpenHA框架的核心是Chain of Action (CoA) 机制。整体架构包含一个大型的VLA模型，该模型接收视觉和语言输入，并输出一系列的抽象动作，这些抽象动作被视为中间推理步骤。然后，模型根据这些抽象动作生成最终的可执行动作。该框架允许使用不同的动作空间进行训练，并且可以在推理时动态地选择合适的动作空间。

**关键创新**：最重要的技术创新点在于将抽象动作视为中间推理步骤，而不是将其视为单独策略的命令。这种方法使得智能体能够更好地理解任务的目标，并根据当前的环境选择合适的动作。与现有方法的本质区别在于，CoA框架将高层规划和低层控制统一在一个模型中，避免了复杂的策略切换机制。

**关键设计**：在训练过程中，使用了多种不同的动作空间，并采用了一种混合训练策略，使得智能体能够学习到通用的策略。损失函数包括动作预测损失和任务完成损失。网络结构采用了Transformer架构，以便更好地处理视觉和语言输入。

## 📊 实验亮点

实验结果表明，基于CoA框架训练的All-in-One智能体在Minecraft的800多个不同任务中取得了显著的性能提升，超越了专门的基线模型，达到了新的state-of-the-art。具体而言，整体任务成功率得到了显著提高，证明了该方法的有效性和泛化能力。

## 🎯 应用场景

该研究成果可应用于游戏AI、机器人控制、自动驾驶等领域。通过学习不同任务的动作空间，智能体可以更好地适应复杂环境，完成各种任务。该研究为构建通用人工智能体提供了新的思路和方法，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The choice of action spaces is a critical yet unresolved challenge in developing capable, end-to-end trainable agents. This paper first presents a large-scale, systematic comparison of prominent abstracted action spaces and tokenizers for Vision-Language-Action (VLA) or hierarchical agent models in the open-ended Minecraft. Our analysis reveals that no single action space is universally optimal; instead, the most effective abstraction is highly task-dependent, creating a dilemma for building generalist agents. To resolve this, we introduce Chain of Action (CoA), a novel framework that unifies high-level planning and low-level control within a single, monolithic VLA model. CoA treats an abstracted action not as a command for a separate policy, but as an intermediate reasoning step--akin to a chain of thought--that guides the generation of the final, executable action. Furthermore, we demonstrate that an All-in-One agent trained on a diverse mixture of action spaces using the CoA paradigm learns a more robust and generalizable policy. This unified agent achieves a new state-of-the-art, improving the overall task success rate over strong, specialized baselines. To foster reproducible research, we release the OpenHA (Open Hierarchical Agents) suite, which includes our comprehensive benchmark of over 800 distinct tasks, curated datasets, source code, and all pretrained model checkpoints at https://github.com/CraftJarvis/OpenHA

