---
layout: default
title: "Graph-MLLM: Harnessing Multimodal Large Language Models for Multimodal Graph Learning"
---

# Graph-MLLM: Harnessing Multimodal Large Language Models for Multimodal Graph Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10282" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10282v1</a>
  <a href="https://arxiv.org/pdf/2506.10282.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10282v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10282v1', 'Graph-MLLM: Harnessing Multimodal Large Language Models for Multimodal Graph Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiajin Liu, Dongzhe Fan, Jiacheng Shen, Chuanhao Ji, Daochen Zha, Qiaoyu Tan

**分类**: cs.LG

**发布日期**: 2025-06-12

**备注**: 16 pages, 4 figures

---

## 💡 一句话要点

**提出Graph-MLLM以解决多模态图学习的评估与整合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态图学习` `大语言模型` `图神经网络` `特征融合` `评估基准` `社交网络` `医疗应用`

## 📋 核心要点

1. 现有多模态图学习方法缺乏统一的基准，难以公平评估不同方法的进展与效果。
2. 本文提出Graph-MLLM，通过系统评估三种多模态图学习范式，填补了这一空白。
3. 实验结果显示，联合视觉与文本属性的使用显著提升了图学习性能，尤其是在特定MMGs上进行微调时。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在表示和理解多样化模态方面表现出色，但通常仅关注模态间的配对对齐，忽视了数据点间的结构关系。将多模态与结构化图信息结合对于社交网络、医疗保健和推荐系统等实际应用至关重要。现有的多模态图学习方法主要分为三种范式：编码器、对齐器和预测器。本文提出Graph-MLLM，一个全面的多模态图学习基准，通过系统评估这三种范式在六个不同领域的数据集上的表现。实验表明，联合考虑节点的视觉和文本属性有助于图学习，且将视觉属性转换为文本描述能进一步提升性能。我们希望开源的库能促进快速、公平的评估，并激发该领域的进一步创新研究。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态图学习中缺乏统一评估基准的问题，现有方法在如何利用多模态信息和图结构方面存在不足。

**核心思路**：提出Graph-MLLM基准，通过系统评估三种不同的多模态图学习范式，探索多模态特征融合对图学习的影响。

**技术框架**：整体架构包括三个主要模块：编码器（MLLM作为特征融合工具）、对齐器（在语言或隐空间中对齐多模态属性）和预测器（作为独立推理器）。

**关键创新**：最重要的创新在于提出了一个综合性的基准，能够公平地评估不同的多模态图学习方法，并发现了视觉属性转文本描述的有效性。

**关键设计**：在实验中，使用了预训练的文本-图像对齐模型（如CLIP）作为编码器，并通过微调MLLMs来优化特定MMGs的性能。实验中还探索了不同损失函数和网络结构的设置。

## 📊 实验亮点

实验结果表明，联合使用视觉和文本属性的节点在图学习中表现优越，尤其是通过将视觉属性转化为文本描述，性能提升显著。在大多数场景下，微调MLLMs可实现最先进的结果，尽管没有显式的图结构信息。

## 🎯 应用场景

该研究的潜在应用领域包括社交网络分析、医疗数据处理和个性化推荐系统等。通过有效整合多模态信息与图结构，能够提升这些领域的智能化水平和决策能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in representing and understanding diverse modalities. However, they typically focus on modality alignment in a pairwise manner while overlooking structural relationships across data points. Integrating multimodality with structured graph information (i.e., multimodal graphs, MMGs) is essential for real-world applications such as social networks, healthcare, and recommendation systems. Existing MMG learning methods fall into three paradigms based on how they leverage MLLMs: Encoder, Aligner, and Predictor. MLLM-as-Encoder focuses on enhancing graph neural networks (GNNs) via multimodal feature fusion; MLLM-as-Aligner aligns multimodal attributes in language or hidden space to enable LLM-based graph reasoning; MLLM-as-Predictor treats MLLMs as standalone reasoners with in-context learning or fine-tuning. Despite their advances, the MMG field lacks a unified benchmark to fairly evaluate across these approaches, making it unclear what progress has been made. To bridge this gap, we present Graph-MLLM, a comprehensive benchmark for multimodal graph learning by systematically evaluating these three paradigms across six datasets with different domains. Through extensive experiments, we observe that jointly considering the visual and textual attributes of the nodes benefits graph learning, even when using pre-trained text-to-image alignment models (e.g., CLIP) as encoders. We also find that converting visual attributes into textual descriptions further improves performance compared to directly using visual inputs. Moreover, we observe that fine-tuning MLLMs on specific MMGs can achieve state-of-the-art results in most scenarios, even without explicit graph structure information. We hope that our open-sourced library will facilitate rapid, equitable evaluation and inspire further innovative research in this field.

