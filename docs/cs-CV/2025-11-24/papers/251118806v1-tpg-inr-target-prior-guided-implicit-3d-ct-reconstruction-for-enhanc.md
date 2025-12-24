---
layout: default
title: "TPG-INR: Target Prior-Guided Implicit 3D CT Reconstruction for Enhanced Sparse-view Imaging"
---

# TPG-INR: Target Prior-Guided Implicit 3D CT Reconstruction for Enhanced Sparse-view Imaging

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18806" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18806v1</a>
  <a href="https://arxiv.org/pdf/2511.18806.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18806v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18806v1', 'TPG-INR: Target Prior-Guided Implicit 3D CT Reconstruction for Enhanced Sparse-view Imaging')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qinglei Cao, Ziyao Tang, Xiaoqin Tang

**分类**: cs.CV

**发布日期**: 2025-11-24

**备注**: Please consider this version as the latest camera-ready version

**🔗 代码/项目**: [GITHUB](https://github.com/qlcao171/TPG-INR)

---

## 💡 一句话要点

**提出TPG-INR以解决超稀视图下3D CT重建精度不足问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D CT重建` `隐式学习` `目标先验` `医学成像` `深度学习` `稀疏视图` `计算机视觉`

## 📋 核心要点

1. 现有隐式3D重建方法在超稀视图情况下，未能有效利用物体的解剖先验，导致重建精度和学习效率不足。
2. 本文提出的TPG-INR框架通过引入目标先验，结合位置和结构编码，提升了体素级隐式重建的效率和质量。
3. 实验结果显示，TPG-INR在复杂腹部数据集上学习效率提升十倍，重建质量在不同投影数下PSNR提升3.57至5.70 dB。

## 📝 摘要（中文）

X射线成像能够详细可视化内部结构，但现有的隐式3D重建方法在超稀视图场景中往往忽视了物体解剖先验的重要性，限制了重建精度和学习效率。为了解决这些挑战，本文提出了一种新颖的3D CT重建框架TPG-INR，利用从投影数据中提取的“目标先验”来增强隐式学习。该方法结合位置和结构编码，促进体素级隐式重建，并通过目标先验引导体素采样，显著提高学习效率和重建质量。实验结果表明，TPG-INR在复杂腹部数据集上显著提升了学习效率，并在重建质量上超越了当前领先模型NAF和最准确模型NeRP。

## 🔬 方法详解

**问题定义**：本文旨在解决现有隐式3D重建方法在超稀视图场景中重建精度不足的问题。现有方法往往忽视物体解剖先验，导致重建效果不佳。

**核心思路**：TPG-INR框架通过引入从投影数据中提取的目标先验，结合位置和结构编码，来增强隐式学习的效果。这种设计旨在提高体素采样的有效性，从而提升重建质量。

**技术框架**：该框架主要包括两个模块：目标先验提取模块和体素级隐式重建模块。目标先验提取模块负责从稀疏投影数据中快速估计高质量的目标先验，而隐式重建模块则利用这些先验信息进行体素重建。

**关键创新**：最重要的创新点在于引入了目标先验来指导体素采样和结构编码，显著提升了学习效率和重建质量。这一方法与现有模型相比，充分利用了物体的解剖信息。

**关键设计**：在技术细节上，采用CUDA加速算法进行目标先验的快速估计，并设计了适应性损失函数以优化重建效果。网络结构上，结合了位置编码和结构编码，以增强模型对复杂结构的学习能力。

## 📊 实验亮点

实验结果表明，TPG-INR在复杂腹部数据集上显著提升了学习效率，相较于当前领先模型NAF，效率提升达十倍。在重建质量方面，TPG-INR在10、20和30个投影下，PSNR分别提升了3.57 dB、5.42 dB和5.70 dB，超越了最准确模型NeRP。

## 🎯 应用场景

该研究的潜在应用领域包括医学成像、计算机辅助诊断和手术规划等。通过提高3D CT重建的精度和效率，TPG-INR能够为临床提供更为准确的内部结构可视化，进而提升医疗决策的质量和效率。未来，该方法有望推广到其他类型的成像技术中，推动医学影像学的发展。

## 📄 摘要（原文）

> X-ray imaging, based on penetration, enables detailed visualization of internal structures. Building on this capability, existing implicit 3D reconstruction methods have adapted the NeRF model and its variants for internal CT reconstruction. However, these approaches often neglect the significance of objects' anatomical priors for implicit learning, limiting both reconstruction precision and learning efficiency, particularly in ultra-sparse view scenarios. To address these challenges, we propose a novel 3D CT reconstruction framework that employs a 'target prior' derived from the object's projection data to enhance implicit learning. Our approach integrates positional and structural encoding to facilitate voxel-wise implicit reconstruction, utilizing the target prior to guide voxel sampling and enrich structural encoding. This dual strategy significantly boosts both learning efficiency and reconstruction quality. Additionally, we introduce a CUDA-based algorithm for rapid estimation of high-quality 3D target priors from sparse-view projections. Experiments utilizing projection data from a complex abdominal dataset demonstrate that the proposed model substantially enhances learning efficiency, outperforming the current leading model, NAF, by a factor of ten. In terms of reconstruction quality, it also exceeds the most accurate model, NeRP, achieving PSNR improvements of 3.57 dB, 5.42 dB, and 5.70 dB with 10, 20, and 30 projections, respectively. The code is available at https://github.com/qlcao171/TPG-INR.

