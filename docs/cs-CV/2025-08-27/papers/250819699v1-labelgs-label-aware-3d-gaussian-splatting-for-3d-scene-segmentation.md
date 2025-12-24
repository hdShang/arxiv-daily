---
layout: default
title: "LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation"
---

# LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19699" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19699v1</a>
  <a href="https://arxiv.org/pdf/2508.19699.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19699v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19699v1', 'LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang

**分类**: cs.CV

**发布日期**: 2025-08-27

**备注**: PRCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/garrisonz/LabelGS)

---

## 💡 一句话要点

**提出LabelGS以解决3D场景分割能力不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景分割` `高斯表示` `遮挡分析` `语义掩码` `深度学习` `计算机视觉` `场景理解`

## 📋 核心要点

1. 现有的3D Gaussian Splatting方法缺乏3D分割能力，限制了其在场景理解中的应用。
2. 本文提出LabelGS，通过引入对象标签和遮挡分析模型，增强3D高斯的语义分割能力。
3. 实验表明，LabelGS在3D场景分割任务中表现优异，训练速度提升22倍，效果显著优于Feature-3DGS。

## 📝 摘要（中文）

3D Gaussian Splatting (3DGS)作为一种新兴的3D场景显式表示方法，虽然在高保真重建和高效渲染方面表现出色，但缺乏3D分割能力，限制了其在场景理解任务中的应用。为了解决这一局限性，本文提出了Label-aware 3D Gaussian Splatting (LabelGS)方法，通过引入对象标签增强高斯表示。LabelGS为3D高斯引入了跨视图一致的语义掩码，并采用新颖的遮挡分析模型以避免优化过程中的遮挡过拟合。此外，主高斯标记模型将2D语义先验提升至3D高斯，Gaussian Projection Filter则用于避免高斯标签冲突。实验结果表明，LabelGS在3D场景分割任务中显著优于现有的最先进方法，训练速度相比Feature-3DGS提升了22倍。

## 🔬 方法详解

**问题定义**：本文旨在解决3D Gaussian Splatting在3D场景分割能力不足的问题。现有方法无法有效识别和隔离特定对象组件，限制了其在复杂场景理解中的应用。

**核心思路**：LabelGS通过引入对象标签来增强高斯表示，结合跨视图一致的语义掩码和遮挡分析模型，优化了3D高斯的分割能力。这样的设计旨在提高模型对遮挡的鲁棒性，避免过拟合。

**技术框架**：LabelGS的整体架构包括多个模块：首先是主高斯标记模型，将2D语义信息提升至3D高斯；其次是遮挡分析模型，确保在优化过程中避免遮挡过拟合；最后是高斯投影过滤器，用于解决高斯标签冲突。

**关键创新**：LabelGS的主要创新在于引入了跨视图一致的语义掩码和遮挡分析模型，这与现有方法的单一视角处理方式形成了鲜明对比，显著提升了3D场景的分割效果。

**关键设计**：在模型设计中，采用了随机区域采样策略以优化3DGS的训练过程，并在损失函数中引入了针对遮挡的惩罚项，以提高模型的泛化能力。

## 📊 实验亮点

实验结果显示，LabelGS在3D场景分割任务中显著优于Feature-3DGS，训练速度提升达到22倍，分辨率为1440X1080，展示了其在效率和效果上的双重优势。

## 🎯 应用场景

LabelGS在3D场景理解、自动驾驶、机器人导航等领域具有广泛的应用潜力。通过提升3D场景分割能力，该方法能够更好地支持智能系统对复杂环境的理解与决策，推动相关技术的发展。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a novel explicit representation for 3D scenes, offering both high-fidelity reconstruction and efficient rendering. However, 3DGS lacks 3D segmentation ability, which limits its applicability in tasks that require scene understanding. The identification and isolating of specific object components is crucial. To address this limitation, we propose Label-aware 3D Gaussian Splatting (LabelGS), a method that augments the Gaussian representation with object label.LabelGS introduces cross-view consistent semantic masks for 3D Gaussians and employs a novel Occlusion Analysis Model to avoid overfitting occlusion during optimization, Main Gaussian Labeling model to lift 2D semantic prior to 3D Gaussian and Gaussian Projection Filter to avoid Gaussian label conflict. Our approach achieves effective decoupling of Gaussian representations and refines the 3DGS optimization process through a random region sampling strategy, significantly improving efficiency. Extensive experiments demonstrate that LabelGS outperforms previous state-of-the-art methods, including Feature-3DGS, in the 3D scene segmentation task. Notably, LabelGS achieves a remarkable 22X speedup in training compared to Feature-3DGS, at a resolution of 1440X1080. Our code will be at https://github.com/garrisonz/LabelGS.

