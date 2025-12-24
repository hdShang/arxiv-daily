---
layout: default
title: Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting
---

# Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20729" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20729v1</a>
  <a href="https://arxiv.org/pdf/2505.20729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20729v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20729v1', 'Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu

**分类**: cs.CV

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出Intern-GS以解决稀疏视图三维重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏视图重建` `三维高斯点云` `视觉基础模型` `深度预测` `运动结构法`

## 📋 核心要点

1. 现有稀疏视图重建方法在数据有限的情况下，常常导致信息不完整，重建效果不理想。
2. Intern-GS通过引入视觉基础模型，优化三维高斯点云的初始化和优化过程，有效提升稀疏视图重建质量。
3. 实验结果显示，Intern-GS在多个数据集上均实现了最先进的渲染质量，超越了传统方法的性能。

## 📝 摘要（中文）

稀疏视图场景重建常面临由于观察数据有限而导致的显著挑战。这些限制导致信息不完整，现有方法的重建效果不佳。为此，我们提出了Intern-GS，这是一种新颖的方法，利用视觉基础模型的丰富先验知识来增强稀疏视图高斯点云重建的过程，从而实现高质量的场景重建。具体而言，Intern-GS在三维高斯点云的初始化和优化过程中均借助视觉基础模型，有效解决稀疏输入的局限性。通过DUSt3R生成稠密且非冗余的高斯点云，显著缓解了传统运动结构法在稀疏视图约束下的局限性。优化过程中，视觉基础模型预测未观察视图的深度和外观，精细调整三维高斯以补偿未见区域的信息缺失。大量实验表明，Intern-GS在包括LLFF、DTU和Tanks and Temples等多样数据集上实现了最先进的渲染质量。

## 🔬 方法详解

**问题定义**：本论文旨在解决稀疏视图下的三维场景重建问题。现有的运动结构法在数据稀缺时表现不佳，导致重建效果不理想。

**核心思路**：Intern-GS的核心思路是利用视觉基础模型的先验知识来指导三维高斯点云的初始化和优化，从而弥补稀疏输入带来的信息缺失。

**技术框架**：该方法的整体架构包括两个主要阶段：初始化阶段和优化阶段。在初始化阶段，使用DUSt3R生成稠密的高斯点云；在优化阶段，利用视觉基础模型预测未观察视图的深度和外观。

**关键创新**：Intern-GS的主要创新在于将视觉基础模型引入稀疏视图重建中，显著提高了重建的质量和准确性。这一方法与传统的运动结构法有本质区别，后者在稀疏数据下常常无法有效工作。

**关键设计**：在设计上，DUSt3R生成的高斯点云具有稠密性和非冗余性，优化过程中采用了深度和外观的预测机制，以补偿未见区域的信息缺失。

## 📊 实验亮点

在多个数据集上进行的实验表明，Intern-GS在渲染质量上达到了最先进的水平，特别是在LLFF、DTU和Tanks and Temples等大型场景中，表现出显著的性能提升，超越了现有的基线方法。

## 🎯 应用场景

该研究在计算机视觉、虚拟现实和机器人导航等领域具有广泛的应用潜力。通过提高稀疏视图下的三维重建质量，Intern-GS可以为自动驾驶、场景理解和增强现实等技术提供更为精确的环境建模，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Sparse-view scene reconstruction often faces significant challenges due to the constraints imposed by limited observational data. These limitations result in incomplete information, leading to suboptimal reconstructions using existing methodologies. To address this, we present Intern-GS, a novel approach that effectively leverages rich prior knowledge from vision foundation models to enhance the process of sparse-view Gaussian Splatting, thereby enabling high-quality scene reconstruction. Specifically, Intern-GS utilizes vision foundation models to guide both the initialization and the optimization process of 3D Gaussian splatting, effectively addressing the limitations of sparse inputs. In the initialization process, our method employs DUSt3R to generate a dense and non-redundant gaussian point cloud. This approach significantly alleviates the limitations encountered by traditional structure-from-motion (SfM) methods, which often struggle under sparse-view constraints. During the optimization process, vision foundation models predict depth and appearance for unobserved views, refining the 3D Gaussians to compensate for missing information in unseen regions. Extensive experiments demonstrate that Intern-GS achieves state-of-the-art rendering quality across diverse datasets, including both forward-facing and large-scale scenes, such as LLFF, DTU, and Tanks and Temples.

