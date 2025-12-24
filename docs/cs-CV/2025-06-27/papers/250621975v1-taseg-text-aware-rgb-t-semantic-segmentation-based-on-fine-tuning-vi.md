---
layout: default
title: "TASeg: Text-aware RGB-T Semantic Segmentation based on Fine-tuning Vision Foundation Models"
---

# TASeg: Text-aware RGB-T Semantic Segmentation based on Fine-tuning Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21975" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21975v1</a>
  <a href="https://arxiv.org/pdf/2506.21975.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21975v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21975v1', 'TASeg: Text-aware RGB-T Semantic Segmentation based on Fine-tuning Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Meng Yu, Te Cui, Qitong Chu, Wenjie Song, Yi Yang, Yufeng Yue

**分类**: cs.CV

**发布日期**: 2025-06-27

**备注**: 6 pages, accepted for publication in lEEE/RSJ international Conference on Intelligent Robots and Systems (lROS 2025)

---

## 💡 一句话要点

**提出TASeg框架以解决RGB-T语义分割中的文本信息缺失问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `RGB-T语义分割` `文本信息融合` `低秩适应` `动态特征融合` `CLIP嵌入` `智能系统` `计算机视觉`

## 📋 核心要点

1. 现有RGB-T语义分割模型主要依赖低级视觉特征，缺乏高级文本信息，导致在相似视觉特征类别间的分割准确性不足。
2. 本文提出TASeg框架，通过低秩适应技术微调视觉基础模型，并引入动态特征融合模块以有效整合多模态特征。
3. 实验结果显示，TASeg在多个数据集上表现优越，尤其在复杂场景中，参数量显著减少，性能提升明显。

## 📝 摘要（中文）

在智能系统中，可靠的开放环境语义分割至关重要，但仍面临显著问题：现有RGB-T语义分割模型主要依赖低级视觉特征，缺乏高级文本信息，导致在类别共享相似视觉特征时难以实现准确分割。此外，尽管SAM在实例级分割中表现出色，但与热成像和文本的结合受到模态异质性和计算效率低下的限制。为此，本文提出了TASeg框架，通过低秩适应（LoRA）微调技术来适应视觉基础模型。具体而言，我们在图像编码器中提出了动态特征融合模块（DFFM），有效融合多种视觉模态的特征，同时冻结SAM的原始变换器块。此外，我们在掩膜解码器中引入了CLIP生成的文本嵌入，以实现语义对齐，从而进一步纠正分类错误，提高语义理解的准确性。实验结果表明，我们的方法在具有挑战性的场景中表现优越，并且训练参数更少。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RGB-T语义分割模型在处理相似视觉特征类别时的准确性不足，尤其是缺乏文本信息的情况下。现有方法在模态异质性和计算效率方面也存在挑战。

**核心思路**：TASeg框架通过低秩适应（LoRA）技术微调视觉基础模型，结合动态特征融合模块（DFFM）和CLIP生成的文本嵌入，增强模型的语义理解能力。

**技术框架**：TASeg的整体架构包括图像编码器、动态特征融合模块和掩膜解码器。图像编码器负责提取多模态特征，DFFM用于融合这些特征，而掩膜解码器则利用文本嵌入进行语义对齐。

**关键创新**：最重要的创新在于引入动态特征融合模块（DFFM），该模块有效整合了来自不同模态的特征，同时保持了SAM的变换器结构不变，从而提高了模型的效率和准确性。

**关键设计**：在模型设计中，采用了低秩适应技术以减少训练参数，损失函数设计上注重语义对齐，网络结构中保持了SAM的原始变换器块不变，以优化计算效率。

## 📊 实验亮点

实验结果表明，TASeg在多个数据集上表现优越，相较于基线模型，性能提升幅度达到XX%，在复杂场景下的分割准确率显著提高，同时训练参数减少了XX%。

## 🎯 应用场景

TASeg框架在智能交通、无人驾驶、安防监控等领域具有广泛的应用潜力。通过提高语义分割的准确性，能够更好地支持环境理解和决策制定，推动智能系统的进一步发展与应用。

## 📄 摘要（原文）

> Reliable semantic segmentation of open environments is essential for intelligent systems, yet significant problems remain: 1) Existing RGB-T semantic segmentation models mainly rely on low-level visual features and lack high-level textual information, which struggle with accurate segmentation when categories share similar visual characteristics. 2) While SAM excels in instance-level segmentation, integrating it with thermal images and text is hindered by modality heterogeneity and computational inefficiency. To address these, we propose TASeg, a text-aware RGB-T segmentation framework by using Low-Rank Adaptation (LoRA) fine-tuning technology to adapt vision foundation models. Specifically, we propose a Dynamic Feature Fusion Module (DFFM) in the image encoder, which effectively merges features from multiple visual modalities while freezing SAM's original transformer blocks. Additionally, we incorporate CLIP-generated text embeddings in the mask decoder to enable semantic alignment, which further rectifies the classification error and improves the semantic understanding accuracy. Experimental results across diverse datasets demonstrate that our method achieves superior performance in challenging scenarios with fewer trainable parameters.

