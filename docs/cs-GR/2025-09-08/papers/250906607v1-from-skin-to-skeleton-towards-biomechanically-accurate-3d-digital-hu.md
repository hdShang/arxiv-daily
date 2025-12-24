---
layout: default
title: "From Skin to Skeleton: Towards Biomechanically Accurate 3D Digital Humans"
---

# From Skin to Skeleton: Towards Biomechanically Accurate 3D Digital Humans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06607" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06607v1</a>
  <a href="https://arxiv.org/pdf/2509.06607.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06607v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06607v1', 'From Skin to Skeleton: Towards Biomechanically Accurate 3D Digital Humans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marilyn Keller, Keenon Werling, Soyong Shin, Scott Delp, Sergi Pujades, C. Karen Liu, Michael J. Black

**分类**: cs.GR, cs.CV

**发布日期**: 2025-09-08

**期刊**: ACM Trans. Graph. 42, 6, Article 253 (December 2023), 12 pages

**DOI**: [10.1145/3618381](https://doi.org/10.1145/3618381)

---

## 💡 一句话要点

**提出SKEL模型，将SMPL模型升级为生物力学精确的3D人体模型**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `3D人体模型` `生物力学` `SMPL模型` `骨骼绑定` `运动学` `参数化模型` `人体姿态估计`

## 📋 核心要点

1. 现有3D人体模型（如SMPL）的运动学结构过于简化，无法满足生物力学分析的精度要求，限制了其应用。
2. 论文提出SKEL模型，通过将SMPL模型与生物力学骨骼重新绑定，构建生物力学精确且易于姿态调整的3D人体模型。
3. 实验表明，SKEL模型具有更精确的关节位置，骨骼与身体表面的贴合度更高，并能升级现有数据集以包含生物力学参数。

## 📝 摘要（中文）

通过训练神经网络直接回归参数化人体模型（如SMPL）的参数，在从图像和视频中估计3D人体姿态和形状方面取得了很大进展。然而，现有的身体模型具有简化的运动学结构，与人体骨骼系统中真实的关节位置和关节运动不符，限制了它们在生物力学中的潜在用途。另一方面，用于估计生物力学精确骨骼运动的方法通常依赖于复杂的运动捕捉系统和昂贵的优化方法。因此，需要一个具有生物力学精确骨骼结构的参数化3D人体模型，并且可以轻松地进行姿势调整。为此，我们开发了SKEL，它使用生物力学骨骼重新装配SMPL身体模型。为了实现这一点，我们需要在各种姿势的SMPL网格内部的骨骼训练数据。我们通过优化来自AMASS序列的SMPL网格内部的生物力学精确骨骼来构建这样的数据集。然后，我们学习一个从SMPL网格顶点到优化后的关节位置和骨骼旋转的回归器。最后，我们使用新的运动学参数重新参数化SMPL网格。由此产生的SKEL模型像SMPL一样可以动画化，但自由度更少，并且更符合生物力学。我们表明，SKEL比SMPL具有更生物力学精确的关节位置，并且骨骼比以前的方法更好地贴合在身体表面内部。通过将SKEL拟合到SMPL网格，我们能够“升级”现有人体姿势和形状数据集，以包括生物力学参数。SKEL提供了一个新工具，可以在实际场景中实现生物力学，同时也为视觉和图形研究人员提供了一个更好约束和更逼真的人体关节运动模型。该模型、代码和数据可在https://skel.is.tue.mpg.de.上获得。

## 🔬 方法详解

**问题定义**：现有参数化人体模型（如SMPL）的运动学结构不够精确，无法准确反映人体骨骼的真实关节位置和运动方式，这限制了它们在生物力学分析等领域的应用。同时，传统的生物力学分析方法依赖于昂贵的运动捕捉系统和复杂的优化算法，难以在实际场景中应用。

**核心思路**：论文的核心思路是将现有的SMPL模型与生物力学上更精确的骨骼结构相结合，创建一个新的参数化人体模型SKEL。通过优化SMPL网格内部的骨骼姿态，并学习从SMPL顶点到骨骼关节位置的回归器，实现SMPL模型的“骨骼升级”。这样既保留了SMPL模型的易用性，又提升了其生物力学精度。

**技术框架**：SKEL模型的构建主要包含以下几个阶段：
1. **数据生成**：利用AMASS数据集，通过优化算法将生物力学精确的骨骼嵌入到SMPL网格中，生成训练数据。
2. **回归器训练**：训练一个回归器，学习从SMPL网格顶点到优化后的关节位置和骨骼旋转的映射关系。
3. **模型重参数化**：使用新的运动学参数（即生物力学骨骼）重新参数化SMPL模型，得到SKEL模型。

**关键创新**：该论文的关键创新在于将参数化人体模型与生物力学骨骼相结合，提出了一种新的3D人体模型SKEL。与传统的SMPL模型相比，SKEL模型具有更精确的关节位置和更真实的运动学结构，更适合用于生物力学分析。此外，该方法还提供了一种“升级”现有SMPL数据集的途径，使其包含生物力学信息。

**关键设计**：
1. **骨骼优化**：使用优化算法，在SMPL网格内部寻找最佳的骨骼姿态，使其尽可能符合生物力学原理。
2. **回归器结构**：回归器的具体网络结构未知，但其目标是学习SMPL顶点到关节位置的非线性映射。
3. **损失函数**：损失函数的设计需要考虑关节位置的精度、骨骼长度的约束以及骨骼与身体表面的贴合度等因素（具体形式未知）。

## 📊 实验亮点

论文通过实验证明，SKEL模型比SMPL模型具有更生物力学精确的关节位置，并且骨骼与身体表面的贴合度更高。通过将SKEL拟合到SMPL网格，能够将现有人体姿势和形状数据集升级为包含生物力学参数的数据集。这些结果表明，SKEL模型在生物力学分析和人体建模方面具有显著优势。

## 🎯 应用场景

SKEL模型可广泛应用于生物力学研究、运动分析、康复医学、虚拟现实和游戏等领域。它能够提供更精确的人体运动学信息，帮助研究人员分析运动损伤机制、设计更有效的康复方案、创建更逼真的虚拟角色。此外，SKEL模型还可以用于改进人体姿态估计和动作捕捉技术，提高其精度和鲁棒性。

## 📄 摘要（原文）

> Great progress has been made in estimating 3D human pose and shape from images and video by training neural networks to directly regress the parameters of parametric human models like SMPL. However, existing body models have simplified kinematic structures that do not correspond to the true joint locations and articulations in the human skeletal system, limiting their potential use in biomechanics. On the other hand, methods for estimating biomechanically accurate skeletal motion typically rely on complex motion capture systems and expensive optimization methods. What is needed is a parametric 3D human model with a biomechanically accurate skeletal structure that can be easily posed. To that end, we develop SKEL, which re-rigs the SMPL body model with a biomechanics skeleton. To enable this, we need training data of skeletons inside SMPL meshes in diverse poses.
>   We build such a dataset by optimizing biomechanically accurate skeletons inside SMPL meshes from AMASS sequences. We then learn a regressor from SMPL mesh vertices to the optimized joint locations and bone rotations. Finally, we re-parametrize the SMPL mesh with the new kinematic parameters. The resulting SKEL model is animatable like SMPL but with fewer, and biomechanically-realistic, degrees of freedom. We show that SKEL has more biomechanically accurate joint locations than SMPL, and the bones fit inside the body surface better than previous methods. By fitting SKEL to SMPL meshes we are able to "upgrade" existing human pose and shape datasets to include biomechanical parameters. SKEL provides a new tool to enable biomechanics in the wild, while also providing vision and graphics researchers with a better constrained and more realistic model of human articulation. The model, code, and data are available for research at https://skel.is.tue.mpg.de..

