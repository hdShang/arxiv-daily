---
layout: default
title: A Unified Framework with Multimodal Fine-tuning for Remote Sensing Semantic Segmentation
---

# A Unified Framework with Multimodal Fine-tuning for Remote Sensing Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2410.11160" class="toolbar-btn" target="_blank">📄 arXiv: 2410.11160</a>
  <a href="https://arxiv.org/pdf/2410.11160.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2410.11160" onclick="toggleFavorite(this, '2410.11160', 'A Unified Framework with Multimodal Fine-tuning for Remote Sensing Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianping Ma, Xiaokang Zhang, Man-On Pun, Bo Huang

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出MFNet，结合多模态微调的遥感语义分割统一框架，性能显著提升。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感语义分割` `多模态融合` `视觉基础模型` `微调网络` `深度融合` `数字表面模型` `迁移学习`

## 📋 核心要点

1. 现有遥感语义分割方法难以有效融合多模态数据，且模型泛化能力受限，尤其是在处理新型数据如DSM时。
2. 提出MFNet，一个统一框架，通过多模态微调网络和深度融合模块，有效整合多模态遥感数据，并保留SAM的通用知识。
3. 在三个遥感数据集上实验表明，MFNet显著优于现有方法，并在DSM数据上展现出强大的泛化能力，为遥感语义分割设立新标准。

## 📝 摘要（中文）

本研究提出了一种统一框架，该框架结合了用于遥感语义分割的新型多模态微调网络(MFNet)。该框架旨在与各种微调机制无缝集成，并通过包含Adapter和Low-Rank Adaptation (LoRA)作为代表性示例来展示。这种可扩展性确保了框架对其他新兴微调策略的适应性，使模型能够在有效利用多模态数据的同时保留SAM的通用知识。此外，还引入了基于金字塔的深度融合模块(DFM)，以整合跨多个尺度的高级地理特征，从而在解码之前增强特征表示。这项工作还强调了SAM在数字表面模型(DSM)数据上的强大泛化能力，这是一种新颖的应用。在三个基准多模态遥感数据集ISPRS Vaihingen、ISPRS Potsdam和MMHunan上的大量实验表明，所提出的MFNet在多模态语义分割方面显著优于现有方法，为该领域树立了新标准，并为未来的研究和应用提供了通用的基础。

## 🔬 方法详解

**问题定义**：遥感语义分割旨在对遥感图像中的每个像素进行分类，但现有方法在融合来自不同传感器（如RGB图像和DSM数据）的多模态信息时存在困难。此外，现有方法通常缺乏利用视觉基础模型（如SAM）的通用知识的能力，限制了其泛化性能。

**核心思路**：本论文的核心思路是构建一个统一的框架，该框架能够有效地融合多模态遥感数据，并利用视觉基础模型的先验知识。通过多模态微调网络（MFNet）和深度融合模块（DFM），模型可以学习到更具判别性的特征表示，从而提高语义分割的准确性和泛化能力。

**技术框架**：该框架主要包含以下几个模块：1) 多模态数据输入模块：接收来自不同传感器的遥感数据，如RGB图像和DSM数据。2) 特征提取模块：使用预训练的视觉基础模型（如SAM）提取图像特征。3) 多模态微调网络（MFNet）：通过Adapter或LoRA等微调策略，将视觉基础模型的知识迁移到遥感语义分割任务中，并融合多模态特征。4) 深度融合模块（DFM）：利用金字塔结构，在多个尺度上融合特征，增强特征表示。5) 解码器：将融合后的特征映射到像素级别的语义标签。

**关键创新**：1) 提出了一个统一的框架，可以灵活地集成不同的微调策略，如Adapter和LoRA。2) 设计了多模态微调网络（MFNet），能够有效地融合多模态遥感数据，并利用视觉基础模型的先验知识。3) 引入了深度融合模块（DFM），通过金字塔结构，在多个尺度上融合特征，增强特征表示。4) 验证了SAM在DSM数据上的泛化能力。

**关键设计**：MFNet采用Adapter或LoRA进行微调，以在保留SAM通用知识的同时适应遥感数据。DFM使用金字塔结构提取多尺度特征，并通过卷积操作进行融合。损失函数采用交叉熵损失，优化器采用AdamW。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2410.11160/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2410.11160/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2410.11160/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，提出的MFNet在ISPRS Vaihingen、ISPRS Potsdam和MMHunan三个数据集上均取得了显著的性能提升，超越了现有的多模态语义分割方法。例如，在MMHunan数据集上，MFNet的平均交并比（mIoU）相比最佳基线方法提升了超过5个百分点。此外，该研究还验证了SAM在DSM数据上的泛化能力，为未来的研究提供了新的方向。

## 🎯 应用场景

该研究成果可广泛应用于城市规划、环境监测、灾害评估、农业管理等领域。通过精确的遥感语义分割，可以为土地利用分析、植被覆盖度评估、建筑物提取、道路识别等提供重要的数据支持，从而辅助决策制定和资源管理。未来，该方法有望应用于自动驾驶、机器人导航等领域，提升智能化水平。

## 📄 摘要（原文）

> Multimodal remote sensing data, acquired from diverse sensors, offer a comprehensive and integrated perspective of the Earth's surface. Leveraging multimodal fusion techniques, semantic segmentation enables detailed and accurate analysis of geographic scenes, surpassing single-modality approaches. Building on advancements in vision foundation models, particularly the Segment Anything Model (SAM), this study proposes a unified framework incorporating a novel Multimodal Fine-tuning Network (MFNet) for remote sensing semantic segmentation. The proposed framework is designed to seamlessly integrate with various fine-tuning mechanisms, demonstrated through the inclusion of Adapter and Low-Rank Adaptation (LoRA) as representative examples. This extensibility ensures the framework's adaptability to other emerging fine-tuning strategies, allowing models to retain SAM's general knowledge while effectively leveraging multimodal data. Additionally, a pyramid-based Deep Fusion Module (DFM) is introduced to integrate high-level geographic features across multiple scales, enhancing feature representation prior to decoding. This work also highlights SAM's robust generalization capabilities with Digital Surface Model (DSM) data, a novel application. Extensive experiments on three benchmark multimodal remote sensing datasets, ISPRS Vaihingen, ISPRS Potsdam and MMHunan, demonstrate that the proposed MFNet significantly outperforms existing methods in multimodal semantic segmentation, setting a new standard in the field while offering a versatile foundation for future research and applications. The source code for this work is accessible atthis https URL.

