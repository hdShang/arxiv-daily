---
layout: default
title: "GraphProp: Training the Graph Foundation Models using Graph Properties"
---

# GraphProp: Training the Graph Foundation Models using Graph Properties

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04594" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04594v1</a>
  <a href="https://arxiv.org/pdf/2508.04594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04594v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04594v1', 'GraphProp: Training the Graph Foundation Models using Graph Properties')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziheng Sun, Qi Feng, Lehao Lin, Chris Ding, Jicong Fan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出GraphProp以解决图基础模型的结构性泛化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图基础模型` `结构泛化` `图不变量` `跨领域学习` `图分类` `少样本学习`

## 📋 核心要点

1. 现有方法主要集中于节点特征的统一表示，缺乏对图结构的跨领域泛化能力，导致在图级任务中表现不佳。
2. 论文提出GraphProp，通过训练结构GFM来捕捉图的不变量，强调图结构在跨领域信息传递中的重要性。
3. 实验结果显示，GraphProp在监督学习和少样本学习中显著提升性能，尤其在缺乏节点属性的图上表现优异。

## 📝 摘要（中文）

本研究聚焦于训练具有强泛化能力的图基础模型（GFM），以应对图分类等图级任务。有效的GFM训练需要捕捉跨领域一致的信息。我们发现，与节点特征和图标签相比，图结构提供了更为一致的跨领域信息。然而，传统GFM主要关注将不同领域的节点特征转化为统一的表示空间，往往缺乏结构上的跨领域泛化。为此，我们提出了GraphProp，强调结构泛化。GraphProp的训练过程分为两个主要阶段：首先，通过预测图不变量来训练结构GFM；其次，利用结构GFM提供的表示作为位置编码，结合领域特定的节点属性和图标签，进一步提升跨领域节点特征的泛化能力。实验表明，GraphProp在监督学习和少样本学习中显著优于竞争对手，尤其在处理没有节点属性的图时表现突出。

## 🔬 方法详解

**问题定义**：本论文旨在解决图基础模型在跨领域任务中的结构性泛化不足的问题。现有方法往往忽视图结构的重要性，导致泛化能力受限。

**核心思路**：论文的核心思路是通过预测图的不变量来训练结构GFM，从而捕捉图的抽象结构信息，并利用这些信息提升跨领域的节点特征泛化能力。

**技术框架**：GraphProp的整体架构分为两个阶段：第一阶段训练结构GFM，第二阶段利用结构GFM的表示作为位置编码，结合领域特定的节点属性和图标签，训练全面的GFM。

**关键创新**：最重要的技术创新在于强调图结构的泛化能力，通过图不变量的预测来实现对图的抽象理解，与传统方法的节点特征转移形成鲜明对比。

**关键设计**：在训练过程中，采用了特定的损失函数来优化图不变量的预测，并设计了适应不同领域的节点属性和图标签的网络结构，以增强模型的泛化能力。

## 📊 实验亮点

实验结果表明，GraphProp在监督学习和少样本学习中显著优于现有方法，尤其在处理没有节点属性的图时，性能提升幅度达到XX%（具体数据待补充）。这些结果验证了GraphProp在图结构泛化方面的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括社交网络分析、生物信息学和推荐系统等。GraphProp能够在缺乏节点属性的情况下，依然有效地进行图分类和其他图级任务，具有重要的实际价值和广泛的应用前景。未来，GraphProp可能推动图学习领域的进一步发展，尤其是在跨领域任务中的应用。

## 📄 摘要（原文）

> This work focuses on training graph foundation models (GFMs) that have strong generalization ability in graph-level tasks such as graph classification. Effective GFM training requires capturing information consistent across different domains. We discover that graph structures provide more consistent cross-domain information compared to node features and graph labels. However, traditional GFMs primarily focus on transferring node features from various domains into a unified representation space but often lack structural cross-domain generalization. To address this, we introduce GraphProp, which emphasizes structural generalization. The training process of GraphProp consists of two main phases. First, we train a structural GFM by predicting graph invariants. Since graph invariants are properties of graphs that depend only on the abstract structure, not on particular labellings or drawings of the graph, this structural GFM has a strong ability to capture the abstract structural information and provide discriminative graph representations comparable across diverse domains. In the second phase, we use the representations given by the structural GFM as positional encodings to train a comprehensive GFM. This phase utilizes domain-specific node attributes and graph labels to further improve cross-domain node feature generalization. Our experiments demonstrate that GraphProp significantly outperforms the competitors in supervised learning and few-shot learning, especially in handling graphs without node attributes.

