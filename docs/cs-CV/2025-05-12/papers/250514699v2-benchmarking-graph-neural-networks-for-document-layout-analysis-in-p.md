---
layout: default
title: Benchmarking Graph Neural Networks for Document Layout Analysis in Public Affairs
---

# Benchmarking Graph Neural Networks for Document Layout Analysis in Public Affairs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14699" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14699v2</a>
  <a href="https://arxiv.org/pdf/2505.14699.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14699v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14699v2', 'Benchmarking Graph Neural Networks for Document Layout Analysis in Public Affairs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Miguel Lopez-Duran, Julian Fierrez, Aythami Morales, Ruben Tolosana, Oscar Delgado-Mohatar, Alvaro Ortigosa

**分类**: cs.CV, cs.CL, cs.LG

**发布日期**: 2025-05-12 (更新: 2025-07-28)

**备注**: 15 pages, 2 figures, accepted paper at The Fifth ICDAR International Workshop on Machine Learning

---

## 💡 一句话要点

**基于图神经网络的文档布局分析方法提升公共事务文档处理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图神经网络` `文档布局分析` `多模态融合` `自动化处理` `公共事务`

## 📋 核心要点

1. 现有方法在处理数字原生PDF文档时，面临布局元素异构性和文本元数据不精确的问题，导致自动分析效果不佳。
2. 本文提出基于图神经网络的布局分类方法，利用k-最近邻图和全连接图构建结构，结合预训练模型生成节点特征，减少手动特征工程的需求。
3. 实验结果显示，GraphSAGE在双分支配置下的k-最近邻图实现了最高的分类准确率，部分来源超越了基线，强调了局部布局关系和多模态融合的重要性。

## 📝 摘要（中文）

数字原生PDF文档的自动布局分析因文本与非文本元素的异构排列以及文本元数据的不精确性而面临挑战。本文基于图神经网络（GNN）架构，对文本块进行细粒度布局分类。我们引入了k-最近邻图和全连接图两种图构建结构，通过预训练的文本和视觉模型生成节点特征，避免了手动特征工程。实验在包含超过20个来源、37K PDF文档和441K页面的公共事务文档数据集上进行，结果表明，GraphSAGE在k-最近邻图的双分支配置下，达到了最高的分类准确率，验证了局部布局关系和多模态融合在数字文档布局分析中的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决数字原生PDF文档的自动布局分析问题，现有方法在处理异构布局和不精确元数据时效果不理想。

**核心思路**：通过引入图神经网络（GNN）架构，利用k-最近邻图和全连接图的构建方式，结合预训练模型生成节点特征，以减少手动特征工程的复杂性。

**技术框架**：整体架构包括图构建、节点特征生成和多模态融合三个主要模块，分别处理文本和视觉信息，最终实现细粒度布局分类。

**关键创新**：引入了k-最近邻图和全连接图的构建方式，并通过双分支配置的GNN模型实现了更高的分类准确率，显著提升了布局分析的效果。

**关键设计**：在实验中，采用了GraphSAGE作为基础模型，设置了不同的图结构和特征生成方式，使用了多模态融合策略以优化模型性能。

## 📊 实验亮点

实验结果表明，GraphSAGE在k-最近邻图的双分支配置下，达到了最高的分类准确率，部分来源的性能超越了基线，显示出局部布局关系和多模态融合的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括公共事务文档的自动化处理、信息提取和数字化归档等。通过提升文档布局分析的准确性，可以有效支持政府和公共机构的信息管理与服务，未来可能推动智能文档处理技术的发展。

## 📄 摘要（原文）

> The automatic analysis of document layouts in digital-born PDF documents remains a challenging problem due to the heterogeneous arrangement of textual and nontextual elements and the imprecision of the textual metadata in the Portable Document Format. In this work, we benchmark Graph Neural Network (GNN) architectures for the task of fine-grained layout classification of text blocks from digital native documents. We introduce two graph construction structures: a k-closest-neighbor graph and a fully connected graph, and generate node features via pre-trained text and vision models, thus avoiding manual feature engineering. Three experimental frameworks are evaluated: single-modality (text or visual), concatenated multimodal, and dual-branch multimodal. We evaluated four foundational GNN models and compared them with the baseline. Our experiments are specifically conducted on a rich dataset of public affairs documents that includes more than 20 sources (e.g., regional and national-level official gazettes), 37K PDF documents, with 441K pages in total. Our results demonstrate that GraphSAGE operating on the k-closest-neighbor graph in a dual-branch configuration achieves the highest per-class and overall accuracy, outperforming the baseline in some sources. These findings confirm the importance of local layout relationships and multimodal fusion exploited through GNNs for the analysis of native digital document layouts.

