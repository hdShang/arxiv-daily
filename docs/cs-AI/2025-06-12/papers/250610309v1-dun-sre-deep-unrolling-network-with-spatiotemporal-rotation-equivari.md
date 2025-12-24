---
layout: default
title: "DUN-SRE: Deep Unrolling Network with Spatiotemporal Rotation Equivariance for Dynamic MRI Reconstruction"
---

# DUN-SRE: Deep Unrolling Network with Spatiotemporal Rotation Equivariance for Dynamic MRI Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10309" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10309v1</a>
  <a href="https://arxiv.org/pdf/2506.10309.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10309v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10309v1', 'DUN-SRE: Deep Unrolling Network with Spatiotemporal Rotation Equivariance for Dynamic MRI Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuliang Zhu, Jing Cheng, Qi Xie, Zhuo-Xu Cui, Qingyong Zhu, Yuanyuan Liu, Xin Liu, Jianfeng Ren, Chengbo Wang, Dong Liang

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出DUN-SRE以解决动态MRI重建中的时空旋转对称性问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `动态MRI` `重建算法` `等变卷积` `时空对称性` `心脏成像` `深度学习` `医学成像`

## 📋 核心要点

1. 现有的动态MRI重建方法未能有效利用时间对称性，导致重建质量不足。
2. DUN-SRE通过(2+1)D等变卷积架构，结合数据一致性和近端映射模块，确保时空对称性约束的传播。
3. 在心脏CINE MRI数据集上，DUN-SRE实现了最先进的重建性能，特别是在旋转对称结构的保持上。

## 📝 摘要（中文）

动态磁共振成像（MRI）具有空间旋转对称性和时间对称性等变换对称性。将这些对称性先验明确纳入重建模型中，可以显著提高图像质量，尤其是在激进欠采样情况下。现有的等变卷积神经网络（ECNN）在利用空间对称性先验方面表现良好，但未能有效建模时间对称性。为此，本文提出了一种新颖的深度展开网络DUN-SRE，采用(2+1)D等变卷积架构，确保时空旋转对称性约束在重建过程中的严格传播，从而更准确地建模心脏运动动态。实验结果表明，DUN-SRE在心脏CINE MRI数据集上实现了最先进的性能，特别是在保持旋转对称结构方面，展现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：动态MRI重建面临的主要问题是现有方法未能有效建模时间对称性，导致重建图像质量下降，尤其在严重欠采样情况下。

**核心思路**：本文提出DUN-SRE，通过引入(2+1)D等变卷积架构，结合数据一致性和近端映射模块，确保在重建过程中严格遵循时空旋转对称性约束。

**技术框架**：DUN-SRE的整体架构包括数据一致性模块、近端映射模块和深度展开网络结构，确保在每个重建步骤中都能有效利用时空对称性。

**关键创新**：DUN-SRE的核心创新在于其时空旋转等变性设计，能够同时处理空间和时间的对称性，这在现有ECNN方法中是缺失的。

**关键设计**：在网络设计中，采用高保真度的组滤波参数化机制，以保持表示精度，同时强制执行对称性约束。

## 📊 实验亮点

在心脏CINE MRI数据集上的实验结果显示，DUN-SRE在重建性能上超越了现有的最先进方法，特别是在保持旋转对称结构方面，提升幅度显著，具体性能数据未提供，但表明其具有强大的泛化能力。

## 🎯 应用场景

该研究在医学成像领域具有广泛的应用潜力，尤其是在心脏MRI重建中。通过提高动态MRI的重建质量，DUN-SRE能够为临床诊断提供更准确的图像，进而改善患者的治疗效果。此外，该方法的设计理念也可推广至其他动态成像技术中，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Dynamic Magnetic Resonance Imaging (MRI) exhibits transformation symmetries, including spatial rotation symmetry within individual frames and temporal symmetry along the time dimension. Explicit incorporation of these symmetry priors in the reconstruction model can significantly improve image quality, especially under aggressive undersampling scenarios. Recently, Equivariant convolutional neural network (ECNN) has shown great promise in exploiting spatial symmetry priors. However, existing ECNNs critically fail to model temporal symmetry, arguably the most universal and informative structural prior in dynamic MRI reconstruction. To tackle this issue, we propose a novel Deep Unrolling Network with Spatiotemporal Rotation Equivariance (DUN-SRE) for Dynamic MRI Reconstruction. The DUN-SRE establishes spatiotemporal equivariance through a (2+1)D equivariant convolutional architecture. In particular, it integrates both the data consistency and proximal mapping module into a unified deep unrolling framework. This architecture ensures rigorous propagation of spatiotemporal rotation symmetry constraints throughout the reconstruction process, enabling more physically accurate modeling of cardiac motion dynamics in cine MRI. In addition, a high-fidelity group filter parameterization mechanism is developed to maintain representation precision while enforcing symmetry constraints. Comprehensive experiments on Cardiac CINE MRI datasets demonstrate that DUN-SRE achieves state-of-the-art performance, particularly in preserving rotation-symmetric structures, offering strong generalization capability to a broad range of dynamic MRI reconstruction tasks.

