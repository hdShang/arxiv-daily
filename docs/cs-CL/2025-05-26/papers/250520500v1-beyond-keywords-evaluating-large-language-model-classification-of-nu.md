---
layout: default
title: "Beyond Keywords: Evaluating Large Language Model Classification of Nuanced Ableism"
---

# Beyond Keywords: Evaluating Large Language Model Classification of Nuanced Ableism

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20500" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20500v1</a>
  <a href="https://arxiv.org/pdf/2505.20500.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20500v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20500v1', 'Beyond Keywords: Evaluating Large Language Model Classification of Nuanced Ableism')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Naba Rizvi, Harper Strickland, Saleha Ahmedi, Aekta Kallepalli, Isha Khirwadkar, William Wu, Imani N. S. Munyaka, Nedjma Ousidhoum

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**评估大型语言模型对细微能力歧视的分类能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `能力歧视` `自闭症` `上下文理解` `内容审核` `偏见识别`

## 📋 核心要点

1. 现有研究对大型语言模型在识别能力歧视方面的能力了解不足，尤其是在自闭症相关内容的识别上存在显著缺陷。
2. 本文通过评估四种大型语言模型在识别细微能力歧视方面的表现，探讨其对相关术语的理解与实际效果之间的差距。
3. 实验结果表明，LLMs能够识别自闭症相关语言，但常常错过有害含义，且与人类标注者在上下文理解上存在显著差异。

## 📝 摘要（中文）

大型语言模型（LLMs）在决策任务中越来越多地被使用，如简历筛选和内容审核，这使得它们有能力放大或抑制某些观点。尽管先前的研究已识别出LLMs中的与残疾相关的偏见，但关于它们如何概念化能力歧视或在文本中检测能力歧视的研究仍然较少。本文评估了四种LLMs识别针对自闭症个体的细微能力歧视的能力，发现LLMs能够识别与自闭症相关的语言，但常常忽视有害或冒犯的含义。此外，本文还进行了人类与LLMs解释的定性比较，发现LLMs倾向于依赖表面关键词匹配，导致上下文误解，而人类标注者则考虑上下文、说话者身份和潜在影响。尽管如此，LLMs与人类在标注方案上达成一致，表明二元分类足以评估LLMs的表现，这与先前涉及人类标注者的研究结果一致。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在识别细微能力歧视方面的不足，特别是针对自闭症个体的内容识别。现有方法往往依赖关键词匹配，导致上下文理解不准确。

**核心思路**：通过评估四种不同的LLMs，分析它们在识别能力歧视时的表现与人类标注者的差异，探讨如何改进模型的上下文理解能力。

**技术框架**：研究采用定量与定性相结合的方法，首先对LLMs进行测试以识别自闭症相关的语言，然后与人类标注者的结果进行比较，分析其在上下文理解上的差异。

**关键创新**：本文的创新在于系统性地评估LLMs在识别细微能力歧视方面的能力，揭示了它们在上下文理解上的局限性，并与人类标注者的表现进行了深入比较。

**关键设计**：研究中使用了标准化的标注方案，确保LLMs与人类标注者在评估标准上的一致性，采用二元分类方法来评估模型性能，确保结果的可比性。

## 📊 实验亮点

实验结果显示，尽管LLMs能够识别与自闭症相关的语言，但在识别有害含义方面的准确率较低，且与人类标注者相比，LLMs的上下文理解能力明显不足。总体而言，LLMs与人类在标注方案上的一致性表明，二元分类方法在评估模型性能时是有效的。

## 🎯 应用场景

该研究的潜在应用领域包括内容审核、社交媒体监控和招聘系统等，能够帮助开发更具包容性的人工智能系统，减少对残疾群体的偏见和歧视。未来，改进大型语言模型的上下文理解能力将有助于提升其在敏感话题上的应用效果，促进社会公平。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used in decision-making tasks like résumé screening and content moderation, giving them the power to amplify or suppress certain perspectives. While previous research has identified disability-related biases in LLMs, little is known about how they conceptualize ableism or detect it in text. We evaluate the ability of four LLMs to identify nuanced ableism directed at autistic individuals. We examine the gap between their understanding of relevant terminology and their effectiveness in recognizing ableist content in context. Our results reveal that LLMs can identify autism-related language but often miss harmful or offensive connotations. Further, we conduct a qualitative comparison of human and LLM explanations. We find that LLMs tend to rely on surface-level keyword matching, leading to context misinterpretations, in contrast to human annotators who consider context, speaker identity, and potential impact. On the other hand, both LLMs and humans agree on the annotation scheme, suggesting that a binary classification is adequate for evaluating LLM performance, which is consistent with findings from prior studies involving human annotators.

