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

**提出GaussianPlant以解决植物3D重建中的结构与外观分离问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D重建` `植物表型分析` `高斯点云` `结构与外观分离` `计算机视觉` `生态监测`

## 📋 核心要点

1. 现有的3D重建方法在植物的外观重建上表现良好，但缺乏对植物结构的有效表示，限制了其在植物表型分析中的应用。
2. 本研究提出GaussianPlant，通过引入结构原语和外观原语，明确分离植物的结构和外观，实现高保真度的重建。
3. 实验结果表明，GaussianPlant在外观和结构重建上均取得显著提升，能够准确提取植物的枝干和叶片实例。

## 📝 摘要（中文）

我们提出了一种基于多视角图像的植物外观和内部结构联合恢复方法，称为GaussianPlant，利用3D高斯点云（3DGS）进行植物的3D重建。尽管3DGS在新视角合成中表现出色，但缺乏对植物外观背后结构的表示，限制了其在植物表型分析等任务中的应用。为此，我们引入了分层的3DGS表示，明确区分结构原语（StPs）和外观原语（ApPs），通过优化自组织方式来准确区分植物的枝干和叶片。实验结果表明，GaussianPlant在外观重建和结构重建方面均表现出高保真度，能够有效提取植物的枝干结构和叶片实例。

## 🔬 方法详解

**问题定义**：本论文旨在解决植物3D重建中外观与结构分离的问题。现有的3D高斯点云方法在重建植物外观时，未能有效捕捉其内部结构特征，限制了其在植物表型分析等领域的应用。

**核心思路**：GaussianPlant通过引入结构原语（StPs）和外观原语（ApPs），将植物的结构和外观进行明确分离。StPs用于表示植物的枝干和叶片几何形状，而ApPs则用于描述其外观特征。这样的设计使得重建过程能够同时关注外观和结构信息。

**技术框架**：GaussianPlant的整体架构包括两个主要模块：结构原语模块和外观原语模块。结构原语模块负责优化植物的枝干和叶片几何形状，而外观原语模块则通过与结构原语的绑定关系来优化外观特征。两者通过重渲染损失和梯度流进行联合优化。

**关键创新**：本研究的主要创新在于引入了结构原语和外观原语的分层表示，解决了传统3DGS方法无法有效捕捉植物结构的问题。这一方法使得植物的枝干和叶片能够被准确建模，显著提升了重建的准确性。

**关键设计**：在参数设置上，StPs的属性（如枝干或叶片）通过自组织方式进行优化。损失函数包括重渲染损失，确保重建结果与输入的多视角图像一致。此外，利用绑定对应信息实现ApP到StP的梯度流，进一步增强了结构与外观的关联性。

## 📊 实验亮点

实验结果表明，GaussianPlant在外观重建方面达到了高保真度，结构重建的准确性也显著提升。与传统方法相比，GaussianPlant在提取植物枝干结构和叶片实例方面表现出更高的准确性和细节保留，具体性能数据尚未披露。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在植物表型分析、生态监测和农业科学等领域。通过准确重建植物的外观和结构，研究人员可以更好地理解植物生长模式、适应性以及与环境的相互作用，推动相关领域的研究进展。

## 📄 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

