---
layout: default
title: "PlantSegNeRF: A few-shot, cross-species method for plant 3D instance point cloud reconstruction via joint-channel NeRF with multi-view image instance matching"
---

# PlantSegNeRF: A few-shot, cross-species method for plant 3D instance point cloud reconstruction via joint-channel NeRF with multi-view image instance matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00371" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00371v3</a>
  <a href="https://arxiv.org/pdf/2507.00371.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00371v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00371v3', 'PlantSegNeRF: A few-shot, cross-species method for plant 3D instance point cloud reconstruction via joint-channel NeRF with multi-view image instance matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Yang, Ruiming Du, Hanyang Huang, Jiayang Xie, Pengyao Xie, Leisen Fang, Ziyue Guo, Nanjun Jiang, Yu Jiang, Haiyan Cen

**分类**: cs.CV

**发布日期**: 2025-07-01 (更新: 2025-10-25)

---

## 💡 一句话要点

**提出PlantSegNeRF以解决植物点云实例分割精度不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `植物点云` `实例分割` `深度学习` `多视角图像` `NeRF` `表型特征` `跨物种泛化` `高精度重建`

## 📋 核心要点

1. 现有植物点云分割技术在分辨率、精度和跨物种泛化能力上存在明显不足，限制了器官级表型特征的提取。
2. 本研究提出PlantSegNeRF，通过多视角图像进行2D实例分割，并利用实例匹配模块优化实例ID，生成高精度点云。
3. 实验结果显示，PlantSegNeRF在植物点云实例分割任务中，平均提升了11.7%、38.2%、32.2%和25.3%的性能指标。

## 📝 摘要（中文）

植物点云的器官分割是高分辨率和准确提取器官级表型特征的前提。尽管深度学习的快速发展推动了植物点云分割研究，但现有技术在分辨率、分割精度和跨物种的泛化能力上仍面临挑战。本研究提出了一种新方法PlantSegNeRF，旨在通过多视角RGB图像序列直接生成高精度的实例点云。该方法在多视角图像上进行2D实例分割，生成每个器官的实例掩码，并通过专门设计的实例匹配模块进行匹配和优化。最终，基于体积密度将隐式场景转换为高精度植物实例点云。实验结果表明，PlantSegNeRF在点云语义分割中优于常用方法，精度、召回率、F1-score和IoU分别提高了16.1%、18.3%、17.8%和24.2%。

## 🔬 方法详解

**问题定义**：本研究旨在解决植物点云的器官分割精度不足的问题。现有方法在处理结构复杂的植物物种时，分割精度和泛化能力较差，限制了高质量3D数据的获取。

**核心思路**：PlantSegNeRF通过结合多视角RGB图像和深度学习技术，直接生成高精度的植物实例点云。该方法首先进行2D实例分割，然后通过实例匹配模块优化实例ID，最终生成高质量的3D点云。

**技术框架**：整体架构包括多个模块：首先对多视角图像进行2D实例分割，生成实例掩码；接着通过实例匹配模块对相同器官的实例ID进行匹配和优化；最后，利用实例NeRF渲染隐式场景，并基于体积密度生成高精度点云。

**关键创新**：PlantSegNeRF的主要创新在于结合了多视角图像的实例分割与实例匹配模块，显著提高了植物点云的分割精度和泛化能力。这一方法在处理复杂结构植物时表现优异，超越了传统的分割技术。

**关键设计**：在技术细节上，PlantSegNeRF采用了特定的损失函数来优化实例匹配过程，并设计了适应不同植物物种的网络结构，以确保在多样化的植物样本中保持高效的性能。实验中还调整了关键参数，以实现最佳的分割效果。

## 📊 实验亮点

实验结果表明，PlantSegNeRF在点云语义分割中表现优异，精度、召回率、F1-score和IoU分别提高了16.1%、18.3%、17.8%和24.2%。在植物点云实例分割任务中，平均提升了11.7%、38.2%、32.2%和25.3%的性能指标，显示出显著的优势。

## 🎯 应用场景

该研究的潜在应用领域包括植物科学、农业监测和生态研究等。通过提供高质量的3D植物数据，PlantSegNeRF能够支持大规模模型的开发，推动植物表型分析和相关研究的进展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Organ segmentation of plant point clouds is a prerequisite for the high-resolution and accurate extraction of organ-level phenotypic traits. Although the fast development of deep learning has boosted much research on segmentation of plant point clouds, the existing techniques for organ segmentation still face limitations in resolution, segmentation accuracy, and generalizability across various plant species. In this study, we proposed a novel approach called plant segmentation neural radiance fields (PlantSegNeRF), aiming to directly generate high-precision instance point clouds from multi-view RGB image sequences for a wide range of plant species. PlantSegNeRF performed 2D instance segmentation on the multi-view images to generate instance masks for each organ with a corresponding ID. The multi-view instance IDs corresponding to the same plant organ were then matched and refined using a specially designed instance matching module. The instance NeRF was developed to render an implicit scene, containing color, density, semantic and instance information. The implicit scene was ultimately converted into high-precision plant instance point clouds based on the volume density. The results proved that in semantic segmentation of point clouds, PlantSegNeRF outperformed the commonly used methods, demonstrating an average improvement of 16.1%, 18.3%, 17.8%, and 24.2% in precision, recall, F1-score, and IoU compared to the second-best results on structurally complex species. More importantly, PlantSegNeRF exhibited significant advantages in plant point cloud instance segmentation tasks. Across all plant species, it achieved average improvements of 11.7%, 38.2%, 32.2% and 25.3% in mPrec, mRec, mCov, mWCov, respectively. This study extends the organ-level plant phenotyping and provides a high-throughput way to supply high-quality 3D data for the development of large-scale models in plant science.

