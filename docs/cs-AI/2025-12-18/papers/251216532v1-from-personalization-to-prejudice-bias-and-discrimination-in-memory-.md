---
layout: default
title: From Personalization to Prejudice: Bias and Discrimination in Memory-Enhanced AI Agents for Recruitment
---

# From Personalization to Prejudice: Bias and Discrimination in Memory-Enhanced AI Agents for Recruitment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16532" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16532v1</a>
  <a href="https://arxiv.org/pdf/2512.16532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16532v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16532v1', 'From Personalization to Prejudice: Bias and Discrimination in Memory-Enhanced AI Agents for Recruitment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Himanshu Gharat, Himanshi Agrawal, Gourab K. Patro

**分类**: cs.AI, cs.IR

**发布日期**: 2025-12-18

**备注**: In Proceedings of the Nineteenth ACM International Conference on Web Search and Data Mining (WSDM '26)

**期刊**: In Proceedings of the Nineteenth ACM International Conference on Web Search and Data Mining (WSDM '26), 2026, Boise, ID, USA. ACM, New York, NY, USA

**DOI**: [10.1145/3773966.3779376](https://doi.org/10.1145/3773966.3779376)

---

## 💡 一句话要点

**揭示记忆增强型AI招聘Agent的偏见引入与强化机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `AI Agent` `记忆增强` `个性化` `偏见` `招聘` `公平性` `机器学习`

## 📋 核心要点

1. 现有研究较少关注记忆增强型AI Agent中的偏见问题，尤其是在个性化过程中如何引入和强化偏见。
2. 该研究模拟了记忆增强型AI招聘Agent的行为，分析偏见在不同阶段的产生和演变过程。
3. 实验结果表明，即使使用安全训练的LLM，偏见仍然会通过个性化被系统性地引入和强化。

## 📝 摘要（中文）

大型语言模型(LLMs)赋予了AI Agent强大的理解、推理和交互能力，可以处理各种任务。通过添加记忆功能，AI Agent能够跨交互保持连续性，从过去的经验中学习，并随着时间的推移提高行为和响应的相关性，这种方式被称为记忆增强型个性化。虽然这种通过记忆实现的个性化提供了明显的优势，但也带来了偏见风险。尽管之前的研究已经强调了ML和LLM中的偏见，但关于记忆增强型个性化Agent所带来的偏见在很大程度上尚未被探索。本文以招聘为例，模拟了记忆增强型个性化Agent的行为，并研究了偏见是如何在各个操作阶段被引入和加强的。对使用安全训练LLM的Agent进行的实验表明，偏见通过个性化被系统地引入和强化，强调了在基于记忆增强型LLM的AI Agent中采取额外保护措施或Agent防护措施的必要性。

## 🔬 方法详解

**问题定义**：论文旨在研究在记忆增强型AI Agent中，尤其是在招聘场景下，偏见是如何被引入和强化的。现有方法主要关注ML和LLM本身的偏见，而忽略了记忆增强和个性化带来的新的偏见来源。这些偏见可能导致不公平的招聘结果，损害求职者的权益。

**核心思路**：论文的核心思路是通过模拟记忆增强型AI Agent在招聘过程中的行为，观察和分析偏见的产生和演变过程。通过控制实验变量，例如Agent的初始知识、交互历史等，来识别偏见的关键来源和影响因素。

**技术框架**：该研究的技术框架主要包括以下几个模块：1) 招聘场景模拟器：模拟真实的招聘流程，包括简历筛选、面试等环节。2) 记忆增强型AI Agent：基于LLM构建，具有记忆功能，能够记录和利用与求职者的交互历史。3) 偏见评估指标：用于量化Agent在招聘过程中产生的偏见程度，例如不同性别、种族求职者的录取率差异。4) 安全训练的LLM：使用经过安全训练的LLM作为Agent的基础模型，以降低初始偏见。

**关键创新**：该研究的关键创新在于关注了记忆增强和个性化对AI Agent偏见的影响。与以往研究主要关注模型本身的偏见不同，该研究揭示了记忆功能如何放大和固化偏见，以及个性化策略如何加剧不公平现象。

**关键设计**：研究中使用了安全训练的LLM，并通过控制Agent的记忆容量、交互策略等参数来模拟不同的个性化程度。同时，设计了多种偏见评估指标，例如统计不同群体求职者的录取率差异、分析Agent的决策依据等。此外，还探索了不同的Agent防护措施，例如偏见检测和纠正机制，以降低偏见的影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16532v1/Figure_1_overview.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，即使使用安全训练的LLM，记忆增强型AI Agent仍然会通过个性化引入和强化偏见。具体来说，Agent在与特定群体的求职者交互后，可能会形成对该群体的刻板印象，从而影响后续的招聘决策。这种偏见会随着交互次数的增加而逐渐加剧，导致不公平的招聘结果。

## 🎯 应用场景

该研究成果可应用于各种需要个性化AI Agent的场景，例如智能客服、教育辅导、金融风控等。通过识别和减轻记忆增强型AI Agent中的偏见，可以提高决策的公平性和透明度，避免歧视性结果，从而提升用户体验和社会福祉。未来的研究可以探索更有效的偏见检测和纠正方法，以及设计更公平的个性化策略。

## 📄 摘要（原文）

> Large Language Models (LLMs) have empowered AI agents with advanced capabilities for understanding, reasoning, and interacting across diverse tasks. The addition of memory further enhances them by enabling continuity across interactions, learning from past experiences, and improving the relevance of actions and responses over time; termed as memory-enhanced personalization. Although such personalization through memory offers clear benefits, it also introduces risks of bias. While several previous studies have highlighted bias in ML and LLMs, bias due to memory-enhanced personalized agents is largely unexplored. Using recruitment as an example use case, we simulate the behavior of a memory-enhanced personalized agent, and study whether and how bias is introduced and amplified in and across various stages of operation. Our experiments on agents using safety-trained LLMs reveal that bias is systematically introduced and reinforced through personalization, emphasizing the need for additional protective measures or agent guardrails in memory-enhanced LLM-based AI agents.

