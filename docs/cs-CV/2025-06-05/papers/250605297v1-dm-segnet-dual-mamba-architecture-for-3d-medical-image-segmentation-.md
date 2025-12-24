---
layout: default
title: "DM-SegNet: Dual-Mamba Architecture for 3D Medical Image Segmentation with Global Context Modeling"
---

# DM-SegNet: Dual-Mamba Architecture for 3D Medical Image Segmentation with Global Context Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05297" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05297v1</a>
  <a href="https://arxiv.org/pdf/2506.05297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05297v1', 'DM-SegNet: Dual-Mamba Architecture for 3D Medical Image Segmentation with Global Context Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hangyu Ji

**分类**: eess.IV, cs.CV

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出DM-SegNet以解决3D医学图像分割中的全局上下文建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `3D医学图像分割` `全局上下文建模` `状态空间模型` `解剖学感知` `深度学习` `卷积神经网络` `医学影像分析` `双Mamba架构`

## 📋 核心要点

1. 现有医学图像分割方法在全局上下文建模与空间拓扑保持之间存在矛盾，导致分割精度不足。
2. DM-SegNet通过双Mamba架构，结合方向状态转移与解剖学感知的分层解码，解决了这一矛盾。
3. 在Synapse和BraTS2023数据集上，DM-SegNet分别达到了85.44%和90.22%的Dice相似系数，显示出显著的性能提升。

## 📝 摘要（中文）

准确的3D医学图像分割需要能够协调全局上下文建模与空间拓扑保持的架构。尽管状态空间模型（SSMs）如Mamba在序列建模中显示出潜力，但现有医学SSMs存在编码器-解码器不兼容的问题：编码器的1D序列展平损害了空间结构，而传统解码器未能利用Mamba的状态传播。我们提出DM-SegNet，一种双Mamba架构，集成了方向状态转移与解剖学感知的分层解码。核心创新包括采用四向3D扫描的四向空间Mamba模块，以保持解剖空间一致性，增强空间敏感特征表示的门控空间卷积层，以及实现跨尺度双向状态同步的Mamba驱动解码框架。对两个临床重要基准的广泛评估表明DM-SegNet的有效性：在Synapse数据集上实现85.44%的最先进Dice相似系数（DSC）用于腹部器官分割，在BraTS2023数据集上实现90.22%的DSC用于脑肿瘤分割。

## 🔬 方法详解

**问题定义**：本论文旨在解决3D医学图像分割中全局上下文建模与空间拓扑保持的矛盾。现有方法在编码器中使用1D序列展平，损害了空间结构，而传统解码器未能有效利用状态空间模型的状态传播特性。

**核心思路**：DM-SegNet的核心思路是通过双Mamba架构，结合方向状态转移与解剖学感知的分层解码，来实现更好的空间结构保持与全局上下文建模。这样的设计使得模型能够在保持解剖结构的同时，充分利用全局信息。

**技术框架**：DM-SegNet的整体架构包括四个主要模块：四向空间Mamba模块、门控空间卷积层、Mamba驱动解码框架和双向状态同步机制。四向空间Mamba模块通过四个方向的3D扫描来保持解剖空间一致性，门控空间卷积层则增强了特征表示。

**关键创新**：DM-SegNet的关键创新在于其四向空间Mamba模块与门控空间卷积层的结合，前者保持了空间一致性，后者提升了特征表达能力。这与现有方法的单向处理和特征提取方式有本质区别。

**关键设计**：在设计中，采用了门控机制来增强空间特征的表示能力，损失函数则结合了分割精度与结构保持的要求，确保模型在训练过程中能够平衡这两者。

## 📊 实验亮点

DM-SegNet在Synapse数据集上实现了85.44%的Dice相似系数，在BraTS2023数据集上达到了90.22%的DSC，均为当前最先进水平，显示出相较于传统方法的显著性能提升，尤其在复杂解剖结构的分割任务中表现优异。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、临床诊断支持系统和手术规划等。DM-SegNet的高精度分割能力可以为医生提供更准确的解剖结构信息，从而提高诊断效率和治疗效果，未来可能在个性化医疗中发挥重要作用。

## 📄 摘要（原文）

> Accurate 3D medical image segmentation demands architectures capable of reconciling global context modeling with spatial topology preservation. While State Space Models (SSMs) like Mamba show potential for sequence modeling, existing medical SSMs suffer from encoder-decoder incompatibility: the encoder's 1D sequence flattening compromises spatial structures, while conventional decoders fail to leverage Mamba's state propagation. We present DM-SegNet, a Dual-Mamba architecture integrating directional state transitions with anatomy-aware hierarchical decoding. The core innovations include a quadri-directional spatial Mamba module employing four-directional 3D scanning to maintain anatomical spatial coherence, a gated spatial convolution layer that enhances spatially sensitive feature representation prior to state modeling, and a Mamba-driven decoding framework enabling bidirectional state synchronization across scales. Extensive evaluation on two clinically significant benchmarks demonstrates the efficacy of DM-SegNet: achieving state-of-the-art Dice Similarity Coefficient (DSC) of 85.44% on the Synapse dataset for abdominal organ segmentation and 90.22% on the BraTS2023 dataset for brain tumor segmentation.

