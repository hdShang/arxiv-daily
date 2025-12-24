---
layout: default
title: "LLMs as Layout Designers: Enhanced Spatial Reasoning for Content-Aware Layout Generation"
---

# LLMs as Layout Designers: Enhanced Spatial Reasoning for Content-Aware Layout Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16891" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16891v2</a>
  <a href="https://arxiv.org/pdf/2509.16891.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16891v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16891v2', 'LLMs as Layout Designers: Enhanced Spatial Reasoning for Content-Aware Layout Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sha Li, Stefano Petrangeli, Yu Shen, Xiang Chen, Naren Ramakrishnan

**分类**: cs.AI

**发布日期**: 2025-09-21 (更新: 2025-11-03)

---

## 💡 一句话要点

**LaySPA：增强空间推理能力，利用LLM进行内容感知布局生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内容感知布局` `大型语言模型` `强化学习` `空间推理` `图形设计`

## 📋 核心要点

1. 现有LLM在空间关系理解和操作方面存在局限性，难以胜任内容感知的图形布局设计任务。
2. LaySPA通过强化学习框架，增强LLM代理的空间推理能力，优化元素间的空间排列。
3. 实验表明，LaySPA在布局生成方面优于通用LLM，性能与专用布局模型相当，提升了布局的结构有效性和视觉吸引力。

## 📝 摘要（中文）

大型语言模型(LLM)在文本领域展现了卓越的推理和规划能力，能够有效执行复杂任务的指令，但它们在理解和操作空间关系方面的能力仍然有限。这种能力对于内容感知的图形布局设计至关重要，其目标是将异构元素排列到画布上，使最终设计在视觉上保持平衡且结构上可行。这个问题需要在受限的视觉空间内精确协调多个元素的位置、对齐和结构组织。为了解决这个局限性，我们引入了LaySPA，这是一个基于强化学习的框架，它通过显式的空间推理能力来增强基于LLM的布局设计代理。LaySPA采用混合奖励信号，共同捕捉几何约束、结构保真度和视觉质量，使代理能够导航画布，建模元素间的关系，并优化空间排列。通过组相对策略优化，该代理生成内容感知的布局，反映显著区域，尊重空间约束，并生成可解释的推理轨迹，解释放置决策和结构化布局规范。实验结果表明，LaySPA显著提高了结构有效和视觉吸引力的布局生成，优于更大的通用LLM，并实现了与最先进的专用布局模型相当的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决内容感知图形布局设计问题，即如何在画布上合理排列异构元素，使其在视觉上平衡且结构上可行。现有方法，特别是直接使用大型语言模型的方法，在理解和操作空间关系方面存在不足，难以满足布局设计的精确性和复杂性要求。

**核心思路**：论文的核心思路是利用强化学习来增强LLM的空间推理能力。通过设计合适的奖励函数，引导LLM代理学习如何在画布上进行元素布局，从而生成满足几何约束、结构保真度和视觉质量的布局。这种方法将LLM的语义理解能力与强化学习的空间优化能力相结合。

**技术框架**：LaySPA框架包含以下主要模块：1) 基于LLM的代理：负责根据内容信息和当前布局状态生成布局动作；2) 强化学习环境：模拟画布环境，接收代理的动作并更新布局状态；3) 混合奖励函数：评估布局的几何约束、结构保真度和视觉质量，为代理提供反馈；4) 组相对策略优化：用于训练代理，使其能够生成高质量的布局。整体流程是，LLM代理根据当前布局状态选择一个动作（例如，放置一个元素），环境执行该动作并更新布局，然后根据混合奖励函数计算奖励，代理根据奖励更新其策略。

**关键创新**：LaySPA的关键创新在于：1) 提出了一个基于强化学习的框架，将LLM与空间推理能力相结合，用于内容感知的布局设计；2) 设计了一个混合奖励函数，综合考虑了几何约束、结构保真度和视觉质量，从而能够生成更合理、更美观的布局；3) 采用了组相对策略优化方法，提高了训练效率和布局质量。

**关键设计**：混合奖励函数是LaySPA的关键设计之一，它由三个部分组成：几何约束奖励、结构保真度奖励和视觉质量奖励。几何约束奖励用于惩罚元素之间的重叠或超出画布边界的情况；结构保真度奖励用于鼓励布局符合预定义的结构模式；视觉质量奖励用于评估布局的视觉平衡和美观程度。具体参数设置和权重分配需要根据具体应用场景进行调整。

## 📊 实验亮点

实验结果表明，LaySPA在布局生成方面显著优于更大的通用LLM，并且实现了与最先进的专用布局模型相当的性能。具体来说，LaySPA在结构有效性和视觉吸引力方面都取得了显著提升，证明了其在内容感知布局设计方面的有效性。量化指标和人工评估都支持了这一结论。

## 🎯 应用场景

LaySPA可应用于广告设计、网页设计、海报设计、PPT制作等领域，能够自动生成符合内容和视觉要求的布局方案，提高设计效率和质量。该研究的未来影响在于，它探索了如何将LLM与强化学习相结合，解决空间推理问题，为其他需要空间规划和优化的任务提供了借鉴。

## 📄 摘要（原文）

> While Large Language Models (LLMs) have demonstrated impressive reasoning and planning abilities in textual domains and can effectively follow instructions for complex tasks, their ability to understand and manipulate spatial relationships remains limited. Such capabilities are crucial for content-aware graphic layout design, where the goal is to arrange heterogeneous elements onto a canvas so that final design remains visually balanced and structurally feasible. This problem requires precise coordination of placement, alignment, and structural organization of multiple elements within a constrained visual space. To address this limitation, we introduce LaySPA, a reinforcement learning-based framework that augments LLM-based agents with explicit spatial reasoning capabilities for layout design. LaySPA employs hybrid reward signals that jointly capture geometric constraints, structural fidelity, and visual quality, enabling agents to navigate the canvas, model inter-element relationships, and optimize spatial arrangements. Through group-relative policy optimization, the agent generates content-aware layouts that reflect salient regions, respect spatial constraints, and produces an interpretable reasoning trace explaining placement decisions and a structured layout specification. Experimental results show that LaySPA substantially improves the generation of structurally valid and visually appealing layouts, outperforming larger general-purpose LLMs and achieving performance comparable to state-of-the-art specialized layout models.

