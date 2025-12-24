---
layout: default
title: "GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars"
---

# GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09162" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09162v1</a>
  <a href="https://arxiv.org/pdf/2512.09162.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09162v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.09162v1', 'GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-09

---

## 💡 一句话要点

**GTAvatar：结合高斯溅射与纹理映射，实现可重光照和编辑的高斯头像**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `高斯溅射` `UV纹理映射` `头像重建` `可编辑性` `重光照`

## 📋 核心要点

1. 现有高斯溅射方法重建的头像缺乏传统网格方法所具备的直观编辑性，限制了其应用。
2. 该论文提出将高斯溅射与UV纹理映射相结合，实现头像的精确重建和直观编辑。
3. 实验表明，该方法重建精度高，重光照效果好，并能通过纹理映射直观地修改头像外观。

## 📝 摘要（中文）

近年来，高斯溅射技术的进步使得重建逼真的头部头像成为可能，为视觉特效、视频会议和虚拟现实等领域带来了机遇。然而，与传统的基于三角网格的方法相比，它缺乏直观的可编辑性。为了解决这个问题，我们提出了一种结合2D高斯溅射的准确性和保真度与UV纹理映射的直观性的方法。通过将每个规范高斯基元的局部坐标系以计算高效的方式嵌入到模板网格的UV空间中的一个patch中，我们从单个单目视频中重建连续的可编辑材质头部纹理到一个常规的UV域上。此外，我们利用一个高效的基于物理的反射模型来实现这些内在材质贴图的重光照和编辑。通过与最先进的方法进行广泛的比较，我们证明了我们重建的准确性、重光照结果的质量，以及通过纹理映射提供直观的控制来修改头像的外观和几何形状的能力，而无需额外的优化。

## 🔬 方法详解

**问题定义**：现有基于高斯溅射的头像重建方法虽然能实现高精度和高保真度的重建，但缺乏像传统基于三角网格方法那样的直观编辑能力。用户难以直接修改头像的几何形状和材质属性，这限制了其在需要灵活编辑的应用场景中的使用。

**核心思路**：该论文的核心思路是将高斯溅射的局部坐标系嵌入到模板网格的UV空间中，从而将高斯溅射的重建结果映射到UV纹理空间。这样，用户就可以像编辑传统纹理贴图一样，直观地修改头像的材质和几何形状。

**技术框架**：该方法主要包含以下几个阶段：1) 使用高斯溅射重建头部头像；2) 将每个高斯基元的局部坐标系嵌入到模板网格的UV空间中，建立高斯基元与UV坐标的对应关系；3) 从单目视频中重建连续的可编辑材质头部纹理到UV域上；4) 利用基于物理的渲染模型，实现材质贴图的重光照和编辑。

**关键创新**：该方法最重要的创新点在于将高斯溅射与UV纹理映射相结合，实现了高精度重建和直观编辑的统一。与现有方法相比，该方法无需额外的优化即可通过纹理映射提供直观的控制来修改头像的外观和几何形状。

**关键设计**：该方法使用了一个高效的嵌入算法，将高斯基元的局部坐标系嵌入到UV空间中。此外，该方法还利用了一个基于物理的反射模型，用于实现材质贴图的重光照和编辑。具体的参数设置和损失函数等细节在论文中有详细描述。

## 📊 实验亮点

论文通过与当前最先进的方法进行对比，证明了该方法在头像重建的准确性、重光照效果和可编辑性方面具有显著优势。实验结果表明，该方法能够重建出高质量的头部纹理，并能够通过纹理映射直观地修改头像的外观和几何形状，而无需额外的优化。

## 🎯 应用场景

该研究成果可广泛应用于虚拟现实、增强现实、视频会议、游戏开发等领域。用户可以利用该技术创建高度逼真且可定制的虚拟化身，用于在线交流、虚拟社交、角色扮演等。此外，该技术还可以用于数字内容创作，例如电影特效、动画制作等，提高内容创作的效率和质量。

## 📄 摘要（原文）

> Recent advancements in Gaussian Splatting have enabled increasingly accurate reconstruction of photorealistic head avatars, opening the door to numerous applications in visual effects, videoconferencing, and virtual reality. This, however, comes with the lack of intuitive editability offered by traditional triangle mesh-based methods. In contrast, we propose a method that combines the accuracy and fidelity of 2D Gaussian Splatting with the intuitiveness of UV texture mapping. By embedding each canonical Gaussian primitive's local frame into a patch in the UV space of a template mesh in a computationally efficient manner, we reconstruct continuous editable material head textures from a single monocular video on a conventional UV domain. Furthermore, we leverage an efficient physically based reflectance model to enable relighting and editing of these intrinsic material maps. Through extensive comparisons with state-of-the-art methods, we demonstrate the accuracy of our reconstructions, the quality of our relighting results, and the ability to provide intuitive controls for modifying an avatar's appearance and geometry via texture mapping without additional optimization.

