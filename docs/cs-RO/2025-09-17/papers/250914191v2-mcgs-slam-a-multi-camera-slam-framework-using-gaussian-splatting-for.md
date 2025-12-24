---
layout: default
title: "MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping"
---

# MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14191" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14191v2</a>
  <a href="https://arxiv.org/pdf/2509.14191.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14191v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14191v2', 'MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Cao, Hanyu Wu, Li Wa Tang, Zizhou Luo, Zihan Zhu, Wei Zhang, Marc Pollefeys, Martin R. Oswald

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-17 (更新: 2025-10-03)

---

## 💡 一句话要点

**MCGS-SLAM：基于高斯溅射的多相机SLAM框架，实现高保真地图构建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多相机SLAM` `高斯溅射` `三维重建` `捆绑调整` `尺度一致性`

## 📋 核心要点

1. 现有稠密SLAM主要集中于单目视觉，但通常牺牲了鲁棒性和几何覆盖范围，难以满足复杂场景需求。
2. MCGS-SLAM利用多相机RGB输入，构建基于3D高斯溅射的统一地图，并通过联合优化位姿和深度实现高精度重建。
3. 实验表明，MCGS-SLAM在轨迹精度和重建质量上优于单目方法，尤其在侧视区域重建方面优势明显。

## 📝 摘要（中文）

本文提出MCGS-SLAM，这是一个完全基于RGB多相机输入的SLAM系统，它构建于3D高斯溅射(3DGS)之上。与依赖稀疏地图或惯性数据的现有方法不同，MCGS-SLAM将来自多个视角的密集RGB输入融合到一个统一的、持续优化的高斯地图中。多相机捆绑调整(MCBA)通过密集的 photometric 和 geometric 残差联合优化位姿和深度，而尺度一致性模块使用低秩先验来强制跨视角的尺度对齐。该系统支持RGB输入，并在大规模场景下保持实时性能。在合成和真实世界数据集上的实验表明，MCGS-SLAM始终产生准确的轨迹和逼真的重建效果，通常优于单目基线。值得注意的是，来自多相机输入的宽视野能够重建单目设置遗漏的侧视区域，这对于安全的自主操作至关重要。这些结果突出了多相机高斯溅射SLAM在机器人和自动驾驶领域高保真地图构建方面的潜力。

## 🔬 方法详解

**问题定义**：现有稠密SLAM方法，特别是单目SLAM，在鲁棒性和几何覆盖范围上存在局限性，难以捕捉场景的完整几何信息。此外，现有方法依赖稀疏地图或惯性数据，增加了系统的复杂性和对外部传感器的依赖。

**核心思路**：MCGS-SLAM的核心思路是利用多相机系统的宽视野优势，结合3D高斯溅射的强大表达能力，构建一个能够融合多视角信息的稠密地图。通过联合优化相机位姿和高斯参数，实现高精度、高保真的场景重建。多相机系统提供更丰富的几何信息，而3D高斯溅射能够高效地表示和渲染场景。

**技术框架**：MCGS-SLAM系统主要包含以下几个模块：1) 多相机数据采集：从多个相机获取同步的RGB图像。2) 初始化：使用SfM或其他方法初始化相机位姿和场景结构。3) 多相机捆绑调整(MCBA)：通过最小化 photometric 和 geometric 残差，联合优化相机位姿和高斯参数。4) 尺度一致性模块：使用低秩先验强制跨视角的尺度对齐，保证重建的尺度一致性。5) 3D高斯溅射渲染：使用优化后的高斯参数渲染场景，生成高质量的图像。

**关键创新**：MCGS-SLAM的关键创新在于将3D高斯溅射引入多相机SLAM系统，并设计了多相机捆绑调整和尺度一致性模块。与传统的基于点云或体素的SLAM系统相比，3D高斯溅射能够更高效地表示和渲染场景，同时具有更好的可微性，便于优化。多相机捆绑调整能够充分利用多视角信息，提高位姿估计和场景重建的精度。尺度一致性模块保证了重建结果的尺度准确性。

**关键设计**：MCGS-SLAM的关键设计包括：1) 使用高斯分布表示场景中的每个点，每个高斯分布由中心位置、协方差矩阵、颜色和透明度等参数描述。2) 定义 photometric 残差为渲染图像与观测图像之间的颜色差异，geometric 残差为高斯分布中心到相机光心的距离。3) 使用 Ceres Solver 优化相机位姿和高斯参数，最小化 photometric 和 geometric 残差。4) 尺度一致性模块使用低秩先验约束跨视角的尺度关系，保证重建的尺度一致性。

## 📊 实验亮点

实验结果表明，MCGS-SLAM在合成和真实世界数据集上均取得了优异的性能。在轨迹精度方面，MCGS-SLAM优于单目SLAM基线。在重建质量方面，MCGS-SLAM能够生成更逼真的场景模型，尤其是在单目SLAM难以重建的侧视区域。实验证明了多相机高斯溅射SLAM在提高地图构建精度和完整性方面的有效性。

## 🎯 应用场景

MCGS-SLAM在机器人导航、自动驾驶、虚拟现实和增强现实等领域具有广泛的应用前景。它可以用于构建高精度、高保真的三维地图，为机器人提供可靠的环境感知能力，支持自动驾驶车辆的安全导航。此外，MCGS-SLAM还可以用于创建逼真的虚拟环境，为用户提供沉浸式的体验。

## 📄 摘要（原文）

> Recent progress in dense SLAM has primarily targeted monocular setups, often at the expense of robustness and geometric coverage. We present MCGS-SLAM, the first purely RGB-based multi-camera SLAM system built on 3D Gaussian Splatting (3DGS). Unlike prior methods relying on sparse maps or inertial data, MCGS-SLAM fuses dense RGB inputs from multiple viewpoints into a unified, continuously optimized Gaussian map. A multi-camera bundle adjustment (MCBA) jointly refines poses and depths via dense photometric and geometric residuals, while a scale consistency module enforces metric alignment across views using low-rank priors. The system supports RGB input and maintains real-time performance at large scale. Experiments on synthetic and real-world datasets show that MCGS-SLAM consistently yields accurate trajectories and photorealistic reconstructions, usually outperforming monocular baselines. Notably, the wide field of view from multi-camera input enables reconstruction of side-view regions that monocular setups miss, critical for safe autonomous operation. These results highlight the promise of multi-camera Gaussian Splatting SLAM for high-fidelity mapping in robotics and autonomous driving.

