---
layout: default
title: "CreAgentive: An Agent Workflow Driven Multi-Category Creative Generation Engine"
---

# CreAgentive: An Agent Workflow Driven Multi-Category Creative Generation Engine

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26461" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26461v1</a>
  <a href="https://arxiv.org/pdf/2509.26461.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26461v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26461v1', 'CreAgentive: An Agent Workflow Driven Multi-Category Creative Generation Engine')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuyang Cheng, Linyue Cai, Changwei Peng, Yumiao Xu, Rongfang Bie, Yong Zhao

**分类**: cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出CreAgentive以解决多类别创作生成的四大问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `创作生成` `多体裁` `故事原型` `知识图谱` `代理工作流` `叙事连贯性` `文本生成` `人工智能`

## 📋 核心要点

1. 当前大型语言模型在创作过程中存在体裁多样性不足、输出长度限制、叙事连贯性差等问题。
2. CreAgentive通过引入故事原型和三阶段代理工作流，解决了上述问题，实现了多体裁的创作生成。
3. 实验结果显示，CreAgentive在多个体裁中稳定生成高质量文本，且成本低于每100章1美元，超越了强基线模型。

## 📝 摘要（中文）

我们提出了CreAgentive，这是一种基于代理工作流的多类别创作生成引擎，旨在解决当前大型语言模型在创作故事、戏剧等方面的四个关键限制：体裁多样性受限、输出长度不足、叙事连贯性弱以及无法执行复杂结构构造。CreAgentive的核心是一个故事原型，它是一种与体裁无关的知识图谱基础的叙事表示，通过将角色、事件和环境编码为语义三元组，从而将故事逻辑与风格实现解耦。该系统采用三阶段代理工作流，包括初始化阶段、生成阶段和写作阶段，最终实现多体裁文本的生成。实验表明，CreAgentive以低于每100章1美元的成本生成数千章高质量文本，且在多个体裁中表现优异，接近人类创作的小说质量。

## 🔬 方法详解

**问题定义**：本论文旨在解决当前大型语言模型在创作生成中的四大痛点，包括体裁多样性不足、输出长度限制、叙事连贯性差以及复杂结构构造能力不足。

**核心思路**：CreAgentive的核心思路是通过构建一个与体裁无关的故事原型，利用知识图谱对叙事进行表示，从而将故事逻辑与风格实现解耦，增强生成的灵活性和多样性。

**技术框架**：CreAgentive采用三阶段代理工作流：初始化阶段构建用户指定的叙事框架；生成阶段通过多代理对话实现故事原型的实例化；写作阶段利用故事原型生成多体裁文本，支持复杂的叙事结构。

**关键创新**：最重要的创新在于引入了知识图谱基础的故事原型，使得叙事逻辑与风格实现解耦，从而提升了生成文本的质量和多样性，与现有方法相比具有显著优势。

**关键设计**：在设计中，CreAgentive通过语义三元组编码角色、事件和环境，减少了存储冗余，并通过长短期目标引导生成过程，确保生成文本的连贯性和结构复杂性。实验中使用的损失函数和网络结构经过精心调整，以优化生成效果。

## 📊 实验亮点

在实验中，CreAgentive以低于每100章1美元的成本生成数千章文本，且在10个叙事指标的评估中，表现出色，稳定超越多个强基线模型，接近人类创作的小说质量，展示了其在多体裁创作中的强大能力。

## 🎯 应用场景

CreAgentive的潜在应用场景包括小说创作、剧本编写、游戏故事生成等领域。其多体裁生成能力和高效的工作流设计，使其在创意产业中具有实际价值，能够帮助创作者快速生成高质量的文本内容，提升创作效率。未来，CreAgentive有望在教育、娱乐等多个领域发挥更大影响。

## 📄 摘要（原文）

> We present CreAgentive, an agent workflow driven multi-category creative generation engine that addresses four key limitations of contemporary large language models in writing stories, drama and other categories of creatives: restricted genre diversity, insufficient output length, weak narrative coherence, and inability to enforce complex structural constructs. At its core, CreAgentive employs a Story Prototype, which is a genre-agnostic, knowledge graph-based narrative representation that decouples story logic from stylistic realization by encoding characters, events, and environments as semantic triples. CreAgentive engages a three-stage agent workflow that comprises: an Initialization Stage that constructs a user-specified narrative skeleton; a Generation Stage in which long- and short-term objectives guide multi-agent dialogues to instantiate the Story Prototype; a Writing Stage that leverages this prototype to produce multi-genre text with advanced structures such as retrospection and foreshadowing. This architecture reduces storage redundancy and overcomes the typical bottlenecks of long-form generation. In extensive experiments, CreAgentive generates thousands of chapters with stable quality and low cost (less than $1 per 100 chapters) using a general-purpose backbone model. To evaluate performance, we define a two-dimensional framework with 10 narrative indicators measuring both quality and length. Results show that CreAgentive consistently outperforms strong baselines and achieves robust performance across diverse genres, approaching the quality of human-authored novels.

