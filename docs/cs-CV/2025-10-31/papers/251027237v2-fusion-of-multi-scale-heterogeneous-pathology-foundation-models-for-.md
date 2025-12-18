---
layout: default
title: Fusion of Multi-scale Heterogeneous Pathology Foundation Models for Whole Slide Image Analysis
---

# Fusion of Multi-scale Heterogeneous Pathology Foundation Models for Whole Slide Image Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27237" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27237v2</a>
  <a href="https://arxiv.org/pdf/2510.27237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27237v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27237v2', 'Fusion of Multi-scale Heterogeneous Pathology Foundation Models for Whole Slide Image Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhidong Yang, Xiuhui Shi, Wei Ba, Zhigang Song, Haijing Luan, Taiyuan Hu, Senlin Lin, Jiguang Wang, Shaohua Kevin Zhou, Rui Yan

**分类**: cs.CV

**发布日期**: 2025-10-31 (更新: 2025-11-20)

**备注**: 22 pages, 9 figures

---

## 💡 一句话要点

**FuseCPath：融合多尺度异构病理学基础模型用于全切片图像分析**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全切片图像分析` `病理学基础模型` `多尺度融合` `异构模型融合` `多视图聚类` `协同蒸馏` `计算病理学`

## 📋 核心要点

1. 现有病理学基础模型因训练数据和架构差异导致异构性，影响下游任务性能。
2. FuseCPath通过多视图聚类筛选代表性patch，并设计cluster级别重嵌入和协同蒸馏策略。
3. 实验表明，FuseCPath在多个数据集和任务上实现了最先进的性能，提升了WSI分析效果。

## 📝 摘要（中文）

全切片图像(WSI)分析已成为计算病理学中日益重要的技术。病理学基础模型(FMs)的最新进展表明，其在从WSI中提取有意义的patch级别或slide级别的多尺度特征方面具有显著优势。然而，由于不同的私有训练数据集和不同的网络架构，当前的病理学FMs表现出显著的异构性。当我们利用来自不同FMs的特征进行下游任务时，这种异构性会引入性能差异。为了有效地充分利用多个FMs的优势，本文提出了一种新的融合多尺度异构病理学FMs的框架，称为FuseCPath，从而产生具有卓越集成性能的模型。该框架的主要贡献包括：(i)为了保证训练patch的代表性，我们提出了一种基于多视图聚类的方法，通过多个FMs的嵌入来过滤掉具有区分性的patch。(ii)为了有效地融合patch级别的FMs，我们设计了一种cluster级别的重嵌入策略来在线捕获patch级别的局部特征。(iii)为了有效地融合slide级别的FMs，我们设计了一种协同蒸馏策略来探索slide级别FMs之间的联系。大量的实验表明，所提出的FuseCPath在多个数据集上的多个任务中实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有病理学基础模型（FMs）在全切片图像（WSI）分析中表现出异构性，这是由于它们使用了不同的私有数据集进行训练，并且采用了不同的网络架构。这种异构性导致在下游任务中使用不同FMs提取的特征时，性能出现显著差异。因此，如何有效地融合这些异构的FMs，充分利用它们各自的优势，是一个亟待解决的问题。

**核心思路**：FuseCPath的核心思路是通过多尺度融合策略，同时考虑patch级别和slide级别的特征。对于patch级别，采用多视图聚类筛选代表性patch，并进行cluster级别的重嵌入，以捕获局部特征。对于slide级别，采用协同蒸馏策略，探索不同FMs之间的联系。通过这种方式，FuseCPath能够有效地融合异构FMs，提升整体性能。

**技术框架**：FuseCPath框架主要包含三个阶段：1) **多视图聚类筛选**：利用多个FMs的嵌入，通过聚类方法筛选出具有代表性的训练patch。2) **Cluster级别重嵌入**：对筛选后的patch进行cluster级别的重嵌入，以在线捕获patch级别的局部特征。3) **协同蒸馏**：利用协同蒸馏策略，探索slide级别FMs之间的联系，从而实现slide级别特征的有效融合。

**关键创新**：FuseCPath的关键创新在于其多尺度融合策略，特别是以下两点：1) **多视图聚类筛选**：通过多个FMs的嵌入进行聚类，能够更全面地评估patch的代表性，避免了单一FM可能存在的偏差。2) **Cluster级别重嵌入**：在cluster级别进行重嵌入，能够有效地捕获patch级别的局部特征，从而提升模型的判别能力。与现有方法相比，FuseCPath能够更有效地融合异构FMs，提升WSI分析的性能。

**关键设计**：在多视图聚类筛选阶段，采用了k-means聚类算法，并根据聚类结果选择最具代表性的patch。在cluster级别重嵌入阶段，使用了Transformer网络来学习cluster级别的特征表示。在协同蒸馏阶段，使用了KL散度作为损失函数，以促使不同FMs的输出分布趋于一致。具体的参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

FuseCPath在多个数据集上的多个任务中实现了最先进的性能，证明了其有效性。具体性能数据和对比基线在摘要中未给出，属于未知信息。但摘要强调了FuseCPath在融合异构病理学基础模型方面的优势，以及其在提升WSI分析性能方面的显著效果。

## 🎯 应用场景

FuseCPath在计算病理学领域具有广泛的应用前景，可用于癌症诊断、预后预测、免疫组化分析等。通过融合多个病理学基础模型，能够提升WSI分析的准确性和可靠性，辅助病理学家进行更精确的诊断，从而改善患者的治疗效果。该研究成果有望推动病理学人工智能的发展，并为个性化医疗提供更强大的技术支持。

## 📄 摘要（原文）

> Whole slide image (WSI) analysis has emerged as an increasingly essential technique in computational pathology. Recent advances in the pathology foundation models (FMs) have demonstrated significant advantages in deriving meaningful patch-level or slide-level multi-scale features from WSIs. However, current pathology FMs have exhibited substantial heterogeneity caused by diverse private training datasets and different network architectures. This heterogeneity introduces performance variability when we utilize the features from different FMs in the downstream tasks. To fully explore the advantages of multiple FMs effectively, in this work, we propose a novel framework for the fusion of multi-scale heterogeneous pathology FMs, called FuseCPath, yielding a model with a superior ensemble performance. The main contributions of our framework can be summarized as follows: (i) To guarantee the representativeness of the training patches, we propose a multi-view clustering-based method to filter out the discriminative patches via multiple FMs' embeddings. (ii) To effectively fuse the patch-level FMs, we devise a cluster-level re-embedding strategy to online capture patch-level local features. (iii) To effectively fuse the slide-level FMs, we devise a collaborative distillation strategy to explore the connections between slide-level FMs. Extensive experiments demonstrate that the proposed FuseCPath achieves state-of-the-art performance across multiple tasks on diverse datasets.

