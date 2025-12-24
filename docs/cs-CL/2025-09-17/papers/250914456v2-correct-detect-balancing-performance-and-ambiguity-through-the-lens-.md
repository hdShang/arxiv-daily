---
layout: default
title: "Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs"
---

# Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14456" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14456v2</a>
  <a href="https://arxiv.org/pdf/2509.14456.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14456v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14456v2', 'Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amber Shore, Russell Scheinberg, Ameeta Agrawal, So Young Lee

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-17 (更新: 2025-10-21)

**备注**: Accepted at EMNLP 2025 (main)

---

## 💡 一句话要点

**揭示LLM在共指消解中性能与歧义检测的权衡：Correct-Detect困境**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `共指消解` `歧义检测` `自然语言理解` `Correct-Detect权衡`

## 📋 核心要点

1. 大型语言模型在共指消解中面临歧义性挑战，影响下游任务性能。
2. 论文提出Correct-Detect框架，研究LLM在消歧和检测歧义间的权衡。
3. 实验表明LLM具备消歧和检测能力，但难以同时优化两者性能。

## 📝 摘要（中文）

大型语言模型（LLM）旨在反映人类的语言能力。但人类可以获取广泛且具象的上下文，这对于检测和解决语言歧义至关重要，即使在孤立的文本片段中也是如此。共指消解任务中存在一种基本的语义歧义：代词与先前提到的人之间的关系是什么？这种能力几乎隐含在每个下游任务中，并且此级别的歧义的存在会显着改变性能。我们表明，LLM可以通过最少的提示在共指消歧和共指歧义检测方面都取得良好的性能，但是，它们不能同时做到这两点。我们提出了CORRECT-DETECT权衡：尽管模型同时具有这两种能力并隐式地部署它们，但成功地平衡这两种能力仍然难以实现。

## 🔬 方法详解

**问题定义**：论文关注大型语言模型（LLM）在共指消解任务中处理歧义的能力。现有的LLM虽然在共指消解上表现良好，但往往忽略了歧义检测的重要性，或者无法同时兼顾消歧和歧义检测，导致在某些场景下性能下降。现有方法的痛点在于无法有效平衡性能和歧义检测能力。

**核心思路**：论文的核心思路是揭示LLM在共指消解任务中，性能（Correct）和歧义检测（Detect）之间存在一种内在的权衡关系。模型在擅长消歧时，往往会忽略歧义的存在；而专注于歧义检测时，又可能牺牲消歧的准确性。这种权衡被称为CORRECT-DETECT权衡。

**技术框架**：论文没有提出一个全新的技术框架，而是通过实验分析来揭示LLM的内在特性。实验流程主要包括：1) 构建包含歧义和非歧义共指消解的测试数据集；2) 使用不同的prompting策略来引导LLM进行共指消解和歧义检测；3) 评估LLM在消歧和歧义检测上的性能；4) 分析性能之间的权衡关系。

**关键创新**：论文的关键创新在于发现了LLM在共指消解任务中存在的CORRECT-DETECT权衡。这并非一个具体的算法或模型，而是一种对LLM内在能力的深刻洞察。这种发现有助于研究人员更好地理解LLM的局限性，并设计更有效的prompting策略或模型结构来解决这一问题。

**关键设计**：论文的关键设计在于精心设计的实验和评估指标。通过控制prompting策略，研究人员可以观察LLM在消歧和歧义检测之间的权衡。评估指标包括消歧的准确率和歧义检测的召回率等。具体的参数设置和网络结构取决于所使用的LLM模型，论文主要关注的是LLM的通用特性，而非特定模型的优化。

## 📊 实验亮点

论文通过实验证明，LLM在共指消解中存在Correct-Detect权衡。虽然LLM具备消歧和歧义检测的能力，但难以同时达到最佳性能。这意味着在设计LLM应用时，需要根据具体场景权衡消歧准确率和歧义检测能力。

## 🎯 应用场景

该研究成果可应用于提升LLM在自然语言理解任务中的鲁棒性和可靠性，尤其是在需要处理歧义性文本的场景，如信息抽取、问答系统和对话系统。通过更好地理解和解决Correct-Detect权衡，可以开发出更智能、更可靠的AI系统。

## 📄 摘要（原文）

> Large Language Models (LLMs) are intended to reflect human linguistic competencies. But humans have access to a broad and embodied context, which is key in detecting and resolving linguistic ambiguities, even in isolated text spans. A foundational case of semantic ambiguity is found in the task of coreference resolution: how is a pronoun related to an earlier person mention? This capability is implicit in nearly every downstream task, and the presence of ambiguity at this level can alter performance significantly. We show that LLMs can achieve good performance with minimal prompting in both coreference disambiguation and the detection of ambiguity in coreference, however, they cannot do both at the same time. We present the CORRECT-DETECT trade-off: though models have both capabilities and deploy them implicitly, successful performance balancing these two abilities remains elusive.

