---
layout: default
title: Describe Anything Anywhere At Any Moment
---

# Describe Anything Anywhere At Any Moment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00565" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00565v1</a>
  <a href="https://arxiv.org/pdf/2512.00565.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00565v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.00565v1', 'Describe Anything Anywhere At Any Moment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicolas Gorlo, Lukas Schmid, Luca Carlone

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-11-29

**备注**: 14 pages, 5 figures, 6 tables

---

## 💡 一句话要点

**提出DAAAM框架，实现大规模场景下任意时空位置的实时语义描述与推理。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `4D场景理解` `时空记忆` `场景图` `语义描述` `机器人导航`

## 📋 核心要点

1. 现有方法在生成丰富的开放词汇描述时，难以兼顾3D场景中实时性能，面临两难。
2. DAAAM通过优化的前端从局部字幕模型推断语义描述，并构建分层4D场景图，实现高效时空记忆。
3. 实验表明，DAAAM在时空问答和任务执行方面均优于现有技术，并在OC-NaVQA上显著提升。

## 📝 摘要（中文）

本文提出了一种名为“Describe Anything, Anywhere, at Any Moment (DAAAM)”的新型时空记忆框架，用于大规模和实时的4D场景理解。DAAAM引入了一种基于优化的前端，利用局部字幕模型（如Describe Anything Model (DAM)）推断详细的语义描述，并通过批量处理将在线处理的推理速度提高了一个数量级。它利用这种语义理解来构建一个分层的4D场景图（SG），该场景图作为一个有效的全局空间和时间一致的记忆表示。DAAAM构建具有详细的、几何对齐的描述的4D SG，同时保持实时性能。我们展示了DAAAM的4D SG与用于推理和推理的工具调用代理良好地接口。我们在NaVQA基准测试中对时空问答的复杂任务进行了全面评估，并展示了其在SG3D基准测试中对顺序任务接地的泛化能力。我们进一步策划了一个扩展的OC-NaVQA基准测试，用于大规模和长时间评估。DAAAM在这两项任务中都取得了最先进的结果，分别将OC-NaVQA问题的准确率提高了53.6%，位置误差提高了21.9%，时间误差提高了21.6%，SG3D任务的准确率提高了27.8%。我们开源发布了我们的数据和代码。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模环境中，如何实时地对任意时空位置进行详细的语义描述和理解的问题。现有方法在生成开放词汇描述时，需要消耗大量的计算资源，难以满足实时性要求，尤其是在3D场景中进行 grounding 时，性能会显著下降。

**核心思路**：论文的核心思路是利用局部captioning模型（如DAM）生成详细的语义描述，并通过优化的前端进行批量处理，从而加速推理过程。同时，构建一个分层的4D场景图（SG），作为全局空间和时间一致的记忆表示，用于存储和检索场景信息。

**技术框架**：DAAAM框架主要包含以下几个模块：1) 局部captioning模型（如DAM）：用于生成场景中物体的语义描述。2) 优化前端：通过批量处理加速语义描述的推理过程。3) 4D场景图构建模块：将语义描述和几何信息整合到4D场景图中，构建全局一致的场景表示。4) 工具调用代理：利用4D场景图进行推理和决策，完成各种任务。

**关键创新**：DAAAM的关键创新在于：1) 提出了一种基于优化的前端，能够显著提高局部captioning模型的推理速度，使其能够满足实时性要求。2) 构建了一个分层的4D场景图，能够有效地存储和检索场景信息，并支持复杂的时空推理任务。

**关键设计**：DAAAM的关键设计包括：1) 优化前端的批量处理策略，如何选择合适的batch size，以平衡推理速度和内存消耗。2) 4D场景图的构建方式，如何有效地整合语义信息和几何信息，并支持高效的查询操作。3) 工具调用代理的设计，如何利用4D场景图进行推理和决策，完成各种任务。

## 📊 实验亮点

DAAAM在NaVQA和SG3D基准测试中取得了显著的性能提升。在OC-NaVQA上，DAAAM的问题准确率提高了53.6%，位置误差降低了21.9%，时间误差降低了21.6%。在SG3D上，DAAAM的任务执行准确率提高了27.8%。这些结果表明，DAAAM能够有效地进行时空推理和任务执行。

## 🎯 应用场景

DAAAM框架具有广泛的应用前景，例如增强现实、机器人自主导航、智能家居等领域。它可以帮助机器人更好地理解周围环境，并根据用户的指令执行各种任务。此外，DAAAM还可以用于构建虚拟现实场景，并为用户提供更加沉浸式的体验。未来，DAAAM有望成为下一代智能系统的核心组成部分。

## 📄 摘要（原文）

> Computer vision and robotics applications ranging from augmented reality to robot autonomy in large-scale environments require spatio-temporal memory frameworks that capture both geometric structure for accurate language-grounding as well as semantic detail. Existing methods face a tradeoff, where producing rich open-vocabulary descriptions comes at the expense of real-time performance when these descriptions have to be grounded in 3D. To address these challenges, we propose Describe Anything, Anywhere, at Any Moment (DAAAM), a novel spatio-temporal memory framework for large-scale and real-time 4D scene understanding. DAAAM introduces a novel optimization-based frontend to infer detailed semantic descriptions from localized captioning models, such as the Describe Anything Model (DAM), leveraging batch processing to speed up inference by an order of magnitude for online processing. It leverages such semantic understanding to build a hierarchical 4D scene graph (SG), which acts as an effective globally spatially and temporally consistent memory representation. DAAAM constructs 4D SGs with detailed, geometrically grounded descriptions while maintaining real-time performance. We show that DAAAM's 4D SG interfaces well with a tool-calling agent for inference and reasoning.
>   We thoroughly evaluate DAAAM in the complex task of spatio-temporal question answering on the NaVQA benchmark and show its generalization capabilities for sequential task grounding on the SG3D benchmark. We further curate an extended OC-NaVQA benchmark for large-scale and long-time evaluations. DAAAM achieves state-of-the-art results in both tasks, improving OC-NaVQA question accuracy by 53.6%, position errors by 21.9%, temporal errors by 21.6%, and SG3D task grounding accuracy by 27.8% over the most competitive baselines, respectively. We release our data and code open-source.

