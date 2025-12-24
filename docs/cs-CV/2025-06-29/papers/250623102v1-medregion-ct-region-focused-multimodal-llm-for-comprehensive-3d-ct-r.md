---
layout: default
title: "MedRegion-CT: Region-Focused Multimodal LLM for Comprehensive 3D CT Report Generation"
---

# MedRegion-CT: Region-Focused Multimodal LLM for Comprehensive 3D CT Report Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23102" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23102v1</a>
  <a href="https://arxiv.org/pdf/2506.23102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23102v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23102v1', 'MedRegion-CT: Region-Focused Multimodal LLM for Comprehensive 3D CT Report Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sunggu Kyung, Jinyoung Seo, Hyunseok Lim, Dongyeong Kim, Hyungbin Park, Jimin Sung, Jihyun Kim, Wooyoung Jo, Yoojin Nam, Namkug Kim

**分类**: eess.IV, cs.CV

**发布日期**: 2025-06-29

**备注**: 14 pages, 5 figures, submitted to ICCV 2025

---

## 💡 一句话要点

**提出MedRegion-CT以解决CT报告生成中的区域特征捕捉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `CT报告生成` `区域特征提取` `医学影像分析` `临床决策支持`

## 📋 核心要点

1. 现有CT报告生成方法主要关注全局特征，难以捕捉区域特定的细节，导致某些临床异常未被识别。
2. 提出MedRegion-CT框架，通过区域代表Token池化、伪掩膜生成和患者特定属性提取，增强模型对区域特征的理解。
3. 在RadGenome-Chest CT基准测试中，MedRegion-CT在自然语言生成质量和临床相关性上实现了领先性能，超越了现有技术。

## 📝 摘要（中文）

最近发布的RadGenome-Chest CT显著推动了基于CT的报告生成。然而，现有方法主要关注全局特征，难以捕捉区域特定细节，可能导致某些异常未被发现。为此，我们提出了MedRegion-CT，一个区域聚焦的多模态大语言模型框架，具有三项关键创新。首先，引入区域代表（$R^2$）Token池化，利用2D预训练视觉模型高效提取3D CT特征。其次，通用分割模型生成伪掩膜，经过掩膜编码器提取区域中心特征。最后，利用分割结果提取患者特定属性，丰富模型对患者背景的理解。通过在RadGenome-Chest CT上进行基准实验，MedRegion-CT在自然语言生成质量和临床相关性方面超越了现有方法，同时保持了解释性。我们的框架代码已公开。

## 🔬 方法详解

**问题定义**：现有CT报告生成方法在处理区域特征时存在不足，主要集中于全局特征，导致区域特定的异常难以识别。

**核心思路**：MedRegion-CT通过区域代表Token池化和伪掩膜生成，聚焦于临床相关区域，提升报告生成的准确性和细致度。

**技术框架**：该框架包括三个主要模块：区域代表Token池化模块、伪掩膜生成模块和患者特定属性提取模块，整体流程为先提取3D特征，再生成区域特征，最后结合患者背景生成报告。

**关键创新**：引入区域代表Token池化和伪掩膜生成技术，使得模型能够有效提取区域特征，与传统方法相比，显著提升了对细节的捕捉能力。

**关键设计**：采用2D预训练视觉模型进行特征提取，使用六个预定义区域掩膜进行分割，并将患者特定的属性（如器官大小、直径和位置）转化为文本提示，增强模型的上下文理解能力。

## 📊 实验亮点

在RadGenome-Chest CT的基准实验中，MedRegion-CT在自然语言生成质量和临床相关性方面达到了最先进的性能，超越了现有方法，具体提升幅度未知，且保持了良好的模型解释性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、临床决策支持和自动化报告生成。通过提高CT报告的准确性和细致度，MedRegion-CT可为医生提供更可靠的诊断依据，进而提升患者护理质量。未来，该技术有望扩展到其他医学影像类型的报告生成中。

## 📄 摘要（原文）

> The recent release of RadGenome-Chest CT has significantly advanced CT-based report generation. However, existing methods primarily focus on global features, making it challenging to capture region-specific details, which may cause certain abnormalities to go unnoticed. To address this, we propose MedRegion-CT, a region-focused Multi-Modal Large Language Model (MLLM) framework, featuring three key innovations. First, we introduce Region Representative ($R^2$) Token Pooling, which utilizes a 2D-wise pretrained vision model to efficiently extract 3D CT features. This approach generates global tokens representing overall slice features and region tokens highlighting target areas, enabling the MLLM to process comprehensive information effectively. Second, a universal segmentation model generates pseudo-masks, which are then processed by a mask encoder to extract region-centric features. This allows the MLLM to focus on clinically relevant regions, using six predefined region masks. Third, we leverage segmentation results to extract patient-specific attributions, including organ size, diameter, and locations. These are converted into text prompts, enriching the MLLM's understanding of patient-specific contexts. To ensure rigorous evaluation, we conducted benchmark experiments on report generation using the RadGenome-Chest CT. MedRegion-CT achieved state-of-the-art performance, outperforming existing methods in natural language generation quality and clinical relevance while maintaining interpretability. The code for our framework is publicly available.

