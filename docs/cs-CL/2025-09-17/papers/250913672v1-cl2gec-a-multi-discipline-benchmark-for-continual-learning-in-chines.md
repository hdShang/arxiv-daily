---
layout: default
title: "CL$^2$GEC: A Multi-Discipline Benchmark for Continual Learning in Chinese Literature Grammatical Error Correction"
---

# CL$^2$GEC: A Multi-Discipline Benchmark for Continual Learning in Chinese Literature Grammatical Error Correction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13672" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13672v1</a>
  <a href="https://arxiv.org/pdf/2509.13672.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13672v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13672v1', 'CL$^2$GEC: A Multi-Discipline Benchmark for Continual Learning in Chinese Literature Grammatical Error Correction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shang Qin, Jingheng Ye, Yinghui Li, Hai-Tao Zheng, Qi Li, Jinxiao Shan, Zhixing Li, Hong-Gee Kim

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出CL$^2$GEC基准，用于评估中文语法纠错系统在多领域持续学习中的性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `中文语法纠错` `持续学习` `多学科基准` `灾难性遗忘` `自然语言处理`

## 📋 核心要点

1. 现有CGEC研究缺乏多学科写作的专用基准，无法有效评估模型在不同领域间的适应能力。
2. 论文提出CL$^2$GEC基准，模拟真实编辑场景，评估模型在持续学习环境下的语法纠错能力。
3. 实验表明，基于正则化的持续学习方法在减轻灾难性遗忘方面优于其他方法。

## 📝 摘要（中文）

针对不同学术领域自动写作辅助的需求日益增长，这需要鲁棒的中文语法纠错(CGEC)系统能够跨学科适应。然而，现有的CGEC研究在很大程度上缺乏针对多学科写作的专用基准，忽略了持续学习(CL)作为处理领域特定语言变异和防止灾难性遗忘的有希望的解决方案。为了填补这一关键空白，我们推出了CL$^2$GEC，这是第一个中文文献语法纠错的持续学习基准，旨在评估跨多个学术领域的自适应CGEC。我们的基准包括10,000个由人工标注的句子，涵盖10个学科，每个学科都表现出独特的语言风格和错误模式。CL$^2$GEC侧重于在持续学习环境中评估语法纠错，模拟顺序接触不同的学术领域，以反映真实的编辑动态。我们评估了大型语言模型在顺序微调、参数高效适应和四种代表性CL算法下的性能，使用标准GEC指标和适应于任务级别变化的持续学习指标。实验结果表明，基于正则化的方法比基于重放或朴素顺序方法更有效地减轻遗忘。我们的基准为未来在不同学术领域进行自适应语法纠错的研究提供了坚实的基础。

## 🔬 方法详解

**问题定义**：论文旨在解决中文语法纠错(CGEC)系统在多学科领域应用时，由于领域差异导致的性能下降问题。现有CGEC研究缺乏针对多学科的持续学习基准，使得模型难以适应不同领域的语言风格和错误模式，容易发生灾难性遗忘。

**核心思路**：论文的核心思路是构建一个多学科的CGEC持续学习基准CL$^2$GEC，通过模拟模型在不同学科领域数据上的顺序学习过程，来评估模型在持续学习环境下的语法纠错能力。这样可以更真实地反映实际应用场景，并促进相关算法的研究。

**技术框架**：CL$^2$GEC基准包含10个学科的10,000个人工标注句子，每个学科都具有独特的语言风格和错误模式。论文使用该基准评估了大型语言模型在顺序微调、参数高效适应以及四种代表性持续学习算法下的性能。评估指标包括标准的GEC指标以及针对任务级别变化的持续学习指标。

**关键创新**：该论文的关键创新在于构建了首个中文文献语法纠错的持续学习基准CL$^2$GEC。该基准的特点是多学科性，能够更真实地模拟实际应用场景，并为持续学习算法在CGEC任务上的研究提供了平台。与现有CGEC数据集相比，CL$^2$GEC更关注模型在不同领域间的适应能力和避免灾难性遗忘的能力。

**关键设计**：CL$^2$GEC基准的数据集构建过程中，需要保证每个学科的数据量和质量，并确保不同学科之间具有一定的差异性。在实验评估中，论文采用了多种持续学习算法，包括基于正则化、基于重放和朴素顺序方法，并使用了标准的GEC指标和针对任务级别变化的持续学习指标来全面评估模型的性能。

## 📊 实验亮点

实验结果表明，在CL$^2$GEC基准上，基于正则化的持续学习方法在减轻灾难性遗忘方面表现更佳，优于基于重放或朴素顺序方法。这表明正则化方法更适合处理多学科CGEC任务，为未来的研究提供了方向。

## 🎯 应用场景

该研究成果可应用于智能写作辅助、在线教育、学术论文润色等领域。通过持续学习，CGEC系统能够适应不同学科的语言风格，提高语法纠错的准确性和效率，帮助用户撰写高质量的学术论文和文档，具有重要的实际应用价值和学术意义。

## 📄 摘要（原文）

> The growing demand for automated writing assistance in diverse academic domains highlights the need for robust Chinese Grammatical Error Correction (CGEC) systems that can adapt across disciplines. However, existing CGEC research largely lacks dedicated benchmarks for multi-disciplinary academic writing, overlooking continual learning (CL) as a promising solution to handle domain-specific linguistic variation and prevent catastrophic forgetting. To fill this crucial gap, we introduce CL$^2$GEC, the first Continual Learning benchmark for Chinese Literature Grammatical Error Correction, designed to evaluate adaptive CGEC across multiple academic fields. Our benchmark includes 10,000 human-annotated sentences spanning 10 disciplines, each exhibiting distinct linguistic styles and error patterns. CL$^2$GEC focuses on evaluating grammatical error correction in a continual learning setting, simulating sequential exposure to diverse academic disciplines to reflect real-world editorial dynamics. We evaluate large language models under sequential tuning, parameter-efficient adaptation, and four representative CL algorithms, using both standard GEC metrics and continual learning metrics adapted to task-level variation. Experimental results reveal that regularization-based methods mitigate forgetting more effectively than replay-based or naive sequential approaches. Our benchmark provides a rigorous foundation for future research in adaptive grammatical error correction across diverse academic domains.

