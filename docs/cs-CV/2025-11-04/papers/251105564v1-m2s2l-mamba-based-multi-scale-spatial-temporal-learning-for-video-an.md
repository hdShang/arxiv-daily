---
layout: default
title: "M2S2L: Mamba-based Multi-Scale Spatial-temporal Learning for Video Anomaly Detection"
---

# M2S2L: Mamba-based Multi-Scale Spatial-temporal Learning for Video Anomaly Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.05564" class="toolbar-btn" target="_blank">📄 arXiv: 2511.05564v1</a>
  <a href="https://arxiv.org/pdf/2511.05564.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05564v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.05564v1', 'M2S2L: Mamba-based Multi-Scale Spatial-temporal Learning for Video Anomaly Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Liu, Boan Chen, Xiaoguang Zhu, Jing Liu, Peng Sun, Wei Zhou

**分类**: cs.CV

**发布日期**: 2025-11-04

**备注**: IEEE VCIP 2025

---

## 💡 一句话要点

**提出基于Mamba的多尺度时空学习框架M2S2L，用于提升视频异常检测的精度和效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频异常检测` `Mamba` `多尺度学习` `时空建模` `特征分解` `视频监控` `序列建模`

## 📋 核心要点

1. 现有视频异常检测方法难以兼顾复杂场景下的检测精度和实时性需求，缺乏有效的时空建模能力。
2. M2S2L框架利用Mamba架构，通过多尺度空间编码和多时间尺度运动建模，实现更全面的时空特征提取。
3. 实验结果表明，M2S2L在多个基准数据集上取得了优异的异常检测性能，并保持了较高的推理速度。

## 📝 摘要（中文）

视频异常检测(VAD)是图像处理领域的一项重要任务，在视频监控方面具有广阔前景，但其在检测精度和计算效率之间取得平衡面临着根本性挑战。随着视频内容日益复杂，行为模式和上下文场景多样化，传统的VAD方法难以对现代监控系统提供稳健的评估。现有方法要么缺乏全面的时空建模，要么需要过多的计算资源才能实现实时应用。为此，本文提出了一种基于Mamba的多尺度时空学习(M2S2L)框架。该方法采用在多个粒度上运行的分层空间编码器和跨不同时间尺度捕获运动动态的多时间编码器。我们还引入了一种特征分解机制，以实现针对外观和运动重建的任务特定优化，从而促进更细致的行为建模和质量感知的异常评估。在三个基准数据集上的实验表明，M2S2L框架在UCSD Ped2、CUHK Avenue和ShanghaiTech上分别实现了98.5%、92.1%和77.9%的帧级别AUC，同时保持了20.1G FLOPs的效率和45 FPS的推理速度，使其适用于实际的监控部署。

## 🔬 方法详解

**问题定义**：视频异常检测旨在识别视频序列中与正常模式显著不同的事件。现有方法通常难以在复杂场景下进行精确的时空建模，导致检测精度下降。同时，一些方法计算复杂度高，难以满足实时性要求，限制了实际应用。

**核心思路**：M2S2L的核心在于利用Mamba架构强大的序列建模能力，同时结合多尺度空间信息和多时间尺度运动信息，从而更全面地捕捉视频中的异常行为。通过特征分解机制，针对外观和运动进行任务特定的优化，进一步提升检测精度。

**技术框架**：M2S2L框架主要包含以下几个模块：1) 多尺度空间编码器：采用分层结构，在不同粒度上提取空间特征。2) 多时间尺度运动编码器：捕捉不同时间跨度的运动动态。3) 特征分解模块：将特征分解为外观和运动分量，分别进行重建。4) 异常评分模块：基于重建误差评估异常程度。

**关键创新**：M2S2L的关键创新在于将Mamba架构引入视频异常检测领域，并结合多尺度时空建模和特征分解机制。与传统的基于CNN或RNN的方法相比，Mamba具有更强的序列建模能力和更高的计算效率，能够更好地捕捉视频中的长程依赖关系。

**关键设计**：多尺度空间编码器采用卷积神经网络实现，不同层级的卷积核大小和步长不同，以提取不同尺度的空间特征。多时间尺度运动编码器采用Mamba架构实现，通过调整状态空间模型的参数，捕捉不同时间跨度的运动信息。特征分解模块采用线性变换实现，将特征分解为外观和运动分量。异常评分模块采用重建误差作为异常指标，通过设定阈值判断是否为异常事件。

## 📊 实验亮点

M2S2L框架在三个基准数据集上取得了显著的性能提升。在UCSD Ped2数据集上，帧级别AUC达到了98.5%；在CUHK Avenue数据集上，达到了92.1%；在ShanghaiTech数据集上，达到了77.9%。同时，该方法保持了较高的推理速度，达到了45 FPS，计算复杂度为20.1G FLOPs，优于许多现有方法。

## 🎯 应用场景

该研究成果可广泛应用于智能视频监控领域，例如公共安全、交通管理、工业生产等。通过实时检测异常事件，可以及时预警和采取措施，有效降低安全风险和损失。未来，该方法还可以扩展到其他视频分析任务，如行为识别、事件检测等。

## 📄 摘要（原文）

> Video anomaly detection (VAD) is an essential task in the image processing community with prospects in video surveillance, which faces fundamental challenges in balancing detection accuracy with computational efficiency. As video content becomes increasingly complex with diverse behavioral patterns and contextual scenarios, traditional VAD approaches struggle to provide robust assessment for modern surveillance systems. Existing methods either lack comprehensive spatial-temporal modeling or require excessive computational resources for real-time applications. In this regard, we present a Mamba-based multi-scale spatial-temporal learning (M2S2L) framework in this paper. The proposed method employs hierarchical spatial encoders operating at multiple granularities and multi-temporal encoders capturing motion dynamics across different time scales. We also introduce a feature decomposition mechanism to enable task-specific optimization for appearance and motion reconstruction, facilitating more nuanced behavioral modeling and quality-aware anomaly assessment. Experiments on three benchmark datasets demonstrate that M2S2L framework achieves 98.5%, 92.1%, and 77.9% frame-level AUCs on UCSD Ped2, CUHK Avenue, and ShanghaiTech respectively, while maintaining efficiency with 20.1G FLOPs and 45 FPS inference speed, making it suitable for practical surveillance deployment.

