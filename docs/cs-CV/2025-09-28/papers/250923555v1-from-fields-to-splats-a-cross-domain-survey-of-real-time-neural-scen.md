---
layout: default
title: "From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations"
---

# From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23555" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23555v1</a>
  <a href="https://arxiv.org/pdf/2509.23555.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23555v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23555v1', 'From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera

**分类**: cs.CV

**发布日期**: 2025-09-28

**备注**: 18 pages

---

## 💡 一句话要点

**综述：实时神经场景表示，从NeRF到3D高斯溅射在多领域的应用与发展**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `神经辐射场` `3D高斯溅射` `神经场景表示` `实时渲染` `SLAM` `机器人操作` `远程呈现` `3D内容生成`

## 📋 核心要点

1. NeRF虽然能实现视角一致的光真实感渲染，但在优化速度和效率上存在不足，限制了其在实时应用中的部署。
2. 3DGS通过显式地使用3D高斯分布来表示场景，实现了高质量渲染和更快的优化速度，使其成为NeRF的有效替代方案。
3. 该综述系统地比较了3DGS在SLAM、远程呈现、机器人操作和3D内容生成等领域的应用，并分析了其优势、局限性和未来发展方向。

## 📝 摘要（中文）

神经场景表示，如神经辐射场（NeRF）和3D高斯溅射（3DGS），已经改变了3D环境的建模、渲染和解释方式。NeRF通过体渲染引入了视角一致的光真实感；3DGS作为一种显式、高效的替代方案迅速崛起，支持高质量渲染、更快的优化以及集成到混合管道中，以增强光真实感和任务驱动的场景理解。本综述考察了3DGS在SLAM、远程呈现和远程操作、机器人操作和3D内容生成中的应用。尽管这些领域存在差异，但它们具有共同的目标：光真实感渲染、有意义的3D结构和准确的下游任务。我们围绕统一的研究问题组织综述，解释了为什么3DGS越来越多地取代基于NeRF的方法：哪些技术优势推动了它的采用？它如何适应不同的输入模态和特定领域的约束？还存在哪些局限性？通过系统地比较特定领域的管道，我们表明3DGS平衡了光真实感、几何保真度和计算效率。该综述为利用神经渲染不仅用于图像合成，还用于真实和虚拟环境中的感知、交互和内容创建提供了一个路线图。

## 🔬 方法详解

**问题定义**：现有神经场景表示方法，特别是NeRF，在实时渲染和优化速度方面存在瓶颈，难以满足SLAM、机器人操作等对实时性要求高的应用场景。此外，NeRF在处理复杂场景时，计算量大，训练时间长，限制了其应用范围。

**核心思路**：论文的核心思路是分析和总结3D高斯溅射（3DGS）作为一种新兴的神经场景表示方法，如何在不同领域取代NeRF。3DGS通过显式地使用3D高斯分布来表示场景，避免了NeRF的体渲染过程，从而提高了渲染速度和优化效率。这种显式表示也使得3DGS更容易与其他图形渲染管线集成。

**技术框架**：该综述没有提出新的技术框架，而是对现有基于3DGS的方法进行了系统性的梳理和分类。它考察了3DGS在SLAM、远程呈现、机器人操作和3D内容生成等领域的应用，并分析了这些应用中3DGS的具体实现方式和性能表现。综述围绕着几个核心问题展开：3DGS的技术优势是什么？它如何适应不同的输入模态和领域约束？它还存在哪些局限性？

**关键创新**：该综述的关键创新在于它提供了一个跨领域的视角，将3DGS在不同领域的应用联系起来，并分析了其共性和差异。通过比较不同领域的应用，综述揭示了3DGS的优势和局限性，并为未来的研究方向提供了指导。

**关键设计**：该综述没有涉及具体的技术细节，而是侧重于对现有方法的分析和总结。它考察了不同领域中3DGS的参数设置、损失函数和网络结构，并分析了这些设计对性能的影响。综述还讨论了3DGS在处理不同类型数据（如RGB图像、深度图像、点云）时的策略。

## 📊 实验亮点

该综述系统地比较了3DGS在不同领域的应用，揭示了其在光真实感、几何保真度和计算效率方面的优势。与NeRF相比，3DGS在渲染速度和优化速度上具有显著优势，使其能够应用于实时场景。此外，3DGS的显式表示也使其更容易与其他图形渲染管线集成，为混合渲染提供了可能性。具体性能数据和对比基线需要在相关论文中查找。

## 🎯 应用场景

该研究对SLAM、远程呈现、机器人操作和3D内容生成等领域具有重要的应用价值。3DGS的快速渲染和优化能力使其能够应用于实时SLAM和机器人操作，提高系统的响应速度和精度。同时，其高质量的渲染效果也使其在远程呈现和3D内容生成方面具有广泛的应用前景，例如虚拟现实、增强现实和游戏开发。

## 📄 摘要（原文）

> Neural scene representations such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have transformed how 3D environments are modeled, rendered, and interpreted. NeRF introduced view-consistent photorealism via volumetric rendering; 3DGS has rapidly emerged as an explicit, efficient alternative that supports high-quality rendering, faster optimization, and integration into hybrid pipelines for enhanced photorealism and task-driven scene understanding. This survey examines how 3DGS is being adopted across SLAM, telepresence and teleoperation, robotic manipulation, and 3D content generation. Despite their differences, these domains share common goals: photorealistic rendering, meaningful 3D structure, and accurate downstream tasks. We organize the review around unified research questions that explain why 3DGS is increasingly displacing NeRF-based approaches: What technical advantages drive its adoption? How does it adapt to different input modalities and domain-specific constraints? What limitations remain? By systematically comparing domain-specific pipelines, we show that 3DGS balances photorealism, geometric fidelity, and computational efficiency. The survey offers a roadmap for leveraging neural rendering not only for image synthesis but also for perception, interaction, and content creation across real and virtual environments.

