---
layout: default
title: "COCO-Urdu: A Large-Scale Urdu Image-Caption Dataset with Multimodal Quality Estimation"
---

# COCO-Urdu: A Large-Scale Urdu Image-Caption Dataset with Multimodal Quality Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09014" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09014v1</a>
  <a href="https://arxiv.org/pdf/2509.09014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09014v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09014v1', 'COCO-Urdu: A Large-Scale Urdu Image-Caption Dataset with Multimodal Quality Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Umair Hassan

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-10

**备注**: 17 pages, 3 figures, 3 tables. Dataset available at https://huggingface.co/datasets/umairhassan02/urdu-translated-coco-captions-subset. Scripts and notebooks to reproduce results available at https://github.com/umair-hassan2/COCO-Urdu

---

## 💡 一句话要点

**COCO-Urdu：构建大规模乌尔都语图像描述数据集，并提出多模态质量评估框架。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `乌尔都语` `图像描述` `多模态` `数据集` `机器翻译` `质量评估` `视觉-语言` `低资源语言`

## 📋 核心要点

1. 多模态研究中乌尔都语资源严重不足，缺乏大规模高质量数据集限制了相关系统的发展，加剧了多语言视觉-语言模型中的偏差。
2. 论文提出COCO-Urdu数据集，通过高质量的机器翻译和多模态质量评估框架，构建大规模乌尔都语图像描述数据集。
3. COCO-Urdu数据集在BLEU等指标上表现良好，为乌尔都语视觉-语言研究提供了宝贵资源，并公开了质量评估流程。

## 📝 摘要（中文）

本文提出了COCO-Urdu，一个大规模的乌尔都语图像描述数据集，旨在弥补多模态和视觉-语言研究中乌尔都语资源的匮乏。该数据集基于MS COCO，包含59,000张图像和319,000条乌尔都语描述，通过分层抽样保留了原始分布。描述使用SeamlessM4T v2翻译，并通过混合多模态质量评估框架进行验证，该框架集成了COMET-Kiwi（翻译质量）、基于CLIP的相似度（视觉对齐）以及BERTScore与回译（语义一致性）。低质量描述通过开源大型语言模型迭代改进。COCO-Urdu在BLEU、SacreBLEU和chrF上进行了基准测试，结果表现良好。据我们所知，COCO-Urdu是目前最大的公开乌尔都语描述数据集。通过发布数据集和质量评估流程，旨在减少多模态研究中的语言偏差，并为包容性的视觉-语言系统奠定基础。

## 🔬 方法详解

**问题定义**：现有的多模态和视觉-语言模型主要集中在高资源语言上，对于乌尔都语这种拥有超过2.5亿使用者的语言，缺乏大规模、高质量的数据集。这导致了乌尔都语相关的多模态系统发展受限，并且加剧了现有模型中的语言偏差。因此，需要构建一个大规模的乌尔都语图像描述数据集，以促进乌尔都语相关的视觉-语言研究。

**核心思路**：论文的核心思路是利用现有的MS COCO数据集，通过高质量的机器翻译和严格的质量控制，生成乌尔都语的图像描述。为了保证翻译质量和语义一致性，论文提出了一个混合多模态质量评估框架，并使用开源大型语言模型对低质量的描述进行迭代改进。

**技术框架**：COCO-Urdu数据集的构建流程主要包括以下几个阶段：1) 数据选择：从MS COCO数据集中选择59,000张图像，并进行分层抽样以保留原始分布。2) 机器翻译：使用SeamlessM4T v2将英文描述翻译成乌尔都语。3) 质量评估：使用混合多模态质量评估框架对翻译后的描述进行评估。该框架包含三个模块：COMET-Kiwi（评估翻译质量）、基于CLIP的相似度（评估视觉对齐程度）和BERTScore与回译（评估语义一致性）。4) 迭代改进：对于质量评估得分较低的描述，使用开源大型语言模型进行迭代改进。

**关键创新**：论文的关键创新在于提出了一个混合多模态质量评估框架，该框架综合考虑了翻译质量、视觉对齐程度和语义一致性，能够有效地评估和筛选高质量的乌尔都语图像描述。此外，论文还采用了迭代改进的方法，利用大型语言模型对低质量的描述进行优化，进一步提高了数据集的质量。

**关键设计**：在质量评估框架中，COMET-Kiwi用于评估翻译的流畅度和准确性；CLIP模型用于计算图像和描述之间的相似度，以确保视觉对齐；BERTScore结合回译技术用于评估描述的语义一致性。这些指标的权重需要根据实际情况进行调整，以达到最佳的评估效果。在迭代改进阶段，需要选择合适的开源大型语言模型，并设计有效的prompt，以指导模型生成高质量的乌尔都语描述。

## 📊 实验亮点

COCO-Urdu数据集是目前最大的公开乌尔都语图像描述数据集，包含59,000张图像和319,000条乌尔都语描述。在BLEU、SacreBLEU和chrF等指标上进行了基准测试，结果表明COCO-Urdu数据集具有较高的质量。例如，在某个测试集上，COCO-Urdu的BLEU得分达到了XX（具体数值未知），SacreBLEU得分达到了YY（具体数值未知），chrF得分达到了ZZ（具体数值未知）。

## 🎯 应用场景

COCO-Urdu数据集可广泛应用于乌尔都语相关的视觉-语言任务，例如图像描述生成、视觉问答、图像检索等。该数据集的发布有助于促进乌尔都语自然语言处理和多模态研究的发展，并减少多语言模型中的语言偏差。此外，该数据集和质量评估流程可以推广到其他低资源语言，为构建更多包容性的视觉-语言系统提供参考。

## 📄 摘要（原文）

> Urdu, spoken by over 250 million people, remains critically under-served in multimodal and vision-language research. The absence of large-scale, high-quality datasets has limited the development of Urdu-capable systems and reinforced biases in multilingual vision-language models trained primarily on high-resource languages. To address this gap, we present COCO-Urdu, a large-scale image-caption dataset derived from MS COCO, containing 59,000 images and 319,000 Urdu captions selected through stratified sampling to preserve the original distribution. Captions were translated using SeamlessM4T v2 and validated with a hybrid multimodal quality estimation framework that integrates COMET-Kiwi for translation quality, CLIP-based similarity for visual grounding, and BERTScore with back-translation for semantic consistency; low-scoring captions were iteratively refined using open-source large language models. We further benchmark COCO-Urdu on BLEU, SacreBLEU, and chrF, reporting consistently strong results. To the best of our knowledge, COCO-Urdu is the largest publicly available Urdu captioning dataset. By releasing both the dataset and the quality estimation pipeline, we aim to reduce language bias in multimodal research and establish a foundation for inclusive vision-language systems.

