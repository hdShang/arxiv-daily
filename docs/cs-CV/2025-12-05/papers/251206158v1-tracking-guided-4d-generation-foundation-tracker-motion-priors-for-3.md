---
layout: default
title: Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation
---

# Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06158" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06158v1</a>
  <a href="https://arxiv.org/pdf/2512.06158.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06158v1" onclick="toggleFavorite(this, '2512.06158v1', 'Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Su Sun, Cheng Zhao, Himangi Mittal, Gaurav Mittal, Rohith Kukkala, Yingjie Victor Chen, Mei Chen

**分类**: cs.CV

**发布日期**: 2025-12-05

**备注**: 15 pages, 11 figures

---

## 💡 一句话要点

**提出Track4DGen，利用跟踪引导的运动先验实现高质量3D模型动画生成。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `4D生成` `动态3D模型` `运动跟踪` `扩散模型` `高斯溅射` `时间一致性` `多视角视频`

## 📋 核心要点

1. 现有方法在从稀疏输入生成动态4D对象时，难以同时保证外观和运动的一致性，并容易出现时间漂移。
2. Track4DGen通过将跟踪器导出的运动先验注入到多视角视频生成和4D-GS的中间特征表示中，显式地利用时间信息。
3. Track4DGen在多视角视频生成和4D生成任务上超越了现有基线方法，生成了时间稳定的、可编辑的4D模型。

## 📝 摘要（中文）

从稀疏输入生成动态4D对象极具挑战，它需要在跨视角和时间上联合保持外观和运动一致性，同时抑制伪影和时间漂移。我们认为，视角差异源于仅限于像素或潜在空间视频扩散损失的监督，这些损失缺乏显式的时间感知、特征级别的跟踪指导。我们提出了Track4DGen，这是一个两阶段框架，它将多视角视频扩散模型与基础点跟踪器和混合4D高斯溅射(4D-GS)重建器相结合。核心思想是将跟踪器导出的运动先验显式地注入到多视角视频生成和4D-GS的中间特征表示中。在第一阶段，我们在扩散生成器内部强制执行密集的特征级别点对应关系，从而产生时间上一致的特征，抑制外观漂移并增强跨视角一致性。在第二阶段，我们使用混合运动编码重建动态4D-GS，该编码将共定位的扩散特征(携带第一阶段跟踪先验)与Hex-plane特征连接起来，并使用4D球谐函数对其进行增强，以实现更高保真度的动态建模。Track4DGen在多视角视频生成和4D生成基准测试中均优于基线，从而产生时间稳定的、文本可编辑的4D资产。最后，我们策划了Sketchfab28，这是一个高质量的数据集，用于基准测试以对象为中心的4D生成并促进未来的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决从稀疏输入生成高质量、时间一致的动态4D对象的问题。现有方法主要依赖于像素或潜在空间的视频扩散损失，缺乏显式的时间感知和特征级别的跟踪指导，导致生成结果在视角和时间上不一致，容易出现伪影和时间漂移。

**核心思路**：论文的核心思路是将跟踪器导出的运动先验显式地注入到多视角视频生成和4D-GS重建过程中。通过在特征级别引入时间一致性约束，可以有效地抑制外观漂移，增强跨视角一致性，从而生成更稳定、更真实的动态4D对象。

**技术框架**：Track4DGen是一个两阶段框架：
1. **多视角视频生成阶段**：利用多视角视频扩散模型，并强制执行密集的特征级别点对应关系，生成时间一致的特征。
2. **4D-GS重建阶段**：使用混合运动编码重建动态4D-GS，将扩散特征（携带跟踪先验）与Hex-plane特征连接，并使用4D球谐函数增强动态建模能力。

**关键创新**：该方法最重要的创新点在于将基础点跟踪器与扩散模型相结合，显式地将跟踪信息作为运动先验注入到特征表示中。这与现有方法仅依赖于像素或潜在空间的损失函数进行监督有本质区别，能够更好地保证生成结果的时间一致性和跨视角一致性。

**关键设计**：
*   **混合运动编码**：结合扩散特征和Hex-plane特征，充分利用跟踪先验和几何信息。
*   **4D球谐函数**：用于更高保真度的动态建模。
*   **Sketchfab28数据集**：用于评估和比较4D生成方法的性能。

## 📊 实验亮点

Track4DGen在多视角视频生成和4D生成基准测试中均超越了现有基线方法，生成了时间稳定的、文本可编辑的4D模型。论文还贡献了一个高质量的4D数据集Sketchfab28，为未来的研究提供了基准。

## 🎯 应用场景

Track4DGen在游戏开发、电影制作、虚拟现实/增强现实等领域具有广泛的应用前景。它可以用于快速生成高质量的动态3D模型，例如动画角色、运动物体等，从而降低内容创作的成本和时间。此外，该方法还可以用于从视频中重建动态场景，为三维重建和场景理解提供新的思路。

## 📄 摘要（原文）

> Generating dynamic 4D objects from sparse inputs is difficult because it demands joint preservation of appearance and motion coherence across views and time while suppressing artifacts and temporal drift. We hypothesize that the view discrepancy arises from supervision limited to pixel- or latent-space video-diffusion losses, which lack explicitly temporally aware, feature-level tracking guidance. We present \emph{Track4DGen}, a two-stage framework that couples a multi-view video diffusion model with a foundation point tracker and a hybrid 4D Gaussian Splatting (4D-GS) reconstructor. The central idea is to explicitly inject tracker-derived motion priors into intermediate feature representations for both multi-view video generation and 4D-GS. In Stage One, we enforce dense, feature-level point correspondences inside the diffusion generator, producing temporally consistent features that curb appearance drift and enhance cross-view coherence. In Stage Two, we reconstruct a dynamic 4D-GS using a hybrid motion encoding that concatenates co-located diffusion features (carrying Stage-One tracking priors) with Hex-plane features, and augment them with 4D Spherical Harmonics for higher-fidelity dynamics modeling. \emph{Track4DGen} surpasses baselines on both multi-view video generation and 4D generation benchmarks, yielding temporally stable, text-editable 4D assets. Lastly, we curate \emph{Sketchfab28}, a high-quality dataset for benchmarking object-centric 4D generation and fostering future research.

