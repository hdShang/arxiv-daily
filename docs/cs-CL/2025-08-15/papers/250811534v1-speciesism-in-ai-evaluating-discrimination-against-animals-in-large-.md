---
layout: default
title: "Speciesism in AI: Evaluating Discrimination Against Animals in Large Language Models"
---

# Speciesism in AI: Evaluating Discrimination Against Animals in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11534" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11534v1</a>
  <a href="https://arxiv.org/pdf/2508.11534.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11534v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11534v1', 'Speciesism in AI: Evaluating Discrimination Against Animals in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Monika Jotautaitė, Lucius Caviola, David A. Brewster, Thilo Hagendorff

**分类**: cs.CL, cs.CY

**发布日期**: 2025-08-15

---

## 💡 一句话要点

**评估大型语言模型中的物种歧视问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `物种歧视` `大型语言模型` `伦理AI` `心理测量` `文本生成任务` `AI公平性` `动物权利` `道德判断`

## 📋 核心要点

1. 现有大型语言模型在伦理倾向上缺乏对非人类动物的公平评估，可能导致物种歧视的延续。
2. 论文通过SpeciesismBench基准、心理测量和文本生成任务，系统评估LLMs的物种歧视表现。
3. 实验结果显示，LLMs识别物种歧视言论但未能有效谴责，且在道德选择中偏向于人类而非动物。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的广泛应用，研究其伦理倾向变得至关重要。本文探讨了LLMs是否表现出基于物种的歧视偏见，以及它们如何看待非人类动物。通过三个范式的系统性研究，发现LLMs能够识别物种歧视言论，但很少对此进行谴责，常常将物种歧视态度视为道德上可接受的。此外，LLMs在心理测量中表现出略低于人类的显性物种歧视，但在直接权衡中更倾向于拯救一个人而非多只动物。研究表明，LLMs在某些情况下可能更重视认知能力而非物种本身。最后，研究呼吁将非人类道德患者纳入AI公平性和对齐框架，以减少这些偏见。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在物种歧视方面的偏见问题。现有方法未能充分评估LLMs对非人类动物的道德态度，可能导致对动物的歧视性看法持续存在。

**核心思路**：研究通过建立SpeciesismBench基准，结合心理测量和文本生成任务，全面评估LLMs在物种歧视方面的表现，旨在揭示其伦理倾向与人类的差异。

**技术框架**：研究分为三个主要模块：首先是SpeciesismBench基准，包含1003个项目用于评估物种歧视言论；其次是心理测量，通过与人类参与者的比较分析LLMs的反应；最后是文本生成任务，探讨LLMs对物种歧视合理化的反应。

**关键创新**：研究的创新点在于系统性地将物种歧视纳入AI公平性研究框架，揭示LLMs在道德判断中的偏见与人类的不同，强调了认知能力在道德选择中的重要性。

**关键设计**：在实验设计中，使用了多种心理测量工具和文本生成策略，确保LLMs的反应能够真实反映其对物种歧视的态度，同时对比了人类参与者的反应，以揭示潜在的偏见。

## 📊 实验亮点

实验结果表明，LLMs能够识别物种歧视言论，但在道德上未能有效谴责，且在选择中更倾向于拯救人类而非动物。具体而言，LLMs在直接权衡中选择拯救一个人而非多只动物的频率高于人类，显示出其在道德判断中的偏见。

## 🎯 应用场景

该研究的潜在应用领域包括AI伦理、动物权利保护和社会政策制定。通过识别和减少LLMs中的物种歧视偏见，可以推动更公平的AI系统设计，促进人类与非人类动物的和谐共处，影响未来的社会文化和法律框架。

## 📄 摘要（原文）

> As large language models (LLMs) become more widely deployed, it is crucial to examine their ethical tendencies. Building on research on fairness and discrimination in AI, we investigate whether LLMs exhibit speciesist bias -- discrimination based on species membership -- and how they value non-human animals. We systematically examine this issue across three paradigms: (1) SpeciesismBench, a 1,003-item benchmark assessing recognition and moral evaluation of speciesist statements; (2) established psychological measures comparing model responses with those of human participants; (3) text-generation tasks probing elaboration on, or resistance to, speciesist rationalizations. In our benchmark, LLMs reliably detected speciesist statements but rarely condemned them, often treating speciesist attitudes as morally acceptable. On psychological measures, results were mixed: LLMs expressed slightly lower explicit speciesism than people, yet in direct trade-offs they more often chose to save one human over multiple animals. A tentative interpretation is that LLMs may weight cognitive capacity rather than species per se: when capacities were equal, they showed no species preference, and when an animal was described as more capable, they tended to prioritize it over a less capable human. In open-ended text generation tasks, LLMs frequently normalized or rationalized harm toward farmed animals while refusing to do so for non-farmed animals. These findings suggest that while LLMs reflect a mixture of progressive and mainstream human views, they nonetheless reproduce entrenched cultural norms around animal exploitation. We argue that expanding AI fairness and alignment frameworks to explicitly include non-human moral patients is essential for reducing these biases and preventing the entrenchment of speciesist attitudes in AI systems and the societies they influence.

