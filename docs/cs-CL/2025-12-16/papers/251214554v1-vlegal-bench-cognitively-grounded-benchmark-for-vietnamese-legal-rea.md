---
layout: default
title: VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models
---

# VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14554" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14554v1</a>
  <a href="https://arxiv.org/pdf/2512.14554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14554v1" onclick="toggleFavorite(this, '2512.14554v1', 'VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nguyen Tien Dong, Minh-Anh Nguyen, Thanh Dat Hoang, Nguyen Tuan Ngoc, Dao Xuan Quang Minh, Phan Phi Hai, Nguyen Thi Ngoc Anh, Dang Van Tu, Binh Vu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出VLegal-Bench，用于评估LLM在越南法律推理任务中的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `越南法律` `大型语言模型` `法律推理` `认知评估` `基准测试`

## 📋 核心要点

1. 现有LLM在处理复杂、层级化且频繁修订的越南法律时，面临理解和应用法律知识的挑战。
2. VLegal-Bench旨在通过模拟实际法律场景的任务，从认知角度全面评估LLM的法律理解能力。
3. 该基准包含10450个样本，由法律专家标注和验证，确保其权威性和真实性，涵盖多种法律任务。

## 📝 摘要（中文）

大型语言模型（LLM）的快速发展为人工智能在法律领域的应用带来了新的可能性。然而，越南法律的复杂性、层级结构和频繁修订对评估这些模型解释和利用法律知识的能力提出了巨大挑战。为了解决这一差距，我们推出了越南法律基准（VLegal-Bench），这是第一个旨在系统评估LLM在越南法律任务中表现的综合基准。VLegal-Bench以Bloom的认知分类学为基础，通过反映实际使用场景的任务，涵盖了多个层次的法律理解。该基准包含10,450个样本，这些样本通过严格的标注流程生成，法律专家使用我们的标注系统对每个实例进行标注和交叉验证，以确保每个样本都基于权威的法律文件，并反映了现实世界的法律助理工作流程，包括一般法律问答、检索增强生成、多步骤推理和针对越南法律的基于场景的问题解决。通过提供一个标准化、透明和认知驱动的评估框架，VLegal-Bench为评估LLM在越南法律环境中的性能奠定了坚实的基础，并支持开发更可靠、可解释和符合伦理的人工智能辅助法律系统。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理越南法律相关任务时，由于越南法律体系的复杂性、层级结构以及频繁的修订，难以准确理解和应用法律知识。这导致了LLM在越南法律领域的应用受限，无法有效辅助法律专业人士的工作。现有方法缺乏一个专门针对越南法律的、综合性的评估基准，难以客观评估LLM的性能。

**核心思路**：VLegal-Bench的核心思路是构建一个全面、标准化的越南法律基准，该基准能够系统地评估LLM在不同认知层次上的法律理解能力。通过模拟实际的法律应用场景，例如法律问答、检索增强生成、多步骤推理和基于场景的问题解决，来考察LLM对越南法律的掌握程度。

**技术框架**：VLegal-Bench的构建流程包括以下几个主要阶段：1) 任务设计：根据Bloom的认知分类学，设计涵盖不同认知层次的法律任务。2) 数据收集：从权威的越南法律文件中收集数据，并根据任务需求进行整理。3) 数据标注：由法律专家使用专门设计的标注系统对数据进行标注和交叉验证，确保标注的准确性和一致性。4) 基准构建：将标注好的数据整理成标准化的基准格式，并提供相应的评估工具。

**关键创新**：VLegal-Bench的关键创新在于：1) 它是第一个专门针对越南法律的综合性评估基准。2) 它采用了Bloom的认知分类学，从认知角度全面评估LLM的法律理解能力。3) 它模拟了实际的法律应用场景，更贴近实际需求。4) 它采用了严格的标注流程，确保数据的质量和可靠性。

**关键设计**：VLegal-Bench包含10,450个样本，涵盖一般法律问答、检索增强生成、多步骤推理和基于场景的问题解决等多种任务。标注过程中，法律专家使用预定义的标注指南，对每个样本进行标注，并进行交叉验证。评估指标包括准确率、召回率、F1值等，用于衡量LLM在不同任务上的性能。

## 📊 实验亮点

VLegal-Bench包含10,450个样本，涵盖多种法律任务，并通过严格的法律专家标注和交叉验证，保证了数据的质量。该基准为评估LLM在越南法律领域的性能提供了一个标准化的平台，可以有效区分不同模型的能力差异，并为模型优化提供指导。

## 🎯 应用场景

VLegal-Bench可用于评估和提升LLM在越南法律领域的应用能力，例如智能法律咨询、法律文书生成、案件分析等。该基准有助于开发更可靠、可解释和符合伦理的人工智能辅助法律系统，提高法律服务的效率和质量，并为法律专业人士提供更强大的工具。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has enabled new possibilities for applying artificial intelligence within the legal domain. Nonetheless, the complexity, hierarchical organization, and frequent revisions of Vietnamese legislation pose considerable challenges for evaluating how well these models interpret and utilize legal knowledge. To address this gap, Vietnamese Legal Benchmark (VLegal-Bench) is introduced, the first comprehensive benchmark designed to systematically assess LLMs on Vietnamese legal tasks. Informed by Bloom's cognitive taxonomy, VLegal-Bench encompasses multiple levels of legal understanding through tasks designed to reflect practical usage scenarios. The benchmark comprises 10,450 samples generated through a rigorous annotation pipeline, where legal experts label and cross-validate each instance using our annotation system to ensure every sample is grounded in authoritative legal documents and mirrors real-world legal assistant workflows, including general legal questions and answers, retrieval-augmented generation, multi-step reasoning, and scenario-based problem solving tailored to Vietnamese law. By providing a standardized, transparent, and cognitively informed evaluation framework, VLegal-Bench establishes a solid foundation for assessing LLM performance in Vietnamese legal contexts and supports the development of more reliable, interpretable, and ethically aligned AI-assisted legal systems.

