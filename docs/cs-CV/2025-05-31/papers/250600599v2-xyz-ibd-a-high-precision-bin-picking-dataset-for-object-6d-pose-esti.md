---
layout: default
title: "XYZ-IBD: A High-precision Bin-picking Dataset for Object 6D Pose Estimation Capturing Real-world Industrial Complexity"
---

# XYZ-IBD: A High-precision Bin-picking Dataset for Object 6D Pose Estimation Capturing Real-world Industrial Complexity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00599" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00599v2</a>
  <a href="https://arxiv.org/pdf/2506.00599.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00599v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00599v2', 'XYZ-IBD: A High-precision Bin-picking Dataset for Object 6D Pose Estimation Capturing Real-world Industrial Complexity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junwen Huang, Jizhong Liang, Jiaqi Hu, Martin Sundermeyer, Peter KT Yu, Nassir Navab, Benjamin Busam

**分类**: cs.CV

**发布日期**: 2025-05-31 (更新: 2025-06-16)

**🔗 代码/项目**: [PROJECT_PAGE](https://xyz-ibd.github.io/XYZ-IBD/)

---

## 💡 一句话要点

**提出XYZ-IBD数据集以解决工业环境中的6D姿态估计问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `6D姿态估计` `数据集` `工业机器人` `深度学习` `计算机视觉` `自动化` `标注技术`

## 📋 核心要点

1. 现有数据集主要集中在家庭物体上，难以应对真实工业环境中的复杂性和挑战。
2. XYZ-IBD数据集通过高精度相机和细致的标注流程，提供了真实工业场景下的6D姿态估计数据。
3. 基准测试显示，在我们的数据集上，现有方法的性能显著下降，强调了真实工业环境的挑战性。

## 📝 摘要（中文）

我们介绍了XYZ-IBD，一个用于6D姿态估计的拾取数据集，捕捉了真实工业环境的复杂性，包括具有挑战性的物体几何形状、反射材料、严重遮挡和密集杂乱。该数据集反映了真实机器人操作场景，具有毫米级精度的标注。与主要关注家庭物体的现有数据集不同，XYZ-IBD代表了尚未解决的真实工业条件。数据集包含15种无纹理、金属且大多对称的物体，具有不同的形状和尺寸。这些物体在高密度的箱子中被严重遮挡和随机排列，复制了真实拾取的挑战。XYZ-IBD使用两台高精度工业相机和一台商用相机收集，提供RGB、灰度和深度图像。它包含75个多视角真实场景，以及在模拟拾取条件下渲染的大规模合成数据集。

## 🔬 方法详解

**问题定义**：本论文旨在解决在真实工业环境中进行6D姿态估计时面临的复杂性和挑战。现有方法多集中于家庭物体，无法有效应对工业场景中的遮挡和杂乱。

**核心思路**：我们提出XYZ-IBD数据集，专注于捕捉真实工业环境中的物体几何、反射特性和高密度排列，通过高精度标注实现毫米级姿态精度。

**技术框架**：数据集的构建包括多个阶段：使用高精度相机采集RGB、灰度和深度图像，进行多视角深度融合，最后通过半自动化标注流程实现精确标注。

**关键创新**：最重要的创新在于数据集的设计，特别是针对工业环境的复杂性进行的细致标注流程，显著提高了姿态估计的准确性。

**关键设计**：在标注过程中使用了抗反射喷雾、深度融合技术和半自动化标注，确保了数据的高质量和准确性。

## 📊 实验亮点

在基准测试中，我们对比了现有的最先进方法，结果显示在XYZ-IBD数据集上，2D检测、6D姿态估计和深度估计任务的性能显著下降，强调了该数据集在真实工业环境中的挑战性。

## 🎯 应用场景

该研究的潜在应用领域包括工业机器人、自动化仓储和制造业等，能够为机器人在复杂环境中的操作提供更为准确的数据支持，推动智能制造的发展。未来，该数据集将为相关领域的研究者提供重要的基准和参考。

## 📄 摘要（原文）

> We introduce XYZ-IBD, a bin-picking dataset for 6D pose estimation that captures real-world industrial complexity, including challenging object geometries, reflective materials, severe occlusions, and dense clutter. The dataset reflects authentic robotic manipulation scenarios with millimeter-accurate annotations. Unlike existing datasets that primarily focus on household objects, which approach saturation,XYZ-IBD represents the unsolved realistic industrial conditions. The dataset features 15 texture-less, metallic, and mostly symmetrical objects of varying shapes and sizes. These objects are heavily occluded and randomly arranged in bins with high density, replicating the challenges of real-world bin-picking. XYZ-IBD was collected using two high-precision industrial cameras and one commercially available camera, providing RGB, grayscale, and depth images. It contains 75 multi-view real-world scenes, along with a large-scale synthetic dataset rendered under simulated bin-picking conditions. We employ a meticulous annotation pipeline that includes anti-reflection spray, multi-view depth fusion, and semi-automatic annotation, achieving millimeter-level pose labeling accuracy required for industrial manipulation. Quantification in simulated environments confirms the reliability of the ground-truth annotations. We benchmark state-of-the-art methods on 2D detection, 6D pose estimation, and depth estimation tasks on our dataset, revealing significant performance degradation in our setups compared to current academic household benchmarks. By capturing the complexity of real-world bin-picking scenarios, XYZ-IBD introduces more realistic and challenging problems for future research. The dataset and benchmark are publicly available at https://xyz-ibd.github.io/XYZ-IBD/.

