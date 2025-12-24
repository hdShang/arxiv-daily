---
layout: default
title: Wideband RF Radiance Field Modeling Using Frequency-embedded 3D Gaussian Splatting
---

# Wideband RF Radiance Field Modeling Using Frequency-embedded 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20714" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20714v2</a>
  <a href="https://arxiv.org/pdf/2505.20714.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20714v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20714v2', 'Wideband RF Radiance Field Modeling Using Frequency-embedded 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zechen Li, Lanqing Yang, Yiheng Bian, Hao Pan, Yongjian Fu, Yezhou Wang, Zhuxi Chen, Yi-Chao Chen, Guangtao Xue

**分类**: cs.NI, cs.AI, cs.LG

**发布日期**: 2025-05-27 (更新: 2025-11-21)

---

## 💡 一句话要点

**提出频率嵌入的3D高斯点云以解决宽带RF建模问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `宽带RF建模` `3D高斯点云` `频率嵌入` `电磁特征网络` `信号处理` `室内环境建模`

## 📋 核心要点

1. 现有的3D高斯点云技术无法在广泛频率范围内建模未知频率的RF辐射场，限制了其应用。
2. 本文提出了一种频率嵌入的电磁特征网络，利用3D高斯球体学习频率与传输特性之间的关系。
3. 实验结果显示，所提模型在功率角谱重建中取得了0.922的SSIM，显著优于现有单频模型的0.863。

## 📝 摘要（中文）

室内环境中通常存在多种频带的RF信号，如NB-IoT、Wi-Fi和毫米波，因此宽带RF建模对于异构RF系统的联合部署、跨频通信和分布式RF感知等实际应用至关重要。尽管现有的3D高斯点云技术能够有效重建单一频率下的RF辐射场，但无法在广泛频率范围内建模未知频率的场。本文提出了一种新颖的3D高斯点云算法，用于统一宽带RF辐射场建模，利用频率嵌入的电磁特征网络学习频率与传输特性之间的关系。通过在特定3D环境中使用稀疏频率样本的数据集，我们的模型能够高效重建任意和未见频率的RF辐射场。实验结果表明，所提模型在多个频率下训练，重建的功率角谱的结构相似性指数（SSIM）达到0.922，超越了现有单频3D高斯点云模型的0.863。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D高斯点云技术在宽带RF建模中的不足，尤其是在未知频率下的建模能力不足。现有方法无法有效处理多频带信号的复杂性，限制了其在实际应用中的有效性。

**核心思路**：论文提出的核心思路是引入频率嵌入的电磁特征网络，通过3D高斯球体在每个空间位置学习频率与传输特性（如衰减和辐射强度）之间的关系，从而实现对任意频率的RF辐射场的高效重建。

**技术框架**：整体架构包括数据采集、频率嵌入特征提取和RF辐射场重建三个主要模块。首先，利用稀疏频率样本构建数据集；然后，通过频率嵌入的电磁特征网络提取特征；最后，重建RF辐射场。

**关键创新**：最重要的技术创新在于引入频率嵌入的电磁特征网络，使得模型能够在广泛频率范围内进行有效建模，这与现有方法的单频建模能力形成鲜明对比。

**关键设计**：模型设计中采用了3D高斯球体作为特征提取的基础，损失函数设计为结构相似性指数（SSIM），以优化重建效果。网络结构上，结合了卷积神经网络和频率特征提取模块，以增强模型的表达能力。

## 📊 实验亮点

实验结果表明，所提模型在功率角谱重建中取得了0.922的结构相似性指数（SSIM），显著优于现有单频3D高斯点云模型的0.863，展示了在多频率下的建模能力和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括异构RF系统的联合部署、跨频通信和分布式RF感知等。通过实现宽带RF建模，能够提升室内环境中无线信号的管理和优化能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Indoor environments typically contain diverse RF signals distributed across multiple frequency bands, including NB-IoT, Wi-Fi, and millimeter-wave. Consequently, wideband RF modeling is essential for practical applications such as joint deployment of heterogeneous RF systems, cross-band communication, and distributed RF sensing. Although 3D Gaussian Splatting (3DGS) techniques effectively reconstruct RF radiance fields at a single frequency, they cannot model fields at arbitrary or unknown frequencies across a wide range. In this paper, we present a novel 3DGS algorithm for unified wideband RF radiance field modeling. RF wave propagation depends on signal frequency and the 3D spatial environment, including geometry and material electromagnetic (EM) properties. To address these factors, we introduce a frequency-embedded EM feature network that utilizes 3D Gaussian spheres at each spatial location to learn the relationship between frequency and transmission characteristics, such as attenuation and radiance intensity. With a dataset containing sparse frequency samples in a specific 3D environment, our model can efficiently reconstruct RF radiance fields at arbitrary and unseen frequencies. To assess our approach, we introduce a large-scale power angular spectrum (PAS) dataset with 50,000 samples spanning 1 to 94 GHz across six indoor environments. Experimental results show that the proposed model trained on multiple frequencies achieves a Structural Similarity Index Measure (SSIM) of 0.922 for PAS reconstruction, surpassing state-of-the-art single-frequency 3DGS models with SSIM of 0.863.

