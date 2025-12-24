---
layout: default
title: "SPADE: Sparsity Adaptive Depth Estimator for Zero-Shot, Real-Time, Monocular Depth Estimation in Underwater Environments"
---

# SPADE: Sparsity Adaptive Depth Estimator for Zero-Shot, Real-Time, Monocular Depth Estimation in Underwater Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.25463" class="toolbar-btn" target="_blank">📄 arXiv: 2510.25463v1</a>
  <a href="https://arxiv.org/pdf/2510.25463.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.25463v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.25463v1', 'SPADE: Sparsity Adaptive Depth Estimator for Zero-Shot, Real-Time, Monocular Depth Estimation in Underwater Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongjie Zhang, Gideon Billings, Stefan B. Williams

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-29

---

## 💡 一句话要点

**SPADE：一种水下零样本、实时、单目深度估计的稀疏自适应深度估计器**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `单目深度估计` `水下环境` `稀疏深度先验` `Deformable Transformer` `实时性` `零样本学习` `深度图细化`

## 📋 核心要点

1. 水下环境感知受限，依赖人工或遥控设备风险高、效率低，尤其在复杂或浑浊水域。
2. SPADE结合相对深度估计和稀疏深度先验，生成稠密、度量尺度的深度图，提升水下感知。
3. SPADE在嵌入式硬件上实现15FPS以上的实时性，并在精度和泛化性上优于现有方法。

## 📝 摘要（中文）

本文提出了一种名为SPADE（SParsity Adaptive Depth Estimator）的单目深度估计流水线，用于解决水下环境中的深度感知问题。水下基础设施由于恶劣的海洋环境需要频繁的检查和维护，目前依赖潜水员或遥控水下机器人，但其感知和操作能力受到限制，尤其是在复杂结构或浑浊水域附近。增强水下机器人的空间感知能力是降低操作风险和实现更高自主性的关键。SPADE结合了预训练的相对深度估计器和稀疏深度先验，生成稠密的、具有度量尺度的深度图。该方法首先利用稀疏深度点缩放相对深度图，然后通过提出的级联Conv-Deformable Transformer块细化最终的度量预测。实验结果表明，该方法在嵌入式硬件上以超过15 FPS的效率运行，并在精度和泛化能力方面优于最先进的基线方法，有望支持实际的水下检查和干预。

## 🔬 方法详解

**问题定义**：水下环境中的单目深度估计是一个具有挑战性的问题。现有的方法通常难以在水下环境中泛化，并且计算成本较高，难以满足实时性要求。特别是在水下基础设施的检查和维护中，需要准确且实时的深度信息来支持自主导航和操作。现有方法在浑浊水域或复杂结构附近表现不佳，限制了水下机器人的应用。

**核心思路**：SPADE的核心思路是结合预训练的相对深度估计器和稀疏深度先验信息，利用稀疏深度信息对相对深度图进行缩放，从而获得具有度量尺度的深度图。然后，通过级联的Conv-Deformable Transformer块对深度图进行细化，提高深度估计的精度。这种方法充分利用了相对深度估计器的泛化能力和稀疏深度信息的准确性，从而在水下环境中实现准确且实时的深度估计。

**技术框架**：SPADE的整体框架包括两个主要阶段：1) 稀疏深度引导的尺度估计：利用稀疏深度点对相对深度图进行尺度缩放，得到初始的度量深度图。2) 级联Conv-Deformable Transformer细化：使用提出的级联Conv-Deformable Transformer块对初始深度图进行细化，从而提高深度估计的精度。整个流程从单目图像输入开始，最终输出稠密的、具有度量尺度的深度图。

**关键创新**：SPADE的关键创新在于提出了级联Conv-Deformable Transformer块，用于深度图的细化。与传统的卷积神经网络相比，Deformable Transformer能够更好地适应水下环境中的复杂几何结构和光照变化。此外，级联结构能够逐步提高深度估计的精度，从而获得更准确的深度图。另一个创新点是结合了相对深度估计和稀疏深度先验，充分利用了两种信息的优势。

**关键设计**：级联Conv-Deformable Transformer块的设计是关键。每个块包含一个卷积层和一个Deformable Transformer层。卷积层用于提取局部特征，Deformable Transformer层用于建模全局关系。级联结构允许逐步细化深度图。损失函数包括深度回归损失和梯度损失，用于提高深度估计的精度和保持深度图的平滑性。稀疏深度先验可以通过水声传感器或激光扫描仪获取。

## 📊 实验亮点

实验结果表明，SPADE在水下数据集上取得了优于现有方法的性能。与最先进的基线方法相比，SPADE在深度估计精度方面有显著提升，并且能够在嵌入式硬件上以超过15 FPS的速度运行，满足实时性要求。这表明SPADE具有很强的实用价值，可以应用于实际的水下场景。

## 🎯 应用场景

SPADE可应用于水下基础设施的自动巡检、水下机器人自主导航、海洋生物研究、水下考古等领域。通过提供准确且实时的深度信息，SPADE能够提高水下机器人的自主性和安全性，降低人工操作的风险和成本。该技术还有助于更深入地了解水下环境，促进海洋科学的发展。

## 📄 摘要（原文）

> Underwater infrastructure requires frequent inspection and maintenance due to harsh marine conditions. Current reliance on human divers or remotely operated vehicles is limited by perceptual and operational challenges, especially around complex structures or in turbid water. Enhancing the spatial awareness of underwater vehicles is key to reducing piloting risks and enabling greater autonomy. To address these challenges, we present SPADE: SParsity Adaptive Depth Estimator, a monocular depth estimation pipeline that combines pre-trained relative depth estimator with sparse depth priors to produce dense, metric scale depth maps. Our two-stage approach first scales the relative depth map with the sparse depth points, then refines the final metric prediction with our proposed Cascade Conv-Deformable Transformer blocks. Our approach achieves improved accuracy and generalisation over state-of-the-art baselines and runs efficiently at over 15 FPS on embedded hardware, promising to support practical underwater inspection and intervention. This work has been submitted to IEEE Journal of Oceanic Engineering Special Issue of AUV 2026.

