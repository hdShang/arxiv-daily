---
layout: default
title: AlignGS: Aligning Geometry and Semantics for Robust Indoor Reconstruction from Sparse Views
---

# AlignGS: Aligning Geometry and Semantics for Robust Indoor Reconstruction from Sparse Views

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07839" target="_blank" class="toolbar-btn">arXiv: 2510.07839v1</a>
    <a href="https://arxiv.org/pdf/2510.07839.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07839v1" 
            onclick="toggleFavorite(this, '2510.07839v1', 'AlignGS: Aligning Geometry and Semantics for Robust Indoor Reconstruction from Sparse Views')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yijie Gao, Houqiang Zhong, Tianchi Zhu, Zhengxue Cheng, Qiang Hu, Li Song

**分类**: cs.CV

**发布日期**: 2025-10-09

**🔗 代码/项目**: [GITHUB](https://github.com/MediaX-SJTU/AlignGS)

---

## 💡 一句话要点

**AlignGS：对齐几何与语义，实现稀疏视角下鲁棒的室内重建**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `三维重建` `语义先验` `几何优化` `稀疏视角` `高斯溅射`

## 📋 核心要点

1. 现有方法在稀疏视角下重建室内场景时，几何结构易出现歧义，语义信息未能有效指导几何重建。
2. AlignGS的核心思想是利用2D基础模型提取的语义先验，主动引导3D几何结构的重建，实现几何与语义的协同优化。
3. 实验结果表明，AlignGS在novel view synthesis和几何精度上均优于现有方法，验证了语义先验作为几何正则化的有效性。

## 📝 摘要（中文）

本文提出AlignGS框架，旨在解决从稀疏视角重建语义丰富的室内三维模型这一难题。现有方法通常将语义视为几何结构的被动特征，忽略了语义对几何重建的指导作用。AlignGS创新性地实现了几何与语义的协同端到端优化。该方法从2D基础模型中提取丰富的先验知识，并通过一系列语义到几何的指导机制（包括深度一致性和多方面法向量正则化）直接约束3D表示。在标准数据集上的大量评估表明，该方法在 novel view synthesis 任务上取得了state-of-the-art的结果，并生成了具有更高几何精度的重建模型。实验结果验证了利用语义先验作为几何正则化项，能够从有限的输入视角生成更连贯和完整的3D模型。

## 🔬 方法详解

**问题定义**：论文旨在解决从稀疏视角重建室内场景时，由于几何歧义性导致的重建质量差的问题。现有方法通常将语义信息作为后处理步骤，在几何结构已经生成后才进行语义标注，忽略了语义信息对几何重建的指导作用，导致重建结果不鲁棒。

**核心思路**：AlignGS的核心思路是将语义理解作为主动的指导力量，通过语义先验来正则化几何重建过程。具体来说，利用2D基础模型提取的语义信息，指导3D几何结构的生成，从而提高重建的鲁棒性和准确性。这种端到端的几何与语义协同优化是本论文的关键。

**技术框架**：AlignGS的整体框架包含以下几个主要模块：1) 2D语义先验提取：利用预训练的2D基础模型（如语义分割模型）提取输入图像的语义信息。2) 3D表示：使用高斯溅射（Gaussian Splatting）作为3D场景的表示方法。3) 语义到几何的指导：设计了一系列语义到几何的指导机制，包括深度一致性约束和多方面法向量正则化。4) 端到端优化：将上述模块集成到一个端到端的优化框架中，联合优化几何结构和语义信息。

**关键创新**：AlignGS最关键的创新在于将语义信息作为几何重建的强先验，并设计了有效的语义到几何的指导机制。与现有方法不同，AlignGS不是简单地将语义信息“绘制”在已有的几何结构上，而是利用语义信息主动地塑造几何结构，从而提高了重建的鲁棒性和准确性。

**关键设计**：在语义到几何的指导方面，AlignGS设计了深度一致性约束和多方面法向量正则化。深度一致性约束旨在保证重建的3D结构与2D图像的深度信息一致。多方面法向量正则化则利用语义信息来约束3D结构的法向量，使其更加平滑和符合物体的形状先验。损失函数包括渲染损失、深度一致性损失和法向量正则化损失。网络结构方面，主要依赖于高斯溅射的优化过程，以及2D语义分割模型提供的语义先验。

## 📊 实验亮点

AlignGS在标准数据集上取得了state-of-the-art的novel view synthesis结果，并显著提高了重建模型的几何精度。与现有方法相比，AlignGS能够生成更连贯、更完整的3D模型，尤其是在稀疏视角下。实验结果验证了语义先验作为几何正则化的有效性，为未来的三维重建研究提供了新的方向。

## 🎯 应用场景

AlignGS在增强现实、虚拟现实和机器人等领域具有广泛的应用前景。高质量的语义三维重建模型可以用于AR/VR场景的构建、机器人的环境感知和导航、以及室内场景的数字化建模等。该研究有助于提升这些应用的用户体验和智能化水平，并为相关领域的研究提供新的思路。

## 📄 摘要（原文）

> The demand for semantically rich 3D models of indoor scenes is rapidly growing, driven by applications in augmented reality, virtual reality, and robotics. However, creating them from sparse views remains a challenge due to geometric ambiguity. Existing methods often treat semantics as a passive feature painted on an already-formed, and potentially flawed, geometry. We posit that for robust sparse-view reconstruction, semantic understanding instead be an active, guiding force. This paper introduces AlignGS, a novel framework that actualizes this vision by pioneering a synergistic, end-to-end optimization of geometry and semantics. Our method distills rich priors from 2D foundation models and uses them to directly regularize the 3D representation through a set of novel semantic-to-geometry guidance mechanisms, including depth consistency and multi-faceted normal regularization. Extensive evaluations on standard benchmarks demonstrate that our approach achieves state-of-the-art results in novel view synthesis and produces reconstructions with superior geometric accuracy. The results validate that leveraging semantic priors as a geometric regularizer leads to more coherent and complete 3D models from limited input views. Our code is avaliable at https://github.com/MediaX-SJTU/AlignGS .

