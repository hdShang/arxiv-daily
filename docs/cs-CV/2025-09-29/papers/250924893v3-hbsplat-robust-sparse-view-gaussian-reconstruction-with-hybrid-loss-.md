---
layout: default
title: "HBSplat: Robust Sparse-View Gaussian Reconstruction with Hybrid-Loss Guided Depth and Bidirectional Warping"
---

# HBSplat: Robust Sparse-View Gaussian Reconstruction with Hybrid-Loss Guided Depth and Bidirectional Warping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24893" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24893v3</a>
  <a href="https://arxiv.org/pdf/2509.24893.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24893v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24893v3', 'HBSplat: Robust Sparse-View Gaussian Reconstruction with Hybrid-Loss Guided Depth and Bidirectional Warping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Ma, Guoliang Wei, Haihong Xiao, Yue Cheng

**分类**: cs.CV

**发布日期**: 2025-09-29 (更新: 2025-10-08)

**备注**: 14 pages, 21 figures

**🔗 代码/项目**: [GITHUB](https://github.com/eternalland/HBSplat)

---

## 💡 一句话要点

**HBSplat：基于混合损失引导深度和双向扭曲的鲁棒稀疏视角高斯重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `新视角合成` `3D高斯溅射` `稀疏视角重建` `深度估计` `虚拟视角合成`

## 📋 核心要点

1. 稀疏视角下的新视角合成面临严重挑战，现有方法易出现过拟合、几何失真和场景碎片化。
2. HBSplat通过混合损失引导深度估计、双向扭曲虚拟视角合成和遮挡感知重建来解决上述问题。
3. 实验结果表明，HBSplat在多个数据集上取得了显著的性能提升，并保持了实时渲染能力。

## 📝 摘要（中文）

本文提出HBSplat，一个统一的框架，旨在提升稀疏视角下的3D高斯溅射(3DGS)性能。针对稀疏视角下3D重建中存在的过拟合、几何失真和场景碎片化问题，HBSplat通过整合鲁棒的结构线索、虚拟视角约束和遮挡区域补全来改进3DGS。主要贡献包括：混合损失深度估计模块，通过利用密集匹配先验并结合重投影、点传播和平滑约束来确保多视角一致性；双向扭曲虚拟视角合成方法，通过双向深度图像扭曲和多视角融合创建高质量虚拟视角，从而施加更强的约束；以及遮挡感知重建组件，利用深度差异掩码和基于学习的图像修复模型来恢复遮挡区域。在LLFF、Blender和DTU基准测试上的大量评估表明，HBSplat达到了新的state-of-the-art，实现了高达21.13 dB的PSNR和0.189的LPIPS，同时保持了实时推理。

## 🔬 方法详解

**问题定义**：论文旨在解决在稀疏视角下，使用3D高斯溅射（3DGS）进行新视角合成时遇到的问题。现有方法在稀疏视角下容易出现过拟合，导致几何结构扭曲、场景不完整，以及产生漂浮伪影等问题。这些问题严重影响了渲染质量和场景的真实感。

**核心思路**：HBSplat的核心思路是通过引入更强的几何约束和上下文信息来缓解稀疏视角带来的不确定性。具体来说，它结合了深度估计、虚拟视角合成和遮挡感知重建三个方面，利用混合损失函数引导深度估计，生成高质量的虚拟视角，并恢复被遮挡的区域，从而提高3DGS在稀疏视角下的重建质量。

**技术框架**：HBSplat的整体框架包含三个主要模块：1) 混合损失深度估计模块：用于估计场景的深度信息，并确保多视角一致性。2) 双向扭曲虚拟视角合成模块：利用估计的深度信息生成高质量的虚拟视角，从而增加训练数据和约束。3) 遮挡感知重建模块：用于恢复场景中被遮挡的区域，提高场景的完整性。这三个模块协同工作，共同提升3DGS在稀疏视角下的性能。

**关键创新**：HBSplat的关键创新在于以下几个方面：1) 提出了混合损失深度估计模块，该模块结合了重投影误差、点传播和平滑约束，能够更准确地估计深度信息。2) 提出了双向扭曲虚拟视角合成方法，该方法能够生成高质量的虚拟视角，从而增加训练数据和约束。3) 提出了遮挡感知重建模块，该模块能够恢复场景中被遮挡的区域，提高场景的完整性。这些创新使得HBSplat在稀疏视角下能够实现更鲁棒和高质量的3D重建。

**关键设计**：混合损失深度估计模块使用了多种损失函数的组合，包括重投影损失、点传播损失和平滑损失。重投影损失用于确保估计的深度与观测图像一致，点传播损失用于将深度信息从已知区域传播到未知区域，平滑损失用于保证深度图的平滑性。双向扭曲虚拟视角合成模块使用了双向深度图像扭曲技术，该技术能够生成更准确的虚拟视角。遮挡感知重建模块使用了深度差异掩码和基于学习的图像修复模型，该模型能够有效地恢复被遮挡的区域。

## 📊 实验亮点

HBSplat在LLFF、Blender和DTU数据集上进行了广泛的评估，实验结果表明，HBSplat在稀疏视角下取得了显著的性能提升。例如，在LLFF数据集上，HBSplat的PSNR指标达到了21.13 dB，LPIPS指标达到了0.189，超过了现有的state-of-the-art方法。此外，HBSplat还保持了实时推理能力，使其能够应用于实时渲染场景。

## 🎯 应用场景

HBSplat在许多领域具有广泛的应用前景，例如：增强现实(AR)、虚拟现实(VR)、机器人导航、自动驾驶、三维地图重建等。该方法能够利用少量图像重建出高质量的三维场景，降低了数据采集的成本，提高了三维重建的效率。未来，HBSplat有望在更多领域得到应用，并推动相关技术的发展。

## 📄 摘要（原文）

> Novel View Synthesis (NVS) from sparse views presents a formidable challenge in 3D reconstruction, where limited multi-view constraints lead to severe overfitting, geometric distortion, and fragmented scenes. While 3D Gaussian Splatting (3DGS) delivers real-time, high-fidelity rendering, its performance drastically deteriorates under sparse inputs, plagued by floating artifacts and structural failures. To address these challenges, we introduce HBSplat, a unified framework that elevates 3DGS by seamlessly integrating robust structural cues, virtual view constraints, and occluded region completion. Our core contributions are threefold: a Hybrid-Loss Depth Estimation module that ensures multi-view consistency by leveraging dense matching priors and integrating reprojection, point propagation, and smoothness constraints; a Bidirectional Warping Virtual View Synthesis method that enforces substantially stronger constraints by creating high-fidelity virtual views through bidirectional depth-image warping and multi-view fusion; and an Occlusion-Aware Reconstruction component that recovers occluded areas using a depth-difference mask and a learning-based inpainting model. Extensive evaluations on LLFF, Blender, and DTU benchmarks validate that HBSplat sets a new state-of-the-art, achieving up to 21.13 dB PSNR and 0.189 LPIPS, while maintaining real-time inference. Code is available at: https://github.com/eternalland/HBSplat.

