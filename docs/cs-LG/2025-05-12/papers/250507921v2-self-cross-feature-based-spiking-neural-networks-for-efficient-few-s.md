---
layout: default
title: Self-cross Feature based Spiking Neural Networks for Efficient Few-shot Learning
---

# Self-cross Feature based Spiking Neural Networks for Efficient Few-shot Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07921" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07921v2</a>
  <a href="https://arxiv.org/pdf/2505.07921.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07921v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07921v2', 'Self-cross Feature based Spiking Neural Networks for Efficient Few-shot Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Xu, Junyang Zhu, Dongdong Zhou, Hao Chen, Yang Liu, Jiangrong Shen, Qiang Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-12 (更新: 2025-05-15)

---

## 💡 一句话要点

**提出基于自交叉特征的脉冲神经网络以解决高效少样本学习问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `脉冲神经网络` `少样本学习` `特征提取` `对比学习` `低功耗计算` `时空特征` `计算机视觉`

## 📋 核心要点

1. 现有的深度神经网络在少样本学习中表现出色，但计算成本高且可扩展性差，限制了其在实际应用中的广泛使用。
2. 本文提出了一种基于脉冲神经网络的少样本学习框架，通过自特征提取和交叉特征对比模块来优化特征表示和降低功耗。
3. 实验结果显示，所提方法在N-Omniglot数据集上显著提升分类性能，并在CUB和miniImageNet等静态数据集上与传统人工神经网络表现相当。

## 📝 摘要（中文）

深度神经网络（DNNs）在计算机视觉任务中表现优异，尤其是在少样本学习（FSL）中。然而，DNNs在实际应用中面临计算成本高和可扩展性问题。脉冲神经网络（SNNs）因其事件驱动特性和低能耗在处理稀疏和动态数据时表现出色，但在捕捉复杂时空特征和进行跨类比较时仍存在困难。为提高SNNs在少样本学习中的性能和效率，本文提出了一种基于SNNs的少样本学习框架，结合自特征提取模块和交叉特征对比模块，以优化特征表示并降低功耗。通过结合时间高效训练损失和InfoNCE损失，优化脉冲列的时间动态性，增强区分能力。实验结果表明，所提FSL-SNN在神经形态数据集N-Omniglot上显著提高了分类性能，并在CUB和miniImageNet等静态数据集上实现了与人工神经网络（ANNs）竞争的性能，同时功耗较低。

## 🔬 方法详解

**问题定义**：本文旨在解决脉冲神经网络在少样本学习中面临的复杂时空特征捕捉和跨类比较困难的问题。现有方法多依赖于深度神经网络，存在计算成本高和可扩展性差的痛点。

**核心思路**：提出一种结合自特征提取模块和交叉特征对比模块的少样本学习框架，以优化特征表示并降低功耗。通过引入时间高效训练损失和InfoNCE损失，增强脉冲列的动态性和区分能力。

**技术框架**：整体架构包括自特征提取模块、交叉特征对比模块和损失优化模块。自特征提取模块负责从输入数据中提取有效特征，交叉特征对比模块则用于增强不同类之间的特征对比。

**关键创新**：最重要的创新在于结合自特征提取与交叉特征对比的双模块设计，显著提升了脉冲神经网络在少样本学习中的表现，与传统深度学习方法相比，能在更低的能耗下实现相似的性能。

**关键设计**：在损失函数设计上，采用时间高效训练损失与InfoNCE损失的结合，以优化脉冲列的时间动态性。此外，网络结构经过精心设计，以确保在低功耗下仍能保持较高的分类精度。

## 📊 实验亮点

实验结果表明，所提FSL-SNN在N-Omniglot数据集上的分类性能显著提升，且在CUB和miniImageNet等静态数据集上与传统人工神经网络的表现相当，且功耗显著降低，展示了其在少样本学习中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、智能监控和医疗图像分析等场景，尤其是在数据稀缺的情况下，能够有效提升模型的学习能力和效率。未来，该方法有望在实际应用中实现更广泛的推广，推动少样本学习技术的发展。

## 📄 摘要（原文）

> Deep neural networks (DNNs) excel in computer vision tasks, especially, few-shot learning (FSL), which is increasingly important for generalizing from limited examples. However, DNNs are computationally expensive with scalability issues in real world. Spiking Neural Networks (SNNs), with their event-driven nature and low energy consumption, are particularly efficient in processing sparse and dynamic data, though they still encounter difficulties in capturing complex spatiotemporal features and performing accurate cross-class comparisons. To further enhance the performance and efficiency of SNNs in few-shot learning, we propose a few-shot learning framework based on SNNs, which combines a self-feature extractor module and a cross-feature contrastive module to refine feature representation and reduce power consumption. We apply the combination of temporal efficient training loss and InfoNCE loss to optimize the temporal dynamics of spike trains and enhance the discriminative power. Experimental results show that the proposed FSL-SNN significantly improves the classification performance on the neuromorphic dataset N-Omniglot, and also achieves competitive performance to ANNs on static datasets such as CUB and miniImageNet with low power consumption.

