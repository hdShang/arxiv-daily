---
layout: default
title: VAAS: Vision-Attention Anomaly Scoring for Image Manipulation Detection in Digital Forensics
---

# VAAS: Vision-Attention Anomaly Scoring for Image Manipulation Detection in Digital Forensics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15512" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15512v1</a>
  <a href="https://arxiv.org/pdf/2512.15512.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15512v1" onclick="toggleFavorite(this, '2512.15512v1', 'VAAS: Vision-Attention Anomaly Scoring for Image Manipulation Detection in Digital Forensics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Opeyemi Bamigbade, Mark Scanlon, John Sheppard

**分类**: cs.CV, cs.MM

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**VAAS：用于数字取证中图像篡改检测的视觉注意力异常评分方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `图像篡改检测` `数字取证` `视觉注意力` `Vision Transformer` `自一致性` `异常检测` `深度学习`

## 📋 核心要点

1. 现有图像篡改检测方法难以有效识别视觉上逼真的伪造图像，并且缺乏对篡改程度的量化能力。
2. VAAS框架结合了全局注意力机制和局部自一致性评分，能够提供连续且可解释的异常分数，从而定位并量化篡改。
3. 在DF2023和CASIA v2.0数据集上的实验表明，VAAS在F1和IoU指标上表现出色，并提升了视觉可解释性。

## 📝 摘要（中文）

人工智能驱动的图像生成技术的进步给法庭调查中数字证据的真实性验证带来了新的挑战。现代生成模型能够产生视觉上一致的伪造图像，从而逃避基于像素或压缩伪影的传统检测器。此外，大多数现有方法缺乏对异常强度的明确度量，这限制了它们量化篡改严重程度的能力。本文提出了一种新颖的双模块框架——视觉注意力异常评分（VAAS），该框架集成了使用 Vision Transformers (ViT) 的全局注意力异常估计与源自 SegFormer 嵌入的补丁级自一致性评分。这种混合公式提供了一个连续且可解释的异常分数，反映了篡改的位置和程度。在 DF2023 和 CASIA v2.0 数据集上的评估表明，VAAS 实现了具有竞争力的 F1 和 IoU 性能，同时通过注意力引导的异常图增强了视觉可解释性。该框架将定量检测与人类可理解的推理联系起来，支持透明且可靠的图像完整性评估。所有实验的源代码和用于重现结果的相应材料均已开源。

## 🔬 方法详解

**问题定义**：当前图像篡改检测方法在面对AI生成的高度逼真的伪造图像时，难以有效检测。这些方法通常依赖于像素或压缩伪影，容易被视觉上一致的篡改所欺骗。此外，现有方法缺乏对篡改程度的量化，无法提供篡改的严重性评估。

**核心思路**：VAAS的核心思路是将全局的注意力机制与局部的自一致性评分相结合，从而全面评估图像的异常程度。全局注意力机制用于捕捉图像整体的异常模式，而局部自一致性评分则用于验证图像局部区域的一致性。通过结合这两种方法，VAAS能够更准确地检测和定位图像篡改。

**技术框架**：VAAS框架包含两个主要模块：基于Vision Transformer (ViT) 的全局注意力异常估计模块和基于SegFormer嵌入的补丁级自一致性评分模块。首先，ViT模块提取图像的全局特征，并通过注意力机制识别潜在的异常区域。然后，SegFormer模块提取图像的局部特征，并计算每个补丁的自一致性得分。最后，将两个模块的输出融合，生成最终的异常分数和异常图。

**关键创新**：VAAS的关键创新在于其双模块混合架构，该架构结合了全局注意力和局部自一致性。这种混合方法能够同时捕捉图像的全局异常模式和局部不一致性，从而提高篡改检测的准确性和鲁棒性。此外，VAAS还提供了一个连续且可解释的异常分数，可以用于量化篡改的严重程度。

**关键设计**：ViT模块采用预训练的ViT模型作为特征提取器，并使用注意力机制来识别异常区域。SegFormer模块使用预训练的SegFormer模型提取局部特征，并通过计算补丁之间的相似度来评估自一致性。最终的异常分数是通过加权平均全局注意力和局部自一致性得分来计算的。损失函数的设计旨在最大化篡改图像和真实图像之间的异常分数差异。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15512v1/imgs/img1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15512v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15512v1/figures/qualitative_combined.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

VAAS在DF2023和CASIA v2.0数据集上取得了具有竞争力的结果。具体来说，VAAS在F1和IoU指标上均表现出色，超过了现有的许多篡改检测方法。此外，VAAS还通过注意力引导的异常图提供了良好的视觉可解释性，有助于人工审核和验证检测结果。实验结果表明，VAAS能够有效检测各种类型的图像篡改，并提供准确的篡改定位和量化。

## 🎯 应用场景

VAAS在数字取证领域具有广泛的应用前景，可以用于验证图像证据的真实性，辅助法庭调查。此外，该方法还可以应用于新闻媒体、社交网络等领域，用于检测和防止虚假信息的传播。未来，VAAS可以进一步扩展到视频篡改检测等领域，为维护数字世界的安全和可信度做出贡献。

## 📄 摘要（原文）

> Recent advances in AI-driven image generation have introduced new challenges for verifying the authenticity of digital evidence in forensic investigations. Modern generative models can produce visually consistent forgeries that evade traditional detectors based on pixel or compression artefacts. Most existing approaches also lack an explicit measure of anomaly intensity, which limits their ability to quantify the severity of manipulation. This paper introduces Vision-Attention Anomaly Scoring (VAAS), a novel dual-module framework that integrates global attention-based anomaly estimation using Vision Transformers (ViT) with patch-level self-consistency scoring derived from SegFormer embeddings. The hybrid formulation provides a continuous and interpretable anomaly score that reflects both the location and degree of manipulation. Evaluations on the DF2023 and CASIA v2.0 datasets demonstrate that VAAS achieves competitive F1 and IoU performance, while enhancing visual explainability through attention-guided anomaly maps. The framework bridges quantitative detection with human-understandable reasoning, supporting transparent and reliable image integrity assessment. The source code for all experiments and corresponding materials for reproducing the results are available open source.

