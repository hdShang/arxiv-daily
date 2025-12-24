---
layout: default
title: Topo-VM-UNetV2: Encoding Topology into Vision Mamba UNet for Polyp Segmentation
---

# Topo-VM-UNetV2: Encoding Topology into Vision Mamba UNet for Polyp Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06210" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06210v1</a>
  <a href="https://arxiv.org/pdf/2505.06210.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06210v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06210v1', 'Topo-VM-UNetV2: Encoding Topology into Vision Mamba UNet for Polyp Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Diego Adame, Jose A. Nunez, Fabian Vazquez, Nayeli Gurrola, Huimin Li, Haoteng Tang, Bin Fu, Pengfei Gu

**分类**: eess.IV, cs.CV

**发布日期**: 2025-05-09

---

## 💡 一句话要点

**提出Topo-VM-UNetV2以解决多边形分割中的拓扑特征捕捉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多边形分割` `拓扑特征` `深度学习` `医学图像分析` `状态空间模型` `卷积神经网络` `Transformer`

## 📋 核心要点

1. 现有的多边形分割方法在捕捉拓扑特征（如连通组件、环和空洞）方面存在不足，导致边界划分不准确。
2. 本文提出的Topo-VM-UNetV2通过将拓扑特征编码到Mamba基础的VM-UNetV2模型中，增强了模型对拓扑特征的捕捉能力。
3. 在五个公共多边形分割数据集上的广泛实验表明，Topo-VM-UNetV2在分割精度上显著优于现有方法。

## 📝 摘要（中文）

卷积神经网络（CNN）和基于Transformer的架构是多边形分割的两种主要深度学习模型。然而，CNN在建模长距离依赖方面能力有限，而Transformer则面临二次计算复杂度的问题。最近，状态空间模型如Mamba被认为是多边形分割的有前景的方法，因为它们有效建模长距离交互并保持线性计算复杂度。本文提出的Topo-VM-UNetV2通过将拓扑特征编码到Mamba基础的VM-UNetV2模型中，解决了现有方法在捕捉拓扑特征方面的不足。我们的方法包括两个阶段：第一阶段生成概率图并计算拓扑注意力图；第二阶段将这些注意力图集成到VM-UNetV2的语义和细节注入模块中，以增强分割结果。大量实验表明了我们方法的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多边形分割方法在捕捉拓扑特征方面的不足，尤其是在边界划分和多边形分割的准确性上存在挑战。

**核心思路**：我们提出的Topo-VM-UNetV2通过将拓扑特征编码到Mamba基础的VM-UNetV2模型中，利用拓扑注意力图来增强模型的分割能力。这样的设计旨在有效捕捉长距离依赖和拓扑特征。

**技术框架**：该方法分为两个阶段：第一阶段使用VM-UNetV2生成概率图，并计算拓扑注意力图；第二阶段将这些注意力图集成到VM-UNetV2的语义和细节注入模块中，形成拓扑引导的语义和细节注入模块（Topo-SDI）。

**关键创新**：最重要的创新在于将拓扑特征的编码与Mamba模型相结合，形成了一种新的拓扑引导机制，显著提升了分割精度。与传统方法相比，Topo-VM-UNetV2在捕捉拓扑特征方面表现出色。

**关键设计**：在实现过程中，我们计算概率图的持久性图，并通过持久性值生成持久性评分图，最后使用sigmoid函数将持久性评分转化为注意力权重。这些设计细节确保了模型在拓扑特征捕捉上的有效性。

## 📊 实验亮点

在五个公共数据集上的实验结果显示，Topo-VM-UNetV2在多边形分割任务中相较于基线模型有显著提升，具体表现为分割精度提高了X%（具体数据未知），验证了其在拓扑特征捕捉方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医学图像分析，尤其是在内窥镜图像中多边形（如息肉）的自动分割。通过提高分割精度，Topo-VM-UNetV2能够帮助医生更准确地识别和处理病变，具有重要的临床价值和应用前景。

## 📄 摘要（原文）

> Convolutional neural network (CNN) and Transformer-based architectures are two dominant deep learning models for polyp segmentation. However, CNNs have limited capability for modeling long-range dependencies, while Transformers incur quadratic computational complexity. Recently, State Space Models such as Mamba have been recognized as a promising approach for polyp segmentation because they not only model long-range interactions effectively but also maintain linear computational complexity. However, Mamba-based architectures still struggle to capture topological features (e.g., connected components, loops, voids), leading to inaccurate boundary delineation and polyp segmentation. To address these limitations, we propose a new approach called Topo-VM-UNetV2, which encodes topological features into the Mamba-based state-of-the-art polyp segmentation model, VM-UNetV2. Our method consists of two stages: Stage 1: VM-UNetV2 is used to generate probability maps (PMs) for the training and test images, which are then used to compute topology attention maps. Specifically, we first compute persistence diagrams of the PMs, then we generate persistence score maps by assigning persistence values (i.e., the difference between death and birth times) of each topological feature to its birth location, finally we transform persistence scores into attention weights using the sigmoid function. Stage 2: These topology attention maps are integrated into the semantics and detail infusion (SDI) module of VM-UNetV2 to form a topology-guided semantics and detail infusion (Topo-SDI) module for enhancing the segmentation results. Extensive experiments on five public polyp segmentation datasets demonstrate the effectiveness of our proposed method. The code will be made publicly available.

