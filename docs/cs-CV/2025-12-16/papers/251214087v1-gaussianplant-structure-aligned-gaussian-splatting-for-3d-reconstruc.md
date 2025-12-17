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

**提出GaussianPlant方法，通过解耦结构和外观的高斯溅射表示，解决植物三维重建中外观与内部结构难以同时恢复的问题。**

🎯 **匹配领域**: **深度估计** **强化学习**

**关键词**: `三维高斯溅射` `植物三维重建` `结构外观解耦` `多视角图像` `植物表型分析` `分层表示` `联合优化` `结构基元`

## 📋 核心要点

1. 现有3DGS方法在植物重建中缺乏内部结构表示，限制了其在表型分析等任务的应用。
2. 提出分层高斯溅射表示，通过结构基元和外观基元解耦结构与外观，实现联合优化。
3. 实验验证了GaussianPlant在外观和结构重建上的高保真性，能有效提取分支和叶片实例。

## 📝 摘要（中文）

我们提出了一种基于三维高斯溅射（3DGS）的方法，用于从多视角图像中联合恢复植物植物的外观和内部结构。虽然3DGS在新视角合成中表现出强大的场景外观重建能力，但它缺乏支撑这些外观的结构表示（例如植物的分支模式），这限制了其在植物表型分析等任务中的应用。为了实现高保真外观和结构重建，我们引入了GaussianPlant，这是一种分层3DGS表示，将结构和外观解耦。具体来说，我们使用结构基元（StPs）来显式表示分支和叶片的几何形状，并使用外观基元（ApPs）通过三维高斯来表示植物的外观。StPs表示植物的简化结构，即将分支建模为圆柱体，叶片建模为圆盘。为了准确区分分支和叶片，StP的属性（即分支或叶片）以自组织方式进行优化。ApPs绑定到每个StP，以像传统3DGS那样表示分支或叶片的外观。StPs和ApPs通过输入多视角图像的重渲染损失以及使用绑定对应信息从ApP到StP的梯度流进行联合优化。我们进行了实验，定性地评估外观和结构的重建准确性，以及实际实验来定性地验证实际性能。实验表明，GaussianPlant通过ApPs实现了高保真外观重建，通过StPs实现了准确的结构重建，从而能够提取分支结构和叶片实例。

## 🔬 方法详解

**问题定义**：论文旨在解决从多视角图像中联合恢复植物外观和内部结构的问题。现有三维高斯溅射（3DGS）方法虽能高效重建外观，但缺乏对植物分支模式等内部结构的显式表示，这限制了其在植物表型分析等需要结构信息的任务中的应用。

**核心思路**：论文提出GaussianPlant，通过引入分层3DGS表示，将结构和外观解耦。具体地，使用结构基元（StPs）显式建模分支和叶片的简化几何，外观基元（ApPs）绑定到StPs以表示外观，从而实现外观与结构的联合优化。

**技术框架**：整体框架包括两个主要模块：结构基元（StPs）和外观基元（ApPs）。StPs负责表示植物的简化结构（分支为圆柱体，叶片为圆盘），ApPs负责表示外观。优化过程基于多视角图像的重渲染损失，以及从ApP到StP的梯度流，通过绑定对应信息实现联合训练。

**关键创新**：最重要的创新点是提出分层高斯溅射表示，将结构和外观解耦，这在传统3DGS中是缺失的。通过StPs显式建模结构，ApPs绑定到StPs，实现了外观与结构的协同优化，本质区别在于引入了结构感知能力。

**关键设计**：关键设计包括：StPs的属性（分支或叶片）通过自组织方式优化以准确区分结构；ApPs使用三维高斯表示外观；损失函数结合重渲染损失和梯度流损失，确保外观和结构的一致性；绑定对应信息用于传递梯度，促进联合优化。

## 📊 实验亮点

实验表明，GaussianPlant在外观重建上达到高保真水平，结构重建准确，能有效提取分支结构和叶片实例。定性评估显示，相比传统3DGS，GaussianPlant在结构表示上有显著提升，实际实验验证了其在真实场景中的鲁棒性。具体性能数据未知，但重建质量得到定性确认。

## 🎯 应用场景

该研究在植物表型分析、农业监测和生态研究中具有重要应用价值。通过同时恢复外观和内部结构，GaussianPlant能支持植物生长跟踪、疾病检测和形态分析，提升自动化农业和生物研究的效率。未来可能扩展到其他复杂结构物体的三维重建。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

