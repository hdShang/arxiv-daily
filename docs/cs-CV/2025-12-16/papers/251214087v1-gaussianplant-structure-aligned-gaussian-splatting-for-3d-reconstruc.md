---
layout: default
title: GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants
---

# GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants

**arXiv**: [2512.14087v1](https://arxiv.org/abs/2512.14087) | [PDF](https://arxiv.org/pdf/2512.14087.pdf)

**作者**: Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Submitted to IEEE TPAMI, under review

---

## 💡 一句话要点

**GaussianPlant：提出结构对齐的高斯溅射方法，用于植物三维重建**

🎯 **匹配领域**: **3D重建与高斯 (3D Reconstruction & Gaussian)**

**关键词**: `植物三维重建` `高斯溅射` `结构化表示` `植物表型分析` `多视角重建`

## 📋 核心要点

1. 现有3D高斯溅射方法在植物重建中缺乏对植物内部结构的有效表示，限制了其在植物表型分析等领域的应用。
2. GaussianPlant通过引入结构基元（StPs）和外观基元（ApPs），显式地解耦了植物的结构和外观表示。
3. 实验结果表明，GaussianPlant能够实现高保真度的外观重建和准确的结构重建，从而能够提取分支结构和叶片实例。

## 📝 摘要（中文）

本文提出了一种基于3D高斯溅射(3DGS)的多视角图像植物外观和内部结构联合重建方法。虽然3DGS在场景外观的新视角合成方面表现出强大的重建能力，但它缺乏对外观背后结构（例如，植物的分枝模式）的表示，这限制了其在植物表型分析等任务中的应用。为了实现高保真外观和结构重建，我们引入了GaussianPlant，一种分层3DGS表示，它解耦了结构和外观。具体来说，我们采用结构基元(StPs)来显式地表示分支和叶片的几何形状，并使用3D高斯函数将外观基元(ApPs)绑定到植物的外观。StPs表示植物的简化结构，即将分支建模为圆柱体，将叶片建模为圆盘。为了准确区分分支和叶片，StP的属性（即分支或叶片）以自组织的方式进行优化。ApPs绑定到每个StP，以表示分支或叶片的外观，类似于传统的3DGS。StPs和ApPs使用输入多视角图像上的重渲染损失以及从ApP到StP的梯度流（使用绑定对应关系信息）进行联合优化。我们进行了实验，以定性地评估外观和结构的重建精度，并进行了真实世界的实验，以定性地验证实际性能。实验表明，GaussianPlant通过ApPs实现了高保真外观重建，并通过StPs实现了准确的结构重建，从而能够提取分支结构和叶片实例。

## 🔬 方法详解

**问题定义**：现有基于3D高斯溅射的植物重建方法主要关注外观重建，缺乏对植物内部结构（如分支模式、叶片分布）的有效建模。这限制了其在需要结构信息的植物表型分析、植物生长模拟等领域的应用。现有方法难以同时保证重建外观的真实性和结构信息的准确性。

**核心思路**：GaussianPlant的核心思路是将植物的结构和外观解耦表示。通过引入结构基元（StPs）显式地建模植物的骨架结构，并使用外观基元（ApPs）表示植物表面的细节纹理。StPs负责捕捉植物的分支和叶片分布，ApPs负责渲染逼真的外观。通过联合优化StPs和ApPs，实现结构和外观的协同重建。

**技术框架**：GaussianPlant的整体框架包含以下几个主要模块：1) **结构基元（StPs）初始化**：使用圆柱体和圆盘分别初始化分支和叶片。2) **外观基元（ApPs）初始化**：在StPs的基础上，使用3D高斯函数初始化外观。3) **联合优化**：通过重渲染损失和结构约束损失，联合优化StPs和ApPs的参数。重渲染损失保证外观重建的质量，结构约束损失保证结构重建的准确性。4) **结构提取**：从优化后的StPs中提取植物的分支结构和叶片实例。

**关键创新**：GaussianPlant的关键创新在于：1) 提出了一种分层的3DGS表示，将植物的结构和外观解耦。2) 引入了结构基元（StPs）来显式地建模植物的骨架结构。3) 设计了一种联合优化策略，同时优化结构和外观，保证了重建的质量和准确性。与现有方法相比，GaussianPlant能够同时实现高保真度的外观重建和准确的结构重建。

**关键设计**：1) **StPs的参数化**：分支表示为圆柱体，叶片表示为圆盘，参数包括位置、方向、半径等。2) **ApPs的参数化**：使用3D高斯函数表示外观，参数包括位置、协方差矩阵、颜色等。3) **重渲染损失**：使用L1损失或L2损失来衡量重建图像与真实图像之间的差异。4) **结构约束损失**：使用正则化项来约束StPs的形状和分布，例如，限制分支的长度和角度。

## 📊 实验亮点

论文通过实验验证了GaussianPlant的有效性。实验结果表明，GaussianPlant能够实现高保真度的外观重建和准确的结构重建。与传统的3DGS方法相比，GaussianPlant在结构重建方面取得了显著的提升。定性结果表明，GaussianPlant能够准确地提取植物的分支结构和叶片实例。真实场景实验验证了GaussianPlant在实际应用中的可行性。

## 🎯 应用场景

GaussianPlant在植物表型分析、植物生长模拟、农业监测、园艺设计等领域具有广泛的应用前景。它可以用于自动提取植物的结构参数，例如分支长度、叶片数量、叶片角度等，从而为植物表型分析提供数据支持。此外，GaussianPlant还可以用于植物生长模拟，预测植物的生长趋势。在农业监测领域，可以用于评估农作物的生长状况。在园艺设计领域，可以用于创建逼真的植物模型。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

