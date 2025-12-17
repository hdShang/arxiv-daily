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

**提出GaussianPlant方法，通过解耦结构和外观的高斯溅射表示，实现植物高保真外观与精确结构的三维重建。**

**关键词**: `三维高斯溅射` `植物三维重建` `结构-外观解耦` `多视角图像` `植物表型分析` `分层表示` `自组织优化` `联合优化`

## 📋 核心要点

1. 现有3DGS方法缺乏植物内部结构表示，限制了在植物表型分析等任务中的应用。
2. 提出分层3DGS表示GaussianPlant，通过结构基元和外观基元解耦结构与外观。
3. 实验验证了该方法在植物外观和结构重建上的高保真性和准确性，支持分枝和叶片提取。

## 📝 摘要（中文）

我们提出了一种基于三维高斯溅射（3DGS）的方法，用于从多视角图像中联合恢复植物外观和内部结构。虽然3DGS在新视角合成中表现出强大的场景外观重建能力，但缺乏支撑这些外观的结构表示（如植物的分枝模式），这限制了其在植物表型分析等任务中的应用。为实现高保真外观和结构重建，我们引入了GaussianPlant，这是一种分层3DGS表示，解耦了结构和外观。具体而言，我们使用结构基元（StPs）显式表示枝干和叶片的几何结构，并使用外观基元（ApPs）通过三维高斯表示植物的外观。StPs表示植物的简化结构，即将枝干建模为圆柱体、叶片建模为圆盘。为准确区分枝干和叶片，StP的属性（即枝干或叶片）以自组织方式进行优化。ApPs绑定到每个StP，以传统3DGS方式表示枝干或叶片的外观。StPs和ApPs通过输入多视角图像的重渲染损失以及利用绑定对应信息从ApP到StP的梯度流进行联合优化。我们进行了实验，定性评估外观和结构的重建准确性，并通过真实世界实验定性验证实际性能。实验表明，GaussianPlant通过ApPs实现了高保真外观重建，通过StPs实现了精确结构重建，从而能够提取分枝结构和叶片实例。

## 🔬 方法详解

GaussianPlant的整体框架基于三维高斯溅射（3DGS），采用分层表示解耦结构和外观。关键技术创新点包括：引入结构基元（StPs）显式建模植物几何结构（枝干为圆柱体、叶片为圆盘），并以自组织方式优化其属性；使用外观基元（ApPs）绑定到StPs，通过三维高斯表示外观；通过重渲染损失和从ApP到StP的梯度流进行联合优化。与现有方法的主要区别在于，传统3DGS仅关注外观重建，而GaussianPlant通过结构-外观解耦，同时实现了高保真外观和精确结构重建，解决了植物三维重建中的结构表示缺失问题。

## 📊 实验亮点

实验表明，GaussianPlant在植物三维重建中实现了高保真外观重建和精确结构重建，能够有效提取分枝结构和叶片实例，验证了其在实际应用中的性能提升。

## 🎯 应用场景

该研究在植物表型分析、农业监测、植物建模和虚拟现实等领域具有潜在应用价值，能够支持精确的植物结构提取和外观渲染，提升相关任务的效率和准确性。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

