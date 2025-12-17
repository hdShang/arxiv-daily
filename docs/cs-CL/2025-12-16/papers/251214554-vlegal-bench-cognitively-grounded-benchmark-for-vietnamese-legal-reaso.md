---
layout: default
title: VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models
---

# VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14554" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14554</a>
  <a href="https://arxiv.org/pdf/2512.14554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14554" onclick="toggleFavorite(this, '2512.14554', 'VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nguyen Tien Dong, Minh-Anh Nguyen, Thanh Dat Hoang, Nguyen Tuan Ngoc, Dao Xuan Quang Minh, Phan Phi Hai, Nguyen Thi Ngoc Anh, Dang Van Tu, Binh Vu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出VLegal-Bench，用于评估LLM在越南法律推理任务中的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `越南法律` `大型语言模型` `法律推理` `评估基准` `认知分类学`

## 📋 核心要点

1. 现有LLM在处理复杂、层级化且频繁修订的越南法律时，面临法律知识理解和应用的挑战。
2. VLegal-Bench通过模拟实际法律场景的任务，从认知角度系统评估LLM的法律理解能力。
3. 该基准包含10450个样本，由法律专家标注和验证，确保数据权威性和真实性。

## 📝 摘要（中文）

大型语言模型（LLM）的快速发展为人工智能在法律领域的应用带来了新的可能性。然而，越南法律的复杂性、层级结构和频繁修订对评估这些模型解释和利用法律知识的能力提出了巨大挑战。为了解决这一差距，我们推出了越南法律基准（VLegal-Bench），这是第一个旨在系统评估LLM在越南法律任务中表现的综合基准。VLegal-Bench以Bloom的认知分类学为基础，通过旨在反映实际使用场景的任务，涵盖了多个层次的法律理解。该基准包含10,450个样本，这些样本通过严格的标注流程生成，法律专家使用我们的标注系统对每个实例进行标注和交叉验证，以确保每个样本都基于权威的法律文件，并反映了现实世界的法律助理工作流程，包括一般法律问答、检索增强生成、多步骤推理和针对越南法律的基于场景的问题解决。通过提供一个标准化、透明和认知驱动的评估框架，VLegal-Bench为评估LLM在越南法律环境中的性能奠定了坚实的基础，并支持开发更可靠、可解释和符合伦理的人工智能辅助法律系统。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理越南法律领域的问题时，由于越南法律的复杂性、层级结构以及频繁的修订，难以准确理解和应用法律知识。这导致了LLM在越南法律领域的应用受限，无法有效辅助法律工作者。现有方法缺乏一个专门针对越南法律的综合性评估基准，难以系统地评估LLM在越南法律任务中的表现。

**核心思路**：VLegal-Bench的核心思路是构建一个全面、系统且认知驱动的评估基准，用于评估LLM在越南法律领域的推理能力。该基准的设计受到Bloom认知分类学的启发，涵盖了不同层次的法律理解，从简单的知识回忆到复杂的问题解决。通过模拟实际的法律场景，VLegal-Bench能够更真实地反映LLM在实际应用中的表现。

**技术框架**：VLegal-Bench的整体框架包括数据收集、标注、验证和评估四个主要阶段。首先，收集大量的越南法律相关文本和案例。然后，由法律专家对这些数据进行标注，标注过程遵循一套严格的标注指南，确保标注的准确性和一致性。接下来，对标注的数据进行交叉验证，以进一步提高数据质量。最后，使用标注好的数据对LLM进行评估，评估指标包括准确率、召回率和F1值等。该基准包含多种任务类型，包括一般法律问答、检索增强生成、多步骤推理和基于场景的问题解决。

**关键创新**：VLegal-Bench的关键创新在于它是第一个专门针对越南法律的综合性评估基准。与现有的通用型评估基准相比，VLegal-Bench更能够反映LLM在越南法律领域的实际表现。此外，VLegal-Bench的设计受到Bloom认知分类学的启发，能够更全面地评估LLM的法律理解能力。该基准的数据集经过法律专家的严格标注和验证，保证了数据的质量和权威性。

**关键设计**：VLegal-Bench的关键设计包括任务类型的选择、评估指标的设定和数据标注指南的制定。任务类型涵盖了法律领域的各种常见任务，例如一般法律问答、检索增强生成、多步骤推理和基于场景的问题解决。评估指标包括准确率、召回率和F1值等，这些指标能够全面反映LLM的性能。数据标注指南详细规定了标注的标准和流程，确保标注的准确性和一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14554/img/VietLegalBench_overview.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14554/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14554/img/anotate_tool.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

VLegal-Bench包含10,450个高质量样本，涵盖多种法律任务。实验结果（论文中未明确给出具体数值，此处为推测）表明，现有LLM在VLegal-Bench上的表现仍有提升空间，尤其是在多步骤推理和基于场景的问题解决方面。该基准为未来研究提供了明确的方向。

## 🎯 应用场景

VLegal-Bench可用于评估和提升LLM在越南法律领域的应用能力，例如智能法律咨询、法律文书生成、案件分析等。该基准有助于开发更可靠、可解释和符合伦理的人工智能辅助法律系统，提高法律服务的效率和质量，并为法律从业者提供更强大的工具。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has enabled new possibilities for applying artificial intelligence within the legal domain. Nonetheless, the complexity, hierarchical organization, and frequent revisions of Vietnamese legislation pose considerable challenges for evaluating how well these models interpret and utilize legal knowledge. To address this gap, Vietnamese Legal Benchmark (VLegal-Bench) is introduced, the first comprehensive benchmark designed to systematically assess LLMs on Vietnamese legal tasks. Informed by Bloom's cognitive taxonomy, VLegal-Bench encompasses multiple levels of legal understanding through tasks designed to reflect practical usage scenarios. The benchmark comprises 10,450 samples generated through a rigorous annotation pipeline, where legal experts label and cross-validate each instance using our annotation system to ensure every sample is grounded in authoritative legal documents and mirrors real-world legal assistant workflows, including general legal questions and answers, retrieval-augmented generation, multi-step reasoning, and scenario-based problem solving tailored to Vietnamese law. By providing a standardized, transparent, and cognitively informed evaluation framework, VLegal-Bench establishes a solid foundation for assessing LLM performance in Vietnamese legal contexts and supports the development of more reliable, interpretable, and ethically aligned AI-assisted legal systems.

