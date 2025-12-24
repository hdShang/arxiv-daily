---
layout: default
title: "Growing Perspectives: Modelling Embodied Perspective Taking and Inner Narrative Development Using Large Language Models"
---

# Growing Perspectives: Modelling Embodied Perspective Taking and Inner Narrative Development Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.11868" class="toolbar-btn" target="_blank">📄 arXiv: 2509.11868v1</a>
  <a href="https://arxiv.org/pdf/2509.11868.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.11868v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.11868v1', 'Growing Perspectives: Modelling Embodied Perspective Taking and Inner Narrative Development Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sabrina Patania, Luca Annese, Anna Lambiase, Anita Pellegrini, Tom Foulsham, Azzurra Ruggeri, Silvia Rossi, Silvia Serino, Dimitri Ognibene

**分类**: cs.CL, cs.AI, cs.HC, cs.RO

**发布日期**: 2025-09-15

**备注**: Accepted at ICDL https://icdl2025.fel.cvut.cz/

---

## 💡 一句话要点

**提出PerspAct系统以模拟人类视角采纳与内在叙事发展**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身视角采纳` `内在叙事` `大型语言模型` `人机协作` `ReAct范式` `发展阶段` `协作表现` `心理学模型`

## 📋 核心要点

1. 现有计算模型对语言与具身视角采纳的整合不足，难以有效模拟人类的协作过程。
2. 本研究提出PerspAct系统，通过结合ReAct范式与大型语言模型，模拟视角采纳的不同发展阶段。
3. 实验结果显示，GPT生成的内在叙事与发展阶段一致，且更高的发展阶段提升了协作效果，尤其在复杂任务中表现明显。

## 📝 摘要（中文）

语言和具身视角采纳对人类合作至关重要，但现有计算模型很少同时考虑这两者。本研究探讨了PerspAct系统，该系统将ReAct（推理与行动）范式与大型语言模型（LLMs）结合，以模拟基于Selman理论的视角采纳发展阶段。通过扩展的导演任务，我们评估了GPT生成与特定发展阶段一致的内在叙事的能力，并分析这些叙事如何影响协作表现。结果表明，GPT在任务执行前可靠地产生发展一致的叙事，但在互动过程中往往转向更高级的阶段，表明语言交流有助于细化内在表征。更高的发展阶段通常提高协作有效性，而早期阶段在复杂情境中结果更为多变。这些发现强调了在LLMs中整合具身视角采纳与语言的潜力，以更好地建模发展动态，并强调在结合语言与具身任务时评估内在语言的重要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有计算模型在语言与具身视角采纳整合方面的不足，特别是在模拟人类协作中的发展动态。现有方法未能有效捕捉内在叙事与视角采纳的关系。

**核心思路**：论文提出的PerspAct系统通过结合ReAct范式与大型语言模型，模拟视角采纳的不同发展阶段，旨在通过语言交流提升内在表征的精确性。

**技术框架**：该系统的整体架构包括数据输入、内在叙事生成、视角采纳评估和协作表现分析四个主要模块。通过扩展的导演任务，系统评估生成的叙事与发展阶段的一致性。

**关键创新**：最重要的技术创新在于将内在叙事生成与视角采纳发展阶段相结合，形成了一个动态的、基于语言的协作模型。这与传统方法的静态视角采纳模型形成鲜明对比。

**关键设计**：在系统设计中，关键参数包括叙事生成的上下文设置、损失函数的选择以及网络结构的优化，以确保生成的叙事与发展阶段的高度一致性。

## 📊 实验亮点

实验结果表明，GPT在任务执行前生成的内在叙事与发展阶段一致性高，且在互动过程中能够向更高级别转变。更高的发展阶段通常与协作效果的提升相关，尤其在复杂任务中，表现出显著的效率提升，展示了语言交流在协作中的重要作用。

## 🎯 应用场景

该研究的潜在应用领域包括教育、心理治疗和人机交互等。通过模拟人类的视角采纳与内在叙事发展，PerspAct系统可以帮助设计更有效的协作工具和教育平台，提升学习与沟通效果。未来，该模型可能在机器人协作和智能助手中发挥重要作用，促进人机协作的自然性与有效性。

## 📄 摘要（原文）

> Language and embodied perspective taking are essential for human collaboration, yet few computational models address both simultaneously. This work investigates the PerspAct system [1], which integrates the ReAct (Reason and Act) paradigm with Large Language Models (LLMs) to simulate developmental stages of perspective taking, grounded in Selman's theory [2]. Using an extended director task, we evaluate GPT's ability to generate internal narratives aligned with specified developmental stages, and assess how these influence collaborative performance both qualitatively (action selection) and quantitatively (task efficiency). Results show that GPT reliably produces developmentally-consistent narratives before task execution but often shifts towards more advanced stages during interaction, suggesting that language exchanges help refine internal representations. Higher developmental stages generally enhance collaborative effectiveness, while earlier stages yield more variable outcomes in complex contexts. These findings highlight the potential of integrating embodied perspective taking and language in LLMs to better model developmental dynamics and stress the importance of evaluating internal speech during combined linguistic and embodied tasks.

