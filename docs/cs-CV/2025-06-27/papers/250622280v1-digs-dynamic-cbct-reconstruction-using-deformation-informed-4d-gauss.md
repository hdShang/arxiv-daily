---
layout: default
title: "DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian Splatting and a Low-Rank Free-Form Deformation Model"
---

# DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian Splatting and a Low-Rank Free-Form Deformation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22280" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22280v1</a>
  <a href="https://arxiv.org/pdf/2506.22280.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22280v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22280v1', 'DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian Splatting and a Low-Rank Free-Form Deformation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuliang Huang, Imraj Singh, Thomas Joyce, Kris Thielemans, Jamie R. McClelland

**分类**: eess.IV, cs.CV

**发布日期**: 2025-06-27

**备注**: Accepted by MICCAI 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Yuliang-Huang/DIGS)

---

## 💡 一句话要点

**提出基于变形信息的4D高斯点云重建方法以解决动态CBCT重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态CBCT` `4D高斯点云` `自由形变` `运动补偿` `医学成像` `放射治疗` `图像重建`

## 📋 核心要点

1. 现有动态CBCT重建方法未能有效处理呼吸变异性，导致图像质量下降。
2. 本文提出了一种基于FFD的变形信息框架，确保高斯运动的一致性，提升重建效果。
3. 在六个CBCT数据集上的实验结果显示，本文方法图像质量优于HexPlane，且速度提升达6倍。

## 📝 摘要（中文）

3D锥束CT（CBCT）在放射治疗中广泛应用，但由于呼吸造成的运动伪影影响图像质量。现有方法通过将投影按呼吸相位排序并逐相位重建图像，未能有效应对呼吸的变异性。本文提出了一种动态CBCT重建方法，利用变形信息的4D高斯点云技术，克服了现有方法的不足。通过引入自由形变（FFD）基础函数和变形信息框架，确保高斯运动的一致性。实验结果表明，该方法在六个CBCT数据集上实现了优越的图像质量，并较HexPlane方法加速了6倍，展示了其在运动补偿CBCT重建中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决动态CBCT重建中由于呼吸引起的运动伪影问题。现有方法通过相位排序重建，无法有效应对呼吸的变异性，导致图像质量下降。

**核心思路**：我们提出了一种基于自由形变（FFD）的变形信息框架，结合4D高斯点云技术，确保高斯运动参数（均值、尺度和旋转）在统一变形场下的一致性，从而提升重建质量。

**技术框架**：整体方法包括数据预处理、FFD基础函数构建、变形信息框架设计和高斯运动参数优化四个主要模块。首先对CBCT数据进行预处理，然后构建FFD基础函数以捕捉空间变形，接着设计变形信息框架以确保运动一致性，最后优化高斯运动参数以实现高质量重建。

**关键创新**：本文的主要创新在于引入FFD基础函数和变形信息框架，克服了现有方法在运动表示上的计算复杂性和不一致性。这一设计使得动态CBCT重建更加高效和准确。

**关键设计**：我们在损失函数中引入了运动一致性约束，并设计了适应性参数设置，以优化高斯运动的均值、尺度和旋转。此外，网络结构采用了多层次的FFD模块，以增强模型对复杂运动的适应能力。

## 📊 实验亮点

实验结果表明，本文提出的方法在六个CBCT数据集上实现了显著的图像质量提升，较HexPlane方法加速了6倍。这一性能提升展示了变形信息的4D高斯点云技术在动态CBCT重建中的有效性，具有重要的临床应用前景。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在放射治疗和医学成像领域。通过提高动态CBCT重建的图像质量和速度，能够更好地支持临床决策，提升患者的治疗效果。此外，该方法的框架也可扩展至其他动态场景的重建任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> 3D Cone-Beam CT (CBCT) is widely used in radiotherapy but suffers from motion artifacts due to breathing. A common clinical approach mitigates this by sorting projections into respiratory phases and reconstructing images per phase, but this does not account for breathing variability. Dynamic CBCT instead reconstructs images at each projection, capturing continuous motion without phase sorting. Recent advancements in 4D Gaussian Splatting (4DGS) offer powerful tools for modeling dynamic scenes, yet their application to dynamic CBCT remains underexplored. Existing 4DGS methods, such as HexPlane, use implicit motion representations, which are computationally expensive. While explicit low-rank motion models have been proposed, they lack spatial regularization, leading to inconsistencies in Gaussian motion. To address these limitations, we introduce a free-form deformation (FFD)-based spatial basis function and a deformation-informed framework that enforces consistency by coupling the temporal evolution of Gaussian's mean position, scale, and rotation under a unified deformation field. We evaluate our approach on six CBCT datasets, demonstrating superior image quality with a 6x speedup over HexPlane. These results highlight the potential of deformation-informed 4DGS for efficient, motion-compensated CBCT reconstruction. The code is available at https://github.com/Yuliang-Huang/DIGS.

