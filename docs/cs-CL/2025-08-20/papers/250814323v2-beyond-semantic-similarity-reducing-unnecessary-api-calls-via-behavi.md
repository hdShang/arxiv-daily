---
layout: default
title: "Beyond Semantic Similarity: Reducing Unnecessary API Calls via Behavior-Aligned Retriever"
---

# Beyond Semantic Similarity: Reducing Unnecessary API Calls via Behavior-Aligned Retriever

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14323" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14323v2</a>
  <a href="https://arxiv.org/pdf/2508.14323.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14323v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14323v2', 'Beyond Semantic Similarity: Reducing Unnecessary API Calls via Behavior-Aligned Retriever')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixin Chen, Ying Xiong, Shangyu Wu, Yufei Cui, Xue Liu, Nan Guan, Chun Jason Xue

**分类**: cs.CL

**发布日期**: 2025-08-20 (更新: 2025-08-25)

---

## 💡 一句话要点

**提出行为对齐检索器以减少不必要的API调用**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工具增强` `大型语言模型` `行为对齐` `对比学习` `函数调用` `自然语言处理` `智能助手`

## 📋 核心要点

1. 现有方法在处理工具增强的LLMs时，面临高训练开销和不一致示范样本导致的调用行为误导等挑战。
2. 本文提出了一种行为对齐检索器（BAR），通过提供行为一致的示范来帮助LLMs做出更准确的工具使用决策。
3. 实验结果显示，该方法显著减少了错误的函数调用，同时保持了高任务性能，展现了其高效性和成本效益。

## 📝 摘要（中文）

工具增强的大型语言模型（LLMs）利用外部功能扩展其能力，但不准确的函数调用可能导致效率低下和成本增加。现有方法通过微调LLMs或使用示范提示来解决这一挑战，但往往面临高训练开销，并且未能考虑不一致的示范样本，误导模型的调用行为。本文训练了一种行为对齐检索器（BAR），提供行为一致的示范，帮助LLMs做出更准确的工具使用决策。我们构建了一个包含不同函数调用行为的语料库，并使用对比学习框架训练BAR，确保行为一致示范的稳健检索。实验表明，我们的方法显著减少了错误函数调用，同时保持了高任务性能，为工具增强的LLMs提供了一种高效且具成本效益的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决工具增强的LLMs在函数调用时的不准确性问题。现有方法往往依赖于微调或示范提示，导致高训练成本和不一致的示范样本影响模型的调用行为。

**核心思路**：论文提出的行为对齐检索器（BAR）通过提供行为一致的示范，帮助LLMs在调用外部功能时做出更准确的决策。这样的设计旨在减少错误调用，提高模型的效率。

**技术框架**：整体架构包括构建一个包含不同函数调用行为的语料库，并使用对比学习框架进行训练。BAR的训练过程涉及定制的正负样本对和双负对比损失，确保检索到的示范具有行为一致性。

**关键创新**：最重要的技术创新在于引入了行为对齐的检索机制，通过对比学习确保示范的一致性，从而显著提高了函数调用的准确性。这与现有方法的示范不一致性形成了本质区别。

**关键设计**：在训练过程中，使用了定制的正负样本对和双负对比损失函数，以增强模型对行为一致示范的学习能力。具体的网络结构和参数设置在实验中经过优化，以确保最佳的检索效果。

## 📊 实验亮点

实验结果表明，行为对齐检索器（BAR）显著减少了错误的函数调用，提升了工具增强LLMs的整体性能。与基线方法相比，错误调用率降低了XX%，同时任务性能保持在高水平，展现了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化工具和其他需要外部功能调用的自然语言处理任务。通过减少错误调用，该方法可以显著降低系统的运行成本，提高用户体验，未来可能在多种行业中得到广泛应用。

## 📄 摘要（原文）

> Tool-augmented large language models (LLMs) leverage external functions to extend their capabilities, but inaccurate function calls can lead to inefficiencies and increased costs.Existing methods address this challenge by fine-tuning LLMs or using demonstration-based prompting, yet they often suffer from high training overhead and fail to account for inconsistent demonstration samples, which misguide the model's invocation behavior. In this paper, we trained a behavior-aligned retriever (BAR), which provides behaviorally consistent demonstrations to help LLMs make more accurate tool-using decisions. To train the BAR, we construct a corpus including different function-calling behaviors, i.e., calling or non-calling.We use the contrastive learning framework to train the BAR with customized positive/negative pairs and a dual-negative contrastive loss, ensuring robust retrieval of behaviorally consistent examples.Experiments demonstrate that our approach significantly reduces erroneous function calls while maintaining high task performance, offering a cost-effective and efficient solution for tool-augmented LLMs.

