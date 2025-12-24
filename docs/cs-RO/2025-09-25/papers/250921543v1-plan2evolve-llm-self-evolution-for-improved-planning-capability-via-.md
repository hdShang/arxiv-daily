---
layout: default
title: "Plan2Evolve: LLM Self-Evolution for Improved Planning Capability via Automated Domain Generation"
---

# Plan2Evolve: LLM Self-Evolution for Improved Planning Capability via Automated Domain Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21543" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21543v1</a>
  <a href="https://arxiv.org/pdf/2509.21543.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21543v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21543v1', 'Plan2Evolve: LLM Self-Evolution for Improved Planning Capability via Automated Domain Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinbang Huang, Zhiyuan Li, Zhanguang Zhang, Xingyue Quan, Jianye Hao, Yingxue Zhang

**分类**: cs.RO

**发布日期**: 2025-09-25

**备注**: 25 pages, 7 figures

---

## 💡 一句话要点

**Plan2Evolve：通过自动领域生成实现LLM自进化，提升规划能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `机器人任务规划` `自动规划领域生成` `思维链` `自进化学习`

## 📋 核心要点

1. 现有方法将LLM生成的规划领域视为搜索工具，忽略了其作为可扩展推理数据来源的潜力。
2. Plan2Evolve框架利用LLM自生成规划领域，并将其转化为扩展的CoT轨迹，对齐符号规划和自然语言推理。
3. 实验表明，该方法能提升LLM的规划成功率、跨任务泛化能力，并降低推理成本。

## 📝 摘要（中文）

大型语言模型（LLMs）最近在机器人任务规划中展现出强大的潜力，特别是通过集成符号搜索的自动规划领域生成。然而，先前的方法主要将这些领域视为搜索工具，而对其作为可扩展的推理数据来源的潜力关注不足。与此同时，推理LLMs的进展受到思维链（CoT）监督的推动，但其在机器人领域的应用仍然依赖于昂贵的人工策划数据集。我们提出了Plan2Evolve，一个LLM自进化框架，其中基础模型生成规划领域，作为产生符号问题-计划对作为推理轨迹的引擎。这些对随后通过相同的模型，借助自然语言解释，被转换为扩展的CoT轨迹，从而显式地将符号规划结构与自然语言推理对齐。由此产生的数据超越了模型固有的规划能力，从而能够进行模型微调，从而产生一个规划增强的LLM，该LLM具有更高的规划成功率、更强的跨任务泛化能力和更低的推理成本。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在机器人任务规划中，依赖人工标注CoT数据进行推理能力提升的问题。现有方法通常将LLM生成的规划领域仅作为搜索工具，忽略了其作为大规模推理数据来源的潜力，且人工标注CoT数据成本高昂。

**核心思路**：论文的核心思路是利用LLM自身生成规划领域，并基于此自动生成问题-计划对，再将这些问题-计划对转化为扩展的CoT轨迹，从而实现LLM的自进化，提升其规划能力。通过这种方式，可以避免对大量人工标注数据的依赖。

**技术框架**：Plan2Evolve框架包含以下几个主要阶段：1) **规划领域生成**：基础LLM生成规划领域描述；2) **问题-计划对生成**：利用生成的规划领域作为引擎，生成符号问题-计划对；3) **CoT轨迹生成**：使用LLM将问题-计划对转化为包含自然语言解释的扩展CoT轨迹；4) **模型微调**：使用生成的CoT数据对LLM进行微调，提升其规划能力。

**关键创新**：该方法最重要的创新点在于提出了一个LLM自进化的框架，通过自动生成规划领域和CoT轨迹，实现了LLM规划能力的自我提升，摆脱了对人工标注数据的依赖。与现有方法相比，Plan2Evolve能够更高效、更经济地提升LLM的规划能力。

**关键设计**：论文的关键设计包括：如何设计提示词，引导LLM生成高质量的规划领域描述；如何将符号问题-计划对转化为自然语言描述的CoT轨迹；以及如何选择合适的微调策略，以最大程度地提升LLM的规划能力。具体的参数设置、损失函数、网络结构等技术细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，Plan2Evolve能够显著提升LLM的规划成功率和跨任务泛化能力。与基线方法相比，该方法在多个机器人任务规划数据集上取得了显著的性能提升，并且降低了推理成本。具体的性能数据和提升幅度在论文的实验部分进行了详细展示。

## 🎯 应用场景

Plan2Evolve具有广泛的应用前景，可以应用于机器人任务规划、游戏AI、智能助手等领域。该方法能够提升LLM在复杂环境下的决策能力，使其能够更好地理解和执行任务。未来，该方法有望应用于更广泛的领域，例如自动驾驶、智能制造等，推动人工智能技术的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have recently shown strong potential in robotic task planning, particularly through automatic planning domain generation that integrates symbolic search. Prior approaches, however, have largely treated these domains as search utilities, with limited attention to their potential as scalable sources of reasoning data. At the same time, progress in reasoning LLMs has been driven by chain-of-thought (CoT) supervision, whose application in robotics remains dependent on costly, human-curated datasets. We propose Plan2Evolve, an LLM self-evolving framework in which the base model generates planning domains that serve as engines for producing symbolic problem-plan pairs as reasoning traces. These pairs are then transformed into extended CoT trajectories by the same model through natural-language explanations, thereby explicitly aligning symbolic planning structures with natural language reasoning. The resulting data extend beyond the model's intrinsic planning capacity, enabling model fine-tuning that yields a planning-enhanced LLM with improved planning success, stronger cross-task generalization, and reduced inference costs.

