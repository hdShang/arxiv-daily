---
layout: default
title: BBox DocVQA: A Large Scale Bounding Box Grounded Dataset for Enhancing Reasoning in Document Visual Question Answer
---

# BBox DocVQA: A Large Scale Bounding Box Grounded Dataset for Enhancing Reasoning in Document Visual Question Answer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15090" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15090v1</a>
  <a href="https://arxiv.org/pdf/2511.15090.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15090v1" onclick="toggleFavorite(this, '2511.15090v1', 'BBox DocVQA: A Large Scale Bounding Box Grounded Dataset for Enhancing Reasoning in Document Visual Question Answer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhan Yu, Wang Chen, Guanqiang Qi, Weikang Li, Yang Li, Lei Sha, Deguo Xia, Jizhou Huang

**分类**: cs.DB, cs.AI, cs.CV

**发布日期**: 2025-11-19

**备注**: 22 pages, 4 figures

---

## 💡 一句话要点

**提出BBox DocVQA数据集，增强文档视觉问答中空间推理能力。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `文档视觉问答` `视觉语言推理` `空间推理` `边界框标注` `多模态学习`

## 📋 核心要点

1. 现有DocVQA数据集缺乏细粒度的空间定位，限制了视觉语言模型的可解释性和空间推理能力。
2. 提出BBox DocVQA数据集，通过显式边界框标注QA对，增强模型在视觉文档中的空间推理和证据定位能力。
3. 实验表明，在BBox DocVQA上微调可以显著提高边界框定位和答案生成，验证了数据集的有效性。

## 📝 摘要（中文）

文档视觉问答(DocVQA)是多模态文档理解的基础任务，也是视觉语言推理的关键测试平台。然而，现有DocVQA数据集大多局限于页面级别，缺乏细粒度的空间定位，限制了视觉语言模型(VLMs)的可解释性和推理能力。为了解决这一问题，我们推出了BBox DocVQA，这是一个大规模的、基于边界框的数据集，旨在增强视觉文档中的空间推理和证据定位。我们进一步提出了一个自动构建流程，即“分割、判断和生成”，该流程集成了用于区域分割的分割模型、用于语义判断的VLM和用于问题答案生成的另一个高级VLM，然后进行人工验证以确保质量。最终数据集包含3.6K个不同的文档和32K个QA对，涵盖单区域和多区域以及单页和多页场景。每个QA实例都基于显式的边界框，从而能够对空间语义对齐进行细粒度评估。在BBox DocVQA上对多个最先进的VLM（例如，GPT 5、Qwen2.5 VL和InternVL）进行基准测试，揭示了空间定位和推理准确性方面持续存在的挑战。此外，在BBox DocVQA上进行微调可以显著提高边界框定位和答案生成，从而验证了其增强VLM推理能力的有效性。我们的数据集和代码将公开发布，以推进可解释和空间定位的视觉语言推理研究。

## 🔬 方法详解

**问题定义**：现有DocVQA数据集主要关注页面级别的问答，缺乏细粒度的空间信息，导致模型难以进行精确的空间推理和定位。这限制了模型在复杂文档场景下的应用，例如需要定位特定表格单元格或图像区域才能回答问题的情况。现有方法难以提供可解释的推理过程，无法明确指出答案的依据。

**核心思路**：BBox DocVQA的核心思路是通过引入边界框标注，将QA对与文档中的特定区域进行关联，从而显式地提供空间信息。这种方式能够迫使模型学习空间语义对齐，并提高模型在空间推理方面的能力。通过细粒度的标注，模型可以更好地理解问题与文档区域之间的关系，从而提高答案的准确性和可解释性。

**技术框架**：BBox DocVQA的构建流程主要包含三个阶段：分割（Segment）、判断（Judge）和生成（Generate）。首先，使用分割模型将文档分割成不同的区域。然后，使用VLM对分割后的区域进行语义判断，筛选出有意义的区域。最后，使用另一个VLM基于这些区域生成问题和答案，并使用人工进行验证和质量保证。这个流程旨在自动化地生成高质量的、带有边界框标注的QA对。

**关键创新**：BBox DocVQA的关键创新在于其大规模的、基于边界框的标注方式。与现有的DocVQA数据集相比，BBox DocVQA提供了更细粒度的空间信息，使得模型能够更好地学习空间语义对齐。此外，自动构建流程也降低了数据集构建的成本，使得可以构建更大规模的数据集。

**关键设计**：在自动构建流程中，选择合适的分割模型、语义判断VLM和问题答案生成VLM至关重要。论文中使用了先进的VLM模型，并进行了人工验证以确保数据集的质量。具体的参数设置和网络结构细节可能因所使用的VLM模型而异，但总体目标是生成高质量的、与文档区域相关的QA对。

## 📊 实验亮点

在BBox DocVQA上对GPT 5、Qwen2.5 VL和InternVL等多个最先进的VLM进行基准测试，揭示了模型在空间定位和推理准确性方面仍存在挑战。在BBox DocVQA上进行微调后，模型的边界框定位和答案生成能力均得到显著提升，验证了该数据集对于增强VLM推理能力的有效性。具体提升幅度未知，需要在论文中查找。

## 🎯 应用场景

BBox DocVQA数据集可应用于各种文档理解和视觉语言推理任务，例如智能文档处理、信息抽取、智能客服等。通过增强模型在空间推理方面的能力，可以提高文档处理的自动化程度和准确性，从而提高工作效率并降低成本。该数据集还有助于开发更可解释的视觉语言模型，提升用户对模型决策的信任度。

## 📄 摘要（原文）

> Document Visual Question Answering (DocVQA) is a fundamental task for multimodal document understanding and a key testbed for vision language reasoning. However, most existing DocVQA datasets are limited to the page level and lack fine grained spatial grounding, constraining the interpretability and reasoning capability of Vision Language Models (VLMs). To address this gap, we introduce BBox DocVQA a large scale, bounding box grounded dataset designed to enhance spatial reasoning and evidence localization in visual documents. We further present an automated construction pipeline, Segment Judge and Generate, which integrates a segment model for region segmentation, a VLM for semantic judgment, and another advanced VLM for question answer generation, followed by human verification for quality assurance. The resulting dataset contains 3.6 K diverse documents and 32 K QA pairs, encompassing single and multi region as well as single and multi page scenarios. Each QA instance is grounded on explicit bounding boxes, enabling fine grained evaluation of spatial semantic alignment. Benchmarking multiple state of the art VLMs (e.g., GPT 5, Qwen2.5 VL, and InternVL) on BBox DocVQA reveals persistent challenges in spatial grounding and reasoning accuracy. Furthermore, fine tuning on BBox DocVQA substantially improves both bounding box localization and answer generation, validating its effectiveness for enhancing the reasoning ability of VLMs. Our dataset and code will be publicly released to advance research on interpretable and spatially grounded vision language reasoning.

