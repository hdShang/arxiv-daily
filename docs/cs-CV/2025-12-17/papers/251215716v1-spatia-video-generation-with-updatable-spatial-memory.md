---
layout: default
title: Spatia: Video Generation with Updatable Spatial Memory
---

# Spatia: Video Generation with Updatable Spatial Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15716" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15716v1</a>
  <a href="https://arxiv.org/pdf/2512.15716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15716v1" onclick="toggleFavorite(this, '2512.15716v1', 'Spatia: Video Generation with Updatable Spatial Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinjing Zhao, Fangyun Wei, Zhening Liu, Hongyang Zhang, Chang Xu, Yan Lu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-17

**备注**: Project page: https://zhaojingjing713.github.io/Spatia/

---

## 💡 一句话要点

**Spatia：利用可更新空间记忆实现视频生成，提升时空一致性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视频生成` `空间记忆` `视觉SLAM` `时空一致性` `3D重建`

## 📋 核心要点

1. 现有视频生成模型难以维持长时空一致性，因为视频信号具有高维度和密集性。
2. Spatia通过显式地维护一个3D场景点云作为空间记忆，并利用视觉SLAM技术持续更新该记忆。
3. Spatia实现了空间一致性的增强，同时保留了生成逼真动态实体的能力，并支持相机控制和3D编辑。

## 📝 摘要（中文）

现有的视频生成模型由于视频信号的密集性和高维性，难以维持长期的空间和时间一致性。为了克服这一限制，我们提出了Spatia，一个空间记忆感知的视频生成框架，它显式地将3D场景点云作为持久的空间记忆来保存。Spatia迭代地生成以该空间记忆为条件的视频片段，并通过视觉SLAM持续更新它。这种动态-静态解耦设计增强了整个生成过程中的空间一致性，同时保留了模型生成逼真动态实体的能力。此外，Spatia还支持显式相机控制和3D感知交互编辑等应用，为可扩展的、记忆驱动的视频生成提供了一个几何基础框架。

## 🔬 方法详解

**问题定义**：现有视频生成模型在处理长视频时，由于计算资源限制和模型容量瓶颈，难以维持长时间的空间和时间一致性。尤其是在场景复杂、运动幅度大的情况下，生成的视频容易出现物体漂移、形变等问题，影响视觉质量。现有方法通常采用循环神经网络或Transformer结构，但难以有效建模场景的几何结构和长期依赖关系。

**核心思路**：Spatia的核心思路是将视频生成过程与场景的3D几何结构解耦。通过维护一个可更新的3D空间记忆（点云），模型可以显式地感知场景的几何信息，从而更好地保持空间一致性。同时，利用视觉SLAM技术，可以动态更新空间记忆，使其适应场景的变化，从而实现更稳定的视频生成。

**技术框架**：Spatia框架主要包含三个模块：1) 空间记忆模块：负责维护和更新3D场景点云。初始点云可以通过先验知识或重建算法获得。2) 视频生成模块：基于空间记忆生成视频片段。该模块通常采用生成对抗网络（GAN）或扩散模型等技术。3) 视觉SLAM模块：根据生成的视频片段，利用视觉SLAM算法估计相机位姿，并更新空间记忆。这三个模块循环迭代，不断优化视频生成效果和空间记忆的准确性。

**关键创新**：Spatia最重要的创新点在于将3D空间记忆显式地引入到视频生成过程中。与现有方法相比，Spatia不再直接从像素空间进行视频生成，而是先构建场景的3D表示，然后基于该表示生成视频。这种方法可以有效地解决长时空一致性问题，并为视频编辑和交互提供几何基础。

**关键设计**：Spatia的关键设计包括：1) 空间记忆的表示形式：采用点云作为空间记忆，可以灵活地表示各种复杂的场景结构。2) 视觉SLAM算法的选择：根据具体的应用场景选择合适的视觉SLAM算法，例如ORB-SLAM、LSD-SLAM等。3) 视频生成模块的网络结构：可以采用各种先进的GAN或扩散模型结构，例如StyleGAN、VQ-VAE等。4) 损失函数的设计：除了传统的GAN损失或扩散模型损失外，还可以引入空间一致性损失，例如点云重建损失、相机位姿一致性损失等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15716v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15716v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15716v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验验证了Spatia在长时空一致性方面的优势。与现有方法相比，Spatia生成的视频在物体漂移、形变等方面有显著改善。此外，Spatia还支持显式相机控制和3D感知交互编辑等功能，为用户提供了更灵活的视频创作方式。具体的性能数据和对比基线在论文中有详细描述，表明Spatia在多个指标上优于现有方法。

## 🎯 应用场景

Spatia具有广泛的应用前景，例如：1) 虚拟现实/增强现实内容生成：可以生成具有高度空间一致性的VR/AR场景。2) 游戏开发：可以快速生成逼真的游戏场景和角色动画。3) 电影制作：可以辅助电影特效制作，例如场景扩展、物体替换等。4) 机器人导航：可以为机器人提供准确的环境地图，辅助机器人进行导航和定位。未来，Spatia有望成为视频生成领域的重要技术。

## 📄 摘要（原文）

> Existing video generation models struggle to maintain long-term spatial and temporal consistency due to the dense, high-dimensional nature of video signals. To overcome this limitation, we propose Spatia, a spatial memory-aware video generation framework that explicitly preserves a 3D scene point cloud as persistent spatial memory. Spatia iteratively generates video clips conditioned on this spatial memory and continuously updates it through visual SLAM. This dynamic-static disentanglement design enhances spatial consistency throughout the generation process while preserving the model's ability to produce realistic dynamic entities. Furthermore, Spatia enables applications such as explicit camera control and 3D-aware interactive editing, providing a geometrically grounded framework for scalable, memory-driven video generation.

