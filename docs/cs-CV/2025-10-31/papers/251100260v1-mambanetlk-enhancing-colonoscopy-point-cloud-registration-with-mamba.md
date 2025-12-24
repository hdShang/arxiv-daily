---
layout: default
title: "MambaNetLK: Enhancing Colonoscopy Point Cloud Registration with Mamba"
---

# MambaNetLK: Enhancing Colonoscopy Point Cloud Registration with Mamba

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00260" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00260v1</a>
  <a href="https://arxiv.org/pdf/2511.00260.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00260v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00260v1', 'MambaNetLK: Enhancing Colonoscopy Point Cloud Registration with Mamba')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linzhe Jiang, Jiayuan Huang, Sophia Bano, Matthew J. Clarkson, Zhehua Mao, Mobarak I. Hoque

**分类**: cs.CV

**发布日期**: 2025-10-31

**备注**: 12 pages, 4 figures, 3 tables, IPCAI conference

---

## 💡 一句话要点

**MambaNetLK：利用Mamba SSM增强结肠镜点云配准精度与鲁棒性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `点云配准` `Mamba SSM` `内窥镜导航` `Lucas-Kanade算法` `医学图像处理`

## 📋 核心要点

1. 现有3D点云配准方法在结肠镜应用中，易受生物组织重复纹理和局部同质几何结构的影响，导致特征退化和配准稳定性下降。
2. MambaNetLK通过将Mamba状态空间模型（SSM）集成到PointNetLK架构中，作为跨模态特征提取器，有效捕获长程依赖关系，提升配准精度。
3. 在临床数据集C3VD-Raycasting-10k上，MambaNetLK显著优于现有方法，中值旋转误差降低56.04%，RMSE平移误差降低26.19%。

## 📝 摘要（中文）

本文提出了一种针对内窥镜导航的3D点云配准新方法MambaNetLK，并构建了一个高质量、临床相关的基准数据集C3VD-Raycasting-10k，包含10014个几何对齐的点云对，这些点云对源自临床CT数据。MambaNetLK是一种无对应关系的配准框架，通过集成Mamba状态空间模型（SSM）作为跨模态特征提取器来增强PointNetLK架构，从而以线性时间复杂度有效地捕获长程依赖关系。该配准通过Lucas-Kanade算法迭代实现。在临床数据集C3VD-Raycasting-10k上，MambaNetLK与最先进的方法相比，实现了最佳性能，中值旋转误差降低了56.04%，RMSE平移误差降低了26.19%。该模型还在ModelNet40上表现出强大的泛化能力，并且对初始姿态扰动具有出色的鲁棒性。MambaNetLK为手术导航中的3D配准提供了坚实的基础，结合全局表达的基于SSM的特征提取器和大规模临床数据集，能够在结肠镜等微创手术中实现更准确和可靠的引导系统。

## 🔬 方法详解

**问题定义**：论文旨在解决在结肠镜引导手术中，由于生物组织特征退化和术前术中数据域差异导致的3D点云配准精度和鲁棒性问题。现有方法难以有效处理这些挑战，影响了病灶定位、边缘评估和导航安全性。

**核心思路**：论文的核心思路是利用Mamba状态空间模型（SSM）强大的长程依赖建模能力，提取更具区分性的点云特征，从而提高配准的准确性和鲁棒性。Mamba SSM能够以线性时间复杂度处理序列数据，适合处理点云数据中的全局上下文信息。

**技术框架**：MambaNetLK框架基于PointNetLK架构，并将其中的特征提取模块替换为Mamba SSM。整体流程包括：1）输入源点云和目标点云；2）使用Mamba SSM分别提取源点云和目标点云的特征；3）使用Lucas-Kanade算法迭代优化变换矩阵，使源点云与目标点云对齐。

**关键创新**：最重要的技术创新点是将Mamba SSM引入到点云配准任务中。与传统的卷积神经网络或Transformer相比，Mamba SSM能够更有效地捕获点云数据中的长程依赖关系，并且具有线性时间复杂度，更适合处理大规模点云数据。

**关键设计**：论文中，Mamba SSM被用作PointNetLK框架中的特征提取器。具体实现细节包括：Mamba SSM的层数、隐藏层维度、激活函数等。此外，论文还设计了一个大规模的临床数据集C3VD-Raycasting-10k，用于评估算法的性能。损失函数采用标准的点云配准损失函数，例如均方误差（MSE）或Huber损失。

## 📊 实验亮点

MambaNetLK在C3VD-Raycasting-10k数据集上取得了显著的性能提升，相较于第二好的方法，中值旋转误差降低了56.04%，RMSE平移误差降低了26.19%。此外，该模型在ModelNet40数据集上表现出良好的泛化能力，并且对初始姿态扰动具有很强的鲁棒性，表明其在实际临床应用中具有很高的潜力。

## 🎯 应用场景

MambaNetLK在内窥镜手术导航领域具有广阔的应用前景，可以应用于结肠镜、胃镜等微创手术中，提高病灶定位的准确性，辅助医生进行更精确的手术操作，减少手术风险，改善患者预后。此外，该方法还可以推广到其他医学图像配准任务中，例如CT、MRI等。

## 📄 摘要（原文）

> Accurate 3D point cloud registration underpins reliable image-guided colonoscopy, directly affecting lesion localization, margin assessment, and navigation safety. However, biological tissue exhibits repetitive textures and locally homogeneous geometry that cause feature degeneracy, while substantial domain shifts between pre-operative anatomy and intra-operative observations further degrade alignment stability. To address these clinically critical challenges, we introduce a novel 3D registration method tailored for endoscopic navigation and a high-quality, clinically grounded dataset to support rigorous and reproducible benchmarking. We introduce C3VD-Raycasting-10k, a large-scale benchmark dataset with 10,014 geometrically aligned point cloud pairs derived from clinical CT data. We propose MambaNetLK, a novel correspondence-free registration framework, which enhances the PointNetLK architecture by integrating a Mamba State Space Model (SSM) as a cross-modal feature extractor. As a result, the proposed framework efficiently captures long-range dependencies with linear-time complexity. The alignment is achieved iteratively using the Lucas-Kanade algorithm. On the clinical dataset, C3VD-Raycasting-10k, MambaNetLK achieves the best performance compared with the state-of-the-art methods, reducing median rotation error by 56.04% and RMSE translation error by 26.19% over the second-best method. The model also demonstrates strong generalization on ModelNet40 and superior robustness to initial pose perturbations. MambaNetLK provides a robust foundation for 3D registration in surgical navigation. The combination of a globally expressive SSM-based feature extractor and a large-scale clinical dataset enables more accurate and reliable guidance systems in minimally invasive procedures like colonoscopy.

