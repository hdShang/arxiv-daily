---
layout: default
title: CountFormer: A Transformer Framework for Learning Visual Repetition and Structure in Class-Agnostic Object Counting
---

# CountFormer: A Transformer Framework for Learning Visual Repetition and Structure in Class-Agnostic Object Counting

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23785" target="_blank" class="toolbar-btn">arXiv: 2510.23785v1</a>
    <a href="https://arxiv.org/pdf/2510.23785.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23785v1" 
            onclick="toggleFavorite(this, '2510.23785v1', 'CountFormer: A Transformer Framework for Learning Visual Repetition and Structure in Class-Agnostic Object Counting')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Md Tanvir Hossain, Akif Islam, Mohd Ruhul Ameen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-27

**备注**: 6 pages, 2 tables, 6 figures. Submitted to IEEE 5th International Conference on Electrical, Computer and Telecommunication Engineering (ICECTE 2025)

---

## 💡 一句话要点

**CountFormer：Transformer框架学习视觉重复与结构，实现类别无关的目标计数**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `目标计数` `Transformer` `DINOv2` `视觉重复` `结构一致性` `类别无关` `密度图` `自监督学习`

## 📋 核心要点

1. 现有计数模型在处理具有复杂形状、内部对称或重叠的对象时，计数准确率较低，无法有效模仿人类的计数能力。
2. CountFormer利用Transformer架构，通过学习视觉重复和结构一致性来进行类别无关的目标计数，更接近人类的计数方式。
3. 实验表明，CountFormer在FSC-147数据集上取得了与SOTA方法相当的性能，并在结构复杂或密集场景中表现出更优的准确性。

## 📝 摘要（中文）

本文提出CountFormer，一个基于Transformer的框架，用于学习视觉重复和结构一致性，从而实现类别无关的目标计数。与依赖类别信息不同，人类通过感知视觉重复和结构关系来计数。现有模型难以复制这种能力，在处理复杂形状、内部对称或重叠对象时容易出错。CountFormer基于CounTR架构，用自监督预训练模型DINOv2替换视觉编码器，以产生更丰富和空间一致的特征表示。此外，模型还融合了位置嵌入，以保留几何关系，然后通过轻量级卷积解码器将这些特征解码为密度图。在FSC-147数据集上的评估表明，该模型达到了与当前最先进方法相当的性能，并在结构复杂或密集场景中表现出更高的准确性。研究结果表明，集成DINOv2等预训练模型使计数系统能够接近人类般的结构感知，从而朝着真正通用和无样本的计数范式迈进。

## 🔬 方法详解

**问题定义**：论文旨在解决类别无关的目标计数问题，即在不依赖对象类别信息的情况下，准确估计图像中特定目标的数量。现有方法在处理具有复杂形状、内部对称性或密集堆叠的对象时，往往表现不佳，因为它们难以捕捉到目标之间的结构关系和重复模式。

**核心思路**：论文的核心思路是利用Transformer架构学习图像中目标的视觉重复模式和结构一致性，从而实现更准确的计数。通过引入自监督预训练模型DINOv2作为视觉编码器，可以提取更丰富和空间一致的特征表示，从而更好地捕捉目标的结构信息。

**技术框架**：CountFormer的整体架构基于CounTR，主要包含以下几个模块：1) DINOv2视觉编码器：用于提取图像的视觉特征；2) 位置嵌入融合：用于保留特征的空间几何关系；3) 轻量级卷积解码器：将特征解码为密度图，密度图上的积分即为目标数量的估计值。

**关键创新**：CountFormer的关键创新在于使用DINOv2作为视觉编码器，并结合位置嵌入融合，从而能够更好地学习目标的结构信息和重复模式。与传统的卷积神经网络相比，Transformer架构具有更强的全局建模能力，能够更好地捕捉目标之间的长程依赖关系。

**关键设计**：DINOv2的选择是因为其自监督学习的特性，使其能够学习到更通用的视觉特征表示。位置嵌入融合采用了一种简单而有效的方式，将位置信息融入到特征中，从而保留了目标的空间几何关系。轻量级卷积解码器的设计旨在减少计算量，同时保证解码的准确性。损失函数采用标准的密度图回归损失。

## 📊 实验亮点

CountFormer在FSC-147数据集上取得了与当前最先进方法相当的性能，并在结构复杂或密集场景中表现出更高的准确性。具体来说，CountFormer在处理具有复杂形状、内部对称性或密集堆叠的对象时，计数准确率显著提升，表明其能够更好地学习目标的结构信息和重复模式。该模型证明了预训练模型在目标计数任务中的有效性，并为未来的研究提供了新的思路。

## 🎯 应用场景

CountFormer在智能监控、自动驾驶、零售分析、医学图像分析等领域具有广泛的应用前景。例如，在智能监控中，可以用于统计人群密度或车辆数量；在自动驾驶中，可以用于检测和计数道路上的行人或车辆；在零售分析中，可以用于统计货架上的商品数量；在医学图像分析中，可以用于计数细胞数量。该研究有助于推动通用计数技术的发展，实现更智能、更高效的视觉分析。

## 📄 摘要（原文）

> Humans can effortlessly count diverse objects by perceiving visual repetition and structural relationships rather than relying on class identity. However, most existing counting models fail to replicate this ability; they often miscount when objects exhibit complex shapes, internal symmetry, or overlapping components. In this work, we introduce CountFormer, a transformer-based framework that learns to recognize repetition and structural coherence for class-agnostic object counting. Built upon the CounTR architecture, our model replaces its visual encoder with the self-supervised foundation model DINOv2, which produces richer and spatially consistent feature representations. We further incorporate positional embedding fusion to preserve geometric relationships before decoding these features into density maps through a lightweight convolutional decoder. Evaluated on the FSC-147 dataset, our model achieves performance comparable to current state-of-the-art methods while demonstrating superior accuracy on structurally intricate or densely packed scenes. Our findings indicate that integrating foundation models such as DINOv2 enables counting systems to approach human-like structural perception, advancing toward a truly general and exemplar-free counting paradigm.

