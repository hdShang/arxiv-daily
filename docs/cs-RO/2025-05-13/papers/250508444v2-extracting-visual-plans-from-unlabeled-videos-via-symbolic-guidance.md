---
layout: default
title: Extracting Visual Plans from Unlabeled Videos via Symbolic Guidance
---

# Extracting Visual Plans from Unlabeled Videos via Symbolic Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08444" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08444v2</a>
  <a href="https://arxiv.org/pdf/2505.08444.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08444v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08444v2', 'Extracting Visual Plans from Unlabeled Videos via Symbolic Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenyan Yang, Ahmet Tikna, Yi Zhao, Yuying Zhang, Luigi Palopoli, Marco Roveri, Joni Pajarinen

**分类**: cs.RO

**发布日期**: 2025-05-13 (更新: 2025-08-07)

---

## 💡 一句话要点

**提出Vis2Plan以解决长时间操作任务中的视觉规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉规划` `符号引导` `任务符号` `多目标规划` `机器人操作` `视频理解` `高效生成`

## 📋 核心要点

1. 现有的视觉规划方法依赖视频生成模型，容易出现模型幻觉且计算成本高，限制了其在长时间操作任务中的应用。
2. 本文提出的Vis2Plan框架通过符号引导，从未标记的视频数据中提取任务符号，构建高层符号转移图，实现高效的视觉规划。
3. 实验结果显示，Vis2Plan在真实机器人环境中成功率提高了53%，且生成视觉规划的速度提升了35倍，展现出显著的性能优势。

## 📝 摘要（中文）

视觉规划通过为目标条件低级策略提供一系列中间视觉子目标，在长时间操作任务中取得了良好的效果。现有方法通常依赖视频生成模型，但面临模型幻觉和计算成本高的问题。本文提出的Vis2Plan是一个高效、可解释的视觉规划框架，利用符号引导从原始未标记的游戏数据中自动提取紧凑的任务符号，从而构建多目标、多阶段规划的高层符号转移图。在测试时，给定期望的任务目标，规划器在符号层面进行规划，并组装出一系列与基础符号表示相一致的物理中间子目标图像。实验结果表明，Vis2Plan在真实机器人环境中比强大的扩散视频生成基础的视觉规划器提高了53%的成功率，同时生成视觉规划的速度提高了35倍。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉规划方法在长时间操作任务中面临的模型幻觉和高计算成本的问题。现有方法依赖视频生成模型，导致生成的视觉子目标不够可靠且效率低下。

**核心思路**：Vis2Plan通过符号引导，从未标记的游戏数据中自动提取任务符号，构建高层符号转移图，从而实现高效且可解释的视觉规划。该方法在规划过程中利用符号表示进行中间子目标的生成，确保生成的目标图像在物理上是一致的。

**技术框架**：Vis2Plan的整体架构包括数据预处理、任务符号提取、符号转移图构建和目标图像生成四个主要模块。在数据预处理阶段，原始视频数据被处理为适合提取符号的格式；接着，利用视觉基础模型提取任务符号；然后，构建符号转移图以支持多目标规划；最后，根据符号表示生成中间子目标图像。

**关键创新**：Vis2Plan的主要创新在于其符号引导的视觉规划方法，区别于传统依赖视频生成的方式。通过符号引导，Vis2Plan能够生成更为可靠的视觉目标，同时提供可解释的推理步骤。

**关键设计**：在设计中，Vis2Plan采用了特定的损失函数来优化符号提取的准确性，并利用视觉基础模型的特征提取能力来增强符号的表达力。此外，规划过程中的参数设置经过精细调整，以确保生成的目标图像在物理上具有一致性。

## 📊 实验亮点

实验结果表明，Vis2Plan在真实机器人环境中的成功率比现有的扩散视频生成基础的视觉规划器高出53%，同时生成视觉规划的速度提升了35倍。这些结果展示了Vis2Plan在效率和效果上的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和人机交互等。Vis2Plan能够在复杂的操作任务中提供高效的视觉规划，提升机器人在动态环境中的适应能力和执行效率。未来，该方法可能在智能家居、无人驾驶等领域发挥重要作用。

## 📄 摘要（原文）

> Visual planning, by offering a sequence of intermediate visual subgoals to a goal-conditioned low-level policy, achieves promising performance on long-horizon manipulation tasks. To obtain the subgoals, existing methods typically resort to video generation models but suffer from model hallucination and computational cost. We present Vis2Plan, an efficient, explainable and white-box visual planning framework powered by symbolic guidance. From raw, unlabeled play data, Vis2Plan harnesses vision foundation models to automatically extract a compact set of task symbols, which allows building a high-level symbolic transition graph for multi-goal, multi-stage planning. At test time, given a desired task goal, our planner conducts planning at the symbolic level and assembles a sequence of physically consistent intermediate sub-goal images grounded by the underlying symbolic representation. Our Vis2Plan outperforms strong diffusion video generation-based visual planners by delivering 53\% higher aggregate success rate in real robot settings while generating visual plans 35$\times$ faster. The results indicate that Vis2Plan is able to generate physically consistent image goals while offering fully inspectable reasoning steps.

