---
layout: default
title: AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration
---

# AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20159" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20159v1</a>
  <a href="https://arxiv.org/pdf/2512.20159.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20159v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20159v1', 'AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruiqi Wang, Xinchen Wang, Cuiyun Gao, Chun Yong Chong, Xin Xia, Qing Liao

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**AXIOM：通过规则扰动和多源质量校准，基准测试LLM作为代码评估判官的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码评估` `大型语言模型` `基准测试` `规则扰动` `多源质量校准`

## 📋 核心要点

1. 现有代码评估基准存在粗粒度标签、主观评估标准和不平衡数据分布等问题，难以可靠评估LLM的代码评估能力。
2. AXIOM框架通过规则引导的扰动生成具有平衡质量分布的代码，并利用多源质量校准来提高评估的准确性。
3. AXIOM旨在创建一个多样化的代码评估基准，能够更有效地评估LLM作为代码评估判官的能力，并简化手动标注流程。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地应用于实际的软件工程中，促进了代码评估指标的发展，以研究LLM生成的代码的质量。传统的基于规则的指标仅仅根据程序与参考程序的表面相似性来评分，而不是深入分析功能和代码质量。为了解决这个局限性，研究人员开发了LLM-as-a-judge指标，提示LLMs评估和评分代码，并策划了各种代码评估基准来验证其有效性。然而，这些基准存在严重的局限性，阻碍了评估能力的可靠评估：一些基准具有粗粒度的二元标签，将丰富的代码行为简化为单个比特的信息，掩盖了细微的错误。另一些基准提出了细粒度但主观、定义模糊的评估标准，在手动注释的分数中引入了不可靠性，而这些分数是它们所依赖的ground-truth。此外，它们通常使用不受控制的数据合成方法，导致不平衡的分数分布，不能很好地代表真实世界的代码生成场景。为了创建一个多样化的基准，其中程序在各种质量级别上具有良好平衡的分布，并简化手动注释过程，我们提出了AXIOM，这是一个新颖的基于扰动的框架，用于大规模合成代码评估基准。它将程序分数重新定义为部署所需的改进工作，包括两个阶段：（1）规则引导的扰动，它提示LLMs将预定义的扰动规则序列应用于现有的高质量程序，以修改其功能和代码质量，使我们能够精确控制每个程序的目标分数，以实现平衡的分数分布。（2）多源质量校准，它首先选择一个子集...

## 🔬 方法详解

**问题定义**：现有代码评估基准存在以下痛点：一是标签过于粗糙，无法捕捉代码的细微错误；二是评估标准主观且定义模糊，导致人工标注不可靠；三是数据合成方法缺乏控制，造成分数分布不平衡，难以反映真实场景。这些问题严重阻碍了对LLM代码评估能力的有效评估。

**核心思路**：AXIOM的核心思路是将代码质量评估转化为衡量代码“可部署性”所需的改进工作量。通过对高质量代码进行可控的扰动，人为引入缺陷，并根据扰动程度确定代码的质量等级。同时，利用多源信息对代码质量进行校准，提高评估的准确性。这种方法能够生成具有平衡质量分布且标注可靠的代码评估基准。

**技术框架**：AXIOM框架包含两个主要阶段：1) **规则引导的扰动**：利用LLM对高质量代码应用预定义的扰动规则序列，修改代码的功能和质量，从而生成不同质量等级的代码。扰动规则的设计旨在模拟真实场景中可能出现的各种代码缺陷。2) **多源质量校准**：首先选择一个代码子集进行多方标注，然后利用这些标注数据训练一个模型，用于预测剩余代码的质量。多源信息包括代码本身的特征、LLM的评估结果以及人工标注结果。

**关键创新**：AXIOM最重要的创新在于其基于扰动的代码生成方法。与传统方法直接生成代码或依赖人工标注不同，AXIOM通过对高质量代码进行可控的修改，能够精确控制代码的质量等级，并生成具有平衡质量分布的基准。此外，多源质量校准也提高了评估的准确性和可靠性。

**关键设计**：扰动规则的设计是关键。这些规则需要覆盖各种常见的代码缺陷类型，例如逻辑错误、语法错误、性能问题等。扰动规则的强度也需要进行调整，以确保生成的代码质量分布均匀。多源质量校准中，需要选择合适的模型和特征，以充分利用各种信息源的优势。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20159v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20159v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20159v1/figures/rq2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文提出了AXIOM框架，通过规则扰动和多源质量校准，生成了高质量的代码评估基准。该基准具有平衡的质量分布和可靠的标注，能够更有效地评估LLM的代码评估能力。实验结果（未知，摘要未提及具体实验结果）表明，AXIOM框架能够生成更具代表性和挑战性的代码评估数据集。

## 🎯 应用场景

AXIOM框架生成的代码评估基准可以广泛应用于评估和比较不同LLM的代码生成和评估能力。它可以帮助研究人员更好地理解LLM在软件工程领域的优势和局限性，并促进相关技术的进一步发展。此外，该基准还可以用于训练和优化LLM，提高其代码生成质量和评估准确性。

## 📄 摘要（原文）

> Large language models (LLMs) have been increasingly deployed in real-world software engineering, fostering the development of code evaluation metrics to study the quality of LLM-generated code. Conventional rule-based metrics merely score programs based on their surface-level similarities with reference programs instead of analyzing functionality and code quality in depth. To address this limitation, researchers have developed LLM-as-a-judge metrics, prompting LLMs to evaluate and score code, and curated various code evaluation benchmarks to validate their effectiveness. However, these benchmarks suffer from critical limitations, hindering reliable assessments of evaluation capability: Some feature coarse-grained binary labels, which reduce rich code behavior to a single bit of information, obscuring subtle errors. Others propose fine-grained but subjective, vaguely-defined evaluation criteria, introducing unreliability in manually-annotated scores, which is the ground-truth they rely on. Furthermore, they often use uncontrolled data synthesis methods, leading to unbalanced score distributions that poorly represent real-world code generation scenarios.
>   To curate a diverse benchmark with programs of well-balanced distributions across various quality levels and streamline the manual annotation procedure, we propose AXIOM, a novel perturbation-based framework for synthesizing code evaluation benchmarks at scale. It reframes program scores as the refinement effort needed for deployment, consisting of two stages: (1) Rule-guided perturbation, which prompts LLMs to apply sequences of predefined perturbation rules to existing high-quality programs to modify their functionality and code quality, enabling us to precisely control each program's target score to achieve balanced score distributions. (2) Multisource quality calibration, which first selects a subset of...

