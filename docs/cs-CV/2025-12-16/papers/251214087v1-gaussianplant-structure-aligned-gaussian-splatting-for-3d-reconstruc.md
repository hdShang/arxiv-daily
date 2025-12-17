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

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `植物重建` `结构建模` `表型分析` `多视角图像`

## 📋 核心要点

1. 现有3DGS方法在植物重建中缺乏对内部结构（如分枝模式）的显式建模，限制了其在植物表型分析等领域的应用。
2. GaussianPlant通过引入结构基元(StPs)和外观基元(ApPs)的分层3DGS表示，解耦了植物的结构和外观信息。
3. 实验结果表明，GaussianPlant能够实现高保真度的外观重建和准确的结构重建，从而能够提取植物的分枝结构和叶片实例。

## 📝 摘要（中文）

本文提出了一种基于3D高斯溅射(3DGS)的多视角图像植物外观和内部结构联合重建方法。3DGS虽然能稳健地重建场景外观以进行新视角合成，但缺乏外观之下的结构表示(例如，植物的分枝模式)，这限制了其在植物表型分析等任务中的应用。为了实现高保真外观和结构重建，我们引入了GaussianPlant，一种分层3DGS表示，它解耦了结构和外观。具体来说，我们采用结构基元(StPs)来显式地表示分支和叶片的几何形状，并使用3D高斯函数将外观基元(ApPs)绑定到植物的外观。StPs表示植物的简化结构，即将分支建模为圆柱体，将叶片建模为圆盘。为了准确区分分支和叶片，StP的属性(即分支或叶片)以自组织的方式进行优化。ApPs绑定到每个StP，以表示分支或叶片的外观，类似于传统的3DGS。StPs和ApPs使用输入多视角图像上的重渲染损失以及从ApP到StP的梯度流(使用绑定对应关系信息)进行联合优化。我们进行了实验，以定性地评估外观和结构的重建精度，并进行了真实世界的实验，以定性地验证实际性能。实验表明，GaussianPlant通过ApPs实现了高保真外观重建，并通过StPs实现了准确的结构重建，从而能够提取分支结构和叶片实例。

## 🔬 方法详解

**问题定义**：现有基于3D高斯溅射的植物重建方法主要关注外观重建，忽略了植物的内部结构信息，如分枝模式、叶片分布等。这使得重建结果难以用于植物表型分析、生长模拟等需要结构信息的应用。因此，如何同时实现植物外观的高保真重建和内部结构的准确建模是一个关键问题。

**核心思路**：GaussianPlant的核心思路是将植物的结构和外观解耦，分别使用结构基元(StPs)和外观基元(ApPs)进行表示。StPs负责建模植物的骨架结构，如分支和叶片的几何形状；ApPs则负责建模植物表面的颜色、纹理等外观信息。通过将ApPs绑定到StPs上，可以实现结构和外观的关联，从而在优化过程中利用外观信息指导结构重建，并利用结构信息约束外观重建。

**技术框架**：GaussianPlant的整体框架包括以下几个主要模块：1) **结构基元(StPs)初始化**：使用简化的几何形状（圆柱体表示分支，圆盘表示叶片）初始化植物的骨架结构。2) **外观基元(ApPs)初始化**：使用3D高斯函数初始化植物的外观信息，类似于传统的3DGS。3) **StPs和ApPs绑定**：建立ApPs和StPs之间的对应关系，将ApPs绑定到相应的StPs上。4) **联合优化**：使用多视角图像的重渲染损失以及从ApP到StP的梯度流，联合优化StPs和ApPs的参数。

**关键创新**：GaussianPlant的关键创新在于：1) 提出了结构和外观解耦的分层3DGS表示，能够同时实现植物外观的高保真重建和内部结构的准确建模。2) 引入了结构基元(StPs)的概念，显式地建模植物的骨架结构。3) 设计了从ApP到StP的梯度流，利用外观信息指导结构重建。

**关键设计**：在StPs的初始化中，分支被建模为圆柱体，叶片被建模为圆盘。StPs的属性（分支或叶片）以自组织的方式进行优化，以准确区分分支和叶片。ApPs绑定到每个StP，以表示分支或叶片的外观，类似于传统的3DGS。StPs和ApPs使用输入多视角图像上的重渲染损失以及从ApP到StP的梯度流(使用绑定对应关系信息)进行联合优化。

## 📊 实验亮点

实验结果表明，GaussianPlant能够实现高保真度的植物外观重建和准确的结构重建。通过与现有3DGS方法进行对比，GaussianPlant在结构重建方面取得了显著的提升，能够准确提取植物的分枝结构和叶片实例。定性实验也验证了GaussianPlant在真实场景中的有效性。

## 🎯 应用场景

GaussianPlant在植物表型分析、虚拟植物建模、农业监测等领域具有广泛的应用前景。它可以用于自动提取植物的分枝结构、叶片数量、叶片大小等表型参数，为植物育种和栽培提供数据支持。此外，GaussianPlant还可以用于创建逼真的虚拟植物模型，应用于游戏、电影等领域。在农业监测方面，可以利用该技术对农作物的生长状态进行评估，及时发现病虫害等问题。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

