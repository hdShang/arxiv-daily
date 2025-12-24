---
layout: default
title: "4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction"
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

**提出4D Primitive-Mâché，通过拼接基元实现持久化4D场景重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `4D场景重建` `动态场景` `基元分解` `运动估计` `单目视觉`

## 📋 核心要点

1. 现有动态场景重建方法难以保持场景的完整性和持久性，尤其是在物体遮挡或离开视野后。
2. 该方法将场景分解为可移动的刚性3D基元，通过优化框架联合推断基元的刚性运动，实现4D场景重建。
3. 实验结果表明，该系统在物体扫描和多物体数据集上，显著优于现有的动态重建方法。

## 📝 摘要（中文）

本文提出了一种动态重建系统，该系统以单目RGB视频作为输入，输出场景的完整且持久的重建结果。换句话说，我们不仅重建当前可见的场景部分，还重建所有先前观察到的部分，从而能够重放所有时间步的完整重建。我们的方法将场景分解为一组刚性3D基元，假设这些基元在场景中移动。利用估计的密集2D对应关系，我们通过优化流程联合推断这些基元的刚性运动，从而产生场景的4D重建，即提供随时间动态移动的3D几何体。为了实现这一点，我们还引入了一种机制来推断不可见物体的运动，采用运动分组技术来保持连续性。由此产生的系统实现了4D时空感知，提供了诸如随时间推移的可重放3D铰接物体重建、多物体扫描和物体持久性等功能。在物体扫描和多物体数据集上，我们的系统在定量和定性方面均显著优于现有方法。

## 🔬 方法详解

**问题定义**：现有的动态场景重建方法通常只能重建当前可见的场景部分，无法保持场景的完整性和持久性，尤其是在物体被遮挡或离开视野后。此外，如何有效地处理场景中多个独立运动的物体也是一个挑战。

**核心思路**：该论文的核心思路是将动态场景分解为一组刚性3D基元，并假设这些基元在场景中进行刚性运动。通过估计的密集2D对应关系，联合优化这些基元的运动轨迹，从而实现对整个场景的4D重建。这种方法能够有效地处理多个独立运动的物体，并且可以通过运动外推来估计不可见物体的运动。

**技术框架**：该系统的整体流程如下：1) 输入单目RGB视频；2) 使用SLAM或SfM等技术估计相机位姿和稀疏点云；3) 将场景分解为一组3D基元；4) 利用密集2D对应关系，通过优化框架联合估计基元的刚性运动；5) 对于不可见的物体，使用运动分组技术进行运动外推；6) 输出完整的4D场景重建结果。

**关键创新**：该论文的关键创新在于提出了一种基于3D基元的4D场景重建方法，能够有效地处理多个独立运动的物体，并且可以通过运动外推来估计不可见物体的运动。此外，该方法还引入了一种运动分组技术，用于保持运动的连续性。

**关键设计**：在优化框架中，使用了包括光度误差、几何误差和运动平滑性约束在内的损失函数。运动分组技术基于物体之间的运动相似性进行分组，并使用卡尔曼滤波器对每个组的运动进行平滑。具体的参数设置和网络结构在论文中进行了详细描述。

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

该系统在物体扫描和多物体数据集上进行了评估，实验结果表明，该系统在定量和定性方面均显著优于现有的动态重建方法。具体而言，该系统在重建精度和完整性方面均取得了显著提升，并且能够有效地处理多个独立运动的物体。

## 🎯 应用场景

该研究成果可应用于增强现实、虚拟现实、机器人导航、自动驾驶等领域。例如，在AR/VR中，可以提供更真实和沉浸式的体验，用户可以与动态场景进行交互。在机器人导航和自动驾驶中，可以帮助机器人更好地理解周围环境，并做出更合理的决策。此外，该技术还可以用于创建数字孪生，用于远程监控和控制。

## 📄 摘要（原文）

> We present a dynamic reconstruction system that receives a casual monocular RGB video as input, and outputs a complete and persistent reconstruction of the scene. In other words, we reconstruct not only the the currently visible parts of the scene, but also all previously viewed parts, which enables replaying the complete reconstruction across all timesteps.
>   Our method decomposes the scene into a set of rigid 3D primitives, which are assumed to be moving throughout the scene. Using estimated dense 2D correspondences, we jointly infer the rigid motion of these primitives through an optimisation pipeline, yielding a 4D reconstruction of the scene, i.e. providing 3D geometry dynamically moving through time. To achieve this, we also introduce a mechanism to extrapolate motion for objects that become invisible, employing motion-grouping techniques to maintain continuity.
>   The resulting system enables 4D spatio-temporal awareness, offering capabilities such as replayable 3D reconstructions of articulated objects through time, multi-object scanning, and object permanence. On object scanning and multi-object datasets, our system significantly outperforms existing methods both quantitatively and qualitatively.

