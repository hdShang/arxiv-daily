---
layout: default
title: Any-Optical-Model: A Universal Foundation Model for Optical Remote Sensing
---

# Any-Optical-Model: A Universal Foundation Model for Optical Remote Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17224" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17224v1</a>
  <a href="https://arxiv.org/pdf/2512.17224.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17224v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17224v1', 'Any-Optical-Model: A Universal Foundation Model for Optical Remote Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuyang Li, Chenyu Li, Danfeng Hong

**分类**: cs.CV

**发布日期**: 2025-12-19

**备注**: Accepted by AAAI2026

---

## 💡 一句话要点

**提出Any-Optical-Model，解决遥感领域跨传感器、分辨率和缺失波段的通用性难题。**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感基础模型` `跨传感器` `多分辨率` `波段缺失` `自监督学习`

## 📋 核心要点

1. 现有遥感基础模型难以处理不同传感器、分辨率和缺失波段带来的挑战，限制了其泛化能力和实际应用。
2. Any-Optical-Model (AOM) 通过频谱独立tokenizer、多尺度自适应patch嵌入和语义对齐机制，实现对任意波段、传感器和分辨率的通用适应。
3. 在多个数据集上的实验表明，AOM 在波段缺失、跨传感器和跨分辨率等场景下均取得了 SOTA 性能。

## 📝 摘要（中文）

光学卫星凭借其多样的波段布局和地面采样距离，为生态系统监测到应急响应等任务提供了不可或缺的证据。然而，不同光学传感器在波段组成和空间分辨率上的显著差异，对现有的遥感基础模型(RSFM)提出了重大挑战。这些模型通常在固定的波段配置和分辨率上进行预训练，使其容易受到涉及缺失波段、跨传感器融合和未见空间尺度的真实场景的影响，从而限制了其泛化能力和实际部署。为了解决这些限制，我们提出了Any Optical Model (AOM)，一个通用RSFM，专门设计用于适应任意波段组成、传感器类型和分辨率尺度。为了在波段缺失或新引入时保持独特的频谱特征，AOM引入了一种频谱独立的tokenizer，为每个通道分配一个专用的波段嵌入，从而能够显式地编码频谱身份。为了有效地捕获从亚米级到百米级图像的纹理和上下文模式，我们设计了一种多尺度自适应patch嵌入机制，动态地调节感受野。此外，为了保持跨不同分辨率的全局语义一致性，AOM结合了一种多尺度语义对齐机制，以及一种通道级的自监督掩码和重建预训练策略，该策略联合建模了光谱-空间关系。在包括Sentinel-2、Landsat和HLS在内的10多个公共数据集上进行的大量实验表明，AOM在诸如波段缺失、跨传感器和跨分辨率设置等具有挑战性的条件下，始终如一地实现了最先进(SOTA)的性能。

## 🔬 方法详解

**问题定义**：现有遥感基础模型通常针对特定传感器和分辨率进行预训练，难以处理实际应用中常见的波段缺失、跨传感器数据融合以及不同分辨率图像分析等问题。这些问题严重限制了模型的泛化能力和实际部署价值。

**核心思路**：AOM的核心思路是设计一个通用的遥感基础模型，使其能够适应任意波段组成、传感器类型和分辨率尺度。通过显式编码波段身份、动态调节感受野以及多尺度语义对齐，模型能够有效提取和利用不同来源遥感数据的光谱和空间信息。

**技术框架**：AOM的整体框架包括以下几个主要模块：1) 频谱独立Tokenizer：为每个通道分配一个独立的波段嵌入，显式编码光谱身份。2) 多尺度自适应Patch嵌入：动态调节感受野，捕获不同分辨率图像的纹理和上下文信息。3) 多尺度语义对齐：保持跨不同分辨率的全局语义一致性。4) 通道级自监督掩码和重建预训练：联合建模光谱-空间关系。

**关键创新**：AOM最重要的技术创新在于其通用性设计，能够有效解决现有遥感基础模型在处理异构遥感数据时面临的挑战。与现有方法相比，AOM不再依赖于特定的波段配置和分辨率，而是能够自适应地处理各种类型的遥感数据。

**关键设计**：AOM的关键设计包括：1) 频谱独立Tokenizer的具体实现方式，例如使用可学习的嵌入向量表示每个波段。2) 多尺度自适应Patch嵌入的动态感受野调节策略，例如使用注意力机制或可变形卷积。3) 多尺度语义对齐的具体方法，例如使用对比学习或知识蒸馏。4) 自监督预训练的掩码策略和重建目标，例如随机掩盖部分通道并预测原始值。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17224v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17224v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17224v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AOM 在包括 Sentinel-2、Landsat 和 HLS 在内的 10 多个公共数据集上进行了广泛的实验，结果表明 AOM 在波段缺失、跨传感器和跨分辨率等具有挑战性的条件下，始终如一地实现了 SOTA 性能。具体性能数据和提升幅度在论文中进行了详细的展示。

## 🎯 应用场景

Any-Optical-Model (AOM) 具有广泛的应用前景，可用于生态环境监测、自然灾害评估、城市规划、农业估产等领域。其通用性设计使其能够有效整合来自不同传感器和分辨率的遥感数据，为决策提供更全面和准确的信息支持，加速遥感技术在各行业的落地应用。

## 📄 摘要（原文）

> Optical satellites, with their diverse band layouts and ground sampling distances, supply indispensable evidence for tasks ranging from ecosystem surveillance to emergency response. However, significant discrepancies in band composition and spatial resolution across different optical sensors present major challenges for existing Remote Sensing Foundation Models (RSFMs). These models are typically pretrained on fixed band configurations and resolutions, making them vulnerable to real world scenarios involving missing bands, cross sensor fusion, and unseen spatial scales, thereby limiting their generalization and practical deployment. To address these limitations, we propose Any Optical Model (AOM), a universal RSFM explicitly designed to accommodate arbitrary band compositions, sensor types, and resolution scales. To preserve distinctive spectral characteristics even when bands are missing or newly introduced, AOM introduces a spectrum-independent tokenizer that assigns each channel a dedicated band embedding, enabling explicit encoding of spectral identity. To effectively capture texture and contextual patterns from sub-meter to hundred-meter imagery, we design a multi-scale adaptive patch embedding mechanism that dynamically modulates the receptive field. Furthermore, to maintain global semantic consistency across varying resolutions, AOM incorporates a multi-scale semantic alignment mechanism alongside a channel-wise self-supervised masking and reconstruction pretraining strategy that jointly models spectral-spatial relationships. Extensive experiments on over 10 public datasets, including those from Sentinel-2, Landsat, and HLS, demonstrate that AOM consistently achieves state-of-the-art (SOTA) performance under challenging conditions such as band missing, cross sensor, and cross resolution settings.

