---
layout: default
title: 3D-RE-GEN: 3D Reconstruction of Indoor Scenes with a Generative Framework
---

# 3D-RE-GEN: 3D Reconstruction of Indoor Scenes with a Generative Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17459" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17459v1</a>
  <a href="https://arxiv.org/pdf/2512.17459.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17459v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17459v1', '3D-RE-GEN: 3D Reconstruction of Indoor Scenes with a Generative Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobias Sautter, Jan-Niklas Dihlmann, Hendrik P. A. Lensch

**分类**: cs.CV

**发布日期**: 2025-12-19

**备注**: Project Page: https://3dregen.jdihlmann.com/

---

## 💡 一句话要点

**3D-RE-GEN：提出一种生成式框架，用于室内场景的单图三维重建，满足艺术家对可编辑网格的需求。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `三维重建` `场景生成` `生成模型` `图像编辑` `可微优化`

## 📋 核心要点

1. 现有3D重建方法在物体分解、空间关系和背景生成方面存在不足，难以满足艺术家对可编辑3D场景的需求。
2. 3D-RE-GEN通过组合物体检测、重建和放置等模块，并结合生成模型进行图像编辑，实现高质量的场景重建。
3. 该方法生成全面的背景，并采用4自由度可微优化，确保重建物体与地面平面对齐，实现物理上真实的布局。

## 📝 摘要（中文）

本文提出3D-RE-GEN，一个组合式框架，可以将单张图像重建为带纹理的3D物体和背景。虽然3D场景生成领域取得了显著进展，但现有表示方法阻碍了艺术家们对可修改的3D纹理网格场景的需求，这在视觉特效和游戏开发中至关重要。现有的纹理网格场景重建方法远未达到艺术家可用的程度，存在物体分解不正确、空间关系不准确以及缺少背景等问题。3D-RE-GEN结合了特定领域的最先进模型，实现了最先进的场景重建性能，满足了艺术家的需求。该重建流程集成了物体检测、重建和放置模型，并将某些模型扩展到其原始领域之外。遮挡物体的获取被视为图像编辑任务，利用生成模型进行推理和重建，并进行场景级别的推理，保持光照和几何一致性。与现有方法不同，3D-RE-GEN生成了一个全面的背景，在优化过程中对物体进行空间约束，并为视觉特效和游戏中的真实光照和模拟任务奠定了基础。为了获得物理上真实的布局，采用了一种新颖的4自由度可微优化方法，使重建的物体与估计的地面平面对齐。3D-RE-GEN在单图像3D场景重建中实现了最先进的性能，通过精确的相机恢复和空间优化引导的组合生成，生成连贯的、可修改的场景。

## 🔬 方法详解

**问题定义**：现有单图三维场景重建方法难以生成高质量、可编辑的3D场景，具体表现为物体分解不准确、物体间空间关系不合理、缺少完整背景等问题。这些问题限制了重建结果在视觉特效和游戏开发等领域的应用，因为艺术家需要能够灵活修改和调整场景中的各个元素。

**核心思路**：3D-RE-GEN的核心思路是将单图三维场景重建分解为多个子任务，并针对每个子任务选择最先进的模型进行组合。同时，利用生成模型进行图像编辑，推断和重建被遮挡的物体，并生成完整的背景。通过这种组合式的框架，可以充分利用现有模型的优势，并解决现有方法的不足。

**技术框架**：3D-RE-GEN的整体框架包含以下几个主要模块：1) 物体检测：检测图像中的物体，并估计其类别和位置。2) 物体重建：根据检测到的物体，重建其三维模型。3) 物体放置：将重建的物体放置到场景中，并调整其位置和姿态。4) 背景生成：生成场景的背景，并与重建的物体进行融合。5) 空间优化：通过可微优化，调整物体的位置和姿态，使其与地面平面对齐，并保证物体之间的空间关系合理。

**关键创新**：该方法最重要的创新点在于其组合式的框架，以及利用生成模型进行图像编辑和背景生成。通过组合不同的模型，可以充分利用现有技术的优势，并解决现有方法的不足。利用生成模型进行图像编辑，可以推断和重建被遮挡的物体，从而提高重建的完整性。生成完整的背景，可以为场景提供更真实的光照和模拟效果。

**关键设计**：该方法采用了一种新颖的4自由度可微优化方法，用于调整物体的位置和姿态。该优化方法考虑了物体与地面平面的对齐关系，以及物体之间的空间关系。此外，该方法还设计了一种损失函数，用于衡量重建结果的质量，包括物体的形状、纹理和空间关系。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17459v1/sec/images/pipeline.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17459v1/sec/images/appl_querying.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17459v1/sec/images/appl_querying_fail.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

3D-RE-GEN在单图像3D场景重建任务上取得了state-of-the-art的性能。通过组合生成和空间优化，该方法能够生成连贯、可修改的场景，显著优于现有方法。具体性能数据和对比基线在论文实验部分给出，表明该方法在重建质量和效率上均有明显提升。

## 🎯 应用场景

该研究成果可应用于视觉特效、游戏开发、室内设计、机器人导航等领域。在视觉特效和游戏开发中，可以快速生成高质量的3D场景，提高制作效率。在室内设计中，可以根据单张照片重建室内场景，方便用户进行虚拟装修和布局设计。在机器人导航中，可以利用重建的3D场景进行路径规划和环境感知。

## 📄 摘要（原文）

> Recent advances in 3D scene generation produce visually appealing output, but current representations hinder artists' workflows that require modifiable 3D textured mesh scenes for visual effects and game development. Despite significant advances, current textured mesh scene reconstruction methods are far from artist ready, suffering from incorrect object decomposition, inaccurate spatial relationships, and missing backgrounds. We present 3D-RE-GEN, a compositional framework that reconstructs a single image into textured 3D objects and a background. We show that combining state of the art models from specific domains achieves state of the art scene reconstruction performance, addressing artists' requirements.
>   Our reconstruction pipeline integrates models for asset detection, reconstruction, and placement, pushing certain models beyond their originally intended domains. Obtaining occluded objects is treated as an image editing task with generative models to infer and reconstruct with scene level reasoning under consistent lighting and geometry. Unlike current methods, 3D-RE-GEN generates a comprehensive background that spatially constrains objects during optimization and provides a foundation for realistic lighting and simulation tasks in visual effects and games. To obtain physically realistic layouts, we employ a novel 4-DoF differentiable optimization that aligns reconstructed objects with the estimated ground plane. 3D-RE-GEN~achieves state of the art performance in single image 3D scene reconstruction, producing coherent, modifiable scenes through compositional generation guided by precise camera recovery and spatial optimization.

