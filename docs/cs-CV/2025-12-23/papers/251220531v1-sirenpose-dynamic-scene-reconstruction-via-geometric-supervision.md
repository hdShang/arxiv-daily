---
layout: default
title: SirenPose: Dynamic Scene Reconstruction via Geometric Supervision
---

# SirenPose: Dynamic Scene Reconstruction via Geometric Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20531" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20531v1</a>
  <a href="https://arxiv.org/pdf/2512.20531.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20531v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20531v1', 'SirenPose: Dynamic Scene Reconstruction via Geometric Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaitong Cai, Jensen Zhang, Jing Yang, Keze Wang

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: Under submission

---

## 💡 一句话要点

**SirenPose：通过几何监督实现动态场景的精确重建与时序一致性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `动态场景重建` `几何监督` `正弦表示网络` `时序一致性` `关键点检测` `图神经网络` `单目视频` `三维重建`

## 📋 核心要点

1. 现有动态场景重建方法在处理快速运动、多物体交互和遮挡等复杂场景时，难以保证重建结果的运动真实性和时空一致性。
2. SirenPose 利用 SIREN 的周期激活特性和关键点几何约束，并引入物理启发的约束，以提升关键点预测的时空连贯性，并捕获细粒度的几何细节。
3. 实验表明，SirenPose 在多个数据集上显著优于现有方法，在时间一致性、几何精度和运动平滑度等方面均有提升。

## 📝 摘要（中文）

SirenPose 是一种几何感知损失函数，它将正弦表示网络 (SIREN) 的周期激活特性与基于关键点的几何监督相结合，从而能够从单目视频中准确且在时间上一致地重建动态 3D 场景。现有方法在快速运动、多对象交互、遮挡和快速场景变化等具有挑战性的环境中，通常难以保证运动的真实性和时空连贯性。SirenPose 结合了受物理学启发的约束，以确保空间和时间维度上关键点预测的连贯性，同时利用高频信号建模来捕获细粒度的几何细节。此外，我们还将 UniKPT 数据集扩展到 600,000 个带注释的实例，并集成图神经网络来建模关键点关系和结构相关性。在 Sintel、Bonn 和 DAVIS 等基准测试上的大量实验表明，SirenPose 始终优于最先进的方法。在 DAVIS 上，SirenPose 在 FVD 方面降低了 17.8%，在 FID 方面降低了 28.7%，在 LPIPS 方面提高了 6.0%（与 MoSCA 相比）。它还提高了时间一致性、几何精度、用户评分和运动平滑度。在姿态估计方面，SirenPose 优于 Monst3R，具有更低的绝对轨迹误差以及更小的平移和旋转相对姿态误差，突显了其在处理快速运动、复杂动力学和物理上合理的重建方面的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决从单目视频中重建动态 3D 场景的问题，尤其是在快速运动、多对象交互、遮挡和快速场景变化等复杂场景下。现有方法难以保证重建结果的运动真实性和时空连贯性，导致重建质量下降。

**核心思路**：论文的核心思路是将 SIREN 的周期激活特性与基于关键点的几何监督相结合，并引入物理启发的约束，从而提升关键点预测的时空连贯性，并捕获细粒度的几何细节。SIREN 擅长表示高频信号，有助于捕捉场景的细节信息。

**技术框架**：SirenPose 的整体框架包含以下几个主要模块：1) 关键点检测与跟踪：使用预训练的关键点检测器和跟踪器从视频中提取关键点信息。2) SIREN 网络：使用 SIREN 网络表示动态场景的 3D 几何信息。3) 几何损失函数：设计几何损失函数，将关键点信息与 SIREN 网络的输出进行约束，保证重建结果的几何精度。4) 时序一致性约束：引入物理启发的约束，保证关键点预测在时间上的连贯性。5) 图神经网络：使用图神经网络建模关键点之间的关系和结构相关性。

**关键创新**：SirenPose 的关键创新在于：1) 提出了几何感知的损失函数，将 SIREN 的周期激活特性与关键点几何约束相结合。2) 引入了物理启发的约束，保证关键点预测在时间上的连贯性。3) 利用图神经网络建模关键点之间的关系和结构相关性。这些创新使得 SirenPose 能够更好地处理复杂动态场景的重建问题。

**关键设计**：论文的关键设计包括：1) 使用 SIREN 作为场景表示网络，利用其高频信号建模能力。2) 设计了几何损失函数，包括关键点位置损失、关键点深度损失等。3) 引入了物理启发的约束，例如速度一致性约束、加速度一致性约束等。4) 使用图神经网络建模关键点之间的关系，例如骨骼连接关系等。这些设计有助于提升重建结果的几何精度和时序一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20531v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20531v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20531v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SirenPose 在 DAVIS 数据集上取得了显著的性能提升，FVD 指标降低了 17.8%，FID 指标降低了 28.7%，LPIPS 指标提高了 6.0%（与 MoSCA 相比）。此外，在姿态估计方面，SirenPose 优于 Monst3R，具有更低的绝对轨迹误差以及更小的平移和旋转相对姿态误差，证明了其在处理快速运动和复杂动力学场景下的有效性。

## 🎯 应用场景

SirenPose 技术可应用于机器人导航、自动驾驶、虚拟现实/增强现实、运动捕捉和视频游戏等领域。它能够帮助机器人更好地理解周围环境，实现更精确的定位和导航。在自动驾驶领域，可以用于重建车辆周围的动态场景，提高驾驶安全性。在 VR/AR 领域，可以用于创建更逼真的虚拟体验。在运动捕捉和视频游戏领域，可以用于生成更自然的动画效果。

## 📄 摘要（原文）

> We introduce SirenPose, a geometry-aware loss formulation that integrates the periodic activation properties of sinusoidal representation networks with keypoint-based geometric supervision, enabling accurate and temporally consistent reconstruction of dynamic 3D scenes from monocular videos. Existing approaches often struggle with motion fidelity and spatiotemporal coherence in challenging settings involving fast motion, multi-object interaction, occlusion, and rapid scene changes. SirenPose incorporates physics inspired constraints to enforce coherent keypoint predictions across both spatial and temporal dimensions, while leveraging high frequency signal modeling to capture fine grained geometric details. We further expand the UniKPT dataset to 600,000 annotated instances and integrate graph neural networks to model keypoint relationships and structural correlations. Extensive experiments on benchmarks including Sintel, Bonn, and DAVIS demonstrate that SirenPose consistently outperforms state-of-the-art methods. On DAVIS, SirenPose achieves a 17.8 percent reduction in FVD, a 28.7 percent reduction in FID, and a 6.0 percent improvement in LPIPS compared to MoSCA. It also improves temporal consistency, geometric accuracy, user score, and motion smoothness. In pose estimation, SirenPose outperforms Monst3R with lower absolute trajectory error as well as reduced translational and rotational relative pose error, highlighting its effectiveness in handling rapid motion, complex dynamics, and physically plausible reconstruction.

