---
layout: default
title: "HQ-OV3D: A High Box Quality Open-World 3D Detection Framework based on Diffision Model"
---

# HQ-OV3D: A High Box Quality Open-World 3D Detection Framework based on Diffision Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10935" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10935v2</a>
  <a href="https://arxiv.org/pdf/2508.10935.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10935v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10935v2', 'HQ-OV3D: A High Box Quality Open-World 3D Detection Framework based on Diffision Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Liu, Yabei Li, Hongsong Wang, Lei He

**分类**: cs.CV, cs.LG, cs.RO

**发布日期**: 2025-08-12 (更新: 2025-08-18)

---

## 💡 一句话要点

**提出HQ-OV3D以解决开放世界3D检测中的伪标签质量问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `开放世界检测` `3D检测` `伪标签生成` `几何一致性` `视觉语言模型`

## 📋 核心要点

1. 现有的开放词汇3D检测方法在几何质量，尤其是边界框精度方面存在不足，影响了检测性能。
2. 本文提出HQ-OV3D框架，通过IMCV提案生成器和ACA去噪器生成和优化高质量伪标签，提升检测精度。
3. 实验结果表明，HQ-OV3D在新类别上实现了7.37%的mAP提升，显示出其伪标签生成的优越性。

## 📝 摘要（中文）

传统的闭集3D检测框架无法满足自动驾驶等开放世界应用的需求。现有的开放词汇3D检测方法通常采用伪标签生成和语义对齐的两阶段流程。尽管视觉语言模型（VLMs）在伪标签的语义准确性上取得了显著进展，但其几何质量，特别是边界框的精度，仍然被普遍忽视。为了解决这一问题，本文提出了高边框质量开放词汇3D检测框架HQ-OV3D，旨在为开放词汇类别生成和优化高质量的伪标签。该框架包括两个关键组件：利用跨模态几何一致性生成高质量初始3D提案的IMCV提案生成器，以及通过基于DDIM的去噪机制逐步优化3D提案的ACA去噪器。与最先进的方法相比，使用我们的方法生成的伪标签进行训练在新类别上实现了7.37%的mAP提升，展示了我们框架生成的伪标签的优越质量。

## 🔬 方法详解

**问题定义**：本文旨在解决开放世界3D检测中伪标签的几何质量不足问题，现有方法往往忽视边界框的精度，导致检测效果不佳。

**核心思路**：HQ-OV3D框架通过引入IMCV提案生成器和ACA去噪器，利用跨模态几何一致性和注释类别的几何先验，生成和优化高质量的伪标签，从而提升检测性能。

**技术框架**：HQ-OV3D框架主要包括两个模块：IMCV提案生成器负责生成初始3D提案，ACA去噪器则通过去噪机制逐步优化这些提案，确保最终伪标签的高质量。

**关键创新**：本研究的创新点在于通过IMCV和ACA的结合，显著提升了伪标签的几何质量，区别于传统方法仅关注语义准确性。

**关键设计**：在IMCV提案生成器中，采用了跨模态几何一致性作为生成依据；在ACA去噪器中，利用DDIM机制进行去噪，结合注释类别的几何先验进行优化。具体的损失函数和网络结构设计尚未详细披露。

## 📊 实验亮点

实验结果显示，HQ-OV3D在新类别上实现了7.37%的mAP提升，相较于最先进的方法，展示了伪标签生成的显著优势，证明了其在开放词汇3D检测中的有效性。

## 🎯 应用场景

HQ-OV3D框架在自动驾驶、机器人导航等开放世界应用中具有广泛的潜在应用价值。通过生成高质量的伪标签，该框架能够提升3D检测系统的整体性能，推动相关领域的技术进步和应用落地。

## 📄 摘要（原文）

> Traditional closed-set 3D detection frameworks fail to meet the demands of open-world applications like autonomous driving. Existing open-vocabulary 3D detection methods typically adopt a two-stage pipeline consisting of pseudo-label generation followed by semantic alignment. While vision-language models (VLMs) recently have dramatically improved the semantic accuracy of pseudo-labels, their geometric quality, particularly bounding box precision, remains commonly neglected. To address this issue, we propose a High Box Quality Open-Vocabulary 3D Detection (HQ-OV3D) framework, dedicated to generate and refine high-quality pseudo-labels for open-vocabulary classes. The framework comprises two key components: an Intra-Modality Cross-Validated (IMCV) Proposal Generator that utilizes cross-modality geometric consistency to generate high-quality initial 3D proposals, and an Annotated-Class Assisted (ACA) Denoiser that progressively refines 3D proposals by leveraging geometric priors from annotated categories through a DDIM-based denoising mechanism. Compared to the state-of-the-art method, training with pseudo-labels generated by our approach achieves a 7.37% improvement in mAP on novel classes, demonstrating the superior quality of the pseudo-labels produced by our framework. HQ-OV3D can serve not only as a strong standalone open-vocabulary 3D detector but also as a plug-in high-quality pseudo-label generator for existing open-vocabulary detection or annotation pipelines.

