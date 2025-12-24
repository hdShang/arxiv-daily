---
layout: default
title: "UniConvNet: Expanding Effective Receptive Field while Maintaining Asymptotically Gaussian Distribution for ConvNets of Any Scale"
---

# UniConvNet: Expanding Effective Receptive Field while Maintaining Asymptotically Gaussian Distribution for ConvNets of Any Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09000" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09000v1</a>
  <a href="https://arxiv.org/pdf/2508.09000.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09000v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09000v1', 'UniConvNet: Expanding Effective Receptive Field while Maintaining Asymptotically Gaussian Distribution for ConvNets of Any Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhao Wang, Wei Xi

**分类**: cs.CV

**发布日期**: 2025-08-12

**备注**: ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/ai-paperwithcode/UniConvNet)

---

## 💡 一句话要点

**提出UniConvNet以扩展有效感受野并保持高斯分布**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `卷积神经网络` `有效感受野` `渐近高斯分布` `视觉识别` `深度学习`

## 📋 核心要点

1. 现有的卷积神经网络在扩展有效感受野时，面临高参数和计算成本的挑战，同时渐近高斯分布被破坏。
2. 本文提出通过组合较小卷积核来扩展有效感受野，同时保持其渐近高斯分布，设计了三层感受野聚合器和层操作符。
3. 实验结果显示，UniConvNet在ImageNet-1K、COCO2017和ADE20K等数据集上表现优异，轻量级模型达到84.2%的准确率。

## 📝 摘要（中文）

卷积神经网络（ConvNets）在扩展有效感受野（ERF）方面仍处于早期阶段，尽管其表现出良好的效果，但面临高参数和FLOPs成本的限制，以及ERF的渐近高斯分布（AGD）被破坏的问题。本文提出了一种替代范式，通过适当组合较小的卷积核（如$7	imes{7}$、$9	imes{9}$、$11	imes{11}$），在扩展ERF的同时保持AGD。我们引入了三层感受野聚合器，并设计了层操作符作为感受野的基本操作符。通过这些设计，我们提出了一种适用于任何规模ConvNet的通用模型UniConvNet。大量实验表明，UniConvNet在多个视觉识别任务中超越了现有的CNN和ViT，且在轻量级和大规模模型中具有可比的吞吐量。

## 🔬 方法详解

**问题定义**：本文旨在解决卷积神经网络在扩展有效感受野时的高参数和计算成本问题，以及ERF的渐近高斯分布被破坏的挑战。

**核心思路**：通过适当组合多个较小的卷积核（如$7	imes{7}$、$9	imes{9}$、$11	imes{11}$），在扩展ERF的同时保持其渐近高斯分布，从而提高网络的效率和效果。

**技术框架**：整体架构包括三层感受野聚合器和层操作符，模块通过堆叠的方式实现有效感受野的扩展，形成通用的UniConvNet模型。

**关键创新**：最重要的技术创新在于提出了通过小卷积核组合来扩展ERF的思路，这与传统方法单纯使用大卷积核的方式有本质区别。

**关键设计**：在网络结构中，设计了层操作符作为基本操作，确保在扩展ERF的同时保持AGD，参数设置经过优化以平衡性能与计算成本。

## 📊 实验亮点

UniConvNet在ImageNet-1K上实现了84.2%的顶级准确率，参数量仅为3000万，FLOPs为5.1G，表现优于现有的最先进CNN和ViT模型。此外，UniConvNet-XL在大规模数据集上也展现出竞争力，达到88.4%的顶级准确率。

## 🎯 应用场景

该研究的潜在应用领域包括图像分类、目标检测和语义分割等视觉识别任务。UniConvNet的高效性和灵活性使其适用于各种规模的模型，能够在资源受限的环境中实现高性能，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Convolutional neural networks (ConvNets) with large effective receptive field (ERF), still in their early stages, have demonstrated promising effectiveness while constrained by high parameters and FLOPs costs and disrupted asymptotically Gaussian distribution (AGD) of ERF. This paper proposes an alternative paradigm: rather than merely employing extremely large ERF, it is more effective and efficient to expand the ERF while maintaining AGD of ERF by proper combination of smaller kernels, such as $7\times{7}$, $9\times{9}$, $11\times{11}$. This paper introduces a Three-layer Receptive Field Aggregator and designs a Layer Operator as the fundamental operator from the perspective of receptive field. The ERF can be expanded to the level of existing large-kernel ConvNets through the stack of proposed modules while maintaining AGD of ERF. Using these designs, we propose a universal model for ConvNet of any scale, termed UniConvNet. Extensive experiments on ImageNet-1K, COCO2017, and ADE20K demonstrate that UniConvNet outperforms state-of-the-art CNNs and ViTs across various vision recognition tasks for both lightweight and large-scale models with comparable throughput. Surprisingly, UniConvNet-T achieves $84.2\%$ ImageNet top-1 accuracy with $30M$ parameters and $5.1G$ FLOPs. UniConvNet-XL also shows competitive scalability to big data and large models, acquiring $88.4\%$ top-1 accuracy on ImageNet. Code and models are publicly available at https://github.com/ai-paperwithcode/UniConvNet.

