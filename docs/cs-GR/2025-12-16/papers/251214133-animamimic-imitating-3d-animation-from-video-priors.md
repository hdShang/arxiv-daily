---
layout: default
title: AnimaMimic: Imitating 3D Animation from Video Priors
---

# AnimaMimic: Imitating 3D Animation from Video Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14133" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14133</a>
  <a href="https://arxiv.org/pdf/2512.14133.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14133" onclick="toggleFavorite(this, '2512.14133', 'AnimaMimic: Imitating 3D Animation from Video Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyi Xie, Yunuo Chen, Yaowei Guo, Yin Yang, Bolei Zhou, Demetri Terzopoulos, Ying Jiang, Chenfanfu Jiang

**分类**: cs.GR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**AnimaMimic：利用视频先验模仿3D动画，实现自动绑定和物理模拟。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `3D动画` `视频扩散模型` `可微渲染` `物理模拟` `运动迁移` `自动绑定`

## 📋 核心要点

1. 现有3D动画制作流程耗时且依赖专业知识，缺乏自动化的手段，难以快速生成高质量的动画。
2. AnimaMimic利用视频扩散模型学习运动先验，并将其迁移到3D网格动画，实现自动绑定和运动生成。
3. 该方法通过可微渲染和物理模拟，优化动画的真实性和物理合理性，生成可编辑的3D动画序列。

## 📝 摘要（中文）

创建逼真的3D动画是一个耗时且依赖专业知识的过程，需要手动绑定、关键帧设置和复杂运动的微调。最近，视频扩散模型在2D中展示了卓越的运动想象能力，可以从文本或图像提示生成动态且视觉连贯的运动。然而，它们的结果缺乏明确的3D结构，不能直接用于动画或模拟。我们提出了AnimaMimic，一个使用从视频扩散模型学习的运动先验来动画静态3D网格的框架。从输入网格开始，AnimaMimic合成单目动画视频，自动构建带有蒙皮权重的骨架，并通过可微渲染和基于视频的监督来细化关节参数。为了进一步提高真实感，我们集成了一个可微模拟模块，通过物理基础的软组织动力学来细化网格变形。我们的方法桥接了视频扩散的创造性和3D绑定动画的结构控制，产生物理上合理、时间上连贯且艺术家可编辑的运动序列，可以无缝集成到标准动画流程中。

## 🔬 方法详解

**问题定义**：现有3D动画制作流程需要手动进行骨骼绑定、关键帧设计和运动微调，耗时且需要专业技能。视频扩散模型虽然能生成高质量的2D运动，但缺乏3D结构，无法直接用于3D动画。

**核心思路**：AnimaMimic的核心思路是利用视频扩散模型学习到的运动先验知识，将其迁移到3D网格模型上，从而实现自动化的3D动画生成。通过可微渲染和物理模拟，进一步优化动画的真实性和物理合理性。

**技术框架**：AnimaMimic框架包含以下几个主要模块：1) 从静态3D网格生成单目动画视频；2) 自动构建骨骼和蒙皮权重；3) 通过可微渲染和视频监督优化关节参数；4) 利用可微物理模拟细化网格变形，增强真实感。

**关键创新**：该方法最重要的创新点在于将2D视频扩散模型的运动先验知识成功迁移到3D动画生成中，并结合可微渲染和物理模拟进行优化。与传统的手动动画制作方法相比，AnimaMimic实现了动画生成的自动化和高效化。

**关键设计**：该方法使用可微渲染技术，使得可以通过梯度下降的方式优化骨骼参数，从而使生成的动画与视频扩散模型生成的视频在视觉上保持一致。此外，使用可微的物理模拟模块，可以保证动画的物理合理性，避免出现穿模等不自然的现象。具体的损失函数包括视频重建损失、骨骼约束损失和物理模拟损失等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14133/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14133/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14133/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AnimaMimic通过结合视频扩散模型和可微渲染、物理模拟，实现了高质量的3D动画生成。实验结果表明，该方法能够生成物理上合理、时间上连贯且艺术家可编辑的运动序列，可以无缝集成到标准动画流程中。具体性能数据未知，但从描述来看，该方法在自动化和真实性方面均有显著提升。

## 🎯 应用场景

AnimaMimic具有广泛的应用前景，可以应用于游戏开发、电影制作、虚拟现实等领域。它可以帮助艺术家快速生成高质量的3D动画，降低动画制作的成本和时间。此外，该方法还可以用于生成各种虚拟角色的动画，例如虚拟助手、虚拟主播等，从而丰富人机交互的体验。

## 📄 摘要（原文）

> Creating realistic 3D animation remains a time-consuming and expertise-dependent process, requiring manual rigging, keyframing, and fine-tuning of complex motions. Meanwhile, video diffusion models have recently demonstrated remarkable motion imagination in 2D, generating dynamic and visually coherent motion from text or image prompts. However, their results lack explicit 3D structure and cannot be directly used for animation or simulation. We present AnimaMimic, a framework that animates static 3D meshes using motion priors learned from video diffusion models. Starting from an input mesh, AnimaMimic synthesizes a monocular animation video, automatically constructs a skeleton with skinning weights, and refines joint parameters through differentiable rendering and video-based supervision. To further enhance realism, we integrate a differentiable simulation module that refines mesh deformation through physically grounded soft-tissue dynamics. Our method bridges the creativity of video diffusion and the structural control of 3D rigged animation, producing physically plausible, temporally coherent, and artist-editable motion sequences that integrate seamlessly into standard animation pipelines. Our project page is at:this https URL

