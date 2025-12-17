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

**提出GaussianPlant方法，通过解耦结构和外观的高斯溅射表示，解决植物三维重建中结构信息缺失的问题。**

🎯 **匹配领域**: **深度估计** **强化学习**

**关键词**: `三维高斯溅射` `植物三维重建` `结构外观解耦` `多视角图像` `植物表型分析` `分层表示` `联合优化` `几何建模`

## 📋 核心要点

1. 现有3DGS方法在植物重建中缺乏结构表示，限制了其在表型分析等任务的应用。
2. 提出分层3DGS表示，通过结构基元和外观基元解耦结构与外观，实现联合优化。
3. 实验验证了GaussianPlant在植物外观和结构重建上的高保真性能，支持枝干和叶片提取。

## 📝 摘要（中文）

我们提出了一种基于三维高斯溅射（3DGS）的方法，用于从多视角图像中联合恢复植物外观和内部结构。虽然3DGS在新视角合成中表现出强大的场景外观重建能力，但缺乏支撑这些外观的结构表示（例如植物的分枝模式），这限制了其在植物表型分析等任务中的应用。为了实现高保真外观和结构重建，我们引入了GaussianPlant，这是一种分层3DGS表示，解耦了结构和外观。具体来说，我们使用结构基元（StPs）显式表示枝干和叶片的几何形状，并使用外观基元（ApPs）通过三维高斯表示植物的外观。StPs表示植物的简化结构，即将枝干建模为圆柱体，叶片建模为圆盘。为了准确区分枝干和叶片，StP的属性（即枝干或叶片）以自组织方式优化。ApPs绑定到每个StP，以像传统3DGS那样表示枝干或叶片的外观。StPs和ApPs通过输入多视角图像的重渲染损失以及使用绑定对应信息从ApP到StP的梯度流进行联合优化。我们进行了实验，定性和定量评估外观和结构的重建准确性，以及实际实验定性验证实际性能。实验表明，GaussianPlant通过ApPs实现了高保真外观重建，通过StPs实现了准确结构重建，从而能够提取枝干结构和叶片实例。

## 🔬 方法详解

**问题定义**：论文旨在解决从多视角图像中重建植物三维模型时，现有3DGS方法缺乏结构表示的问题，导致无法准确捕捉植物的分枝模式和叶片实例，限制了在植物表型分析等领域的应用。

**核心思路**：通过引入分层3DGS表示，将植物的结构和外观解耦，使用结构基元（StPs）显式建模几何结构，外观基元（ApPs）负责外观细节，实现联合优化以同时获得高保真外观和准确结构。

**技术框架**：整体流程包括：1）从多视角图像初始化StPs和ApPs；2）StPs建模枝干为圆柱体、叶片为圆盘，属性自组织优化；3）ApPs绑定到StPs，使用3D高斯表示外观；4）通过重渲染损失和梯度流联合优化StPs和ApPs，最终输出解耦的结构和外观模型。

**关键创新**：最重要的创新是提出结构对齐的高斯溅射表示，通过StPs和ApPs的分层设计，首次在3DGS框架中实现植物结构和外观的显式解耦与联合重建，克服了传统方法结构信息缺失的痛点。

**关键设计**：关键设计包括：1）StPs使用简化几何（圆柱体和圆盘）表示结构，属性通过自组织方式优化以区分枝干和叶片；2）ApPs绑定到StPs，继承结构信息；3）损失函数结合重渲染损失（基于输入图像）和从ApP到StP的梯度流，利用绑定对应信息促进结构优化；4）优化过程联合更新StPs和ApPs参数，确保结构和外观一致性。

## 📊 实验亮点

实验结果表明，GaussianPlant在植物三维重建中实现了高保真外观和准确结构重建。具体地，通过ApPs获得的外观重建质量与传统3DGS相当，而通过StPs提取的枝干结构和叶片实例在定性评估中表现出色，验证了方法在联合优化中的有效性。实际实验进一步定性验证了其在实际场景中的稳健性能，支持植物表型分析任务。

## 🎯 应用场景

该研究在植物表型分析、农业监测、生态研究和虚拟植物建模等领域具有潜在应用价值。通过提供高保真外观和准确结构重建，GaussianPlant能够支持植物生长分析、病害检测和自动化农业管理，提升植物科学研究和农业技术的效率与精度。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

