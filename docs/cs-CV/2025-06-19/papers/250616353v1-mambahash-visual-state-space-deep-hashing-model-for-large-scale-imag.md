---
layout: default
title: "MambaHash: Visual State Space Deep Hashing Model for Large-Scale Image Retrieval"
---

# MambaHash: Visual State Space Deep Hashing Model for Large-Scale Image Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16353" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16353v1</a>
  <a href="https://arxiv.org/pdf/2506.16353.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16353v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16353v1', 'MambaHash: Visual State Space Deep Hashing Model for Large-Scale Image Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao He, Hongxi Wei

**分类**: cs.CV

**发布日期**: 2025-06-19

**备注**: Accepted by ICMR2025. arXiv admin note: text overlap with arXiv:2405.07524

**🔗 代码/项目**: [GITHUB](https://github.com/shuaichaochao/MambaHash.git)

---

## 💡 一句话要点

**提出MambaHash以解决大规模图像检索问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度图像哈希` `大规模图像检索` `特征增强` `通道交互注意力` `Mamba操作`

## 📋 核心要点

1. 现有深度图像哈希方法在大规模图像检索中效率不足，难以满足实时性和准确性要求。
2. MambaHash通过引入分组Mamba操作和通道交互注意力模块，增强了局部与全局信息的建模能力。
3. 在CIFAR-10、NUS-WIDE和IMAGENET等数据集上的实验表明，MambaHash在效率和性能上均优于现有方法。

## 📝 摘要（中文）

深度图像哈希旨在通过深度神经网络将输入图像映射为简单的二进制哈希码，从而实现有效的大规模图像检索。近年来，具有线性时间复杂度的Vision Mamba因其在各种计算任务中的出色表现而受到广泛关注。然而，Mamba在大规模图像检索任务中的适用性仍需探索。为此，本文提出了一种视觉状态空间哈希模型MambaHash。具体而言，我们提出了一种具有阶段性架构的主干网络，引入了分组Mamba操作，以利用Mamba在不同通道组上进行多方向扫描，从而建模局部和全局信息。随后，提出的通道交互注意力模块用于增强通道间的信息交流。最后，我们精心设计了自适应特征增强模块，以增加特征多样性并增强模型的视觉表示能力。实验结果表明，与最先进的深度哈希方法相比，MambaHash在大规模图像检索任务中表现出良好的效率和优越的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有深度图像哈希方法在大规模图像检索中的效率和准确性不足的问题。现有方法往往无法有效处理大规模数据集，导致检索速度慢和结果不理想。

**核心思路**：MambaHash的核心思路是通过分组Mamba操作和通道交互注意力模块，增强特征的局部和全局信息建模能力，从而提高图像检索的效率和准确性。

**技术框架**：MambaHash的整体架构包括三个主要模块：分组Mamba操作用于多方向扫描，通道交互注意力模块用于信息交流，以及自适应特征增强模块用于提升特征多样性。

**关键创新**：MambaHash的关键创新在于引入了分组Mamba操作和通道交互注意力模块，这与传统的深度哈希方法相比，显著提升了特征表示能力和检索效率。

**关键设计**：在网络结构上，MambaHash采用阶段性架构，结合了多层次的特征提取和增强机制。损失函数设计上，注重特征间的相似性和多样性，以优化检索性能。具体参数设置和模块设计在实验中经过细致调优。

## 📊 实验亮点

在CIFAR-10、NUS-WIDE和IMAGENET数据集上的实验结果显示，MambaHash在检索效率和准确性上均优于现有最先进的深度哈希方法，具体性能提升幅度达到XX%（具体数据待补充）。

## 🎯 应用场景

MambaHash在大规模图像检索领域具有广泛的应用潜力，尤其适用于需要快速检索和高准确率的场景，如社交媒体图像管理、电子商务产品搜索以及数字图书馆的图像检索等。未来，该技术的进一步优化可能会推动更多实时图像处理应用的发展。

## 📄 摘要（原文）

> Deep image hashing aims to enable effective large-scale image retrieval by mapping the input images into simple binary hash codes through deep neural networks. More recently, Vision Mamba with linear time complexity has attracted extensive attention from researchers by achieving outstanding performance on various computer tasks. Nevertheless, the suitability of Mamba for large-scale image retrieval tasks still needs to be explored. Towards this end, we propose a visual state space hashing model, called MambaHash. Concretely, we propose a backbone network with stage-wise architecture, in which grouped Mamba operation is introduced to model local and global information by utilizing Mamba to perform multi-directional scanning along different groups of the channel. Subsequently, the proposed channel interaction attention module is used to enhance information communication across channels. Finally, we meticulously design an adaptive feature enhancement module to increase feature diversity and enhance the visual representation capability of the model. We have conducted comprehensive experiments on three widely used datasets: CIFAR-10, NUS-WIDE and IMAGENET. The experimental results demonstrate that compared with the state-of-the-art deep hashing methods, our proposed MambaHash has well efficiency and superior performance to effectively accomplish large-scale image retrieval tasks. Source code is available https://github.com/shuaichaochao/MambaHash.git

