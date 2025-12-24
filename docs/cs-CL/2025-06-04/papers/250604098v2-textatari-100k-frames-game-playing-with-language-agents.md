---
layout: default
title: "TextAtari: 100K Frames Game Playing with Language Agents"
---

# TextAtari: 100K Frames Game Playing with Language Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04098" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04098v2</a>
  <a href="https://arxiv.org/pdf/2506.04098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04098v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04098v2', 'TextAtari: 100K Frames Game Playing with Language Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhao Li, Wenwu Li, Chuyun Shen, Junjie Sheng, Zixiao Huang, Di Wu, Yun Hua, Wei Yin, Xiangfeng Wang, Hongyuan Zha, Bo Jin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-04 (更新: 2025-06-10)

**备注**: 51 pages, 39 figures

**🔗 代码/项目**: [GITHUB](https://github.com/Lww007/Text-Atari-Agents)

---

## 💡 一句话要点

**提出TextAtari基准以评估语言代理在长时间决策任务中的表现**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间决策` `语言代理` `自然语言处理` `Atari游戏` `无监督学习` `基准测试` `智能系统` `多模态学习`

## 📋 核心要点

1. 现有方法在长时间决策任务中面临顺序推理和状态跟踪的挑战，导致语言代理与人类玩家的表现差距显著。
2. 论文提出TextAtari基准，通过将视觉状态转换为文本描述，创建了一个结合自然语言处理与决策任务的测试平台。
3. 实验结果表明，语言代理在复杂规划任务中表现不佳，尤其是在长时间决策中，显示出显著的性能差距。

## 📝 摘要（中文）

我们提出了TextAtari，这是一个用于评估语言代理在长达100,000步的决策任务中的基准。通过将经典Atari游戏的视觉状态表示转换为丰富的文本描述，TextAtari创建了一个将顺序决策与自然语言处理相结合的挑战性测试平台。该基准包括近100个具有不同复杂性、动作空间和规划视野的任务，所有任务通过无监督表示学习框架（AtariARI）呈现。我们评估了三种开源大型语言模型（Qwen2.5-7B、Gemma-7B和Llama3.1-8B）在三种代理框架（零-shot、少-shot链式思维和反思推理）下的表现，探讨不同形式的先验知识如何影响这些长时间挑战的表现。结果显示，语言代理与人类玩家在复杂规划任务中存在显著性能差距，突显了在数万步的顺序推理、状态跟踪和战略规划中的挑战。TextAtari提供了标准化的评估协议、基线实现和促进语言模型与规划交叉研究的框架。

## 🔬 方法详解

**问题定义**：本文旨在解决语言代理在长时间决策任务中的表现不足，现有方法在顺序推理和状态跟踪方面存在显著挑战，导致与人类玩家的差距。

**核心思路**：通过创建TextAtari基准，将经典Atari游戏的视觉状态转换为文本描述，从而为语言代理提供丰富的上下文信息，促进其在复杂决策任务中的表现。

**技术框架**：整体架构包括任务生成模块、无监督表示学习框架（AtariARI）和评估模块。任务生成模块负责创建多样化的任务，AtariARI负责将视觉信息转换为文本，评估模块则用于对代理的表现进行标准化评估。

**关键创新**：最重要的技术创新在于将视觉状态与自然语言处理结合，形成一个新的基准测试平台，填补了现有方法在长时间决策任务中的空白。

**关键设计**：在参数设置上，使用了多种大型语言模型（如Qwen2.5-7B、Gemma-7B和Llama3.1-8B），并在不同的代理框架下（零-shot、少-shot链式思维和反思推理）进行评估，确保了方法的全面性和有效性。

## 📊 实验亮点

实验结果显示，语言代理在长时间决策任务中的表现与人类玩家相比存在显著差距，尤其是在复杂的规划任务中，表现提升幅度有限。这一发现强调了在数万步的决策过程中，顺序推理和状态跟踪的挑战。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、智能助手和自动化决策系统。通过提升语言代理在复杂决策中的表现，TextAtari为未来的多模态学习和智能系统的发展提供了重要的参考和基础。其实际价值在于推动自然语言处理与决策制定的结合，促进更智能的交互系统的实现。

## 📄 摘要（原文）

> We present TextAtari, a benchmark for evaluating language agents on very long-horizon decision-making tasks spanning up to 100,000 steps. By translating the visual state representations of classic Atari games into rich textual descriptions, TextAtari creates a challenging test bed that bridges sequential decision-making with natural language processing. The benchmark includes nearly 100 distinct tasks with varying complexity, action spaces, and planning horizons, all rendered as text through an unsupervised representation learning framework (AtariARI). We evaluate three open-source large language models (Qwen2.5-7B, Gemma-7B, and Llama3.1-8B) across three agent frameworks (zero-shot, few-shot chain-of-thought, and reflection reasoning) to assess how different forms of prior knowledge affect performance on these long-horizon challenges. Four scenarios-Basic, Obscured, Manual Augmentation, and Reference-based-investigate the impact of semantic understanding, instruction comprehension, and expert demonstrations on agent decision-making. Our results reveal significant performance gaps between language agents and human players in extensive planning tasks, highlighting challenges in sequential reasoning, state tracking, and strategic planning across tens of thousands of steps. TextAtari provides standardized evaluation protocols, baseline implementations, and a framework for advancing research at the intersection of language models and planning. Our code is available at https://github.com/Lww007/Text-Atari-Agents.

