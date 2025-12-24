---
layout: default
title: "VAR-SLAM: Visual Adaptive and Robust SLAM for Dynamic Environments"
---

# VAR-SLAM: Visual Adaptive and Robust SLAM for Dynamic Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16205" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16205v1</a>
  <a href="https://arxiv.org/pdf/2510.16205.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16205v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16205v1', 'VAR-SLAM: Visual Adaptive and Robust SLAM for Dynamic Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: João Carlos Virgolino Soares, Gabriel Fischer Abati, Claudio Semini

**分类**: cs.RO

**发布日期**: 2025-10-17

**备注**: Code available at https://github.com/iit-DLSLab/VAR-SLAM

---

## 💡 一句话要点

**VAR-SLAM：面向动态环境的视觉自适应鲁棒SLAM**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉SLAM` `动态环境` `鲁棒性` `自适应损失函数` `语义分割` `ORB-SLAM3`

## 📋 核心要点

1. 现有动态环境SLAM方法依赖于语义过滤或固定鲁棒核，无法有效处理未知移动对象，导致精度下降。
2. VAR-SLAM结合语义关键点过滤和Barron自适应鲁棒损失，在线估计鲁棒核形状参数，适应不同移动对象。
3. 实验结果表明，VAR-SLAM在多个数据集上优于现有方法，ATE RMSE降低高达25%，并保持实时性能。

## 📝 摘要（中文）

在动态环境中进行视觉SLAM仍然具有挑战性，因为许多现有方法依赖于仅处理已知对象类别的语义过滤，或者使用无法适应未知移动对象的固定鲁棒核，导致当它们出现在场景中时精度下降。我们提出了VAR-SLAM（视觉自适应鲁棒SLAM），这是一个基于ORB-SLAM3的系统，它结合了一个轻量级的语义关键点滤波器来处理已知的移动对象，以及Barron的自适应鲁棒损失来处理未知的移动对象。鲁棒核的形状参数根据残差在线估计，允许系统在Gaussian和重尾行为之间自动调整。我们在TUM RGB-D、Bonn RGB-D Dynamic和OpenLORIS数据集上评估了VAR-SLAM，这些数据集包括已知和未知的移动对象。结果表明，与最先进的基线相比，轨迹精度和鲁棒性得到了提高，在具有挑战性的序列上，ATE RMSE比NGD-SLAM降低了高达25%，同时保持了平均27 FPS的性能。

## 🔬 方法详解

**问题定义**：动态环境下的视觉SLAM面临的挑战是如何有效地处理场景中移动的物体，特别是那些未知的、未被预先定义的物体。现有的方法要么依赖于语义信息，只能处理已知的物体类别，要么使用固定的鲁棒核，无法适应不同类型和运动状态的移动物体，导致SLAM系统的精度和鲁棒性下降。

**核心思路**：VAR-SLAM的核心思路是结合语义信息和自适应鲁棒损失函数，以同时处理已知和未知的移动物体。对于已知的移动物体，使用轻量级的语义关键点滤波器进行过滤。对于未知的移动物体，则利用Barron的自适应鲁棒损失函数，该函数可以根据残差的大小动态调整损失函数的形状，从而降低移动物体对SLAM系统的影响。

**技术框架**：VAR-SLAM基于ORB-SLAM3构建，主要包含以下几个模块：1) 特征提取与匹配：使用ORB特征进行提取和匹配。2) 语义关键点过滤：利用语义信息过滤掉已知移动物体的关键点。3) 运动估计：使用PnP算法估计相机运动。4) 地图构建与优化：构建稀疏地图，并使用Bundle Adjustment进行优化。5) 自适应鲁棒损失：在Bundle Adjustment中使用Barron损失函数，并在线估计其形状参数。

**关键创新**：VAR-SLAM的关键创新在于引入了Barron自适应鲁棒损失函数，并将其应用于动态环境下的视觉SLAM。通过在线估计Barron损失函数的形状参数，系统可以自动调整对不同残差的权重，从而有效地降低移动物体对SLAM系统的影响。这种自适应性使得VAR-SLAM能够更好地处理未知的移动物体，提高SLAM系统的鲁棒性和精度。

**关键设计**：Barron损失函数的形状参数是VAR-SLAM的关键设计。该参数通过在线估计残差的大小来动态调整。具体来说，系统会计算每个关键点的残差，并根据残差的分布来估计Barron损失函数的形状参数。这种在线估计的方式使得VAR-SLAM能够适应不同的场景和移动物体，从而提高SLAM系统的性能。

## 📊 实验亮点

VAR-SLAM在TUM RGB-D、Bonn RGB-D Dynamic和OpenLORIS数据集上进行了评估，结果表明其在轨迹精度和鲁棒性方面优于现有方法。在具有挑战性的序列上，VAR-SLAM的ATE RMSE比NGD-SLAM降低了高达25%，同时保持了平均27 FPS的性能。这些结果表明，VAR-SLAM能够有效地处理动态环境下的视觉SLAM问题。

## 🎯 应用场景

VAR-SLAM在机器人导航、自动驾驶、增强现实等领域具有广泛的应用前景。尤其是在动态环境中，例如人流密集的商场、街道等，VAR-SLAM能够提供更准确、更鲁棒的定位和地图构建能力，从而提高机器人的自主性和安全性。此外，该方法还可以应用于三维重建、场景理解等任务。

## 📄 摘要（原文）

> Visual SLAM in dynamic environments remains challenging, as several existing methods rely on semantic filtering that only handles known object classes, or use fixed robust kernels that cannot adapt to unknown moving objects, leading to degraded accuracy when they appear in the scene. We present VAR-SLAM (Visual Adaptive and Robust SLAM), an ORB-SLAM3-based system that combines a lightweight semantic keypoint filter to deal with known moving objects, with Barron's adaptive robust loss to handle unknown ones. The shape parameter of the robust kernel is estimated online from residuals, allowing the system to automatically adjust between Gaussian and heavy-tailed behavior. We evaluate VAR-SLAM on the TUM RGB-D, Bonn RGB-D Dynamic, and OpenLORIS datasets, which include both known and unknown moving objects. Results show improved trajectory accuracy and robustness over state-of-the-art baselines, achieving up to 25% lower ATE RMSE than NGD-SLAM on challenging sequences, while maintaining performance at 27 FPS on average.

