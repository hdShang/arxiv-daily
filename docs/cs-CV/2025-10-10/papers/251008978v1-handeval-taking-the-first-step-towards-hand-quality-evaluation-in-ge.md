---
layout: default
title: HandEval: Taking the First Step Towards Hand Quality Evaluation in Generated Images
---

# HandEval: Taking the First Step Towards Hand Quality Evaluation in Generated Images

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08978" target="_blank" class="toolbar-btn">arXiv: 2510.08978v1</a>
    <a href="https://arxiv.org/pdf/2510.08978.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08978v1" 
            onclick="toggleFavorite(this, '2510.08978v1', 'HandEval: Taking the First Step Towards Hand Quality Evaluation in Generated Images')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zichuan Wang, Bo Peng, Songlin Yang, Zhenchen Tang, Jing Dong

**分类**: cs.CV

**发布日期**: 2025-10-10

---

## 💡 一句话要点

**提出HandEval，用于评估生成图像中手部质量，提升AIGC应用效果。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手部质量评估` `生成图像` `多模态大语言模型` `AIGC检测` `文图生成` `手部关键点` `HandPair数据集`

## 📋 核心要点

1. 现有的文图生成模型在复杂局部区域（特别是手部）的细节生成方面存在困难，导致生成的手部结构扭曲、纹理不真实。
2. 论文提出HandEval模型，利用多模态大语言模型和手部关键点先验知识，实现对手部质量的精准评估。
3. 实验表明，HandEval与人类判断更一致，集成到图像生成和AIGC检测流程后，能显著提高手部真实感和检测精度。

## 📝 摘要（中文）

本文提出了首个针对生成图像中手部区域质量评估的任务，并展示了其丰富的下游应用。为此，作者构建了HandPair数据集，包含48k个由高质量和低质量手部图像对组成的数据，无需手动标注即可实现低成本、高效的监督学习。基于此，开发了HandEval，一个精心设计的手部质量评估模型。该模型利用多模态大型语言模型（MLLM）强大的视觉理解能力，并结合手部关键点的先验知识，从而获得对手部质量的强大感知能力。此外，作者还构建了一个人工标注的测试集，包含来自各种最先进（SOTA）T2I模型的手部图像，以验证其质量评估能力。结果表明，HandEval比现有的SOTA方法更符合人类判断。HandEval被集成到图像生成和AIGC检测流程中，显著提高了生成手部的真实感和检测精度，证实了其在下游应用中的普遍有效性。代码和数据集将会开源。

## 🔬 方法详解

**问题定义**：当前文图生成模型在生成手部等复杂局部区域时，细节质量较差，容易出现结构扭曲和纹理不真实的问题。现有的质量评估方法通常关注整体图像质量，忽略了对手部等特定区域的评估，缺乏针对性，无法有效指导生成模型的优化和AIGC检测。

**核心思路**：论文的核心思路是构建一个专门针对生成手部区域的质量评估模型HandEval。该模型通过结合多模态大语言模型的视觉理解能力和手部关键点的先验知识，从而能够更准确地判断生成手部的质量。

**技术框架**：HandEval的技术框架主要包括以下几个部分：1）HandPair数据集的构建，用于训练质量评估模型；2）HandEval模型的构建，利用MLLM和手部关键点信息进行质量评估；3）人工标注的测试集的构建，用于验证HandEval的性能；4）将HandEval集成到图像生成和AIGC检测流程中，验证其在下游应用中的有效性。

**关键创新**：HandEval的关键创新在于：1）首次提出了针对生成手部区域的质量评估任务；2）构建了HandPair数据集，无需手动标注即可实现低成本、高效的监督学习；3）将多模态大语言模型和手部关键点信息相结合，提高了手部质量评估的准确性。

**关键设计**：HandEval的关键设计包括：1）HandPair数据集的构建方式，通过高质量和低质量手部图像对来提供监督信号；2）MLLM的选择和使用，如何利用MLLM的视觉理解能力来提取手部特征；3）手部关键点信息的融合方式，如何将关键点信息融入到质量评估过程中；4）损失函数的设计，如何训练HandEval模型使其能够准确地判断手部质量。

## 📊 实验亮点

实验结果表明，HandEval在手部质量评估方面与人类判断的对齐程度优于现有的SOTA方法。将HandEval集成到图像生成流程中，可以显著提高生成手部的真实感。在AIGC检测任务中，HandEval的加入也显著提高了检测精度，验证了其在下游应用中的有效性。具体性能数据（例如，与人类判断的对齐程度提升百分比，AIGC检测精度提升百分比）需要在论文中查找。

## 🎯 应用场景

该研究成果可广泛应用于AIGC领域，例如：提升文图生成模型生成手部的真实感，优化人像生成质量；提高AIGC检测的准确率，有效识别AI生成内容；辅助手部相关的医疗诊断，例如评估手部畸形程度；以及在虚拟现实和增强现实应用中，提升手部交互的真实感和用户体验。

## 📄 摘要（原文）

> Although recent text-to-image (T2I) models have significantly improved the overall visual quality of generated images, they still struggle in the generation of accurate details in complex local regions, especially human hands. Generated hands often exhibit structural distortions and unrealistic textures, which can be very noticeable even when the rest of the body is well-generated. However, the quality assessment of hand regions remains largely neglected, limiting downstream task performance like human-centric generation quality optimization and AIGC detection. To address this, we propose the first quality assessment task targeting generated hand regions and showcase its abundant downstream applications. We first introduce the HandPair dataset for training hand quality assessment models. It consists of 48k images formed by high- and low-quality hand pairs, enabling low-cost, efficient supervision without manual annotation. Based on it, we develop HandEval, a carefully designed hand-specific quality assessment model. It leverages the powerful visual understanding capability of Multimodal Large Language Model (MLLM) and incorporates prior knowledge of hand keypoints, gaining strong perception of hand quality. We further construct a human-annotated test set with hand images from various state-of-the-art (SOTA) T2I models to validate its quality evaluation capability. Results show that HandEval aligns better with human judgments than existing SOTA methods. Furthermore, we integrate HandEval into image generation and AIGC detection pipelines, prominently enhancing generated hand realism and detection accuracy, respectively, confirming its universal effectiveness in downstream applications. Code and dataset will be available.

