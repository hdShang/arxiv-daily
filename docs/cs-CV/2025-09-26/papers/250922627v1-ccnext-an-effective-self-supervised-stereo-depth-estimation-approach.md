---
layout: default
title: "CCNeXt: An Effective Self-Supervised Stereo Depth Estimation Approach"
---

# CCNeXt: An Effective Self-Supervised Stereo Depth Estimation Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22627" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22627v1</a>
  <a href="https://arxiv.org/pdf/2509.22627.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22627v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22627v1', 'CCNeXt: An Effective Self-Supervised Stereo Depth Estimation Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexandre Lopes, Roberto Souza, Helio Pedrini

**分类**: cs.CV

**发布日期**: 2025-09-26

**🔗 代码/项目**: [GITHUB](https://github.com/alelopes/CCNext)

---

## 💡 一句话要点

**提出CCNeXt，一种高效的自监督立体深度估计方法，在计算成本和精度间取得平衡。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `立体视觉` `深度估计` `自监督学习` `卷积神经网络` `交叉注意力`

## 📋 核心要点

1. 现有深度估计方法难以在计算资源有限的场景下，同时保证精度和效率。
2. CCNeXt采用新型窗口化极线交叉注意力模块和重新设计的解码器，提升特征提取和深度估计能力。
3. 实验表明，CCNeXt在KITTI数据集上取得了优异的性能，并在速度上显著优于现有方法。

## 📝 摘要（中文）

深度估计在机器人、自动驾驶和增强现实等应用中起着关键作用。这些场景通常受到计算能力的限制。立体图像对为深度估计提供了一种有效的解决方案，因为它只需要估计图像对中像素的视差，即可确定已知校正系统中的深度。由于难以在各种场景中获取可靠的真实深度数据，自监督技术应运而生，尤其是在有大量未标记数据集可用时。我们提出了一种新颖的自监督卷积方法，该方法优于现有的最先进的卷积神经网络（CNN）和视觉Transformer（ViT），同时平衡了计算成本。所提出的CCNeXt架构采用了一种现代CNN特征提取器，在编码器中采用了一种新颖的窗口化极线交叉注意力模块，并对深度估计解码器进行了全面的重新设计。我们的实验表明，CCNeXt在KITTI Eigen Split测试数据上实现了具有竞争力的指标，同时比当前最佳模型快10.18倍，并且与最近提出的技术相比，在KITTI Eigen Split Improved Ground Truth和Driving Stereo数据集的所有指标中都实现了最先进的结果。为了确保完全的可重复性，我们的项目可在https://github.com/alelopes/CCNext上访问。

## 🔬 方法详解

**问题定义**：论文旨在解决立体视觉深度估计问题，特别是在自监督学习框架下，如何在计算资源受限的情况下，提升深度估计的精度和效率。现有方法，尤其是基于Transformer的模型，虽然精度较高，但计算成本也较高，难以在实际应用中部署。

**核心思路**：论文的核心思路是在保持精度的前提下，显著降低计算复杂度。通过设计高效的网络结构，特别是窗口化极线交叉注意力模块，来提取图像特征，并利用重新设计的解码器进行深度估计。这种设计旨在充分利用CNN的局部特征提取能力和交叉注意力的全局信息融合能力。

**技术框架**：CCNeXt的整体架构包括一个CNN特征提取器、一个窗口化极线交叉注意力模块和一个深度估计解码器。首先，CNN特征提取器从左右图像中提取特征。然后，窗口化极线交叉注意力模块在极线上进行特征融合，以增强视差信息的提取。最后，深度估计解码器将融合后的特征映射到深度图。

**关键创新**：论文的关键创新在于提出了窗口化极线交叉注意力模块。该模块通过在极线上进行局部窗口内的交叉注意力计算，有效地融合了左右图像的特征，同时降低了计算复杂度。与传统的全局注意力机制相比，窗口化极线交叉注意力模块更加高效，更适合于处理高分辨率图像。

**关键设计**：窗口大小是窗口化极线交叉注意力模块的关键参数。论文可能通过实验确定了最佳的窗口大小，以在精度和效率之间取得平衡。此外，损失函数的设计也至关重要，通常包括光度一致性损失和视差平滑损失，以约束深度图的生成。具体的网络结构细节，如卷积层的数量、滤波器大小等，也需要根据实验进行调整。

## 📊 实验亮点

CCNeXt在KITTI Eigen Split测试数据上取得了具有竞争力的指标，并且比当前最佳模型快10.18倍。在KITTI Eigen Split Improved Ground Truth和Driving Stereo数据集上，CCNeXt在所有指标上都达到了最先进的结果，证明了其在自监督立体深度估计方面的优越性能和效率。

## 🎯 应用场景

该研究成果可广泛应用于机器人导航、自动驾驶、增强现实等领域。在这些场景中，实时性和准确性至关重要。CCNeXt在计算效率上的优势使其能够部署在资源受限的平台上，例如嵌入式系统或移动设备上，从而推动这些技术的普及和应用。未来的研究可以进一步探索如何将CCNeXt与其他感知模块集成，以构建更强大的智能系统。

## 📄 摘要（原文）

> Depth Estimation plays a crucial role in recent applications in robotics, autonomous vehicles, and augmented reality. These scenarios commonly operate under constraints imposed by computational power. Stereo image pairs offer an effective solution for depth estimation since it only needs to estimate the disparity of pixels in image pairs to determine the depth in a known rectified system. Due to the difficulty in acquiring reliable ground-truth depth data across diverse scenarios, self-supervised techniques emerge as a solution, particularly when large unlabeled datasets are available. We propose a novel self-supervised convolutional approach that outperforms existing state-of-the-art Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) while balancing computational cost. The proposed CCNeXt architecture employs a modern CNN feature extractor with a novel windowed epipolar cross-attention module in the encoder, complemented by a comprehensive redesign of the depth estimation decoder. Our experiments demonstrate that CCNeXt achieves competitive metrics on the KITTI Eigen Split test data while being 10.18$\times$ faster than the current best model and achieves state-of-the-art results in all metrics in the KITTI Eigen Split Improved Ground Truth and Driving Stereo datasets when compared to recently proposed techniques. To ensure complete reproducibility, our project is accessible at \href{https://github.com/alelopes/CCNext}{\texttt{https://github.com/alelopes/CCNext}}.

