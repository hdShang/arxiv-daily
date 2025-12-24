---
layout: default
title: "MedBench-IT: A Comprehensive Benchmark for Evaluating Large Language Models on Italian Medical Entrance Examinations"
---

# MedBench-IT: A Comprehensive Benchmark for Evaluating Large Language Models on Italian Medical Entrance Examinations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07135" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07135v1</a>
  <a href="https://arxiv.org/pdf/2509.07135.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07135v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07135v1', 'MedBench-IT: A Comprehensive Benchmark for Evaluating Large Language Models on Italian Medical Entrance Examinations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruggero Marino Lazzaroni, Alessandro Angioi, Michelangelo Puliga, Davide Sanna, Roberto Marras

**分类**: cs.CL

**发布日期**: 2025-09-08

**备注**: Accepted as an oral presentation at CLiC-it 2025

---

## 💡 一句话要点

**MedBench-IT：首个意大利医学入学考试LLM综合评测基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医学入学考试` `意大利语` `评估基准` `自然语言处理`

## 📋 核心要点

1. 现有针对非英语、特定领域的LLM评估基准匮乏，限制了LLM在这些领域的应用和发展。
2. MedBench-IT构建了一个包含17410道意大利医学入学考试题目的综合基准，用于评估LLM在该领域的性能。
3. 实验评估了多种LLM，并分析了可重复性、排序偏差和问题可读性等因素，为后续研究提供参考。

## 📝 摘要（中文）

大型语言模型(LLMs)在教育领域展现出日益增长的潜力，但针对特定领域非英语语言的基准仍然稀缺。我们推出了MedBench-IT，这是首个用于评估LLMs在意大利医学大学入学考试表现的综合基准。MedBench-IT的数据来源于领先的备考材料出版商Edizioni Simone，包含17410道由专家编写的选择题，涵盖六个科目（生物、化学、逻辑、普通文化、数学、物理）和三个难度级别。我们评估了包括专有LLMs（GPT-4o、Claude系列）和资源高效的开源替代方案（<30B参数）在内的各种模型，重点关注实际部署能力。除了准确性之外，我们还进行了严格的可重复性测试（88.86%的响应一致性，因科目而异），排序偏差分析（影响极小）和推理提示评估。我们还检查了问题可读性与模型性能之间的相关性，发现了一种统计上显著但较小的负相关关系。MedBench-IT为意大利NLP社区、EdTech开发者和从业者提供了一个关键资源，为这一关键领域提供了对当前能力和标准化评估方法的见解。

## 🔬 方法详解

**问题定义**：论文旨在解决缺乏针对意大利语医学入学考试的LLM评估基准的问题。现有方法要么是通用基准无法准确反映特定领域的能力，要么是缺乏意大利语的专业数据集，导致无法有效评估LLM在意大利医学领域的应用潜力。

**核心思路**：论文的核心思路是构建一个高质量、大规模的意大利语医学入学考试题库，并基于此题库设计一套全面的评估流程，从而为LLM在该领域的性能提供客观、可靠的评估。通过分析模型在不同科目、不同难度级别上的表现，以及考察模型的可重复性、排序偏差等因素，可以更深入地了解LLM的优势和不足。

**技术框架**：MedBench-IT的整体框架包括以下几个主要步骤：1) 数据收集：从Edizioni Simone获取意大利医学入学考试题目，涵盖六个科目和三个难度级别。2) 数据清洗和整理：对原始数据进行清洗、去重、格式化等处理，确保数据的质量和一致性。3) 模型评估：选择多种LLM进行评估，包括专有模型和开源模型。4) 性能分析：分析模型在不同科目、不同难度级别上的准确率，并进行统计分析。5) 可靠性分析：评估模型的可重复性、排序偏差等因素。

**关键创新**：该论文的关键创新在于构建了首个针对意大利语医学入学考试的LLM评估基准MedBench-IT。该基准不仅提供了大规模、高质量的题库，还设计了一套全面的评估流程，包括性能分析、可靠性分析等。此外，论文还分析了问题可读性与模型性能之间的关系，为后续研究提供了新的视角。

**关键设计**：在模型评估方面，论文采用了标准的准确率作为评估指标。为了评估模型的可重复性，论文对同一问题多次提问，并计算响应的一致性。为了评估排序偏差，论文对选项的顺序进行随机打乱，并观察模型性能的变化。在问题可读性分析方面，论文采用了Flesch Reading Ease公式来计算问题的可读性得分，并分析其与模型性能之间的相关性。

## 📊 实验亮点

MedBench-IT基准包含17410道题目，涵盖六个科目和三个难度级别。实验结果表明，不同LLM在MedBench-IT上的表现存在差异，GPT-4o等专有模型表现优于开源模型。可重复性测试显示，模型的响应一致性为88.86%，排序偏差的影响极小。问题可读性与模型性能之间存在统计上显著但较小的负相关关系。

## 🎯 应用场景

MedBench-IT可应用于评估和改进LLM在意大利医学教育领域的应用，例如智能辅导系统、自动阅卷系统等。该基准还可以促进意大利语NLP技术的发展，并为其他语言的特定领域基准构建提供参考。此外，该研究可以帮助教育机构和学生更好地了解LLM的能力，从而更有效地利用LLM辅助学习。

## 📄 摘要（原文）

> Large language models (LLMs) show increasing potential in education, yet benchmarks for non-English languages in specialized domains remain scarce. We introduce MedBench-IT, the first comprehensive benchmark for evaluating LLMs on Italian medical university entrance examinations. Sourced from Edizioni Simone, a leading preparatory materials publisher, MedBench-IT comprises 17,410 expert-written multiple-choice questions across six subjects (Biology, Chemistry, Logic, General Culture, Mathematics, Physics) and three difficulty levels. We evaluated diverse models including proprietary LLMs (GPT-4o, Claude series) and resource-efficient open-source alternatives (<30B parameters) focusing on practical deployability.
>   Beyond accuracy, we conducted rigorous reproducibility tests (88.86% response consistency, varying by subject), ordering bias analysis (minimal impact), and reasoning prompt evaluation. We also examined correlations between question readability and model performance, finding a statistically significant but small inverse relationship. MedBench-IT provides a crucial resource for Italian NLP community, EdTech developers, and practitioners, offering insights into current capabilities and standardized evaluation methodology for this critical domain.

