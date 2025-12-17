---
layout: default
title: Train a Unified Multimodal Data Quality Classifier with Synthetic Data
---

# Train a Unified Multimodal Data Quality Classifier with Synthetic Data

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15162" target="_blank" class="toolbar-btn">arXiv: 2510.15162v1</a>
    <a href="https://arxiv.org/pdf/2510.15162.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15162v1" 
            onclick="toggleFavorite(this, '2510.15162v1', 'Train a Unified Multimodal Data Quality Classifier with Synthetic Data')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Weizhi Wang, Rongmei Lin, Shiyang Li, Colin Lockard, Ritesh Sarkhel, Sanket Lokegaonkar, Jingbo Shang, Xifeng Yan, Nasser Zalmout, Xian Li

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-16

**备注**: EMNLP 2025 Findings

---

## 💡 一句话要点

**提出UniFilter：一种基于合成数据的统一多模态数据质量分类器**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `数据质量` `数据过滤` `合成数据` `大型语言模型` `预训练` `图像文本` `交错文档`

## 📋 核心要点

1. 高质量多模态数据过滤是MLLM预训练的关键，但现有方法在处理图像-文本交错文档数据时存在不足。
2. UniFilter通过半合成方法生成多质量级别的数据，用于训练统一的多模态数据质量分类器，有效过滤数据。
3. 实验表明，使用UniFilter过滤的数据预训练的MLLM在零样本推理和上下文学习方面显著提升。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)持续地在图像-文本描述数据和交错文档数据的混合数据上进行预训练，然而，针对图像-文本交错文档数据的高质量数据过滤研究不足。我们提出训练一个高效的MLLM，作为一个统一的多模态数据质量分类器，以过滤高质量的图像-文本描述和交错数据(UniFilter)。为了解决收集多样化标注多模态数据的挑战，我们引入了一种半合成方法，该方法利用现成的原始图像，并生成跨四个质量级别的相应文本。这种方法能够有效地为描述和交错文档数据创建样本-分数对，以训练UniFilter。我们将UniFilter应用于从DataComp描述数据集和OBELICS图像-文本交错数据集筛选高质量的描述数据和交错数据。在过滤后的数据上预训练的MLLM相比于在基线过滤数据上训练的MLLM，表现出显著增强的能力，实现了更强的零样本推理和上下文学习能力。在视觉监督微调后，这些UniFilter诱导的MLLM在各种基准测试上实现了更强的性能，突出了高质量多模态预训练的下游优势。我们将用于训练UniFilter的合成训练数据、UniFilter模型检查点以及由UniFilter策划的高质量交错文档子集OBELICS-HQ发布给社区，以供重现和进一步开发。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）预训练过程中，图像-文本交错文档数据质量不高的问题。现有方法缺乏有效的数据过滤机制，导致预训练的MLLM性能受限。高质量的多模态数据难以获取，标注成本高昂，成为一个主要痛点。

**核心思路**：论文的核心思路是训练一个统一的多模态数据质量分类器（UniFilter），用于区分高质量和低质量的图像-文本数据，包括图像-文本描述数据和交错文档数据。通过半合成数据生成方法，降低数据标注成本，并为UniFilter提供充足的训练数据。

**技术框架**：UniFilter的训练流程主要包括以下几个阶段：1) 利用现成的原始图像，通过半合成方法生成不同质量级别的图像-文本数据对，包括描述数据和交错文档数据。2) 使用生成的合成数据训练UniFilter，使其能够对多模态数据的质量进行评分。3) 将UniFilter应用于大规模多模态数据集（如DataComp和OBELICS），过滤出高质量的数据子集。4) 使用过滤后的高质量数据预训练MLLM，并在下游任务上进行微调。

**关键创新**：论文的关键创新在于提出了一种半合成数据生成方法，用于创建多质量级别的图像-文本数据。这种方法避免了人工标注的成本，并能够生成足够多的训练数据，用于训练UniFilter。此外，UniFilter的设计使其能够同时处理图像-文本描述数据和交错文档数据，具有更强的通用性。

**关键设计**：半合成数据生成方法是关键设计之一。具体来说，论文利用现有的图像数据，并使用不同的文本生成策略（例如，使用不同的语言模型或不同的解码策略）生成对应于不同质量级别的文本描述。例如，高质量的文本描述可能包含更详细、更准确的信息，而低质量的文本描述可能包含错误、不相关的信息或语法错误。损失函数的设计目标是使UniFilter能够准确地预测多模态数据的质量得分，从而区分高质量和低质量的数据。

## 📊 实验亮点

实验结果表明，使用UniFilter过滤后的数据预训练的MLLM在零样本推理和上下文学习能力上显著提升。经过视觉监督微调后，这些MLLM在各种基准测试上取得了更强的性能，验证了高质量多模态预训练的有效性。UniFilter能够有效提升MLLM的下游任务性能。

## 🎯 应用场景

该研究成果可广泛应用于多模态大型语言模型的预训练数据清洗、数据增强和模型优化。通过UniFilter过滤高质量数据，能够提升MLLM在图像理解、文本生成、视觉问答等任务上的性能，并可应用于智能客服、内容创作、教育等领域。

## 📄 摘要（原文）

> The Multimodal Large Language Models (MLLMs) are continually pre-trained on a mixture of image-text caption data and interleaved document data, while the high-quality data filtering towards image-text interleaved document data is under-explored. We propose to train an efficient MLLM as a Unified Mulitmodal Data Quality Classifier to Filter both high-quality image-text caption and interleaved data (UniFilter). To address the challenge of collecting diverse labeled multimodal data, we introduce a semi-synthetic approach that leverages readily available raw images and generates corresponding text across four quality levels. This method enables efficient creation of sample-score pairs for both caption and interleaved document data to train UniFilter. We apply UniFilter to curate high-quality caption data from DataComp caption dataset and interleaved data from the OBELICS image-text interleaved dataset. MLLMs pre-trained on the filtered data demonstrate significantly enhanced capabilities compared to those trained on baseline-filtered data, achieving stronger zero-shot reasoning and in-context learning capabilities. After visual supervised fine-tuning, these UniFilter-induced MLLMs achieve stronger performance on various benchmarks, highlighting the downstream benefits of high-quality multimodal pre-training. We release the synthetic training data used for training UniFilter, the UniFilter model checkpoints, and the high-quality interleaved document subset OBELICS-HQ, curated by UniFilter, to the community for reproduction and further development.

