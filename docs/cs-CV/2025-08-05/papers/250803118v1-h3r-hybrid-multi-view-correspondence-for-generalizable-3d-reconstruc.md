---
layout: default
title: "H3R: Hybrid Multi-view Correspondence for Generalizable 3D Reconstruction"
---

# H3R: Hybrid Multi-view Correspondence for Generalizable 3D Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03118" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03118v1</a>
  <a href="https://arxiv.org/pdf/2508.03118.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03118v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03118v1', 'H3R: Hybrid Multi-view Correspondence for Generalizable 3D Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heng Jia, Linchao Zhu, Na Zhao

**分类**: cs.CV

**发布日期**: 2025-08-05

**备注**: ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/JiaHeng-DLUT/H3R)

---

## 💡 一句话要点

**提出H3R框架以解决多视角对应建模的挑战**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D重建` `多视角对应` `几何一致性` `深度学习` `计算机视觉` `Transformer` `特征聚合`

## 📋 核心要点

1. 现有的3D重建方法在多视角对应建模中面临几何精度与鲁棒性之间的权衡，导致在复杂场景中表现不佳。
2. H3R框架通过结合体积潜在融合与注意力特征聚合，提升了几何一致性和自适应对应优化的能力。
3. 在多个数据集上，H3R方法实现了显著的性能提升，PSNR分别提高了0.59 dB、1.06 dB和0.22 dB，展示了其优越性。

## 📝 摘要（中文）

尽管前馈3D高斯点云技术取得了进展，但通用3D重建仍然面临挑战，尤其是在多视角对应建模方面。现有方法存在根本性权衡：显式方法在几何精度上表现良好，但在模糊区域中表现不佳；隐式方法则提供了鲁棒性，但收敛速度较慢。本文提出的H3R框架通过整合体积潜在融合与基于注意力的特征聚合，解决了这一限制。该框架由两个互补组件组成：一个高效的潜在体积，通过极线约束强制几何一致性；一个摄像机感知的Transformer，利用Plücker坐标进行自适应对应优化。实验表明，该方法在多个基准测试中实现了最先进的性能，PSNR分别提升0.59 dB、1.06 dB和0.22 dB。

## 🔬 方法详解

**问题定义**：本文旨在解决通用3D重建中的多视角对应建模问题，现有方法在几何精度和鲁棒性之间存在权衡，导致在复杂场景中的表现不理想。

**核心思路**：H3R框架的核心思路是通过整合显式的几何约束与隐式的特征聚合，来提高重建的准确性和收敛速度。通过这种设计，框架能够在保持几何一致性的同时，增强对模糊区域的处理能力。

**技术框架**：H3R框架主要由两个模块组成：一个高效的潜在体积模块，利用极线约束来确保几何一致性；另一个是摄像机感知的Transformer模块，利用Plücker坐标进行自适应的对应优化。整体流程包括输入多视角图像，经过潜在体积和Transformer模块处理后输出重建结果。

**关键创新**：H3R的主要创新在于将体积潜在融合与注意力机制结合，形成了一种新的多视角对应建模方法。这种方法在处理模糊区域时表现出色，显著提高了重建的准确性和效率。

**关键设计**：在设计中，H3R使用了特定的损失函数来平衡几何一致性与特征聚合的效果，同时在Transformer模块中引入了Plücker坐标，以增强对应优化的灵活性和准确性。

## 📊 实验亮点

H3R方法在多个基准测试中表现出色，特别是在RealEstate10K、ACID和DTU数据集上，PSNR分别提升了0.59 dB、1.06 dB和0.22 dB，展现了其在3D重建领域的领先地位。与现有方法相比，H3R的收敛速度提高了2倍，进一步验证了其有效性。

## 🎯 应用场景

H3R框架在计算机视觉和机器人领域具有广泛的应用潜力，尤其是在自动驾驶、虚拟现实和增强现实等场景中。其高效的3D重建能力能够为这些领域提供更为精准的环境理解和交互体验，推动相关技术的进步与发展。

## 📄 摘要（原文）

> Despite recent advances in feed-forward 3D Gaussian Splatting, generalizable 3D reconstruction remains challenging, particularly in multi-view correspondence modeling. Existing approaches face a fundamental trade-off: explicit methods achieve geometric precision but struggle with ambiguous regions, while implicit methods provide robustness but suffer from slow convergence. We present H3R, a hybrid framework that addresses this limitation by integrating volumetric latent fusion with attention-based feature aggregation. Our framework consists of two complementary components: an efficient latent volume that enforces geometric consistency through epipolar constraints, and a camera-aware Transformer that leverages Plücker coordinates for adaptive correspondence refinement. By integrating both paradigms, our approach enhances generalization while converging 2$\times$ faster than existing methods. Furthermore, we show that spatial-aligned foundation models (e.g., SD-VAE) substantially outperform semantic-aligned models (e.g., DINOv2), resolving the mismatch between semantic representations and spatial reconstruction requirements. Our method supports variable-number and high-resolution input views while demonstrating robust cross-dataset generalization. Extensive experiments show that our method achieves state-of-the-art performance across multiple benchmarks, with significant PSNR improvements of 0.59 dB, 1.06 dB, and 0.22 dB on the RealEstate10K, ACID, and DTU datasets, respectively. Code is available at https://github.com/JiaHeng-DLUT/H3R.

