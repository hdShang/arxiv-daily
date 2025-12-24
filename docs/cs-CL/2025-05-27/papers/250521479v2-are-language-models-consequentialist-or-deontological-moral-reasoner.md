---
layout: default
title: Are Language Models Consequentialist or Deontological Moral Reasoners?
---

# Are Language Models Consequentialist or Deontological Moral Reasoners?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21479" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21479v2</a>
  <a href="https://arxiv.org/pdf/2505.21479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21479v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21479v2', 'Are Language Models Consequentialist or Deontological Moral Reasoners?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keenan Samway, Max Kleiman-Weiner, David Guzman Piedrahita, Rada Mihalcea, Bernhard Schölkopf, Zhijing Jin

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-10-12)

**备注**: EMNLP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/keenansamway/moral-lens)

---

## 💡 一句话要点

**提出道德推理分类框架以分析语言模型的伦理决策**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `道德推理` `大型语言模型` `伦理决策` `结果主义` `义务论` `电车难题` `人工智能伦理` `推理分析`

## 📋 核心要点

1. 现有研究主要集中在大型语言模型的道德判断，而缺乏对其道德推理过程的深入分析。
2. 本文提出了一种道德理性分类框架，利用600多个电车难题系统性分析LLMs的推理模式。
3. 研究结果表明，LLMs的推理链更倾向于义务论，而事后解释则转向结果主义，揭示了其伦理决策的复杂性。

## 📝 摘要（中文）

随着人工智能系统在医疗、法律和治理等领域的应用日益增多，理解它们如何处理伦理复杂场景变得至关重要。以往的研究主要关注大型语言模型（LLMs）的道德判断，而非其道德推理过程。本文通过对600多个不同的电车难题进行大规模分析，提出了一种道德理性分类法，系统地根据结果主义和义务论两种主要规范伦理理论对推理轨迹进行分类。研究发现，LLMs的推理链倾向于支持基于道德义务的义务论原则，而事后解释则显著转向强调效用的结果主义理性。该框架为理解LLMs如何处理和表达伦理考量提供了基础，推动了在高风险决策环境中安全和可解释的LLMs部署。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在伦理复杂场景中的道德推理过程缺乏系统分析的问题。现有方法主要关注道德判断，未能深入探讨推理机制。

**核心思路**：通过引入道德理性分类法，利用大量电车难题作为探针，系统性地分析不同LLMs的推理轨迹，揭示其道德推理的模式和倾向。

**技术框架**：研究分为几个主要模块，包括道德理性分类法的构建、数据集的准备（600多个电车难题）、LLMs的推理分析以及结果的比较与解释。

**关键创新**：本研究的创新点在于首次系统性地分类和分析LLMs的道德推理轨迹，揭示了其在义务论和结果主义之间的推理倾向，填补了现有研究的空白。

**关键设计**：在实验中，采用了特定的道德理性分类标准，并对LLMs的推理链进行了详细的编码和分析，以确保结果的准确性和可解释性。

## 📊 实验亮点

实验结果显示，LLMs在道德推理中更倾向于义务论原则，而在事后解释中则显著转向结果主义。这一发现揭示了LLMs在伦理决策中的复杂性，为理解其推理过程提供了新的视角。具体而言，研究表明LLMs的推理链与传统伦理理论之间存在显著的关联性，推动了对其伦理行为的深入理解。

## 🎯 应用场景

该研究的潜在应用领域包括医疗决策支持、法律判决辅助和政策制定等高风险场景。通过理解LLMs的道德推理过程，可以提高其在复杂伦理情境下的决策透明度和安全性，从而推动更负责任的人工智能应用。未来，该框架还可能为其他类型的AI系统提供伦理决策分析的参考。

## 📄 摘要（原文）

> As AI systems increasingly navigate applications in healthcare, law, and governance, understanding how they handle ethically complex scenarios becomes critical. Previous work has mainly examined the moral judgments in large language models (LLMs), rather than their underlying moral reasoning process. In contrast, we focus on a large-scale analysis of the moral reasoning traces provided by LLMs. Furthermore, unlike prior work that attempted to draw inferences from only a handful of moral dilemmas, our study leverages over 600 distinct trolley problems as probes for revealing the reasoning patterns that emerge within different LLMs. We introduce and test a taxonomy of moral rationales to systematically classify reasoning traces according to two main normative ethical theories: consequentialism and deontology. Our analysis reveals that LLM chains-of-thought tend to favor deontological principles based on moral obligations, while post-hoc explanations shift notably toward consequentialist rationales that emphasize utility. Our framework provides a foundation for understanding how LLMs process and articulate ethical considerations, an important step toward safe and interpretable deployment of LLMs in high-stakes decision-making environments. Our code is available at https://github.com/keenansamway/moral-lens .

