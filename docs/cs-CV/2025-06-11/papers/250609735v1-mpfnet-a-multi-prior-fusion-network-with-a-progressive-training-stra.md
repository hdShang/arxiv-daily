---
layout: default
title: "MPFNet: A Multi-Prior Fusion Network with a Progressive Training Strategy for Micro-Expression Recognition"
---

# MPFNet: A Multi-Prior Fusion Network with a Progressive Training Strategy for Micro-Expression Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09735" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09735v1</a>
  <a href="https://arxiv.org/pdf/2506.09735.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09735v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09735v1', 'MPFNet: A Multi-Prior Fusion Network with a Progressive Training Strategy for Micro-Expression Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuang Ma, Shaokai Zhao, Dongdong Zhou, Yu Pei, Zhiguo Luo, Liang Xie, Ye Yan, Erwei Yin

**分类**: cs.CV

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出MPFNet以解决微表情识别中的多源信息融合问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `微表情识别` `多先验融合` `渐进式训练` `情感计算` `深度学习`

## 📋 核心要点

1. 现有微表情识别方法多依赖单一先验知识，未能充分利用多源信息，导致性能受限。
2. 本文提出MPFNet，通过渐进式训练策略和双编码器设计，优化微表情识别任务。
3. 实验结果表明，MPFNet在多个数据集上显著提升了识别准确率，达到当前最优性能。

## 📝 摘要（中文）

微表情识别（MER）是情感计算的一个重要子领域，因其持续时间短、强度低而面临更大挑战。现有方法多依赖于简单的单一先验知识，未能充分利用多源信息。本文提出了多先验融合网络（MPFNet），结合渐进式训练策略优化MER任务。我们设计了两个互补编码器：通用特征编码器（GFE）和高级特征编码器（AFE），均基于膨胀3D卷积网络（I3D）和坐标注意力机制（CA），以增强模型捕捉时空和通道特征的能力。通过大量实验，MPFNet在SMIC、CASME II和SAMM数据集上分别达到了0.811、0.924和0.857的准确率，显著提升了MER的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决微表情识别中的多源信息融合问题。现有方法多依赖于简单的单一先验知识，未能充分利用多源信息，导致识别性能受限。

**核心思路**：论文提出的MPFNet通过渐进式训练策略和双编码器设计，旨在优化微表情识别任务，充分挖掘多源信息的潜力。

**技术框架**：MPFNet整体架构包括两个主要模块：通用特征编码器（GFE）和高级特征编码器（AFE），均基于膨胀3D卷积网络（I3D）和坐标注意力机制（CA），以增强模型对时空和通道特征的捕捉能力。

**关键创新**：MPFNet的核心创新在于其双编码器结构和渐进式训练策略，能够有效整合多源先验知识，与现有方法相比，显著提升了微表情识别的准确性和鲁棒性。

**关键设计**：在网络结构上，采用了I3D卷积层和CA机制，优化了特征提取过程。损失函数设计上，考虑了多类别平衡，确保模型在不同类别上的表现均衡。

## 📊 实验亮点

MPFNet在SMIC、CASME II和SAMM数据集上分别达到了0.811、0.924和0.857的准确率，显著优于现有方法，尤其在SMIC和SAMM数据集上实现了最先进的性能，展示了其在微表情识别领域的强大能力。

## 🎯 应用场景

该研究在情感计算、心理健康监测和人机交互等领域具有广泛的应用潜力。通过提高微表情识别的准确性，MPFNet可以帮助开发更智能的情感识别系统，促进人机交互的自然性和有效性，未来可能在心理健康评估和情感分析中发挥重要作用。

## 📄 摘要（原文）

> Micro-expression recognition (MER), a critical subfield of affective computing, presents greater challenges than macro-expression recognition due to its brief duration and low intensity. While incorporating prior knowledge has been shown to enhance MER performance, existing methods predominantly rely on simplistic, singular sources of prior knowledge, failing to fully exploit multi-source information. This paper introduces the Multi-Prior Fusion Network (MPFNet), leveraging a progressive training strategy to optimize MER tasks. We propose two complementary encoders: the Generic Feature Encoder (GFE) and the Advanced Feature Encoder (AFE), both based on Inflated 3D ConvNets (I3D) with Coordinate Attention (CA) mechanisms, to improve the model's ability to capture spatiotemporal and channel-specific features. Inspired by developmental psychology, we present two variants of MPFNet--MPFNet-P and MPFNet-C--corresponding to two fundamental modes of infant cognitive development: parallel and hierarchical processing. These variants enable the evaluation of different strategies for integrating prior knowledge. Extensive experiments demonstrate that MPFNet significantly improves MER accuracy while maintaining balanced performance across categories, achieving accuracies of 0.811, 0.924, and 0.857 on the SMIC, CASME II, and SAMM datasets, respectively. To the best of our knowledge, our approach achieves state-of-the-art performance on the SMIC and SAMM datasets.

