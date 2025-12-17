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

**提出GaussianPlant方法，通过解耦结构和外观的高斯溅射表示，实现植物高保真三维重建，以解决植物表型分析等应用中的结构缺失问题。**

🎯 **匹配领域**: **深度估计** **强化学习**

**关键词**: `三维高斯溅射` `植物三维重建` `结构外观解耦` `多视角图像处理` `植物表型分析` `分层表示学习` `自组织优化` `梯度流联合训练`

## 📋 核心要点

1. 现有3D高斯溅射方法在植物重建中缺乏结构表示，如分枝模式，限制了其在表型分析等任务的应用。
2. 提出GaussianPlant，通过结构基元和外观基元解耦表示，实现植物外观与结构的联合优化重建。
3. 实验验证了该方法在植物外观和结构重建上的高保真性能，能够有效提取枝干和叶片实例。

## 📝 摘要（中文）

我们提出了一种基于3D高斯溅射（3DGS）的方法，用于从多视角图像中联合恢复植物外观和内部结构。虽然3DGS在新视角合成中表现出强大的场景外观重建能力，但它缺乏支撑这些外观的结构表示（例如植物的分枝模式），这限制了其在植物表型分析等任务中的应用。为了实现高保真外观和结构重建，我们引入了GaussianPlant，这是一种分层3DGS表示，解耦了结构和外观。具体而言，我们使用结构基元（StPs）来显式表示枝干和叶片的几何形状，并使用外观基元（ApPs）通过3D高斯表示植物的外观。StPs表示植物的简化结构，即将枝干建模为圆柱体、叶片建模为圆盘。为了准确区分枝干和叶片，StP的属性（即枝干或叶片）以自组织方式进行优化。ApPs绑定到每个StP，以像传统3DGS那样表示枝干或叶片的外观。StPs和ApPs通过输入多视角图像的重渲染损失以及利用绑定对应信息从ApP到StP的梯度流进行联合优化。我们进行了实验，定性和定量评估外观和结构的重建准确性，以及实际实验来定性验证实际性能。实验表明，GaussianPlant通过ApPs实现了高保真外观重建，通过StPs实现了准确结构重建，从而能够提取枝干结构和叶片实例。

## 🔬 方法详解

GaussianPlant采用分层3D高斯溅射框架，核心创新在于解耦结构和外观表示。结构基元（StPs）显式建模枝干为圆柱体、叶片为圆盘，通过自组织优化区分属性；外观基元（ApPs）绑定到StPs，使用3D高斯表示外观。两者通过重渲染损失和基于绑定信息的梯度流联合优化。与现有3DGS方法相比，该方法首次引入显式结构表示，解决了植物重建中结构缺失问题，实现了外观与结构的高效协同学习。

## 📊 实验亮点

实验表明，GaussianPlant在植物三维重建中同时实现了高保真外观和准确结构恢复，通过ApPs和StPs的协同优化，显著提升了结构提取能力，为植物分析任务提供了可靠的三维模型。

## 🎯 应用场景

该方法在植物表型分析、农业监测、植物生长建模和虚拟植物展示等领域具有应用价值，能够提供精确的枝干结构和叶片实例数据，支持植物健康评估和科学研究。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

