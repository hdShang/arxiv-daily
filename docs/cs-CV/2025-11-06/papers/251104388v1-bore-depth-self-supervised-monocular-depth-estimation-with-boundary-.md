---
layout: default
title: "BoRe-Depth: Self-supervised Monocular Depth Estimation with Boundary Refinement for Embedded Systems"
---

# BoRe-Depth: Self-supervised Monocular Depth Estimation with Boundary Refinement for Embedded Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.04388" class="toolbar-btn" target="_blank">📄 arXiv: 2511.04388v1</a>
  <a href="https://arxiv.org/pdf/2511.04388.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04388v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.04388v1', 'BoRe-Depth: Self-supervised Monocular Depth Estimation with Boundary Refinement for Embedded Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chang Liu, Juan Li, Sheng Zhang, Chang Liu, Jie Li, Xu Zhang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-06

**备注**: 8 pages, 5 figures, published to IROS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/liangxiansheng093/BoRe-Depth)

---

## 💡 一句话要点

**提出BoRe-Depth模型，在嵌入式系统上实现高精度、高效率的单目深度估计，并提升边界质量。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `单目深度估计` `嵌入式系统` `边界细化` `特征融合` `语义分割`

## 📋 核心要点

1. 现有单目深度估计方法在嵌入式系统上面临深度估计性能差和对象边界模糊的挑战。
2. BoRe-Depth模型通过增强特征自适应融合模块（EFAF）和语义知识集成，提升边界细节表示和对象识别能力。
3. BoRe-Depth在NVIDIA Jetson Orin上以50.7 FPS运行，并在多个数据集上优于其他轻量级模型。

## 📝 摘要（中文）

本文提出了一种名为BoRe-Depth的单目深度估计模型，该模型仅包含870万个参数，旨在嵌入式系统上实现精确的深度图估计，并显著提高边界质量。首先，设计了一个增强特征自适应融合模块（EFAF），自适应地融合深度特征，以增强边界细节的表示。其次，将语义知识集成到编码器中，以提高对象识别和边界感知能力。最后，BoRe-Depth部署在NVIDIA Jetson Orin上，并以50.7 FPS的效率运行。实验结果表明，所提出的模型在多个具有挑战性的数据集上明显优于先前的轻量级模型，并且提供了所提出方法的详细消融研究。代码已在https://github.com/liangxiansheng093/BoRe-Depth上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决单目深度估计在嵌入式系统上的应用问题，现有方法在计算资源受限的情况下，难以保证深度估计的精度和边界质量，尤其是在对象边界处容易出现模糊不清的情况。

**核心思路**：论文的核心思路是通过设计轻量级的网络结构，并结合特征自适应融合和语义信息引导，在保证计算效率的同时，提升深度估计的精度和边界质量。通过EFAF模块增强边界细节的表示，并利用语义信息提高对象识别和边界感知能力。

**技术框架**：BoRe-Depth模型主要包含编码器、解码器和增强特征自适应融合模块（EFAF）。编码器负责提取图像特征，并集成语义知识。EFAF模块自适应地融合不同尺度的深度特征，增强边界细节的表示。解码器则根据融合后的特征生成最终的深度图。整体流程是从输入图像开始，经过编码器提取特征，然后通过EFAF模块进行特征融合，最后由解码器生成深度图。

**关键创新**：论文的关键创新在于增强特征自适应融合模块（EFAF）的设计，该模块能够自适应地融合不同尺度的深度特征，从而有效地增强边界细节的表示。此外，将语义知识集成到编码器中，也有助于提高对象识别和边界感知能力，这是与现有轻量级模型的本质区别。

**关键设计**：EFAF模块的具体实现细节未知，但可以推测其可能采用了注意力机制或者其他自适应权重分配方法，以实现不同尺度特征的有效融合。损失函数方面，论文可能采用了深度回归常用的L1损失或L2损失，并可能结合了边界损失，以进一步提升边界质量。网络结构方面，为了保证轻量化，可能采用了MobileNet或者ShuffleNet等轻量级骨干网络。

## 📊 实验亮点

BoRe-Depth模型在NVIDIA Jetson Orin上实现了50.7 FPS的运行速度，证明了其在嵌入式系统上的高效性。实验结果表明，该模型在多个具有挑战性的数据集上明显优于先前的轻量级模型，尤其是在边界质量方面有显著提升。具体的性能数据和提升幅度需要在论文中进一步查找。

## 🎯 应用场景

该研究成果可广泛应用于无人机、机器人、自动驾驶等嵌入式系统中，为这些系统提供低成本、高精度的三维感知能力。通过提升深度估计的精度和边界质量，可以提高这些系统在复杂环境中的导航、避障和目标识别能力，具有重要的实际应用价值和广阔的市场前景。

## 📄 摘要（原文）

> Depth estimation is one of the key technologies for realizing 3D perception in unmanned systems. Monocular depth estimation has been widely researched because of its low-cost advantage, but the existing methods face the challenges of poor depth estimation performance and blurred object boundaries on embedded systems. In this paper, we propose a novel monocular depth estimation model, BoRe-Depth, which contains only 8.7M parameters. It can accurately estimate depth maps on embedded systems and significantly improves boundary quality. Firstly, we design an Enhanced Feature Adaptive Fusion Module (EFAF) which adaptively fuses depth features to enhance boundary detail representation. Secondly, we integrate semantic knowledge into the encoder to improve the object recognition and boundary perception capabilities. Finally, BoRe-Depth is deployed on NVIDIA Jetson Orin, and runs efficiently at 50.7 FPS. We demonstrate that the proposed model significantly outperforms previous lightweight models on multiple challenging datasets, and we provide detailed ablation studies for the proposed methods. The code is available at https://github.com/liangxiansheng093/BoRe-Depth.

