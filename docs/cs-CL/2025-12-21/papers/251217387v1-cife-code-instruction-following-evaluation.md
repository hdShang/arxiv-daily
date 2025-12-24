---
layout: default
title: "CIFE: Code Instruction-Following Evaluation"
---

# CIFE: Code Instruction-Following Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17387" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17387v1</a>
  <a href="https://arxiv.org/pdf/2512.17387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17387v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17387v1', 'CIFE: Code Instruction-Following Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sravani Gunnu, Shanmukha Guttula, Hima Patel

**分类**: cs.SE, cs.CL

**发布日期**: 2025-12-19

**备注**: 20 pages, 22 figures, 2 tables

---

## 💡 一句话要点

**CIFE：提出代码指令遵循评估基准，衡量LLM在代码生成中对开发者约束的遵守程度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `大型语言模型` `指令遵循` `评估基准` `开发者约束`

## 📋 核心要点

1. 现有代码生成评估主要关注功能正确性，忽略了开发者对代码鲁棒性、格式和安全性的明确约束。
2. CIFE基准通过人工-LLM协作，构建了包含丰富开发者约束的Python代码生成任务集。
3. 实验表明，现有模型在部分约束遵守方面表现较好，但在严格遵守所有约束方面仍有较大提升空间。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地应用于实际的代码生成，但仅凭功能正确性不足以保证可靠部署。开发者还期望模型能够遵守明确的需求，例如鲁棒性、格式和安全性。本文提出了一个包含1000个Python任务的基准测试，每个任务都配有平均7个开发者指定的约束，涵盖13个类别。这些约束通过四阶段的人工-LLM流水线进行筛选，以确保其原子性、相关性和客观性。我们使用互补的遵守度指标评估了14个开源和闭源模型，并提出了C2A评分，这是一个综合指标，共同衡量正确性和约束合规性。结果表明，部分满足和严格满足之间存在巨大差距，虽然强大的模型实现了超过90%的部分遵守度，但严格遵守度仍然在39-66%之间。这些发现强调，可信的代码生成不仅需要正确性，还需要始终如一地遵守开发者意图。

## 🔬 方法详解

**问题定义**：现有代码生成评估方法主要通过测试用例执行来评估代码的功能正确性，忽略了开发者在实际应用中对代码风格、安全性、鲁棒性等方面的约束。这些约束往往以自然语言的形式存在，如何评估模型对这些约束的遵循程度是一个挑战。

**核心思路**：本文的核心思路是构建一个包含丰富开发者约束的代码生成评估基准，并设计相应的评估指标来衡量模型对这些约束的遵守程度。通过这个基准，可以更全面地评估代码生成模型的性能，并促进模型在实际应用中的可靠性。

**技术框架**：CIFE基准的构建包含以下几个主要阶段：1) 收集Python代码生成任务；2) 通过人工和LLM协作，为每个任务生成多个开发者约束；3) 对约束进行筛选和验证，确保其原子性、相关性和客观性；4) 设计评估指标，包括部分遵守度和严格遵守度，以及综合指标C2A Score。

**关键创新**：CIFE基准的关键创新在于其对开发者约束的显式建模和评估。与传统的只关注功能正确性的评估方法不同，CIFE基准更关注模型对开发者意图的理解和执行能力。此外，CIFE基准的约束生成过程采用了人工-LLM协作的方式，保证了约束的多样性和质量。

**关键设计**：CIFE基准的约束涵盖13个类别，包括输入验证、错误处理、代码风格、安全性等方面。C2A Score是一个综合指标，它结合了代码的正确性和约束遵守度，可以更全面地评估代码生成模型的性能。C2A Score的计算公式为：C2A Score = Correctness * Strict Adherence，其中Correctness表示代码的功能正确性，Strict Adherence表示代码对所有约束的严格遵守度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17387v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17387v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17387v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有代码生成模型在CIFE基准上的表现参差不齐。虽然一些强大的模型可以实现超过90%的部分约束遵守度，但严格遵守度仍然较低，在39-66%之间。这表明现有模型在理解和执行开发者意图方面仍有提升空间。C2A Score的引入可以更全面地评估代码生成模型的性能，并为模型改进提供指导。

## 🎯 应用场景

CIFE基准可以应用于代码生成模型的评估和改进，帮助开发者选择更可靠的代码生成工具。此外，CIFE基准还可以用于研究如何更好地将自然语言约束融入到代码生成过程中，提高代码生成模型的智能化水平。该研究的成果有助于提高软件开发的效率和质量，降低软件维护成本。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly applied to real-world code generation, where functional correctness alone is insufficient for reliable deployment, developers also expect adherence to explicit requirements for robustness, formatting, and security. Existing benchmarks primarily assess correctness through test-case execution, offering limited insight into how reliably models follow such constraints. We introduce a benchmark of 1,000 Python tasks, each paired with an average of 7 developer-specified constraints spanning 13 categories. Constraints are curated through a four-stage human-LLM pipeline to ensure they are atomic, relevant, and objective. We evaluate 14 open- and closed-source models using complementary adherence metrics and propose the C2A Score, a composite measure that jointly captures correctness and constraint compliance. Results reveal a substantial gap between partial and strict satisfaction, while strong models achieve over 90% partial adherence, strict adherence remains between 39-66%. These findings highlight that trustworthy code generation requires not only correctness but also consistent adherence to developer intent.

