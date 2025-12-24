---
layout: default
title: "MESTI-MEGANet: Micro-expression Spatio-Temporal Image and Micro-expression Gradient Attention Networks for Micro-expression Recognition"
---

# MESTI-MEGANet: Micro-expression Spatio-Temporal Image and Micro-expression Gradient Attention Networks for Micro-expression Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00056" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00056v2</a>
  <a href="https://arxiv.org/pdf/2509.00056.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00056v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00056v2', 'MESTI-MEGANet: Micro-expression Spatio-Temporal Image and Micro-expression Gradient Attention Networks for Micro-expression Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luu Tu Nguyen, Vu Tram Anh Khuong, Thanh Ha Le, Thi Duyen Ngo

**分类**: cs.CV

**发布日期**: 2025-08-25 (更新: 2025-09-07)

---

## 💡 一句话要点

**提出MESTI-MEGANet以解决微表情识别挑战**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `微表情识别` `时空图像` `梯度注意网络` `特征提取` `深度学习`

## 📋 核心要点

1. 微表情识别面临的核心问题是现有方法无法有效捕捉短暂的面部运动，导致识别性能不佳。
2. 论文提出的MESTI通过将视频序列转化为单幅图像，保留了微表情的关键特征，结合MEGANet增强特征提取。
3. 实验结果显示，MESTI与MEGANet的结合在多个数据集上实现了显著的性能提升，设定了新的识别准确率基准。

## 📝 摘要（中文）

微表情识别（MER）是一项具有挑战性的任务，因其微妙且短暂的特性，传统输入方式如顶点帧、光流和动态图像常常无法充分捕捉这些快速的面部运动，导致性能不佳。本研究提出了微表情时空图像（MESTI），一种新颖的动态输入方式，将视频序列转换为单幅图像，同时保留微运动的基本特征。此外，我们还提出了微表情梯度注意网络（MEGANet），通过引入新颖的梯度注意模块，增强微表情中细粒度运动特征的提取。通过结合MESTI和MEGANet，我们旨在建立更有效的MER方法。实验结果表明，MESTI在与现有输入方式的比较中表现出色，并且在CASMEII和SAMM数据集上，MEGANet的表现达到了最新的技术水平，设定了微表情识别的新基准。

## 🔬 方法详解

**问题定义**：微表情识别的主要挑战在于现有方法如顶点帧和光流无法有效捕捉短暂且微妙的面部运动，导致识别精度低下。

**核心思路**：本研究提出MESTI作为一种新型输入方式，通过将视频序列转换为单幅图像，保留微表情的关键特征；同时，MEGANet通过引入梯度注意模块，增强了对细粒度运动特征的提取能力。

**技术框架**：整体架构包括MESTI模块和MEGANet网络。MESTI负责将视频序列处理为时空图像，MEGANet则在此基础上进行特征提取和分类。

**关键创新**：MESTI作为新输入方式，能够有效捕捉微表情的动态特征；MEGANet的梯度注意模块则是其核心创新，能够更好地关注细节，提升识别性能。

**关键设计**：在网络结构上，MEGANet采用了特定的卷积层和梯度注意机制，损失函数设计为适应微表情特征的提取，确保了模型的高效性和准确性。

## 📊 实验亮点

实验结果表明，MESTI与MEGANet的结合在CASMEII和SAMM数据集上达到了最新的技术水平，识别准确率显著提高，超越了现有的基线方法，设定了新的微表情识别基准。

## 🎯 应用场景

该研究的潜在应用领域包括情感分析、心理健康监测以及人机交互等。通过提高微表情识别的准确性，能够在安全监控、客户服务和医疗诊断等多个领域产生实际价值，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Micro-expression recognition (MER) is a challenging task due to the subtle and fleeting nature of micro-expressions. Traditional input modalities, such as Apex Frame, Optical Flow, and Dynamic Image, often fail to adequately capture these brief facial movements, resulting in suboptimal performance. In this study, we introduce the Micro-expression Spatio-Temporal Image (MESTI), a novel dynamic input modality that transforms a video sequence into a single image while preserving the essential characteristics of micro-movements. Additionally, we present the Micro-expression Gradient Attention Network (MEGANet), which incorporates a novel Gradient Attention block to enhance the extraction of fine-grained motion features from micro-expressions. By combining MESTI and MEGANet, we aim to establish a more effective approach to MER. Extensive experiments were conducted to evaluate the effectiveness of MESTI, comparing it with existing input modalities across three CNN architectures (VGG19, ResNet50, and EfficientNetB0). Moreover, we demonstrate that replacing the input of previously published MER networks with MESTI leads to consistent performance improvements. The performance of MEGANet, both with MESTI and Dynamic Image, is also evaluated, showing that our proposed network achieves state-of-the-art results on the CASMEII and SAMM datasets. The combination of MEGANet and MESTI achieves the highest accuracy reported to date, setting a new benchmark for micro-expression recognition. These findings underscore the potential of MESTI as a superior input modality and MEGANet as an advanced recognition network, paving the way for more effective MER systems in a variety of applications.

