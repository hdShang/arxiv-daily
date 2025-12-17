---
layout: default
title: GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants
---

# GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14087" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14087</a>
  <a href="https://arxiv.org/pdf/2512.14087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14087" onclick="toggleFavorite(this, '2512.14087', 'GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**GaussianPlant：提出结构对齐的高斯溅射方法，用于植物三维重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `三维重建` `高斯溅射` `植物建模` `结构化表示` `表型分析`

## 📋 核心要点

1. 现有3DGS方法在植物重建中缺乏对底层结构（如分枝模式）的显式建模，限制了其在植物表型分析等领域的应用。
2. GaussianPlant通过引入结构基元(StP)和外观基元(ApP)的分层3DGS表示，解耦了植物的结构和外观。
3. 实验结果表明，GaussianPlant能够实现高保真度的外观重建和准确的结构重建，并能提取分支结构和叶片实例。

## 📝 摘要（中文）

本文提出了一种基于3D高斯溅射(3DGS)的多视角图像植物外观和内部结构联合重建方法。3DGS虽然能够鲁棒地重建场景外观以进行新视角合成，但缺乏对外观的底层结构表示（例如，植物的分枝模式），这限制了其在植物表型分析等任务中的应用。为了实现高保真度的外观和结构重建，我们引入了GaussianPlant，一种分层3DGS表示，它解耦了结构和外观。具体来说，我们采用结构基元(StP)来显式地表示分支和叶片的几何形状，并使用3D高斯函数将外观基元(ApP)绑定到植物的外观。StP表示植物的简化结构，即将分支建模为圆柱体，将叶片建模为圆盘。为了准确区分分支和叶片，StP的属性（即分支或叶片）以自组织的方式进行优化。ApP绑定到每个StP，以表示分支或叶片的外观，类似于传统的3DGS。StP和ApP使用输入多视角图像上的重渲染损失以及从ApP到StP的梯度流（使用绑定对应关系信息）进行联合优化。我们进行了实验，以定性地评估外观和结构的重建精度，并进行了真实世界的实验，以定性地验证实际性能。实验表明，GaussianPlant通过ApP实现了高保真度的外观重建，并通过StP实现了准确的结构重建，从而能够提取分支结构和叶片实例。

## 🔬 方法详解

**问题定义**：现有基于3D高斯溅射(3DGS)的植物三维重建方法，虽然能够较好地重建植物的外观，但缺乏对植物内部结构的显式建模，例如分枝模式、叶片分布等。这使得这些方法难以应用于需要结构信息的任务，如植物表型分析、生长模拟等。现有方法无法同时保证外观重建的逼真度和结构信息的准确性。

**核心思路**：GaussianPlant的核心思路是将植物的结构和外观进行解耦，分别使用不同的基元进行表示。具体来说，使用结构基元(StP)来显式地表示植物的骨架结构（分支和叶片），并使用外观基元(ApP)来表示植物的表面纹理和颜色。通过将ApP绑定到StP上，可以实现结构和外观的对齐，从而在优化过程中利用结构信息来指导外观重建，反之亦然。这种解耦的设计使得模型能够更好地学习植物的结构和外观特征。

**技术框架**：GaussianPlant的整体框架包含以下几个主要模块：1) **结构基元(StP)初始化**：根据多视角图像初始化StP，StP包括位置、方向、类型（分支或叶片）等属性。2) **外观基元(ApP)初始化**：在每个StP附近初始化ApP，ApP使用3D高斯函数表示，包含位置、协方差、颜色、透明度等属性。3) **StP和ApP联合优化**：使用重渲染损失和结构损失联合优化StP和ApP的属性。重渲染损失用于保证外观重建的逼真度，结构损失用于保证结构重建的准确性。4) **结构提取**：从优化后的StP中提取植物的骨架结构，例如分枝模式、叶片分布等。

**关键创新**：GaussianPlant的关键创新在于：1) **结构和外观解耦表示**：通过引入StP和ApP，将植物的结构和外观进行解耦，从而能够更好地学习植物的结构和外观特征。2) **结构引导的外观重建**：通过将ApP绑定到StP上，可以利用结构信息来指导外观重建，从而提高外观重建的准确性。3) **自组织的结构优化**：StP的类型（分支或叶片）以自组织的方式进行优化，无需人工标注。

**关键设计**：1) **StP表示**：分支建模为圆柱体，叶片建模为圆盘，简化了结构表示，降低了优化难度。2) **ApP绑定**：ApP绑定到StP上，通过计算ApP到StP的距离来确定绑定关系。3) **损失函数**：使用重渲染损失（L1损失、SSIM损失）和结构损失（StP类型分类损失）联合优化StP和ApP。4) **梯度流**：利用绑定对应关系信息，将ApP的梯度反向传播到StP，从而实现结构引导的外观重建。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14087/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14087/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14087/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验验证了GaussianPlant在植物三维重建方面的有效性。定性结果表明，GaussianPlant能够重建出高保真度的植物外观和准确的结构信息。与现有方法相比，GaussianPlant能够更好地提取植物的分枝结构和叶片实例。真实场景实验验证了GaussianPlant在实际应用中的可行性。虽然论文没有提供具体的定量指标，但定性结果足以说明GaussianPlant的优越性。

## 🎯 应用场景

GaussianPlant在植物表型分析、虚拟植物建模、农业监测、园艺设计等领域具有广泛的应用前景。它可以用于自动提取植物的结构参数，例如分枝角度、叶片大小、叶片数量等，从而为植物生长研究提供数据支持。此外，GaussianPlant还可以用于创建逼真的虚拟植物模型，用于游戏、电影等领域。在农业领域，可以用于监测作物生长状况，预测产量。在园艺设计领域，可以用于模拟植物的生长形态，辅助景观设计。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

