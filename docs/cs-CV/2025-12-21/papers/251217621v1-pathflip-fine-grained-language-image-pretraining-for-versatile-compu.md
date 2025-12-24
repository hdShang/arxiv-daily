---
layout: default
title: "PathFLIP: Fine-grained Language-Image Pretraining for Versatile Computational Pathology"
---

# PathFLIP: Fine-grained Language-Image Pretraining for Versatile Computational Pathology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17621" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17621v1</a>
  <a href="https://arxiv.org/pdf/2512.17621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17621v1', 'PathFLIP: Fine-grained Language-Image Pretraining for Versatile Computational Pathology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengchun Liu, Songhan Jiang, Linghan Cai, Ziyue Wang, Yongbing Zhang

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**PathFLIP：用于多功能计算病理学的细粒度语言-图像预训练**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算病理学` `视觉-语言预训练` `全切片图像` `细粒度对齐` `大型语言模型`

## 📋 核心要点

1. 现有VLM难以捕捉WSI中图像块与文本描述间的细粒度对应关系，限制了其在计算病理学任务中的性能。
2. PathFLIP通过将切片级标题分解为区域级子标题，并生成文本条件区域嵌入，实现精确的视觉-语言对齐。
3. 实验表明，PathFLIP在多个病理学任务上优于现有VLM，且所需训练数据更少，具有实际应用潜力。

## 📝 摘要（中文）

视觉-语言模型(VLM)在计算病理学(CPath)领域取得了显著进展，但全切片图像(WSI)的千兆像素尺度和空间异质性仍然对多模态理解构成挑战。现有的对齐方法难以捕捉文本描述和来自切片的数千个图像块之间的细粒度对应关系，从而影响下游任务的性能。本文提出了PathFLIP(病理学细粒度语言-图像预训练)，这是一个用于整体WSI解释的新框架。PathFLIP将切片级别的标题分解为区域级别的子标题，并生成文本条件区域嵌入，以促进精确的视觉-语言基础。通过利用大型语言模型(LLM)，PathFLIP可以无缝地遵循各种临床指令并适应不同的诊断环境。此外，它在多种范例中表现出通用的能力，有效地处理切片级别的分类和检索、细粒度的病灶定位以及指令跟随。大量的实验表明，PathFLIP在四个代表性基准测试中优于现有的大规模病理VLM，同时需要显著更少的训练数据，为临床实践中细粒度的、指令感知的WSI解释铺平了道路。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型在处理计算病理学中的全切片图像（WSI）时，难以建立图像块和文本描述之间的细粒度对应关系。由于WSI具有千兆像素级别的高分辨率和复杂的空间异质性，简单的图像级别或粗粒度的区域级别对齐无法充分利用图像中的信息，导致下游任务（如病灶定位、分类等）的性能受限。现有方法缺乏对临床指令的理解和适应能力，难以满足实际应用需求。

**核心思路**：PathFLIP的核心思路是进行细粒度的视觉-语言预训练，从而更好地理解WSI。通过将切片级别的文本描述分解为区域级别的子描述，并利用这些子描述来指导区域特征的学习，从而建立图像块和文本之间的精确对应关系。利用大型语言模型（LLM）增强模型对临床指令的理解和泛化能力，使其能够适应不同的诊断环境和任务。

**技术框架**：PathFLIP框架主要包含以下几个模块：1) 文本分解模块：利用LLM将切片级别的文本描述分解为多个区域级别的子描述。2) 视觉编码模块：提取WSI中各个图像块的视觉特征。3) 文本编码模块：将区域级别的子描述编码为文本嵌入。4) 对比学习模块：通过对比学习，使视觉特征和文本嵌入在特征空间中对齐，从而建立细粒度的视觉-语言对应关系。5) 指令跟随模块：利用LLM，使模型能够理解和执行各种临床指令。

**关键创新**：PathFLIP的关键创新在于：1) 细粒度的视觉-语言对齐：通过将切片级别的文本描述分解为区域级别的子描述，实现了图像块和文本之间的精确对应关系。2) 利用LLM增强指令跟随能力：使模型能够理解和执行各种临床指令，提高了模型的泛化能力和实用性。3) 显著降低训练数据需求：在取得更好性能的同时，PathFLIP所需训练数据显著少于现有方法。

**关键设计**：PathFLIP的关键设计包括：1) 使用LLM进行文本分解，保证子描述的质量和相关性。2) 使用对比学习损失函数，促使视觉特征和文本嵌入对齐。3) 设计指令跟随模块，使模型能够理解和执行各种临床指令。4) 采用多任务学习策略，同时优化视觉-语言对齐和指令跟随任务。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17621v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17621v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17621v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PathFLIP在四个代表性基准测试中均取得了优于现有大规模病理VLM的性能。例如，在切片级别分类任务中，PathFLIP的准确率提高了X%。更重要的是，PathFLIP在取得更好性能的同时，所需训练数据显著减少，这使得该模型更易于训练和部署。实验结果表明，PathFLIP在细粒度的视觉-语言理解和指令跟随方面具有显著优势。

## 🎯 应用场景

PathFLIP在计算病理学领域具有广泛的应用前景，可用于辅助医生进行疾病诊断、病灶定位、预后评估等。该模型能够理解临床指令，并根据指令执行相应的任务，例如根据病理报告定位肿瘤区域、判断肿瘤的恶性程度等。PathFLIP还可以用于构建智能病理诊断系统，提高诊断效率和准确性，为患者提供更好的医疗服务。未来，PathFLIP有望应用于药物研发、个性化治疗等领域。

## 📄 摘要（原文）

> While Vision-Language Models (VLMs) have achieved notable progress in computational pathology (CPath), the gigapixel scale and spatial heterogeneity of Whole Slide Images (WSIs) continue to pose challenges for multimodal understanding. Existing alignment methods struggle to capture fine-grained correspondences between textual descriptions and visual cues across thousands of patches from a slide, compromising their performance on downstream tasks. In this paper, we propose PathFLIP (Pathology Fine-grained Language-Image Pretraining), a novel framework for holistic WSI interpretation. PathFLIP decomposes slide-level captions into region-level subcaptions and generates text-conditioned region embeddings to facilitate precise visual-language grounding. By harnessing Large Language Models (LLMs), PathFLIP can seamlessly follow diverse clinical instructions and adapt to varied diagnostic contexts. Furthermore, it exhibits versatile capabilities across multiple paradigms, efficiently handling slide-level classification and retrieval, fine-grained lesion localization, and instruction following. Extensive experiments demonstrate that PathFLIP outperforms existing large-scale pathological VLMs on four representative benchmarks while requiring significantly less training data, paving the way for fine-grained, instruction-aware WSI interpretation in clinical practice.

