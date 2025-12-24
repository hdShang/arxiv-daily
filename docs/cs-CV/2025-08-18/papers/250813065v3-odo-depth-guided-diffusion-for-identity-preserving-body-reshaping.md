---
layout: default
title: "Odo: Depth-Guided Diffusion for Identity-Preserving Body Reshaping"
---

# Odo: Depth-Guided Diffusion for Identity-Preserving Body Reshaping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13065" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13065v3</a>
  <a href="https://arxiv.org/pdf/2508.13065.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13065v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13065v3', 'Odo: Depth-Guided Diffusion for Identity-Preserving Body Reshaping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siddharth Khandelwal, Sridhar Kamath, Arjun Jain

**分类**: cs.CV

**发布日期**: 2025-08-18 (更新: 2025-09-25)

---

## 💡 一句话要点

**提出Odo以解决人形编辑中的形状保留问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `人形编辑` `深度学习` `扩散模型` `3D重塑` `计算机视觉` `虚拟现实` `图像处理`

## 📋 核心要点

1. 现有的人形编辑方法多依赖于3D模型或图像扭曲，导致不自然的身体比例和纹理失真。
2. 本文提出Odo，一个基于扩散的端到端方法，结合冻结的UNet和ControlNet，实现真实的身体重塑。
3. 实验结果显示，Odo在每个顶点重建误差上达到7.5mm，显著优于基线方法的13.6mm，效果更加真实。

## 📝 摘要（中文）

人形编辑允许对个体体型进行可控变换，如瘦、肌肉发达或超重，同时保持姿势、身份、服装和背景。与快速发展的姿势编辑相比，形状编辑仍相对未被充分探索。现有方法通常依赖于3D可变形模型或图像扭曲，常引入不现实的身体比例、纹理失真和背景不一致等问题。本文首次引入一个包含18,573张图像的大规模数据集，专为受控人形编辑设计。基于该数据集，我们提出了Odo，一个基于扩散的端到端方法，能够通过简单的语义属性实现真实且直观的身体重塑。实验表明，我们的方法在每个顶点重建误差上达到7.5mm，显著低于基线方法的13.6mm，同时生成的结果真实且准确匹配目标形状。

## 🔬 方法详解

**问题定义**：本文旨在解决人形编辑中形状保留的问题，现有方法常引入不自然的身体比例和纹理失真，缺乏大规模公开数据集以支持训练和评估。

**核心思路**：Odo方法通过结合冻结的UNet和ControlNet，利用目标SMPL深度图引导形状变换，从而实现更为真实和直观的身体重塑。

**技术框架**：整体架构包括两个主要模块：冻结的UNet用于保留输入图像的细节，ControlNet则负责根据深度图引导形状变换。

**关键创新**：Odo的核心创新在于其扩散基础的设计，能够在保持身份和背景一致性的同时，实现灵活的体型变换，这与传统方法显著不同。

**关键设计**：在网络结构上，采用了冻结的UNet以确保细节保留，同时使用了特定的损失函数来优化形状重塑的准确性，确保生成结果的真实感。

## 📊 实验亮点

Odo方法在每个顶点重建误差上达到7.5mm，显著低于基线方法的13.6mm，展示了其在形状重塑中的优越性能。实验结果表明，该方法生成的结果更为真实，能够准确匹配目标形状，显示出良好的应用前景。

## 🎯 应用场景

该研究在虚拟现实、游戏开发和个性化时尚等领域具有广泛的应用潜力。通过实现真实的身体形状编辑，用户可以在数字环境中更好地表达自我，提升交互体验。此外，该技术也可用于医学图像分析和个性化健身指导等场景，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Human shape editing enables controllable transformation of a person's body shape, such as thin, muscular, or overweight, while preserving pose, identity, clothing, and background. Unlike human pose editing, which has advanced rapidly, shape editing remains relatively under-explored. Current approaches typically rely on 3D morphable models or image warping, often introducing unrealistic body proportions, texture distortions, and background inconsistencies due to alignment errors and deformations. A key limitation is the lack of large-scale, publicly available datasets for training and evaluating body shape manipulation methods. In this work, we introduce the first large-scale dataset of 18,573 images across 1523 subjects, specifically designed for controlled human shape editing. It features diverse variations in body shape, including fat, muscular and thin, captured under consistent identity, clothing, and background conditions. Using this dataset, we propose Odo, an end-to-end diffusion-based method that enables realistic and intuitive body reshaping guided by simple semantic attributes. Our approach combines a frozen UNet that preserves fine-grained appearance and background details from the input image with a ControlNet that guides shape transformation using target SMPL depth maps. Extensive experiments demonstrate that our method outperforms prior approaches, achieving per-vertex reconstruction errors as low as 7.5mm, significantly lower than the 13.6mm observed in baseline methods, while producing realistic results that accurately match the desired target shapes.

