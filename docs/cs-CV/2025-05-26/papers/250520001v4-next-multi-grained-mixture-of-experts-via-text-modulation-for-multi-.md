---
layout: default
title: "NEXT: Multi-Grained Mixture of Experts via Text-Modulation for Multi-Modal Object Re-Identification"
---

# NEXT: Multi-Grained Mixture of Experts via Text-Modulation for Multi-Modal Object Re-Identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20001" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20001v4</a>
  <a href="https://arxiv.org/pdf/2505.20001.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20001v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20001v4', 'NEXT: Multi-Grained Mixture of Experts via Text-Modulation for Multi-Modal Object Re-Identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shihao Li, Aihua Zheng, Andong Lu, Jin Tang, Jixin Ma

**分类**: cs.CV

**发布日期**: 2025-05-26 (更新: 2025-08-10)

---

## 💡 一句话要点

**提出NEXT框架以解决多模态物体重识别中的细粒度特征建模问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态重识别` `文本调制` `专家混合模型` `细粒度特征` `结构一致性` `特征聚合` `深度学习`

## 📋 核心要点

1. 现有的多模态物体重识别方法多依赖隐式特征融合，难以有效建模细粒度的识别模式。
2. 本文提出的NEXT框架通过文本调制的多粒度专家混合模型，解耦语义与结构特征的捕捉，提升识别精度。
3. 在四个公共数据集上的实验结果显示，NEXT框架显著超越了现有的最先进方法，提升了识别性能。

## 📝 摘要（中文）

多模态物体重识别（ReID）旨在跨异构模态获取准确的身份特征。然而，现有方法依赖隐式特征融合模块，难以在现实世界的各种挑战下建模细粒度识别模式。本文提出了一种基于属性置信度的可靠字幕生成管道，显著降低了多模态大语言模型（MLLMs）的未知识别率，并提高了生成文本的质量。此外，我们提出了一种新颖的ReID框架NEXT，即通过文本调制的多粒度专家混合模型，旨在建模多样的身份模式。通过解耦识别问题为语义和结构两个分支，我们分别捕捉细粒度外观特征和粗粒度结构特征。实验结果表明，该方法在四个公共数据集上显著优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态物体重识别中的细粒度特征建模问题。现有方法往往依赖隐式特征融合，导致在复杂场景下的识别性能不足。

**核心思路**：我们提出NEXT框架，通过文本调制的多粒度专家混合模型，分别捕捉语义和结构特征，以应对多样化的身份模式。这样的设计使得模型能够更好地利用多模态信息，提升识别精度。

**技术框架**：NEXT框架包括三个主要模块：文本调制语义专家（TMSE）、上下文共享结构专家（CSSE）和多粒度特征聚合（MGFA）。TMSE通过高质量字幕调制专家以捕捉语义特征，CSSE则关注整体物体结构并通过软路由机制保持身份结构一致性，MGFA则负责将多粒度专家的特征有效融合。

**关键创新**：最重要的创新在于引入了文本调制机制和多粒度专家混合模型，这与现有方法的隐式特征融合形成了本质区别，能够更精确地捕捉细粒度特征。

**关键设计**：在模型设计中，我们设置了高质量字幕的随机采样机制，采用了软路由机制来维护结构一致性，并在特征聚合阶段采用统一的融合策略，以确保多粒度特征的有效整合。

## 📊 实验亮点

在四个公共数据集上的实验结果表明，NEXT框架在识别准确率上显著优于现有最先进的方法，具体提升幅度达到XX%（具体数据待补充），验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、安防系统等，能够在复杂环境中实现高效的物体重识别。通过提升多模态识别的准确性，未来可为人机交互、智能城市等领域带来更大的价值和影响。

## 📄 摘要（原文）

> Multi-modal object Re-Identification (ReID) aims to obtain accurate identity features across heterogeneous modalities. However, most existing methods rely on implicit feature fusion modules, making it difficult to model fine-grained recognition patterns under various challenges in real world. Benefiting from the powerful Multi-modal Large Language Models (MLLMs), the object appearances are effectively translated into descriptive captions. In this paper, we propose a reliable caption generation pipeline based on attribute confidence, which significantly reduces the unknown recognition rate of MLLMs and improves the quality of generated text. Additionally, to model diverse identity patterns, we propose a novel ReID framework, named NEXT, the Multi-grained Mixture of Experts via Text-Modulation for Multi-modal Object Re-Identification. Specifically, we decouple the recognition problem into semantic and structural branches to separately capture fine-grained appearance features and coarse-grained structure features. For semantic recognition, we first propose a Text-Modulated Semantic Experts (TMSE), which randomly samples high-quality captions to modulate experts capturing semantic features and mining inter-modality complementary cues. Second, to recognize structure features, we propose a Context-Shared Structure Experts (CSSE), which focuses on the holistic object structure and maintains identity structural consistency via a soft routing mechanism. Finally, we propose a Multi-Grained Features Aggregation (MGFA), which adopts a unified fusion strategy to effectively integrate multi-grained experts into the final identity representations. Extensive experiments on four public datasets demonstrate the effectiveness of our method and show that it significantly outperforms existing state-of-the-art methods.

