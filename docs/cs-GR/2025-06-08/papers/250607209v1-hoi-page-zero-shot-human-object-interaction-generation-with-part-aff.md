---
layout: default
title: "HOI-PAGE: Zero-Shot Human-Object Interaction Generation with Part Affordance Guidance"
---

# HOI-PAGE: Zero-Shot Human-Object Interaction Generation with Part Affordance Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.07209" class="toolbar-btn" target="_blank">📄 arXiv: 2506.07209v1</a>
  <a href="https://arxiv.org/pdf/2506.07209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.07209v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.07209v1', 'HOI-PAGE: Zero-Shot Human-Object Interaction Generation with Part Affordance Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Li, Angela Dai

**分类**: cs.GR, cs.CV

**发布日期**: 2025-06-08

**备注**: Project page: https://hoipage.github.io/ Video: https://youtu.be/b1pJU9lKQTE

---

## 💡 一句话要点

**提出HOI-PAGE以解决零样本人机交互生成问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `零样本学习` `部件可供性` `4D合成` `运动约束` `多模态生成` `虚拟现实`

## 📋 核心要点

1. 现有方法主要集中在整体身体与物体的运动上，缺乏对人类身体部位与物体部件之间细致交互的理解。
2. 论文提出通过部件可供性图（PAGs）来引导HOI合成，强调部件级的接触关系和运动约束。
3. 实验结果显示，HOI-PAGE在生成复杂交互序列方面表现出色，真实感和文本对齐度显著提升。

## 📝 摘要（中文）

我们提出了HOI-PAGE，这是一种从文本提示中以零样本方式合成4D人机交互（HOIs）的新方法，基于部件级的可供性推理。与以往关注整体身体-物体运动的4D HOI合成方法不同，我们观察到生成真实且多样的HOIs需要更细致的理解，即人类身体部位如何与物体部件互动。因此，我们引入了部件可供性图（PAGs），这是一种从大型语言模型（LLMs）中提炼的结构化HOI表示，编码了细粒度的部件信息及接触关系。我们利用这些PAGs指导三阶段合成：首先，将输入的3D物体分解为几何部件；然后，从文本提示生成参考HOI视频，并提取基于部件的运动约束；最后，优化4D HOI运动序列，使其不仅模仿参考动态，还满足部件级接触约束。大量实验表明，我们的方法灵活且能够生成复杂的多物体或多人交互序列，显著提高了零样本4D HOI生成的真实感和文本对齐度。

## 🔬 方法详解

**问题定义**：本论文旨在解决零样本人机交互生成中的细粒度理解问题。现有方法往往忽视了人类身体部位与物体部件之间的具体交互，导致生成的HOIs缺乏真实感和多样性。

**核心思路**：论文的核心思路是引入部件可供性图（PAGs），通过对人机交互的部件级分析，提升生成的HOIs的真实感和多样性。这种设计使得模型能够更好地理解和模拟人类与物体之间的复杂交互。

**技术框架**：整体架构分为三个主要阶段：第一阶段，将输入的3D物体分解为几何部件；第二阶段，从文本提示生成参考HOI视频，并提取基于部件的运动约束；第三阶段，优化生成的4D HOI运动序列，使其符合参考动态和部件级接触约束。

**关键创新**：最重要的技术创新点在于引入了部件可供性图（PAGs），这使得模型能够在部件级别上进行更细致的交互理解，与现有方法的整体运动生成方式形成鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡运动约束与接触关系，同时在网络结构上进行了优化，以确保生成的HOIs在真实感和多样性方面达到最佳效果。

## 📊 实验亮点

实验结果表明，HOI-PAGE在生成复杂多物体或多人交互序列方面表现优异，相较于基线方法，生成的HOIs在真实感和文本对齐度上有显著提升，具体提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发、机器人交互等。通过生成更真实的人机交互，HOI-PAGE能够提升用户体验，并为自动化系统提供更自然的交互方式。未来，该技术可能在智能助手和人机协作领域产生深远影响。

## 📄 摘要（原文）

> We present HOI-PAGE, a new approach to synthesizing 4D human-object interactions (HOIs) from text prompts in a zero-shot fashion, driven by part-level affordance reasoning. In contrast to prior works that focus on global, whole body-object motion for 4D HOI synthesis, we observe that generating realistic and diverse HOIs requires a finer-grained understanding -- at the level of how human body parts engage with object parts. We thus introduce Part Affordance Graphs (PAGs), a structured HOI representation distilled from large language models (LLMs) that encodes fine-grained part information along with contact relations. We then use these PAGs to guide a three-stage synthesis: first, decomposing input 3D objects into geometric parts; then, generating reference HOI videos from text prompts, from which we extract part-based motion constraints; finally, optimizing for 4D HOI motion sequences that not only mimic the reference dynamics but also satisfy part-level contact constraints. Extensive experiments show that our approach is flexible and capable of generating complex multi-object or multi-person interaction sequences, with significantly improved realism and text alignment for zero-shot 4D HOI generation.

