---
layout: default
title: "ArchGPT: Understanding the World's Architectures with Large Multimodal Models"
---

# ArchGPT: Understanding the World's Architectures with Large Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20858" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20858v1</a>
  <a href="https://arxiv.org/pdf/2509.20858.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20858v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20858v1', 'ArchGPT: Understanding the World\'s Architectures with Large Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuze Wang, Luo Yang, Junyi Wang, Yue Qi

**分类**: cs.GR, cs.CV, cs.MM

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**ArchGPT：利用大型多模态模型理解世界建筑**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `建筑视觉问答` `多模态学习` `大型语言模型` `数据增强` `知识蒸馏`

## 📋 核心要点

1. 现有VR/MR/AR系统在建筑领域的应用缺乏可扩展性，依赖于特定案例和硬编码注释，难以适应多样化的建筑环境。
2. ArchGPT提出了一种多模态建筑视觉问答模型，并构建了可扩展的数据流程，用于生成高质量、特定于建筑的VQA注释。
3. 通过在Arch-300K数据集上微调ShareGPT4V-7B，ArchGPT在建筑视觉问答任务上取得了良好效果，为建筑理解提供了新途径。

## 📝 摘要（中文）

建筑体现了美学、文化和历史价值，是人类文明的切实证明。研究人员长期以来利用虚拟现实（VR）、混合现实（MR）和增强现实（AR）来实现对建筑的沉浸式探索和解读，从而提高教育、遗产保护和专业设计实践中建筑的可访问性、公众理解和创意工作流程。然而，现有的VR/MR/AR系统通常是针对特定案例开发的，依赖于硬编码的注释和特定于任务的交互，无法跨越不同的建筑环境进行扩展。本文提出了ArchGPT，一个多模态建筑视觉问答（VQA）模型，以及一个可扩展的数据构建流程，用于管理高质量的、特定于建筑的VQA注释。该流程生成了Arch-300K，一个包含约315,000个图像-问题-答案三元组的领域专用数据集。Arch-300K是通过一个多阶段过程构建的：首先，我们从维基共享资源中管理建筑场景，并使用一种新颖的由粗到精的策略过滤非约束的游客照片集，该策略集成了3D重建和语义分割，以选择无遮挡、结构一致的建筑图像。为了减轻原始文本元数据中的噪声和不一致性，我们提出了一种由LLM引导的文本验证和知识蒸馏流程，以生成可靠的、特定于建筑的问题-答案对。使用这些精心策划的图像和改进的元数据，我们进一步综合形式分析注释——包括详细的描述和方面引导的对话——以提供更丰富的语义多样性，同时保持对数据的忠实性。我们在Arch-300K上对开源多模态骨干网络ShareGPT4V-7B进行监督微调，从而得到ArchGPT。

## 🔬 方法详解

**问题定义**：论文旨在解决现有VR/MR/AR系统在建筑领域应用中，缺乏可扩展性和泛化能力的问题。现有方法依赖于针对特定建筑的硬编码注释和任务特定交互，无法有效处理多样化的建筑环境，且数据标注成本高昂。

**核心思路**：论文的核心思路是利用大型多模态模型（LLM）的强大能力，结合高质量的建筑图像和文本数据，构建一个能够理解和回答关于建筑视觉问题的模型。通过数据驱动的方式，避免了人工标注的局限性，提高了模型的可扩展性和泛化能力。

**技术框架**：ArchGPT的构建包含以下几个主要阶段：1) **数据收集与筛选**：从Wikimedia Commons等来源收集建筑图像，并使用基于3D重建和语义分割的粗到精策略，筛选出高质量、无遮挡的建筑图像。2) **数据标注与增强**：利用LLM对图像的原始文本元数据进行验证和知识蒸馏，生成可靠的、特定于建筑的问题-答案对。同时，合成形式分析注释，包括详细描述和方面引导的对话，以增加数据的语义多样性。3) **模型训练**：在构建的Arch-300K数据集上，对开源多模态骨干网络ShareGPT4V-7B进行监督微调，得到ArchGPT模型。

**关键创新**：论文的关键创新在于：1) 提出了一个可扩展的数据构建流程，能够自动生成高质量的建筑VQA数据集，降低了数据标注成本。2) 利用LLM进行文本验证和知识蒸馏，有效减轻了原始文本元数据中的噪声和不一致性。3) 通过合成形式分析注释，增加了数据的语义多样性，提升了模型的理解能力。

**关键设计**：在数据筛选阶段，采用了基于3D重建和语义分割的粗到精策略，以确保图像的结构一致性和无遮挡性。在数据标注阶段，利用LLM进行文本验证和知识蒸馏，并设计了特定的prompt来生成高质量的问题-答案对。在模型训练阶段，选择了ShareGPT4V-7B作为骨干网络，并采用了监督微调的方式进行训练。

## 📊 实验亮点

论文构建了包含315,000个图像-问题-答案三元组的Arch-300K数据集，并通过在ShareGPT4V-7B上进行微调，得到了ArchGPT模型。实验结果表明，ArchGPT在建筑视觉问答任务上取得了显著的性能提升，证明了该方法的可行性和有效性。

## 🎯 应用场景

ArchGPT具有广泛的应用前景，可用于增强现实建筑导览、建筑设计辅助、建筑遗产保护和教育等领域。它可以帮助用户更深入地理解建筑的结构、历史和文化价值，并为建筑师和设计师提供更智能的设计工具。未来，ArchGPT有望成为建筑领域的重要基础设施。

## 📄 摘要（原文）

> Architecture embodies aesthetic, cultural, and historical values, standing as a tangible testament to human civilization. Researchers have long leveraged virtual reality (VR), mixed reality (MR), and augmented reality (AR) to enable immersive exploration and interpretation of architecture, enhancing accessibility, public understanding, and creative workflows around architecture in education, heritage preservation, and professional design practice. However, existing VR/MR/AR systems are often developed case-by-case, relying on hard-coded annotations and task-specific interactions that do not scale across diverse built environments. In this work, we present ArchGPT, a multimodal architectural visual question answering (VQA) model, together with a scalable data-construction pipeline for curating high-quality, architecture-specific VQA annotations. This pipeline yields Arch-300K, a domain-specialized dataset of approximately 315,000 image-question-answer triplets. Arch-300K is built via a multi-stage process: first, we curate architectural scenes from Wikimedia Commons and filter unconstrained tourist photo collections using a novel coarse-to-fine strategy that integrates 3D reconstruction and semantic segmentation to select occlusion-free, structurally consistent architectural images. To mitigate noise and inconsistency in raw textual metadata, we propose an LLM-guided text verification and knowledge-distillation pipeline to generate reliable, architecture-specific question-answer pairs. Using these curated images and refined metadata, we further synthesize formal analysis annotations-including detailed descriptions and aspect-guided conversations-to provide richer semantic variety while remaining faithful to the data. We perform supervised fine-tuning of an open-source multimodal backbone ,ShareGPT4V-7B, on Arch-300K, yielding ArchGPT.

