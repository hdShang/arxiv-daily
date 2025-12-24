---
layout: default
title: "Large Language Models Don't Make Sense of Word Problems. A Scoping Review from a Mathematics Education Perspective"
---

# Large Language Models Don't Make Sense of Word Problems. A Scoping Review from a Mathematics Education Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24006" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24006v2</a>
  <a href="https://arxiv.org/pdf/2506.24006.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24006v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24006v2', 'Large Language Models Don\'t Make Sense of Word Problems. A Scoping Review from a Mathematics Education Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anselm R. Strohmaier, Wim Van Dooren, Kathrin Seßler, Brian Greer, Lieven Verschaffel

**分类**: cs.CL, math.HO

**发布日期**: 2025-06-30 (更新: 2025-08-09)

**备注**: v2: added analyses for GPT-5, also leading to small adjustments in the text, no major new interpretations

---

## 💡 一句话要点

**探讨大型语言模型在数学问题解决中的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数学教育` `文字问题` `教育技术` `实证评估` `理解能力` `教学工具`

## 📋 核心要点

1. 现有大型语言模型在理解数学文字问题的真实背景方面存在显著不足，影响其在教育中的应用。
2. 论文通过技术概述、文献综述和实证评估，系统分析LLMs在数学问题解决中的能力与局限。
3. 实证评估显示，最新的LLMs在处理简单问题时准确率接近完美，但在复杂问题上表现不佳，反映出其理解能力的缺陷。

## 📝 摘要（中文）

大型语言模型（LLMs）如ChatGPT的进展引发了如何将其整合到教育中的讨论。研究表明，尽管LLMs在处理文本输入方面表现出色，但它们在理解真实世界背景及其在课堂中的应用仍存在不确定性。本文通过技术概述、文献综述和实证评估三部分，分析了LLMs在数学文字问题中的表现，发现它们在处理不需要真实背景的简单问题时准确率接近完美，但在面对复杂的现实问题时表现出明显的不足。总体而言，LLMs掌握了表面解决过程，但未能真正理解数学问题，这可能限制了它们作为教学工具的价值。

## 🔬 方法详解

**问题定义**：本文旨在探讨大型语言模型在解决数学文字问题时的真实能力及其局限性。现有方法在处理需要真实世界背景的复杂问题时表现不佳，无法有效支持数学教育。

**核心思路**：通过对LLMs与学生在解决数学问题时的思维过程进行对比，揭示LLMs在理解问题背景方面的不足，从而为教育应用提供参考。

**技术框架**：研究分为三个主要部分：技术概述、文献综述和实证评估。技术概述对比了LLMs与学生在解决问题时的思维过程，文献综述分析了213项研究中的文字问题，实证评估则测试了多种LLMs在287个问题上的表现。

**关键创新**：论文的创新在于系统性地将LLMs的能力与数学教育中的实际需求进行对比，揭示了LLMs在处理复杂问题时的理解缺陷，这一视角在现有研究中较为少见。

**关键设计**：在实证评估中，使用了287个数学文字问题，涵盖了不同类型的问题，特别关注了那些需要真实背景理解的问题，以评估LLMs的实际表现。

## 📊 实验亮点

实证评估结果显示，最新的LLMs在处理简单的数学文字问题时准确率接近完美，特别是在20个PISA问题上获得满分。然而，在面对需要真实世界背景理解的复杂问题时，它们的表现明显不足，揭示了其在教育应用中的局限性。

## 🎯 应用场景

该研究为教育工作者和研究人员提供了关于大型语言模型在数学教育中应用的深刻见解，尤其是在如何有效利用这些工具来支持学生学习方面。未来，研究结果可能推动教育技术的改进，使其更好地适应学生的学习需求。

## 📄 摘要（原文）

> The progress of Large Language Models (LLMs) like ChatGPT raises the question of how they can be integrated into education. One hope is that they can support mathematics learning, including word-problem solving. Since LLMs can handle textual input with ease, they appear well-suited for solving mathematical word problems. Yet their real competence, whether they can make sense of the real-world context, and the implications for classrooms remain unclear. We conducted a scoping review from a mathematics-education perspective, including three parts: a technical overview, a systematic review of word problems used in research, and a state-of-the-art empirical evaluation of LLMs on mathematical word problems. First, in the technical overview, we contrast the conceptualization of word problems and their solution processes between LLMs and students. In computer-science research this is typically labeled mathematical reasoning, a term that does not align with usage in mathematics education. Second, our literature review of 213 studies shows that the most popular word-problem corpora are dominated by s-problems, which do not require a consideration of realities of their real-world context. Finally, our evaluation of GPT-3.5-turbo, GPT-4o-mini, GPT-4.1, o3, and GPT-5 on 287 word problems shows that most recent LLMs solve these s-problems with near-perfect accuracy, including a perfect score on 20 problems from PISA. LLMs still showed weaknesses in tackling problems where the real-world context is problematic or non-sensical. In sum, we argue based on all three aspects that LLMs have mastered a superficial solution process but do not make sense of word problems, which potentially limits their value as instructional tools in mathematics classrooms.

