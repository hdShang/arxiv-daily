---
layout: default
title: "Large language models management of medications: three performance analyses"
---

# Large language models management of medications: three performance analyses

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22926" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22926v2</a>
  <a href="https://arxiv.org/pdf/2509.22926.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22926v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22926v2', 'Large language models management of medications: three performance analyses')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kelli Henry, Steven Xu, Kaitlin Blotske, Moriah Cargile, Erin F. Barreto, Brian Murray, Susan Smith, Seth R. Bauer, Xingmeng Zhao, Adeleine Tilley, Yanjun Gao, Tianming Liu, Sunghwan Sohn, Andrea Sikora

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26 (更新: 2025-10-14)

---

## 💡 一句话要点

**评估大型语言模型在药物管理任务中的性能表现，揭示其局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `药物管理` `药物配方匹配` `药物相互作用` `药物医嘱生成`

## 📋 核心要点

1. 现有大型语言模型在药物管理方面缺乏充分评估，无法保证其推荐药物方案的准确性和安全性。
2. 本研究通过三个药物管理任务评估GPT-4o的性能，包括药物配方匹配、药物相互作用识别和药物医嘱生成。
3. 实验结果表明GPT-4o在药物管理任务中表现不佳，需要领域特定训练和更全面的评估框架。

## 📝 摘要（中文）

本研究旨在评估大型语言模型（LLMs）在药物管理任务中的一致性，特别是针对特定诊断推荐合适药物方案的能力。药物管理是一项复杂的任务，需要综合药物配方和完整的医嘱信息以确保安全使用。研究测试了GPT-4o（ChatGPT中的LLM）在三个药物管理任务中的表现：识别给定通用药物名称的可用配方、识别给定药物方案的药物-药物相互作用（DDI）以及为给定通用药物名称准备药物医嘱。结果表明，在药物配方匹配任务中，GPT-4o的准确率为49%，平均每种药物遗漏1.23种配方，产生1.14个幻觉。在药物-药物相互作用识别任务中，准确率为54.7%。在药物医嘱生成任务中，GPT-4o在65.8%的情况下生成了不包含药物或缩写错误的医嘱语句。结论是，模型在基本药物任务中的表现始终较差，强调需要通过临床医生标注的数据集进行领域特定训练，并建立全面的评估框架来衡量性能。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型在药物管理任务中的性能，特别是其在药物配方匹配、药物相互作用识别和药物医嘱生成方面的能力。现有方法，即直接使用通用LLM，在这些任务中表现出不足，无法保证药物推荐的准确性和安全性，可能导致医疗风险。

**核心思路**：论文的核心思路是通过设计三个具体的药物管理任务，直接测试LLM（GPT-4o）在这些任务中的表现，并使用临床医生评估和标准LLM指标（TF-IDF, Levenshtein similarity, ROUGE）进行综合评估。通过量化LLM在这些任务中的准确率、遗漏和幻觉等指标，揭示其在药物管理方面的局限性。

**技术框架**：研究的技术框架包括三个主要阶段：
1. **任务设计**：设计药物配方匹配、药物相互作用识别和药物医嘱生成三个任务。
2. **模型测试**：使用GPT-4o对每个任务进行测试，记录模型的原始文本响应。
3. **性能评估**：使用临床医生评估和标准LLM指标（TF-IDF, Levenshtein similarity, ROUGE）对模型的响应进行评估。

**关键创新**：论文的关键创新在于：
1.  针对药物管理领域，设计了三个具体的、可量化的评估任务。
2.  结合临床医生评估和标准LLM指标，对LLM的性能进行综合评估。
3.  揭示了通用LLM在药物管理任务中的局限性，强调了领域特定训练的重要性。

**关键设计**：论文的关键设计包括：
1.  药物配方匹配任务：评估模型将通用药物名称匹配到所有可用配方的准确性，并统计遗漏和幻觉的数量。
2.  药物相互作用识别任务：评估模型识别给定药物方案中药物-药物相互作用的准确性。
3.  药物医嘱生成任务：评估模型生成不包含药物或缩写错误的医嘱语句的比例。
4.  评估指标：使用准确率、遗漏数量、幻觉数量、TF-IDF向量、归一化Levenshtein相似度和ROUGE 1/ROUGE L F1等指标进行综合评估。

## 📊 实验亮点

实验结果显示，GPT-4o在药物配方匹配任务中的准确率为49%，平均每种药物遗漏1.23种配方，产生1.14个幻觉。在药物-药物相互作用识别任务中，准确率为54.7%。在药物医嘱生成任务中，GPT-4o在65.8%的情况下生成了不包含药物或缩写错误的医嘱语句。这些数据表明，通用LLM在药物管理任务中表现不佳，需要进行领域特定训练。

## 🎯 应用场景

该研究结果可应用于指导开发更可靠的、领域特定的药物管理AI系统。通过针对性地训练LLM，可以提高其在药物推荐、药物相互作用识别和药物医嘱生成方面的准确性，从而辅助医生进行决策，减少医疗错误，并改善患者的用药安全。

## 📄 摘要（原文）

> Purpose: Large language models (LLMs) have proven performance for certain diagnostic tasks, however limited studies have evaluated their consistency in recommending appropriate medication regimens for a given diagnosis. Medication management is a complex task that requires synthesis of drug formulation and complete order instructions for safe use. Here, the performance of GPT 4o, an LLM available with ChatGPT, was tested for three medication management tasks. Methods: GPT-4o performance was tested using three medication tasks: identifying available formulations for a given generic drug name, identifying drug-drug interactions (DDI) for a given medication regimen, and preparing a medication order for a given generic drug name. For each experiment, the models raw text response was captured exactly as returned and evaluated using clinician evaluation in addition to standard LLM metrics, including Term Frequency-Inverse Document Frequency (TF IDF) vectors, normalized Levenshtein similarity, and Recall-Oriented Understudy for Gisting Evaluation (ROUGE 1/ROUGE L F1) between each response and its reference string. Results: For the first task of drug-formulation matching, GPT-4o had 49% accuracy for generic medications being matched to all available formulations, with an average of 1.23 omissions per medication and 1.14 hallucinations per medication. For the second task of drug-drug interaction identification, the accuracy was 54.7% for identifying the DDI pair. For the third task, GPT-4o generated order sentences containing no medication or abbreviation errors in 65.8% of cases. Conclusions: Model performance for basic medication tasks was consistently poor. This evaluation highlights the need for domain-specific training through clinician-annotated datasets and a comprehensive evaluation framework for benchmarking performance.

