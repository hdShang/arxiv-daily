---
layout: default
title: "Artificial Phantasia: Evidence for Propositional Reasoning-Based Mental Imagery in Large Language Models"
---

# Artificial Phantasia: Evidence for Propositional Reasoning-Based Mental Imagery in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23108" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23108v1</a>
  <a href="https://arxiv.org/pdf/2509.23108.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23108v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23108v1', 'Artificial Phantasia: Evidence for Propositional Reasoning-Based Mental Imagery in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Morgan McCarty, Jorge Morales

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-27

**备注**: 30 pages,15 figures

---

## 💡 一句话要点

**提出基于命题推理的心智意象任务，评估大语言模型复杂认知能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `心智意象` `认知能力` `命题推理` `空间推理` `人工智能` `认知心理学`

## 📋 核心要点

1. 现有评估LLM认知能力的方法依赖于训练数据中已有的任务，无法充分挖掘其潜在的复杂认知能力。
2. 该研究设计了一种基于心智意象的认知任务，要求模型在没有视觉输入的情况下，仅通过文本指令完成空间推理。
3. 实验结果表明，先进的LLM在心智意象任务上的表现显著优于人类平均水平，证明了其潜在的非图像推理能力。

## 📝 摘要（中文）

本研究提出了一种新颖的方法，用于评估人工智能系统中复杂的认知行为。由于大语言模型（LLMs）在训练数据中已包含的任务以及仅使用自然语言即可完成的任务上表现最佳，因此限制了我们对其涌现的复杂认知能力的理解。本文创建了数十个认知心理学中经典心智意象任务的新项目。传统上，认知心理学家认为该任务只能通过视觉心智意象来解决（即，仅凭语言是不够的）。LLMs非常适合测试这个假设。首先，我们测试了几个最先进的LLMs，向文本模型提供书面指令，并要求它们报告在执行上述任务中的转换后产生的对象。然后，我们通过在完全相同的任务中测试100名人类受试者来创建基线。我们发现，最好的LLMs的表现明显高于平均人类水平。最后，我们测试了设置为不同推理水平的推理模型，发现当模型分配更多的推理tokens时，性能最强。这些结果表明，最好的LLMs可能具有完成依赖于意象的任务的能力，尽管其架构的非图像性质。我们的研究不仅证明了LLMs在执行新任务时涌现的认知能力，而且还为该领域提供了一项新任务，该任务为在其他方面已经非常强大的模型留下了很大的改进空间。最后，我们的发现重新引发了关于人类视觉意象表征形式的辩论，表明命题推理（或至少是非意象推理）可能足以完成长期以来被认为是依赖于意象的任务。

## 🔬 方法详解

**问题定义**：现有的大语言模型评估方法主要依赖于自然语言任务，这些任务可能已经包含在模型的训练数据中，无法有效评估模型是否具备真正的认知能力，特别是那些需要视觉心智意象才能解决的问题。传统的观点认为，某些认知任务，例如空间推理和物体操作，必须依赖于视觉心智意象才能完成，而语言本身是不够的。

**核心思路**：本研究的核心思路是利用认知心理学中经典的心智意象任务，设计一系列新的测试用例，并将其转化为纯文本指令，让大语言模型在没有视觉输入的情况下完成任务。通过比较模型和人类在这些任务上的表现，评估模型是否具备通过非图像方式（例如命题推理）解决问题的能力。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 设计新的心智意象任务，这些任务需要对物体进行一系列的空间变换，例如旋转、翻转等；2) 将这些任务转化为纯文本指令，输入到大语言模型中；3) 评估模型输出的答案是否正确，并与人类的表现进行比较；4) 通过调整模型的推理tokens数量，观察其对性能的影响。

**关键创新**：该研究的关键创新在于：1) 提出了一种新的评估LLM认知能力的方法，该方法不依赖于模型的训练数据，而是通过设计专门的心智意象任务来评估其推理能力；2) 证明了LLM可能具备通过非图像方式（例如命题推理）解决传统上被认为是依赖于视觉心智意象的任务的能力；3) 为LLM的研究提供了一个新的方向，即探索其在认知心理学领域的应用。

**关键设计**：研究中关键的设计包括：1) 心智意象任务的设计，需要保证任务的难度适中，既能考察模型的推理能力，又不会过于复杂；2) 文本指令的设计，需要清晰明确，避免歧义，确保模型能够正确理解任务的要求；3) 模型推理tokens数量的调整，通过增加推理tokens，可以提高模型的推理能力，但也会增加计算成本。

## 📊 实验亮点

实验结果表明，最先进的LLM在心智意象任务上的表现显著优于平均人类水平。此外，研究发现，增加模型的推理tokens数量可以显著提高其性能。这些结果表明，LLM可能具备通过非图像方式解决复杂认知问题的能力，挑战了传统认知心理学中关于心智意象的观点。

## 🎯 应用场景

该研究的潜在应用领域包括：1) 提升大语言模型的认知能力，使其能够更好地理解和解决现实世界中的问题；2) 探索人工智能在认知心理学领域的应用，例如模拟人类的认知过程；3) 为机器人技术提供新的思路，例如让机器人能够通过语言指令完成复杂的空间操作。该研究的实际价值在于，它为评估和提升大语言模型的认知能力提供了一种新的方法，并为人工智能的发展开辟了新的方向。未来，该研究可能会促进人工智能在认知科学、机器人技术等领域的广泛应用。

## 📄 摘要（原文）

> This study offers a novel approach for benchmarking complex cognitive behavior in artificial systems. Almost universally, Large Language Models (LLMs) perform best on tasks which may be included in their training data and can be accomplished solely using natural language, limiting our understanding of their emergent sophisticated cognitive capacities. In this work, we created dozens of novel items of a classic mental imagery task from cognitive psychology. A task which, traditionally, cognitive psychologists have argued is solvable exclusively via visual mental imagery (i.e., language alone would be insufficient). LLMs are perfect for testing this hypothesis. First, we tested several state-of-the-art LLMs by giving text-only models written instructions and asking them to report the resulting object after performing the transformations in the aforementioned task. Then, we created a baseline by testing 100 human subjects in exactly the same task. We found that the best LLMs performed significantly above average human performance. Finally, we tested reasoning models set to different levels of reasoning and found the strongest performance when models allocate greater amounts of reasoning tokens. These results provide evidence that the best LLMs may have the capability to complete imagery-dependent tasks despite the non-pictorial nature of their architectures. Our study not only demonstrates an emergent cognitive capacity in LLMs while performing a novel task, but it also provides the field with a new task that leaves lots of room for improvement in otherwise already highly capable models. Finally, our findings reignite the debate over the formats of representation of visual imagery in humans, suggesting that propositional reasoning (or at least non-imagistic reasoning) may be sufficient to complete tasks that were long-thought to be imagery-dependent.

