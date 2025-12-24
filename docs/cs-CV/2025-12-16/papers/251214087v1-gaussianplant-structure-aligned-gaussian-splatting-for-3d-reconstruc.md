---
layout: default
title: "GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants"
---

# GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14087" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14087v1</a>
  <a href="https://arxiv.org/pdf/2512.14087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14087v1', 'GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Submitted to IEEE TPAMI, under review

---

## 💡 一句话要点

**GaussianPlant：提出结构对齐的高斯溅射方法，用于植物三维重建。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `植物重建` `结构化表示` `表型分析` `多视角图像` `外观建模` `结构建模`

## 📋 核心要点

1. 现有3DGS方法在植物重建中缺乏对内部结构的建模，限制了其在植物表型分析等领域的应用。
2. GaussianPlant通过引入结构基元(StPs)和外观基元(ApPs)，解耦了植物的结构和外观表示。
3. 实验结果表明，GaussianPlant能够实现高保真度的外观重建和精确的结构重建，并能提取分支结构和叶片实例。

## 📝 摘要（中文）

本文提出了一种基于3D高斯溅射(3DGS)的方法，用于从多视角图像中联合恢复植物的外观和内部结构。虽然3DGS在场景外观的新视角合成方面表现出强大的重建能力，但它缺乏支撑这些外观的结构表示(例如，植物的分枝模式)，这限制了其在植物表型分析等任务中的适用性。为了实现高保真外观和结构重建，我们引入了GaussianPlant，一种分层的3DGS表示，它解耦了结构和外观。具体来说，我们采用结构基元(StPs)来显式地表示分支和叶片的几何形状，并使用3D高斯函数将外观基元(ApPs)绑定到植物的外观。StPs表示植物的简化结构，即，将分支建模为圆柱体，将叶片建模为圆盘。为了准确区分分支和叶片，StP的属性(即，分支或叶片)以自组织的方式进行优化。ApPs绑定到每个StP，以表示分支或叶片的外观，就像传统的3DGS一样。StPs和ApPs使用输入多视角图像上的重渲染损失以及从ApP到StP的梯度流(使用绑定对应关系信息)进行联合优化。我们进行了实验，以定性地评估外观和结构的重建精度，并进行了真实世界的实验，以定性地验证实际性能。实验表明，GaussianPlant通过ApPs实现了高保真外观重建，并通过StPs实现了精确的结构重建，从而能够提取分支结构和叶片实例。

## 🔬 方法详解

**问题定义**：现有的3D高斯溅射方法虽然能够较好地重建场景的外观，但在植物的三维重建任务中，无法有效地捕捉植物的内部结构，例如分支的拓扑结构和叶片的分布。这使得这些方法难以应用于需要理解植物结构的下游任务，如植物表型分析。现有方法缺乏对植物结构信息的显式建模，导致重建结果仅仅是外观的复现，而无法提供结构上的可解释性。

**核心思路**：GaussianPlant的核心思路是将植物的结构和外观进行解耦表示。通过引入结构基元（StPs）来显式地建模植物的骨架结构，例如将分支建模为圆柱体，叶片建模为圆盘。然后，使用外观基元（ApPs）来表示植物表面的细节外观，ApPs与StPs绑定，从而将外观信息与结构信息关联起来。通过联合优化StPs和ApPs，可以同时实现高保真度的外观重建和精确的结构重建。

**技术框架**：GaussianPlant的整体框架包含以下几个主要模块：1) **结构基元（StPs）初始化**：根据输入的多视角图像，初始化一组StPs，用于表示植物的骨架结构。2) **外观基元（ApPs）初始化**：为每个StP绑定一组ApPs，用于表示该结构基元对应的外观信息。3) **联合优化**：通过最小化重渲染损失，联合优化StPs和ApPs的参数。重渲染损失衡量了重建图像与输入图像之间的差异。同时，利用ApP到StP的梯度流，将外观信息反向传播到结构信息，从而优化StPs的结构参数。4) **结构提取**：优化完成后，可以从StPs中提取植物的分支结构和叶片实例。

**关键创新**：GaussianPlant的关键创新在于引入了结构化的3D高斯溅射表示，将植物的结构和外观进行解耦。与传统的3DGS方法相比，GaussianPlant能够显式地建模植物的内部结构，从而实现更精确的结构重建。此外，通过ApP到StP的梯度流，可以将外观信息反向传播到结构信息，从而优化结构参数，进一步提高了结构重建的精度。

**关键设计**：在StPs的设计上，论文将分支建模为圆柱体，叶片建模为圆盘，并使用参数化的方式表示这些几何形状。StPs的属性（分支或叶片）通过自组织的方式进行优化，以准确区分不同的结构元素。在损失函数的设计上，除了重渲染损失外，还引入了正则化项，以约束StPs的形状和分布。ApPs的优化方式与传统的3DGS类似，使用梯度下降法更新高斯分布的参数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14087v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14087v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14087v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GaussianPlant能够实现高保真度的外观重建和精确的结构重建。与传统的3DGS方法相比，GaussianPlant能够更准确地提取植物的分支结构和叶片实例。在合成数据集和真实数据集上都取得了良好的效果，验证了该方法的有效性和鲁棒性。

## 🎯 应用场景

GaussianPlant在植物表型分析、农业监测、虚拟植物建模等领域具有广泛的应用前景。它可以用于自动提取植物的结构特征，例如分支长度、叶片数量等，从而为植物生长研究提供数据支持。此外，GaussianPlant还可以用于创建逼真的虚拟植物模型，应用于游戏、电影等领域。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

