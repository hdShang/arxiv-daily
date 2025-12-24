---
layout: default
title: "How Large Language Models play humans in online conversations: a simulated study of the 2016 US politics on Reddit"
---

# How Large Language Models play humans in online conversations: a simulated study of the 2016 US politics on Reddit

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21620" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21620v1</a>
  <a href="https://arxiv.org/pdf/2506.21620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21620v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21620v1', 'How Large Language Models play humans in online conversations: a simulated study of the 2016 US politics on Reddit')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniele Cirulli, Giulio Cimini, Giovanni Palermo

**分类**: cs.CL, cs.AI, cs.CY, cs.SI, physics.soc-ph

**发布日期**: 2025-06-23

---

## 💡 一句话要点

**评估大型语言模型在2016年美国政治讨论中的表现**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自然语言生成` `政治讨论` `社交媒体` `情感分析` `语义嵌入` `在线辩论` `AI操控`

## 📋 核心要点

1. 现有方法在模拟人类在线政治讨论时，面临生成内容的真实性和多样性挑战。
2. 论文通过GPT-4生成评论，模拟真实和人工用户，探索其在政治讨论中的表现。
3. 实验结果显示，GPT-4生成的评论在语义上与真实评论相似，但更倾向于形成共识而非异议。

## 📝 摘要（中文）

大型语言模型（LLMs）最近成为自然语言生成的强大工具，应用范围广泛，包括内容创作和社会模拟。本文研究了LLMs在模拟2016年美国总统选举期间Reddit讨论中的表现，特别是通过GPT-4生成用户评论，分析其政治倾向、情感和语言特征。研究发现，GPT-4能够生成与社区支持的候选人一致的现实评论，但更容易创造共识而非异议。此外，真实与人工评论在语义嵌入空间中表现出良好的分离性，尽管手动检查时难以区分。这些发现为LLMs在在线讨论中的潜在影响提供了见解，尤其是在政治辩论和叙事塑造方面，具有更广泛的AI驱动话语操控的含义。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在模拟人类在线政治讨论时生成内容的真实性和多样性问题。现有方法在这方面的表现不足，尤其是在处理复杂的政治情境时。

**核心思路**：论文的核心思路是利用GPT-4生成用户评论，通过模拟真实和人工用户的方式，评估其在政治讨论中的表现和影响。这样的设计旨在揭示LLMs在复杂社会情境中的应用潜力。

**技术框架**：研究采用了三种不同的实验设计，分别让GPT-4模拟真实用户和人工用户生成评论。分析阶段包括对生成评论的政治倾向、情感和语言特征进行比较，基于真实用户贡献和基线模型进行基准测试。

**关键创新**：最重要的技术创新点在于通过LLMs生成的评论能够在语义上与真实评论相似，且在手动检查时难以区分，这表明LLMs在在线讨论中的潜在影响力。

**关键设计**：在实验中，GPT-4的参数设置和生成策略经过精心设计，以确保生成评论的多样性和真实性。损失函数和评估标准也经过调整，以便更好地反映评论的政治倾向和情感特征。

## 📊 实验亮点

实验结果显示，GPT-4生成的评论在语义上与真实用户的评论表现出良好的相似性，且在政治倾向上能够有效模拟支持或反对候选人的观点。尽管生成的评论更容易形成共识，但在语义嵌入空间中，真实与人工评论表现出明显的分离性，表明LLMs在在线讨论中的潜在影响。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容生成、政治舆论分析和在线辩论的模拟。通过理解LLMs在政治讨论中的表现，可以为政策制定者和社会科学家提供重要的见解，帮助他们更好地应对AI驱动的舆论操控和信息传播问题。

## 📄 摘要（原文）

> Large Language Models (LLMs) have recently emerged as powerful tools for natural language generation, with applications spanning from content creation to social simulations. Their ability to mimic human interactions raises both opportunities and concerns, particularly in the context of politically relevant online discussions. In this study, we evaluate the performance of LLMs in replicating user-generated content within a real-world, divisive scenario: Reddit conversations during the 2016 US Presidential election. In particular, we conduct three different experiments, asking GPT-4 to generate comments by impersonating either real or artificial partisan users. We analyze the generated comments in terms of political alignment, sentiment, and linguistic features, comparing them against real user contributions and benchmarking against a null model. We find that GPT-4 is able to produce realistic comments, both in favor of or against the candidate supported by the community, yet tending to create consensus more easily than dissent. In addition we show that real and artificial comments are well separated in a semantically embedded space, although they are indistinguishable by manual inspection. Our findings provide insights on the potential use of LLMs to sneak into online discussions, influence political debate and shape political narratives, bearing broader implications of AI-driven discourse manipulation.

