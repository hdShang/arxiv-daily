---
layout: default
title: "Bias Mitigation Agent: Optimizing Source Selection for Fair and Balanced Knowledge Retrieval"
---

# Bias Mitigation Agent: Optimizing Source Selection for Fair and Balanced Knowledge Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18724" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18724v1</a>
  <a href="https://arxiv.org/pdf/2508.18724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18724v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18724v1', 'Bias Mitigation Agent: Optimizing Source Selection for Fair and Balanced Knowledge Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karanbir Singh, Deepak Muppiri, William Ngu

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-26

**备注**: Accepted at KDD'2025 Agent4IR workshop

---

## 💡 一句话要点

**提出偏差缓解代理以优化知识检索中的源选择**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏差缓解` `知识检索` `多代理系统` `公平性` `信息源选择`

## 📋 核心要点

1. 现有方法在知识检索中存在偏见问题，影响信息的公平性和用户信任。
2. 本文提出的偏差缓解代理通过多代理系统优化信息源选择，以减少偏见。
3. 实验结果显示，该方法相比基线策略偏见减少了81.82%，显著提升了信息公平性。

## 📝 摘要（中文）

大型语言模型（LLMs）已在人工智能领域引发了变革，开启了生成应用的新纪元。然而，这些模型继承了内部和外部信息源中的偏见，影响了检索信息的公平性和均衡性，降低了用户信任。为了解决这一关键挑战，本文提出了一种新颖的偏差缓解代理，这是一个多代理系统，旨在通过优化源选择来协调偏差缓解的工作流程，从而确保检索内容既高度相关又尽量减少偏见，以促进公平和均衡的知识传播。实验结果表明，与基线的简单检索策略相比，偏见减少了81.82%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在知识检索中继承的偏见问题。现有方法在信息源选择上存在不足，导致检索结果的公平性和均衡性受到影响。

**核心思路**：论文提出的偏差缓解代理通过多代理系统优化信息源选择，旨在减少偏见并提高信息的相关性和公平性。该设计旨在通过专门的代理协调偏差缓解工作流程。

**技术框架**：整体架构包括多个专门的代理，每个代理负责不同的信息源选择和偏差评估。系统通过协作来优化最终的知识检索结果。

**关键创新**：最重要的创新点在于引入了多代理系统来动态优化信息源选择，从而有效减少偏见。这一方法与传统的单一检索策略有本质区别。

**关键设计**：在设计中，系统设置了多个参数以评估信息源的偏见程度，并采用特定的损失函数来优化检索结果的公平性和相关性。

## 📊 实验亮点

实验结果表明，偏差缓解代理相比基线的简单检索策略，偏见减少了81.82%。这一显著提升证明了该方法在促进公平和均衡知识传播方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动化信息检索、智能问答系统和内容推荐等。通过优化信息源选择，能够提高系统的公平性和用户信任，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have transformed the field of artificial intelligence by unlocking the era of generative applications. Built on top of generative AI capabilities, Agentic AI represents a major shift toward autonomous, goal-driven systems that can reason, retrieve, and act. However, they also inherit the bias present in both internal and external information sources. This significantly affects the fairness and balance of retrieved information, and hence reduces user trust. To address this critical challenge, we introduce a novel Bias Mitigation Agent, a multi-agent system designed to orchestrate the workflow of bias mitigation through specialized agents that optimize the selection of sources to ensure that the retrieved content is both highly relevant and minimally biased to promote fair and balanced knowledge dissemination. The experimental results demonstrate an 81.82\% reduction in bias compared to a baseline naive retrieval strategy.

