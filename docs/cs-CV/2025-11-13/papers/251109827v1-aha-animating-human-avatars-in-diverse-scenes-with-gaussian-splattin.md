---
layout: default
title: AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting
---

# AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09827" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09827v1</a>
  <a href="https://arxiv.org/pdf/2511.09827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09827v1" onclick="toggleFavorite(this, '2511.09827v1', 'AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aymen Mir, Jian Wang, Riza Alp Guler, Chuan Guo, Gerard Pons-Moll, Bing Zhou

**分类**: cs.CV

**发布日期**: 2025-11-13

---

## 💡 一句话要点

**提出基于高斯溅射的人体动画框架，实现场景中逼真的人体自由视角渲染。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人体动画` `3D高斯溅射` `神经渲染` `自由视角渲染` `人机交互`

## 📋 核心要点

1. 现有方法难以实现人体与复杂3D场景的自然交互动画，尤其是在几何一致性和自由视角渲染方面。
2. 提出基于3D高斯溅射的人体动画框架，将人体和场景表示为高斯分布，解耦渲染和运动合成。
3. 通过高斯对齐的运动模块和人体-场景高斯细化优化，实现逼真的人体动画和自然的交互效果。

## 📝 摘要（中文）

本文提出了一种新颖的框架，用于在3D场景中动画化人体，该框架使用3D高斯溅射（3DGS）。3DGS是一种神经场景表示方法，最近在novel-view synthesis方面取得了state-of-the-art的逼真结果，但在人体-场景动画和交互方面仍未得到充分探索。与使用网格或点云作为底层3D表示的现有动画流程不同，我们的方法引入了3DGS作为3D表示来解决场景中人体动画的问题。通过将人和场景表示为高斯分布，我们的方法允许对与3D场景交互的人进行几何一致的自由视角渲染。我们的关键见解是，渲染可以与运动合成分离，并且每个子问题都可以独立解决，而无需配对的人体-场景数据。该方法的核心是一个高斯对齐的运动模块，该模块在没有显式场景几何的情况下合成运动，使用基于不透明度的线索和投影的高斯结构来指导人体放置和姿势对齐。为了确保自然的交互，我们进一步提出了一种人体-场景高斯细化优化，以强制执行真实的接触和导航。我们在来自Scannet++和SuperSplat库的场景以及从稀疏和密集的多视图人体捕获重建的化身上评估了我们的方法。最后，我们证明了我们的框架允许新的应用，例如使用新的动画人物对编辑过的单目RGB视频进行几何一致的自由视角渲染，展示了3DGS在基于单目视频的人体动画方面的独特优势。

## 🔬 方法详解

**问题定义**：现有的人体动画方法通常依赖于网格或点云作为3D表示，这些方法在处理复杂场景交互时存在几何不一致的问题，并且难以实现自由视角的逼真渲染。此外，现有方法通常需要配对的人体-场景数据进行训练，限制了其应用范围。

**核心思路**：本文的核心思路是将人体和场景都表示为3D高斯分布，利用3D高斯溅射（3DGS）的优势，实现几何一致的自由视角渲染。通过解耦渲染和运动合成，可以独立地处理这两个子问题，避免了对配对数据的依赖。

**技术框架**：该框架主要包含以下几个模块：1) 人体和场景的3DGS表示：使用3DGS表示人体和场景的几何和外观信息。2) 高斯对齐的运动模块：该模块负责合成人体的运动，利用基于不透明度的线索和投影的高斯结构来指导人体放置和姿势对齐，无需显式的场景几何信息。3) 人体-场景高斯细化优化：该模块通过优化高斯分布的参数，强制执行真实的人体-场景接触和导航，从而实现自然的交互效果。

**关键创新**：该方法最重要的创新点在于将3DGS引入到人体动画领域，并提出了一种解耦渲染和运动合成的框架。与传统的基于网格或点云的方法相比，该方法能够实现几何一致的自由视角渲染，并且无需配对的人体-场景数据。

**关键设计**：高斯对齐的运动模块使用opacity-based cues和projected Gaussian structures来指导人体放置和姿势对齐。人体-场景高斯细化优化使用损失函数来强制执行真实的人体-场景接触和导航。具体的损失函数和优化算法的细节在论文中有详细描述。

## 📊 实验亮点

该方法在Scannet++和SuperSplat数据集上进行了评估，并与现有的方法进行了比较。实验结果表明，该方法能够生成几何一致的自由视角渲染，并且能够实现自然的人体-场景交互。此外，该方法还展示了在编辑单目视频方面的应用，证明了3DGS在人体动画方面的独特优势。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、游戏开发、电影制作等领域。例如，可以将该框架用于创建逼真的虚拟化身，使其能够在虚拟环境中与用户进行自然的交互。此外，该框架还可以用于编辑现有的单目视频，将新的动画人物添加到视频中，从而实现各种创意应用。

## 📄 摘要（原文）

> We present a novel framework for animating humans in 3D scenes using 3D Gaussian Splatting (3DGS), a neural scene representation that has recently achieved state-of-the-art photorealistic results for novel-view synthesis but remains under-explored for human-scene animation and interaction. Unlike existing animation pipelines that use meshes or point clouds as the underlying 3D representation, our approach introduces the use of 3DGS as the 3D representation to the problem of animating humans in scenes. By representing humans and scenes as Gaussians, our approach allows for geometry-consistent free-viewpoint rendering of humans interacting with 3D scenes. Our key insight is that the rendering can be decoupled from the motion synthesis and each sub-problem can be addressed independently, without the need for paired human-scene data. Central to our method is a Gaussian-aligned motion module that synthesizes motion without explicit scene geometry, using opacity-based cues and projected Gaussian structures to guide human placement and pose alignment. To ensure natural interactions, we further propose a human-scene Gaussian refinement optimization that enforces realistic contact and navigation. We evaluate our approach on scenes from Scannet++ and the SuperSplat library, and on avatars reconstructed from sparse and dense multi-view human capture. Finally, we demonstrate that our framework allows for novel applications such as geometry-consistent free-viewpoint rendering of edited monocular RGB videos with new animated humans, showcasing the unique advantage of 3DGS for monocular video-based human animation.

