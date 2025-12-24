---
layout: default
title: "From Personalization to Prejudice: Bias and Discrimination in Memory-Enhanced AI Agents for Recruitment"
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

**揭示记忆增强型AI招聘Agent中的偏见引入与强化机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `AI Agent` `记忆增强` `个性化` `偏见` `招聘` `公平性` `机器学习`

## 📋 核心要点

1. 现有研究较少关注记忆增强型AI Agent中的偏见问题，尤其是在个性化过程中如何引入和强化偏见。
2. 该研究通过模拟招聘场景下的记忆增强型Agent，分析偏见的产生和演变过程，揭示个性化带来的潜在风险。
3. 实验结果表明，即使使用安全训练的LLM，偏见仍然会通过个性化被系统性地引入和强化，需要额外的安全措施。

## 📝 摘要（中文）

大型语言模型(LLMs)赋予了AI Agent强大的理解、推理和交互能力，使其能够胜任各种任务。通过添加记忆功能，AI Agent可以实现跨交互的连续性，从过去的经验中学习，并随着时间的推移提高行为和响应的相关性，这种方式被称为记忆增强型个性化。虽然这种通过记忆实现的个性化具有明显的优势，但也带来了偏见的风险。尽管之前的研究已经强调了ML和LLM中的偏见，但由于记忆增强型个性化Agent而产生的偏见在很大程度上尚未被探索。本文以招聘为例，模拟了记忆增强型个性化Agent的行为，并研究了偏见是如何在操作的各个阶段引入和加强的。对使用安全训练LLM的Agent进行的实验表明，偏见是通过个性化系统地引入和强化的，这强调了在基于记忆增强型LLM的AI Agent中采取额外保护措施或Agent防护措施的必要性。

## 🔬 方法详解

**问题定义**：论文旨在研究在记忆增强型AI Agent中，个性化如何引入和强化偏见。现有方法主要关注ML和LLM的固有偏见，忽略了记忆增强和个性化带来的新偏见来源。在招聘场景下，这种偏见可能导致不公平的候选人筛选，损害公平性。

**核心思路**：论文的核心思路是通过模拟一个记忆增强型AI招聘Agent，观察其在与不同候选人交互过程中，如何逐渐形成和强化偏见。通过控制实验变量，分析偏见产生的具体环节和影响因素。这种模拟方法能够更深入地理解偏见的动态演变过程。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 构建一个基于LLM的AI招聘Agent，该Agent具有记忆功能，可以记录与候选人的交互历史。2) 设计模拟的候选人数据集，包含不同的背景和特征。3) Agent与候选人进行交互，根据候选人的信息和历史记录进行评估和筛选。4) 分析Agent的决策过程，识别偏见产生的环节，并量化偏见的程度。

**关键创新**：该研究的关键创新在于关注了记忆增强型AI Agent中的个性化偏见问题，并提出了一个模拟框架来研究这种偏见的产生和演变。与以往研究不同，该研究不仅关注LLM的固有偏见，更关注个性化带来的新偏见来源。

**关键设计**：在实验设计方面，论文可能控制了候选人的某些特征（例如性别、种族、教育背景等），并观察Agent在不同特征组合下的决策差异。此外，论文可能使用了特定的指标来量化偏见的程度，例如公平性指标（如机会均等、统计均等）或偏差指标（如优势比、差异倍数）。具体的LLM选择和训练方法（例如，是否使用安全训练）也是关键的设计因素。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16532v1/Figure_1_overview.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该研究通过实验证明，即使使用经过安全训练的LLM，记忆增强型个性化Agent仍然会系统性地引入和强化偏见。这表明，仅仅依靠LLM的安全训练是不够的，还需要额外的保护措施或Agent防护措施来减轻个性化带来的偏见风险。具体的性能数据和提升幅度未知，需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于各种需要个性化推荐或决策的AI系统中，例如金融信贷、教育评估、医疗诊断等。通过理解和减轻记忆增强型AI Agent中的偏见，可以提高AI系统的公平性、透明度和可靠性，避免歧视性结果，促进社会公平。

## 📄 摘要（原文）

> Large Language Models (LLMs) have empowered AI agents with advanced capabilities for understanding, reasoning, and interacting across diverse tasks. The addition of memory further enhances them by enabling continuity across interactions, learning from past experiences, and improving the relevance of actions and responses over time; termed as memory-enhanced personalization. Although such personalization through memory offers clear benefits, it also introduces risks of bias. While several previous studies have highlighted bias in ML and LLMs, bias due to memory-enhanced personalized agents is largely unexplored. Using recruitment as an example use case, we simulate the behavior of a memory-enhanced personalized agent, and study whether and how bias is introduced and amplified in and across various stages of operation. Our experiments on agents using safety-trained LLMs reveal that bias is systematically introduced and reinforced through personalization, emphasizing the need for additional protective measures or agent guardrails in memory-enhanced LLM-based AI agents.

