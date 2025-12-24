---
layout: default
title: "DESIGNER: Design-Logic-Guided Multidisciplinary Data Synthesis for LLM Reasoning"
---

# DESIGNER: Design-Logic-Guided Multidisciplinary Data Synthesis for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12726" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12726v5</a>
  <a href="https://arxiv.org/pdf/2508.12726.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12726v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12726v5', 'DESIGNER: Design-Logic-Guided Multidisciplinary Data Synthesis for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weize Liu, Yongchi Zhao, Yijia Luo, Mingyu Xu, Jiaheng Liu, Yanan Li, Xiguo Hu, Zhiqi Bai, Yuchi Xu, Wenbo Su, Bo Zheng

**分类**: cs.CL

**发布日期**: 2025-08-18 (更新: 2025-12-02)

---

## 💡 一句话要点

**提出DESIGNER以解决多学科推理数据合成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理数据合成` `设计逻辑` `多学科推理` `教育技术` `智能问答系统` `数据集构建`

## 📋 核心要点

1. 现有推理数据集在学科广度、推理深度和多样性方面存在不足，限制了LLMs的推理能力。
2. 提出DESIGNER管道，通过设计逻辑指导LLMs模仿人类教育者的问题创建过程，实现高难度问题的自动合成。
3. 合成的DLR-Book和DLR-Web数据集在多学科推理能力上显著提升，超越了现有数据集的表现。

## 📝 摘要（中文）

大型语言模型（LLMs）在许多自然语言任务中取得了显著成功，但在复杂的多步骤推理方面仍然面临挑战，尤其是在不同学科之间。现有的推理数据集往往缺乏学科广度、推理深度和多样性，以及问题合成的指导原则。为此，本文提出了DESIGNER：一种基于设计逻辑的推理数据合成管道，利用自然可用的广泛原始文档（如书籍语料库和网络语料库）生成多学科的挑战性问题。我们通过反向工程从现有问题中提取了超过120,000种设计逻辑，并通过与源文档匹配生成可控类型和难度的推理问题。最终，我们合成了两个涵盖75个学科的大规模推理数据集，验证结果显示合成问题的难度和多样性显著优于基线数据集。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推理数据集在学科广度和推理深度不足的问题，导致LLMs在复杂推理任务中的表现不佳。

**核心思路**：通过引入“设计逻辑”概念，指导LLMs模仿人类教育者的问题创建过程，从而实现高难度、多样化问题的自动合成。

**技术框架**：整体架构包括数据收集、设计逻辑提取、问题生成和数据集构建四个主要模块。首先，从书籍和网络语料库中提取原始文档，然后反向工程提取设计逻辑，最后生成推理问题并构建数据集。

**关键创新**：最重要的创新在于设计逻辑的引入，使得问题合成过程更具指导性和系统性，显著提升了问题的难度和多样性。

**关键设计**：在设计过程中，采用了特定的参数设置和损失函数，以确保生成问题的质量和多样性，同时使用了多种网络结构来优化问题生成的效果。

## 📊 实验亮点

实验结果表明，合成的数据集在推理能力上显著优于现有基线数据集。特别是在使用Qwen3和Llama3模型进行监督微调时，仅使用合成数据就超越了经过完整后训练过程的官方最终模型，显示出合成数据的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能问答系统和多学科知识推理等。通过提升LLMs在多学科推理任务中的能力，能够为教育、科研和信息检索等领域带来更高效的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable success in many natural language tasks but still struggle with complex, multi-step reasoning, particularly across diverse disciplines. Existing reasoning datasets often lack disciplinary breadth, reasoning depth, and diversity, as well as guiding principles for question synthesis. We propose DESIGNER: a DESIGN-logic-guidEd Reasoning data synthesis pipeline that leverages naturally available, extensive raw documents (e.g., book corpus and web corpus) to generate multidisciplinary challenging questions. We introduce the concept of "design logic" and instruct LLMs to mimic human educators' question-creation process, enabling the automated synthesis of large-scale, high-difficulty questions. We use LLMs to reverse-engineer and abstract over 120,000 design logics from existing questions across various disciplines. By matching these design logics with source documents, we are able to generate reasoning questions with controllable question types and difficulty levels. Using this pipeline, we synthesized two large-scale reasoning datasets that span 75 disciplines: DLR-Book (3.04 million questions from the book corpus) and DLR-Web (1.66 million questions from the web corpus). Data analysis indicates that the questions synthesized by our method exhibit greater difficulty and diversity compared to those in the baseline datasets. We validate our synthesized data through supervised fine-tuning (SFT) on the Qwen3 and Llama3 model families. Our data substantially enhances their multidisciplinary reasoning capabilities, outperforming existing datasets. Notably, by applying SFT on the base versions of these models using only our data, we even surpass their official final models that have undergone the full post-training process.

