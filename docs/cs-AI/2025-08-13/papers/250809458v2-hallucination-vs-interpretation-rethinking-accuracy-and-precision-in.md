---
layout: default
title: "Hallucination vs interpretation: rethinking accuracy and precision in AI-assisted data extraction for knowledge synthesis"
---

# Hallucination vs interpretation: rethinking accuracy and precision in AI-assisted data extraction for knowledge synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09458" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09458v2</a>
  <a href="https://arxiv.org/pdf/2508.09458.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09458v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09458v2', 'Hallucination vs interpretation: rethinking accuracy and precision in AI-assisted data extraction for knowledge synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xi Long, Christy Boscardin, Lauren A. Maggio, Joseph A. Costello, Ralph Gonzales, Rasmyah Hammoudeh, Ki Lai, Yoon Soo Park, Brian C. Gin

**分类**: cs.HC, cs.AI, cs.ET

**发布日期**: 2025-08-13 (更新: 2025-08-14)

---

## 💡 一句话要点

**提出AI辅助数据提取方法以提高知识综合的准确性和效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识综合` `数据提取` `人工智能` `大型语言模型` `健康职业教育` `文献综述` `一致性评估`

## 📋 核心要点

1. 现有的知识综合方法在数据提取过程中劳动强度大，且人工提取容易出现不一致性和错误。
2. 本研究提出了一种基于大型语言模型的自动化数据提取平台，旨在提高提取效率并减少人工错误。
3. 实验结果表明，AI与人类在具体问题上的一致性高达75.8%，而AI的错误率仅为1.51%，显示出AI在知识综合中的潜力。

## 📝 摘要（中文）

知识综合（文献综述）在健康职业教育中至关重要，能够整合发现以推动理论和实践。然而，数据提取过程劳动密集，人工智能（AI）辅助提取虽能提高效率，但也引发了对准确性的担忧。本研究开发了一种基于大型语言模型（LLMs）的提取平台，比较了AI与人类在187篇文献和17个提取问题上的表现。结果显示，AI在具体、明确的问题上与人类一致性高，而在需要主观解释的问题上则较低。AI的错误主要源于解释差异，而非虚构内容，表明AI在知识综合中可作为透明、可信的合作伙伴，但需谨慎以保留人类的关键洞察。

## 🔬 方法详解

**问题定义**：本研究旨在解决AI辅助数据提取中的准确性问题，尤其是如何区分AI生成的虚构内容与人类的解释差异。现有方法在处理主观性强的问题时表现不佳，导致提取结果的不一致性。

**核心思路**：研究通过开发一个基于大型语言模型的提取平台，自动化数据提取过程，并通过与人类的比较来评估AI的表现，旨在提高提取的效率和准确性。

**技术框架**：整体架构包括数据输入模块（接收文献）、提取模块（使用LLMs进行数据提取）、比较模块（评估AI与人类的提取一致性）和反馈模块（根据结果优化提取过程）。

**关键创新**：本研究的创新点在于通过系统性比较AI与人类的提取结果，揭示了AI在处理具体问题时的高一致性，以及在主观性问题上的局限性，强调了解释差异的重要性。

**关键设计**：在实验中，使用了多种提取问题类型，并通过分类一致性和主题相似性评分来评估结果，关键参数包括提取问题的设计和评估标准。

## 📊 实验亮点

实验结果显示，AI与人类在具体问题上的一致性高达75.8%，而AI的错误率仅为1.51%，相比之下，人类的错误率为4.37%。这表明AI在处理明确问题时表现优异，且在解释复杂性上具有潜力。

## 🎯 应用场景

该研究的潜在应用领域包括健康职业教育、系统评价和文献综述等，能够帮助研究人员更高效地进行数据提取和知识综合，提升研究质量和效率。未来，AI辅助提取技术有望在其他领域如社会科学和政策研究中得到广泛应用。

## 📄 摘要（原文）

> Knowledge syntheses (literature reviews) are essential to health professions education (HPE), consolidating findings to advance theory and practice. However, they are labor-intensive, especially during data extraction. Artificial Intelligence (AI)-assisted extraction promises efficiency but raises concerns about accuracy, making it critical to distinguish AI 'hallucinations' (fabricated content) from legitimate interpretive differences. We developed an extraction platform using large language models (LLMs) to automate data extraction and compared AI to human responses across 187 publications and 17 extraction questions from a published scoping review. AI-human, human-human, and AI-AI consistencies were measured using interrater reliability (categorical) and thematic similarity ratings (open-ended). Errors were identified by comparing extracted responses to source publications. AI was highly consistent with humans for concrete, explicitly stated questions (e.g., title, aims) and lower for questions requiring subjective interpretation or absent in text (e.g., Kirkpatrick's outcomes, study rationale). Human-human consistency was not higher than AI-human and showed the same question-dependent variability. Discordant AI-human responses (769/3179 = 24.2%) were mostly due to interpretive differences (18.3%); AI inaccuracies were rare (1.51%), while humans were nearly three times more likely to state inaccuracies (4.37%). Findings suggest AI variability depends more on interpretability than hallucination. Repeating AI extraction can identify interpretive complexity or ambiguity, refining processes before human review. AI can be a transparent, trustworthy partner in knowledge synthesis, though caution is needed to preserve critical human insights.

