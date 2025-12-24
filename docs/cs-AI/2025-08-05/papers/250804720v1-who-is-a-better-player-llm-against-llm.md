---
layout: default
title: "Who is a Better Player: LLM against LLM"
---

# Who is a Better Player: LLM against LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04720" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04720v1</a>
  <a href="https://arxiv.org/pdf/2508.04720.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04720v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04720v1', 'Who is a Better Player: LLM against LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingjie Zhou, Jiezhang Cao, Farong Wen, Li Xu, Yanwei Jiang, Jun Jia, Ronghui Li, Xiaohong Liu, Yu Zhou, Xiongkuo Min, Jie Guo, Zicheng Zhang, Guangtao Zhai

**分类**: cs.AI

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出对抗性基准框架以评估大型语言模型的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `对抗性游戏` `评估框架` `Elo评分系统` `性能循环图` `心理适应性` `人工智能评估`

## 📋 核心要点

1. 现有的问答基准方法依赖于大量数据，限制了对大型语言模型在对抗性环境中的全面评估。
2. 论文提出了Qi Town评估平台，通过对抗性棋类游戏来评估LLMs的综合表现，采用Elo评分和性能循环图。
3. 实验结果显示，LLMs在高压环境下表现出更强的适应性，但其技能表现存在不稳定性，需进一步研究。

## 📝 摘要（中文）

对抗性棋类游戏作为战略推理和智能的典型领域，长期以来既是流行的竞技活动，也是评估人工智能系统的基准。基于此，我们提出了一种对抗性基准框架，通过棋类比赛评估大型语言模型（LLMs）的综合表现，弥补了主流问答基准方法的数据依赖性限制。我们引入了Qi Town，一个支持五种广泛游戏的专用评估平台，涉及20个LLM驱动的玩家。该平台采用Elo评分系统和新颖的性能循环图（PLG）来定量评估LLMs的技术能力，同时在游戏过程中捕捉积极情感评分（PSS）以评估心理适应能力。评估以循环赛的形式进行，能够系统地比较各个玩家。实验结果表明，尽管技术差异，绝大多数LLMs对胜负持乐观态度，表现出比人类更强的适应高压对抗环境的能力。另一方面，PLGs中循环胜负的复杂关系揭示了LLMs在游戏中技能表现的不稳定性，值得进一步解释和探索。

## 🔬 方法详解

**问题定义**：论文旨在解决现有问答基准方法在评估大型语言模型（LLMs）时的局限性，特别是其对数据的高度依赖性，导致无法全面反映模型在对抗性环境中的表现。

**核心思路**：通过引入对抗性棋类游戏作为评估手段，论文设计了一个新的基准框架，旨在通过实际对抗来评估LLMs的综合能力和心理适应性。

**技术框架**：整体架构包括Qi Town评估平台，支持五种棋类游戏，采用Elo评分系统和性能循环图（PLG）来量化评估。评估过程为循环赛，确保各个玩家之间的系统比较。

**关键创新**：最重要的技术创新在于引入性能循环图（PLG），它能够揭示LLMs在游戏中的技能表现波动，提供比传统方法更深入的分析。

**关键设计**：在参数设置上，Elo评分系统用于量化玩家表现，积极情感评分（PSS）用于评估心理适应性，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果表明，尽管存在技术差异，大多数LLMs在对抗性环境中表现出乐观的胜负态度，适应性优于人类。同时，性能循环图揭示了LLMs技能表现的不稳定性，提示未来研究的方向。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、教育和心理健康评估等。通过对抗性游戏的评估框架，可以更好地理解和提升大型语言模型在复杂环境中的表现，推动AI系统在实际应用中的可靠性和适应性。

## 📄 摘要（原文）

> Adversarial board games, as a paradigmatic domain of strategic reasoning and intelligence, have long served as both a popular competitive activity and a benchmark for evaluating artificial intelligence (AI) systems. Building on this foundation, we propose an adversarial benchmarking framework to assess the comprehensive performance of Large Language Models (LLMs) through board games competition, compensating the limitation of data dependency of the mainstream Question-and-Answer (Q&A) based benchmark method. We introduce Qi Town, a specialized evaluation platform that supports 5 widely played games and involves 20 LLM-driven players. The platform employs both the Elo rating system and a novel Performance Loop Graph (PLG) to quantitatively evaluate the technical capabilities of LLMs, while also capturing Positive Sentiment Score (PSS) throughout gameplay to assess mental fitness. The evaluation is structured as a round-robin tournament, enabling systematic comparison across players. Experimental results indicate that, despite technical differences, most LLMs remain optimistic about winning and losing, demonstrating greater adaptability to high-stress adversarial environments than humans. On the other hand, the complex relationship between cyclic wins and losses in PLGs exposes the instability of LLMs' skill play during games, warranting further explanation and exploration.

