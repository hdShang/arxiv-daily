---
layout: default
title: 4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction
---

# 4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16564" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16564v1</a>
  <a href="https://arxiv.org/pdf/2512.16564.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16564v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16564v1', '4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kirill Mazur, Marwan Taher, Andrew J. Davison

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: For project page, see https://makezur.github.io/4DPM/

---

## 💡 一句话要点

**提出4D Primitive-Mâché，用于单目视频的持久化4D场景重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `4D重建` `动态场景` `单目视觉` `刚性图元` `运动估计` `场景理解` `持久化重建`

## 📋 核心要点

1. 现有动态场景重建方法难以重建所有时间步长的完整场景，尤其是在物体遮挡或离开视野后。
2. 该论文提出将场景分解为刚性3D图元，通过优化方法联合推断图元的刚性运动，实现4D场景重建。
3. 实验结果表明，该方法在物体扫描和多物体数据集上，显著优于现有方法，实现了更好的重建效果。

## 📝 摘要（中文）

本文提出了一种动态重建系统，该系统以单目RGB视频作为输入，输出场景的完整且持久的重建结果。换句话说，我们不仅重建当前可见的场景部分，还重建所有先前观察到的部分，从而能够重放所有时间步长的完整重建。我们的方法将场景分解为一组刚性3D图元，这些图元被认为是在整个场景中移动的。利用估计的密集2D对应关系，我们通过优化流程联合推断这些图元的刚性运动，从而产生场景的4D重建，即提供随时间动态移动的3D几何体。为此，我们还引入了一种机制来推断不可见物体的运动，采用运动分组技术来保持连续性。该系统实现了4D时空感知，提供了诸如随时间推移的可重放3D铰接物体重建、多物体扫描和物体持久性等功能。在物体扫描和多物体数据集上，我们的系统在定量和定性方面均显著优于现有方法。

## 🔬 方法详解

**问题定义**：现有动态场景重建方法通常只能重建当前帧可见的场景部分，无法持久化地重建整个场景，尤其是在物体被遮挡或离开视野后。这限制了对场景的完整理解和后续应用，例如重放特定时间段的场景状态。现有方法在处理复杂运动和遮挡时，重建质量也会显著下降。

**核心思路**：该论文的核心思路是将动态场景分解为一组刚性3D图元，并假设这些图元在场景中进行刚性运动。通过估计图像中的2D对应关系，并优化这些图元的运动参数，可以实现对场景的4D重建，即得到随时间变化的3D几何信息。这种基于图元的表示方法能够更好地处理遮挡和运动，并实现对不可见区域的运动推断。

**技术框架**：该方法主要包含以下几个阶段：1) 输入单目RGB视频；2) 估计图像中的密集2D对应关系；3) 将场景分解为一组刚性3D图元；4) 通过优化方法，联合推断这些图元的刚性运动参数，得到4D重建结果；5) 对于不可见的物体，采用运动分组技术来推断其运动轨迹，保持重建的连续性。

**关键创新**：该方法的关键创新在于：1) 提出了基于刚性3D图元的4D场景表示方法，能够更好地处理遮挡和运动；2) 引入了运动分组技术，用于推断不可见物体的运动轨迹，实现持久化的场景重建；3) 通过联合优化图元的运动参数，实现了对场景的全局一致性重建。

**关键设计**：该方法使用优化框架来估计图元的运动参数。损失函数可能包含以下几个部分：1) 2D对应关系约束，确保图元的投影与图像中的特征点匹配；2) 刚性运动约束，保证图元的运动符合刚性运动的规律；3) 运动平滑约束，避免图元的运动出现突变。具体的优化算法和参数设置未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16564v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16564v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16564v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该系统在物体扫描和多物体数据集上进行了评估，实验结果表明，该方法在定量和定性方面均显著优于现有方法。具体的性能数据和提升幅度未知，但摘要强调了显著的性能提升。

## 🎯 应用场景

该研究成果可应用于增强现实、虚拟现实、机器人导航、自动驾驶等领域。例如，在AR/VR中，可以实现对真实场景的动态重建和交互；在机器人导航中，可以帮助机器人理解周围环境的动态变化，从而做出更合理的决策；在自动驾驶中，可以提高对道路上其他车辆和行人的感知能力，增强安全性。

## 📄 摘要（原文）

> We present a dynamic reconstruction system that receives a casual monocular RGB video as input, and outputs a complete and persistent reconstruction of the scene. In other words, we reconstruct not only the the currently visible parts of the scene, but also all previously viewed parts, which enables replaying the complete reconstruction across all timesteps.
>   Our method decomposes the scene into a set of rigid 3D primitives, which are assumed to be moving throughout the scene. Using estimated dense 2D correspondences, we jointly infer the rigid motion of these primitives through an optimisation pipeline, yielding a 4D reconstruction of the scene, i.e. providing 3D geometry dynamically moving through time. To achieve this, we also introduce a mechanism to extrapolate motion for objects that become invisible, employing motion-grouping techniques to maintain continuity.
>   The resulting system enables 4D spatio-temporal awareness, offering capabilities such as replayable 3D reconstructions of articulated objects through time, multi-object scanning, and object permanence. On object scanning and multi-object datasets, our system significantly outperforms existing methods both quantitatively and qualitatively.

