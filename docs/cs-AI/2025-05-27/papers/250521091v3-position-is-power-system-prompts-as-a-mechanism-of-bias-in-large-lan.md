---
layout: default
title: "Position is Power: System Prompts as a Mechanism of Bias in Large Language Models (LLMs)"
---

# Position is Power: System Prompts as a Mechanism of Bias in Large Language Models (LLMs)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21091" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21091v3</a>
  <a href="https://arxiv.org/pdf/2505.21091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21091v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21091v3', 'Position is Power: System Prompts as a Mechanism of Bias in Large Language Models (LLMs)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anna Neumann, Elisabeth Kirsten, Muhammad Bilal Zafar, Jatinder Singh

**分类**: cs.CY, cs.AI, cs.CL

**发布日期**: 2025-05-27 (更新: 2025-06-23)

**备注**: Published in Proceedings of ACM FAccT 2025 Update Comment: Fixed the error where user vs. system and implicit vs. explicit labels in the heatmaps were switched. The takeaways remain the same

**DOI**: [10.1145/3715275.3732038](https://doi.org/10.1145/3715275.3732038)

---

## 💡 一句话要点

**探讨系统提示对大型语言模型偏见的影响及其透明性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `系统提示` `偏见分析` `透明性` `AI审计` `人口统计信息` `模型公平性`

## 📋 核心要点

1. 现有的LLMs在使用系统提示时缺乏透明性，导致潜在的偏见和不平等的表现。
2. 论文提出通过比较系统提示与用户提示中人口统计信息的处理方式，来揭示模型行为的偏见。
3. 实验结果显示，六种LLMs在处理不同人口统计组时存在显著差异，影响了用户的代表性和决策过程。

## 📝 摘要（中文）

本文研究了大型语言模型（LLMs）中的系统提示如何影响模型行为，尤其是其在处理用户输入时的优先级。随着系统提示的复杂性增加，可能会引入未被考虑的副作用，导致用户无法检测或纠正的偏见。通过比较六种商业LLMs在处理人口统计信息时的表现，发现了显著的偏见，影响了用户代表性和决策场景。研究强调了系统提示分析在AI审计过程中的重要性，尤其是在可定制系统提示日益普及的背景下。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中系统提示的透明性不足及其引发的偏见问题。现有方法未能有效识别和纠正系统提示对模型输出的影响，导致潜在的代表性和分配偏见。

**核心思路**：研究通过比较系统提示与用户提示在处理人口统计信息时的差异，揭示信息位置对模型行为的影响。这种设计旨在提高对系统提示的理解，进而促进模型的公平性。

**技术框架**：研究采用了对比分析的方法，选取六种商业LLMs，并对50个不同的人口统计组进行测试。主要模块包括数据收集、模型输出分析和偏见评估。

**关键创新**：本文的创新点在于系统性地分析了系统提示的层次结构对模型输出的影响，揭示了其在不同上下文中的偏见表现。这与传统的用户输入分析方法有本质区别。

**关键设计**：研究中使用了标准化的测试集和评估指标，以确保结果的可重复性和可靠性。模型的输出被系统地分类和比较，以识别潜在的偏见和不平等表现。

## 📊 实验亮点

实验结果表明，在处理人口统计信息时，六种LLMs之间存在显著的偏见，具体表现为在用户代表性和决策场景中的差异。这些偏见的存在可能导致不平等的结果，强调了系统提示分析在AI模型开发中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括AI审计、模型开发和政策制定等。通过提高对系统提示的透明性，能够帮助开发者和用户更好地理解和控制模型行为，从而减少偏见和不平等现象的发生。未来，随着AI技术的普及，这一研究将对促进公平和透明的AI系统具有重要价值。

## 📄 摘要（原文）

> System prompts in Large Language Models (LLMs) are predefined directives that guide model behaviour, taking precedence over user inputs in text processing and generation. LLM deployers increasingly use them to ensure consistent responses across contexts. While model providers set a foundation of system prompts, deployers and third-party developers can append additional prompts without visibility into others' additions, while this layered implementation remains entirely hidden from end-users. As system prompts become more complex, they can directly or indirectly introduce unaccounted for side effects. This lack of transparency raises fundamental questions about how the position of information in different directives shapes model outputs. As such, this work examines how the placement of information affects model behaviour. To this end, we compare how models process demographic information in system versus user prompts across six commercially available LLMs and 50 demographic groups. Our analysis reveals significant biases, manifesting in differences in user representation and decision-making scenarios. Since these variations stem from inaccessible and opaque system-level configurations, they risk representational, allocative and potential other biases and downstream harms beyond the user's ability to detect or correct. Our findings draw attention to these critical issues, which have the potential to perpetuate harms if left unexamined. Further, we argue that system prompt analysis must be incorporated into AI auditing processes, particularly as customisable system prompts become increasingly prevalent in commercial AI deployments.

