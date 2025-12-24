---
layout: default
title: "Too Big to Think: Capacity, Memorization, and Generalization in Pre-Trained Transformers"
---

# Too Big to Think: Capacity, Memorization, and Generalization in Pre-Trained Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09099" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09099v2</a>
  <a href="https://arxiv.org/pdf/2506.09099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09099v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09099v2', 'Too Big to Think: Capacity, Memorization, and Generalization in Pre-Trained Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joshua Barron, Devin White

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-10 (更新: 2025-06-17)

**备注**: Accepted for oral presentation to Tiny Titans: The next wave of On-Device Learning for Foundational Models Workshop at the 42nd International Conference on Machine Learning

---

## 💡 一句话要点

**探讨预训练变换器模型的记忆与泛化能力的关系**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `记忆与泛化` `变换器模型` `算术外推` `事实回忆` `模型容量` `预训练`

## 📋 核心要点

1. 现有大型语言模型在记忆与泛化能力之间存在权衡，导致模型在某一方面的性能提升可能会牺牲另一方的能力。
2. 本研究通过预训练容量有限的变换器模型，设计了两个合成任务，分别考察记忆与泛化的能力，揭示其内在关系。
3. 实验结果表明，小模型在外推能力上表现良好，但记忆能力不足；而大模型则相反，且中等容量模型也显示出向记忆的倾斜。

## 📝 摘要（中文）

在大型语言模型（LLMs）中，记忆与泛化之间的关系仍然是一个开放的研究领域，越来越多的证据表明二者密切相关。本研究通过从头开始预训练一系列容量有限的变换器模型，针对两个合成字符级任务进行探讨，分别考察泛化（通过算术外推）和记忆（通过事实回忆）。研究发现：小模型能够外推未见的算术案例，但无法记忆事实；而大模型则能够记忆但无法外推。中等容量模型表现出向记忆的转变。当同时训练两个任务时，无论模型大小，均未能成功外推。这些发现表明，预训练可能在本质上偏向于某种学习模式。通过在受控环境中隔离这些动态，本研究为模型容量如何影响学习行为提供了见解，并对小型语言模型的设计和部署具有更广泛的启示。

## 🔬 方法详解

**问题定义**：本研究旨在探讨大型语言模型中记忆与泛化之间的关系，现有方法未能有效平衡这两种能力，导致模型在特定任务上的表现不佳。

**核心思路**：通过预训练一系列不同容量的变换器模型，分别在算术外推和事实回忆任务上进行训练，以观察模型在记忆与泛化之间的权衡。

**技术框架**：研究设计了两个合成字符级任务，分别用于评估模型的泛化能力和记忆能力。模型在这两个任务上进行训练，观察其性能变化。

**关键创新**：本研究首次系统性地揭示了模型容量对记忆与泛化能力的影响，提出了在预训练过程中可能存在的学习模式偏向。

**关键设计**：模型的容量设置为小、中、大三种，采用不同的损失函数来分别优化记忆与泛化能力，实验中通过联合训练观察模型的表现。

## 📊 实验亮点

实验结果显示，小模型在算术外推任务上表现优异，而大模型则在事实记忆任务中占优。中等容量模型在这两者之间表现出向记忆的转变，且无论模型大小，联合训练后均未能成功实现外推，揭示了模型容量与学习模式之间的复杂关系。

## 🎯 应用场景

该研究的结果对小型语言模型的设计和应用具有重要意义，尤其是在需要平衡记忆与泛化能力的自然语言处理任务中。未来，研究者可以基于这些发现优化模型架构，以提升其在特定任务中的表现。

## 📄 摘要（原文）

> The relationship between memorization and generalization in large language models (LLMs) remains an open area of research, with growing evidence that the two are deeply intertwined. In this work, we investigate this relationship by pre-training a series of capacity-limited Transformer models from scratch on two synthetic character-level tasks designed to separately probe generalization (via arithmetic extrapolation) and memorization (via factual recall). We observe a consistent trade-off: small models extrapolate to unseen arithmetic cases but fail to memorize facts, while larger models memorize but fail to extrapolate. An intermediate-capacity model exhibits a similar shift toward memorization. When trained on both tasks jointly, no model (regardless of size) succeeds at extrapolation. These findings suggest that pre-training may intrinsically favor one learning mode over the other. By isolating these dynamics in a controlled setting, our study offers insight into how model capacity shapes learning behavior and offers broader implications for the design and deployment of small language models.

