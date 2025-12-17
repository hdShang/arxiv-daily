---
layout: default
title: ShelfOcc: Native 3D Supervision beyond LiDAR for Vision-Based Occupancy Estimation
---

# ShelfOcc: Native 3D Supervision beyond LiDAR for Vision-Based Occupancy Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15396" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15396v1</a>
  <a href="https://arxiv.org/pdf/2511.15396.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15396v1" onclick="toggleFavorite(this, '2511.15396v1', 'ShelfOcc: Native 3D Supervision beyond LiDAR for Vision-Based Occupancy Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simon Boeder, Fabian Gigengack, Simon Roesler, Holger Caesar, Benjamin Risse

**分类**: cs.CV

**发布日期**: 2025-11-19

---

## 💡 一句话要点

**ShelfOcc：提出一种纯视觉的3D体素占据估计方法，无需激光雷达即可实现原生3D监督。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `体素占据估计` `纯视觉` `3D场景理解` `自监督学习` `弱监督学习` `深度学习` `自动驾驶`

## 📋 核心要点

1. 现有自监督/弱监督占据估计方法依赖2D投影，存在几何不一致和深度泄露问题。
2. ShelfOcc提出一种纯视觉方法，从视频生成度量一致的3D体素标签，实现原生3D监督。
3. 在Occ3D-nuScenes上，ShelfOcc显著优于之前的弱监督/自监督方法，相对提升高达34%。

## 📝 摘要（中文）

本文提出ShelfOcc，一种纯视觉的体素占据估计方法，克服了以往基于2D投影或渲染监督的几何不一致性和深度泄露问题，无需激光雷达即可实现原生3D监督。ShelfOcc通过视频生成度量一致的语义体素标签，实现真正的3D监督，无需额外的传感器或手动3D标注。虽然现有的基于视觉的3D几何基础模型提供了一种有前景的先验知识来源，但由于几何体的稀疏、噪声和不一致性，尤其是在动态驾驶场景中，它们无法直接用作预测。本文方法引入了一个专用框架，通过跨帧一致地过滤和积累静态几何体、处理动态内容以及将语义信息传播到稳定的体素表示中来缓解这些问题。这种以数据为中心的弱监督/自监督体素占据估计的监督方式，允许使用任何SOTA体素占据模型架构，而无需依赖激光雷达数据。高质量的监督对于鲁棒的体素占据学习至关重要，并且是架构创新的重要补充。在Occ3D-nuScenes基准测试中，ShelfOcc显著优于所有先前的弱监督/自监督方法（高达34%的相对改进），为无激光雷达的3D场景理解建立了一个新的数据驱动方向。

## 🔬 方法详解

**问题定义**：论文旨在解决在没有激光雷达数据的情况下，如何利用纯视觉信息进行精确的3D体素占据估计。现有方法主要依赖于2D投影或渲染进行监督，这导致了严重的几何不一致性和深度泄露问题，限制了3D场景理解的准确性。

**核心思路**：论文的核心思路是通过视频数据生成高质量的3D体素标签，从而实现原生3D监督。通过跨帧积累静态几何信息，过滤动态内容，并将语义信息传播到稳定的体素表示中，从而克服了现有视觉3D几何基础模型的稀疏性、噪声和不一致性问题。

**技术框架**：ShelfOcc框架主要包含以下几个阶段：1) 从视频帧中提取视觉特征；2) 利用视觉3D几何基础模型（如深度估计网络）生成初始的3D几何体；3) 通过跨帧一致性过滤和积累静态几何体，消除噪声和不一致性；4) 处理动态内容，例如通过光流或语义分割区分动态物体；5) 将语义信息传播到体素表示中，生成最终的3D体素占据标签。

**关键创新**：该方法最重要的创新在于提出了一个数据驱动的3D监督框架，能够从纯视觉数据中生成高质量的3D体素标签，而无需依赖激光雷达数据或手动3D标注。这与以往依赖2D投影或渲染进行监督的方法有着本质的区别，避免了几何不一致性和深度泄露问题。

**关键设计**：关键设计包括：1) 跨帧一致性过滤算法，用于消除噪声和不一致性；2) 动态内容处理模块，用于区分和处理动态物体；3) 语义信息传播机制，用于将语义信息从图像空间传播到体素空间；4) 体素表示的构建方式，例如体素大小、体素范围等。

## 📊 实验亮点

ShelfOcc在Occ3D-nuScenes基准测试中取得了显著的性能提升，大幅超越了所有先前的弱监督/自监督方法，相对提升高达34%。这表明该方法生成的3D体素标签质量很高，能够有效提升3D场景理解的准确性。实验结果验证了该方法在无激光雷达条件下的有效性和优越性。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、机器人导航、场景重建等领域。通过纯视觉的3D场景理解，可以降低对昂贵激光雷达传感器的依赖，从而降低成本并提高系统的鲁棒性。未来，该技术有望应用于智能交通、智慧城市等领域，实现更安全、更高效的智能化服务。

## 📄 摘要（原文）

> Recent progress in self- and weakly supervised occupancy estimation has largely relied on 2D projection or rendering-based supervision, which suffers from geometric inconsistencies and severe depth bleeding. We thus introduce ShelfOcc, a vision-only method that overcomes these limitations without relying on LiDAR. ShelfOcc brings supervision into native 3D space by generating metrically consistent semantic voxel labels from video, enabling true 3D supervision without any additional sensors or manual 3D annotations. While recent vision-based 3D geometry foundation models provide a promising source of prior knowledge, they do not work out of the box as a prediction due to sparse or noisy and inconsistent geometry, especially in dynamic driving scenes. Our method introduces a dedicated framework that mitigates these issues by filtering and accumulating static geometry consistently across frames, handling dynamic content and propagating semantic information into a stable voxel representation. This data-centric shift in supervision for weakly/shelf-supervised occupancy estimation allows the use of essentially any SOTA occupancy model architecture without relying on LiDAR data. We argue that such high-quality supervision is essential for robust occupancy learning and constitutes an important complementary avenue to architectural innovation. On the Occ3D-nuScenes benchmark, ShelfOcc substantially outperforms all previous weakly/shelf-supervised methods (up to a 34% relative improvement), establishing a new data-driven direction for LiDAR-free 3D scene understanding.

