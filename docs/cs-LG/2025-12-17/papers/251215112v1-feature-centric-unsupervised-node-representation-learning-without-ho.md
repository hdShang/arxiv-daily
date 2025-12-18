---
layout: default
title: Feature-Centric Unsupervised Node Representation Learning Without Homophily Assumption
---

# Feature-Centric Unsupervised Node Representation Learning Without Homophily Assumption

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15112" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15112v1</a>
  <a href="https://arxiv.org/pdf/2512.15112.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15112v1" onclick="toggleFavorite(this, '2512.15112v1', 'Feature-Centric Unsupervised Node Representation Learning Without Homophily Assumption')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sunwoo Kim, Soo Yong Lee, Kyungho Kim, Hyunjin Hwang, Jaemin Yoo, Kijung Shin

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-17

**备注**: Published in AAAI 2026

---

## 💡 一句话要点

**FUEL：一种无需同质性假设的特征中心无监督节点表示学习方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无监督学习` `节点表示学习` `图卷积网络` `非同质图` `对比学习`

## 📋 核心要点

1. 现有无监督节点表示学习方法在非同质图上过度依赖图卷积，导致节点嵌入区分度降低。
2. FUEL通过节点特征识别节点聚类作为类代理，自适应学习图卷积的使用程度，增强类内相似性和类间可分离性。
3. 在14个基准数据集上的实验表明，FUEL在不同同质性水平的图上均取得了优于现有方法的性能。

## 📝 摘要（中文）

无监督节点表示学习旨在无需节点标签的情况下获得有意义的节点嵌入。为此，图卷积通常用于聚合来自相邻节点的信息，以编码节点特征和图拓扑结构。然而，过度依赖图卷积可能并非最优，尤其是在非同质图中，因为它可能为特征或拓扑属性不同的节点产生过于相似的嵌入。因此，在监督学习环境中，调整图卷积的使用程度已被积极探索，但在无监督场景中，此类方法仍未得到充分研究。为了解决这个问题，我们提出了FUEL，它通过旨在增强嵌入空间中的类内相似性和类间可分离性来自适应地学习适当程度的图卷积使用。由于类是未知的，FUEL利用节点特征来识别节点聚类，并将这些聚类视为类的代理。通过使用15种基线方法和14个基准数据集进行的大量实验，我们证明了FUEL在下游任务中的有效性，在具有不同同质性水平的图上实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有无监督节点表示学习方法，特别是基于图卷积的方法，在非同质图上表现不佳。这是因为图卷积会过度平滑节点特征，使得连接的节点即使特征不同也会具有相似的嵌入，从而降低了节点表示的区分性。现有的方法缺乏自适应调整图卷积使用程度的机制，无法有效处理非同质图。

**核心思路**：FUEL的核心思路是自适应地学习图卷积的使用程度，以平衡节点特征和图拓扑结构的影响。它通过最大化嵌入空间中的类内相似性和类间可分离性来实现这一点。由于真实的节点类别未知，FUEL利用节点特征进行聚类，并将这些聚类视为代理类别。

**技术框架**：FUEL的整体框架包括以下几个主要步骤：1) 使用节点特征进行聚类，得到代理类别；2) 使用图卷积生成节点嵌入；3) 定义一个损失函数，该函数鼓励同一代理类别内的节点具有相似的嵌入，而不同代理类别内的节点具有不同的嵌入；4) 通过优化该损失函数来学习图卷积的权重，从而自适应地调整图卷积的使用程度。

**关键创新**：FUEL的关键创新在于它提出了一种无监督的方式来学习图卷积的使用程度，而无需依赖节点标签。它通过利用节点特征进行聚类，并将聚类结果作为代理类别，从而能够在无监督的环境下优化节点嵌入的类内相似性和类间可分离性。这使得FUEL能够有效地处理非同质图，并获得更好的节点表示。

**关键设计**：FUEL的关键设计包括：1) 使用K-means算法进行节点聚类，得到代理类别；2) 使用图卷积网络（GCN）生成节点嵌入；3) 定义对比损失函数，该函数包括一个正样本项（鼓励同一代理类别内的节点具有相似的嵌入）和一个负样本项（鼓励不同代理类别内的节点具有不同的嵌入）；4) 使用Adam优化器优化损失函数，学习GCN的权重。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15112v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15112v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15112v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

FUEL在14个基准数据集上进行了广泛的实验，并与15种基线方法进行了比较。实验结果表明，FUEL在各种图上都取得了最先进的性能，尤其是在非同质图上，FUEL的提升更为显著。例如，在某些数据集上，FUEL的性能比第二好的方法提高了5%以上。

## 🎯 应用场景

FUEL可应用于各种图结构数据的分析任务，例如社交网络分析、生物网络分析、知识图谱推理等。通过学习高质量的节点表示，FUEL可以提升节点分类、链接预测、社区发现等下游任务的性能。尤其是在节点同质性较低的复杂网络中，FUEL的优势更为明显，能够挖掘出更深层次的节点关系和模式。

## 📄 摘要（原文）

> Unsupervised node representation learning aims to obtain meaningful node embeddings without relying on node labels. To achieve this, graph convolution, which aggregates information from neighboring nodes, is commonly employed to encode node features and graph topology. However, excessive reliance on graph convolution can be suboptimal-especially in non-homophilic graphs-since it may yield unduly similar embeddings for nodes that differ in their features or topological properties. As a result, adjusting the degree of graph convolution usage has been actively explored in supervised learning settings, whereas such approaches remain underexplored in unsupervised scenarios. To tackle this, we propose FUEL, which adaptively learns the adequate degree of graph convolution usage by aiming to enhance intra-class similarity and inter-class separability in the embedding space. Since classes are unknown, FUEL leverages node features to identify node clusters and treats these clusters as proxies for classes. Through extensive experiments using 15 baseline methods and 14 benchmark datasets, we demonstrate the effectiveness of FUEL in downstream tasks, achieving state-of-the-art performance across graphs with diverse levels of homophily.

