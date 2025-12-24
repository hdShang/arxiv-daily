---
layout: default
title: "Perceive, Reflect and Understand Long Video: Progressive Multi-Granular Clue Exploration with Interactive Agents"
---

# Perceive, Reflect and Understand Long Video: Progressive Multi-Granular Clue Exploration with Interactive Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24943" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24943v1</a>
  <a href="https://arxiv.org/pdf/2509.24943.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24943v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24943v1', 'Perceive, Reflect and Understand Long Video: Progressive Multi-Granular Clue Exploration with Interactive Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahua Li, Kun Wei, Zhe Xu, Zibo Su, Xu Yang, Cheng Deng

**分类**: cs.CV

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**CogniGPT：交互式多粒度线索探索，提升长视频理解的效率与可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `多粒度感知` `交互式代理` `视觉认知` `大型语言模型`

## 📋 核心要点

1. 现有基于LLM的长视频理解方法在捕获关键信息的完整性和效率上存在不足，难以兼顾。
2. CogniGPT通过多粒度感知代理和验证增强反射代理的交互，模拟人类视觉认知过程，高效探索任务相关线索。
3. 实验表明，CogniGPT在多个数据集上超越现有方法，在EgoSchema上仅用少量帧就达到与Gemini 1.5-Pro相当的性能。

## 📝 摘要（中文）

长视频由于其时间复杂性和稀疏的任务相关信息，给AI系统带来了巨大的推理挑战。尽管各种基于大型语言模型（LLM）的方法在长视频理解方面取得了进展，但它们在捕获任务关键信息的完整性和效率方面仍然存在困难。受人类渐进式视觉认知的启发，我们提出了CogniGPT，一个利用多粒度感知代理（MGPA）和验证增强反射代理（VERA）之间的交互循环的框架，用于高效和可靠的长视频理解。具体来说，MGPA模仿人类视觉的发散和聚焦注意力来捕获任务相关信息，而VERA验证感知到的关键线索，以减轻幻觉并优化后续的感知策略。通过这种交互过程，CogniGPT探索最少数量的信息丰富且可靠的任务相关线索。在EgoSchema、Video-MME、NExT-QA和MovieChat数据集上的大量实验表明，CogniGPT在准确性和效率方面均优于现有方法。值得注意的是，在EgoSchema上，它仅使用11.2帧就超越了现有的免训练方法，并达到了与Gemini 1.5-Pro相当的性能。

## 🔬 方法详解

**问题定义**：长视频理解任务面临时间跨度大、信息冗余、关键信息稀疏等挑战。现有方法难以在保证信息完整性的同时，实现高效推理，并且容易产生幻觉。

**核心思路**：模仿人类的视觉认知过程，采用渐进式、交互式的探索方式。通过发散和聚焦注意力，逐步提取关键信息，并利用验证机制减少幻觉，提高信息可靠性。

**技术框架**：CogniGPT包含两个主要模块：多粒度感知代理（MGPA）和验证增强反射代理（VERA）。MGPA负责从视频中提取不同粒度的信息，模拟人类视觉的发散和聚焦过程。VERA则负责验证MGPA提取的关键线索，评估其可靠性，并指导MGPA进行后续的感知策略调整。这两个模块通过交互循环，逐步提炼出最相关的任务信息。

**关键创新**：引入交互式的代理架构，模拟人类视觉认知过程，实现高效且可靠的长视频理解。通过多粒度感知和验证机制，有效减少了幻觉，提高了信息提取的准确性。

**关键设计**：MGPA采用多层级的视觉特征提取器，捕捉不同时间尺度的信息。VERA使用LLM进行线索验证，并根据验证结果调整MGPA的注意力权重。损失函数的设计旨在鼓励MGPA提取更可靠、更相关的线索，并惩罚VERA的错误验证。

## 📊 实验亮点

CogniGPT在EgoSchema数据集上，仅使用11.2帧就超越了现有的免训练方法，并达到了与Gemini 1.5-Pro相当的性能。在Video-MME、NExT-QA和MovieChat等数据集上也取得了显著的性能提升，证明了其在长视频理解方面的优越性。实验结果表明，CogniGPT在准确性和效率方面均优于现有方法。

## 🎯 应用场景

CogniGPT可应用于智能监控、自动驾驶、视频内容分析、智能客服等领域。例如，在智能监控中，可以快速定位异常事件；在自动驾驶中，可以准确理解复杂的交通场景；在视频内容分析中，可以自动提取关键信息，生成摘要或标签。该研究有助于提升AI系统在复杂环境下的感知和理解能力。

## 📄 摘要（原文）

> Long videos, characterized by temporal complexity and sparse task-relevant information, pose significant reasoning challenges for AI systems. Although various Large Language Model (LLM)-based approaches have advanced long video understanding, they still struggle to achieve both completeness and efficiency in capturing task-critical information. Inspired by human progressive visual cognition, we propose CogniGPT, a framework that leverages an interactive loop between Multi-Granular Perception Agent (MGPA) and Verification-Enhanced Reflection Agent (VERA) for efficient and reliable long video understanding. Specifically, MGPA mimics human visual divergent and focused attention to capture task-related information, while VERA verifies perceived key clues to mitigate hallucination and optimize subsequent perception strategies. Through this interactive process, CogniGPT explores a minimal set of informative and reliable task-related clues. Extensive experiments on EgoSchema, Video-MME, NExT-QA, and MovieChat datasets demonstrate CogniGPT's superiority in both accuracy and efficiency. Notably, on EgoSchema, it surpasses existing training-free methods using only 11.2 frames and achieves performance comparable to Gemini 1.5-Pro.

