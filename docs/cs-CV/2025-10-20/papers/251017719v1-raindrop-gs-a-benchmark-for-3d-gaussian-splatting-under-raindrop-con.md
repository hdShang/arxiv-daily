---
layout: default
title: Raindrop GS: A Benchmark for 3D Gaussian Splatting under Raindrop Conditions
---

# Raindrop GS: A Benchmark for 3D Gaussian Splatting under Raindrop Conditions

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.17719" target="_blank" class="toolbar-btn">arXiv: 2510.17719v1</a>
    <a href="https://arxiv.org/pdf/2510.17719.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17719v1" 
            onclick="toggleFavorite(this, '2510.17719v1', 'Raindrop GS: A Benchmark for 3D Gaussian Splatting under Raindrop Conditions')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhiqiang Teng, Beibei Lin, Tingting Chen, Zifeng Yuan, Xuanyi Li, Xuanyu Zhang, Shunli Zhang

**分类**: cs.CV

**发布日期**: 2025-10-20

---

## 💡 一句话要点

**Raindrop GS：提出雨滴环境下3D高斯溅射重建的综合评测基准**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `雨滴环境` `三维重建` `基准数据集` `相机位姿估计`

## 📋 核心要点

1. 现有3DGS方法在雨滴环境下，由于遮挡、畸变和位姿估计误差，重建质量显著下降。
2. RaindropGS基准旨在提供真实雨滴数据，评估从原始图像到最终重建的完整3DGS流程。
3. 实验分析揭示了相机聚焦位置、位姿估计误差等因素对3DGS重建性能的影响。

## 📝 摘要（中文）

本文提出了RaindropGS，一个用于评估雨滴条件下3D高斯溅射(3DGS)性能的综合基准。雨滴会导致严重的遮挡和光学畸变，显著降低重建质量。现有基准通常使用已知相机位姿的合成雨滴图像进行评估，过于理想化。真实场景中，雨滴会干扰相机位姿估计和点云初始化，且合成雨滴与真实雨滴存在显著的领域差距。RaindropGS旨在评估从受雨滴干扰的无约束图像到清晰3DGS重建的完整流程，包括数据准备、数据处理和雨滴感知的3DGS评估。该基准包含真实雨滴重建数据集，每个场景包含对齐的雨滴聚焦、背景聚焦和无雨真值图像集。实验分析揭示了现有3DGS方法在无约束雨滴图像上的性能瓶颈，以及不同流程组件的影响，为开发更鲁棒的雨滴条件下的3DGS方法提供了明确的方向。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射方法在雨滴环境下表现不佳，主要原因是雨滴造成的遮挡和光学畸变，以及相机位姿估计和点云初始化的困难。现有基准主要使用合成数据，与真实雨滴场景存在较大差距，无法有效评估算法的泛化能力。此外，现有方法通常假设相机位姿已知，忽略了雨滴对位姿估计的影响。

**核心思路**：RaindropGS的核心思路是构建一个更贴近真实场景的雨滴数据集，并提供一个完整的评估流程，从原始图像到最终的3DGS重建。该基准旨在评估3DGS方法在真实雨滴环境下的鲁棒性和泛化能力，并分析不同因素对重建质量的影响。

**技术框架**：RaindropGS基准的整体流程包括三个主要部分：数据准备、数据处理和雨滴感知的3DGS评估。数据准备阶段收集真实雨滴场景的数据，并提供对齐的雨滴聚焦、背景聚焦和无雨真值图像集。数据处理阶段包括相机位姿估计、点云初始化和单图像去雨比较。雨滴感知的3DGS评估阶段则对3DGS训练结果进行评估。

**关键创新**：RaindropGS的关键创新在于其真实雨滴数据集和完整的评估流程。该数据集包含多种雨滴干扰类型，并提供不同聚焦条件下的图像，可以更全面地评估3DGS方法在雨滴环境下的性能。评估流程则涵盖了从原始图像到最终重建的各个环节，可以更深入地分析不同因素对重建质量的影响。

**关键设计**：RaindropGS数据集包含多个真实雨滴场景，每个场景包含三个对齐的图像集：雨滴聚焦、背景聚焦和无雨真值。这种设计允许研究人员评估不同聚焦条件下的重建质量，并分析雨滴对重建的影响。评估指标包括重建质量、位姿估计精度和去雨效果等。

## 📊 实验亮点

实验结果表明，现有3DGS方法在RaindropGS基准上表现不佳，尤其是在相机位姿估计和点云初始化方面。实验还发现，相机聚焦位置对重建质量有显著影响，雨滴聚焦图像会导致重建质量下降。这些发现为改进3DGS方法在雨滴环境下的性能提供了重要的指导。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、户外监控等领域，提升这些系统在雨天环境下的感知能力。通过RaindropGS基准，可以促进更鲁棒的3D重建算法的开发，提高系统在恶劣天气条件下的可靠性。未来，该基准可以扩展到其他天气条件，如雾、雪等。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) under raindrop conditions suffers from severe occlusions and optical distortions caused by raindrop contamination on the camera lens, substantially degrading reconstruction quality. Existing benchmarks typically evaluate 3DGS using synthetic raindrop images with known camera poses (constrained images), assuming ideal conditions. However, in real-world scenarios, raindrops often interfere with accurate camera pose estimation and point cloud initialization. Moreover, a significant domain gap between synthetic and real raindrops further impairs generalization. To tackle these issues, we introduce RaindropGS, a comprehensive benchmark designed to evaluate the full 3DGS pipeline-from unconstrained, raindrop-corrupted images to clear 3DGS reconstructions. Specifically, the whole benchmark pipeline consists of three parts: data preparation, data processing, and raindrop-aware 3DGS evaluation, including types of raindrop interference, camera pose estimation and point cloud initialization, single image rain removal comparison, and 3D Gaussian training comparison. First, we collect a real-world raindrop reconstruction dataset, in which each scene contains three aligned image sets: raindrop-focused, background-focused, and rain-free ground truth, enabling a comprehensive evaluation of reconstruction quality under different focus conditions. Through comprehensive experiments and analyses, we reveal critical insights into the performance limitations of existing 3DGS methods on unconstrained raindrop images and the varying impact of different pipeline components: the impact of camera focus position on 3DGS reconstruction performance, and the interference caused by inaccurate pose and point cloud initialization on reconstruction. These insights establish clear directions for developing more robust 3DGS methods under raindrop conditions.

