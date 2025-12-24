---
layout: default
title: "DyGSSM: Multi-view Dynamic Graph Embeddings with State Space Model Gradient Update"
---

# DyGSSM: Multi-view Dynamic Graph Embeddings with State Space Model Gradient Update

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09017" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09017v2</a>
  <a href="https://arxiv.org/pdf/2505.09017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09017v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09017v2', 'DyGSSM: Multi-view Dynamic Graph Embeddings with State Space Model Gradient Update')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bizhan Alipour Pijan, Serdar Bozdag

**分类**: cs.LG, cs.SI

**发布日期**: 2025-05-13 (更新: 2025-12-21)

**备注**: Published in LOG conference, 2025. This version corresponds to the published article

---

## 💡 一句话要点

**提出DyGSSM以解决动态图表示学习中信息提取不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动态图表示学习` `图卷积网络` `门控循环单元` `状态空间模型` `HiPPO算法` `特征提取` `时间依赖管理`

## 📋 核心要点

1. 现有动态图表示学习方法在信息提取上存在局限，无法同时捕捉全局和局部特征。
2. DyGSSM方法结合GCN和GRU进行特征提取，并使用HiPPO算法优化状态空间模型更新。
3. 在五个公共数据集上的实验表明，DyGSSM在17个案例中超越了现有的基线和最先进方法。

## 📝 摘要（中文）

大多数动态图表示学习方法将动态图划分为离散快照，以捕捉节点随时间演变的行为。现有方法主要通过消息传递和随机游走方法捕捉每个快照中节点的局部或全局结构，随后利用基于序列的模型（如变换器）对节点嵌入的时间演变进行编码，并使用元学习技术更新模型参数。然而，这些方法存在两个主要局限性：一是未能同时提取每个快照中的全局和局部信息；二是在参数更新时未考虑当前快照的模型性能，导致缺乏时间依赖管理。为了解决这些问题，我们提出了一种新方法DyGSSM，结合图卷积网络（GCN）和门控循环单元（GRU）进行特征提取，并引入基于HiPPO算法的状态空间模型（SSM）来处理长期依赖。实验结果表明，我们的方法在20个案例中有17个超越了现有基线和最先进的方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决动态图表示学习中信息提取不足的问题，现有方法未能同时提取快照中的全局和局部信息，并且在参数更新时未考虑当前快照的模型性能，缺乏时间依赖管理。

**核心思路**：我们提出的DyGSSM方法通过结合图卷积网络（GCN）进行局部特征提取和门控循环单元（GRU）进行全局特征提取，利用交叉注意力机制整合局部和全局特征，同时引入基于HiPPO算法的状态空间模型（SSM）来处理长期依赖。

**技术框架**：DyGSSM的整体架构包括三个主要模块：局部特征提取模块（GCN）、全局特征提取模块（GRU）和状态空间模型更新模块。首先，通过GCN提取每个快照的局部特征，然后使用GRU提取全局特征，最后通过交叉注意力机制整合这些特征，并利用SSM进行参数更新。

**关键创新**：DyGSSM的主要创新在于同时提取快照中的全局和局部信息，并通过引入HiPPO算法优化状态空间模型的参数更新，确保模型在每个快照的性能能够影响后续更新，这在现有方法中是未曾实现的。

**关键设计**：在DyGSSM中，GCN和GRU的网络结构经过精心设计，以确保特征提取的有效性；损失函数采用了结合局部和全局特征的复合损失，以提升模型的整体性能。

## 📊 实验亮点

在五个公共数据集上的实验结果显示，DyGSSM在17个案例中超越了现有的基线和最先进的方法，证明了其在动态图表示学习中的有效性和优越性，展示了显著的性能提升。

## 🎯 应用场景

DyGSSM方法在社交网络分析、交通流量预测和生物信息学等多个领域具有广泛的应用潜力。通过有效捕捉动态图中的节点演变和关系变化，该方法能够为实时决策提供支持，并推动智能系统的进一步发展。

## 📄 摘要（原文）

> Most of the dynamic graph representation learning methods involve dividing a dynamic graph into discrete snapshots to capture the evolving behavior of nodes over time. Existing methods primarily capture only local or global structures of each node within a snapshot using message-passing and random walk-based methods. Then, they utilize sequence-based models (e.g., transformers) to encode the temporal evolution of node embeddings, and meta-learning techniques to update the model parameters. However, these approaches have two limitations. First, they neglect the extraction of global and local information simultaneously in each snapshot. Second, they fail to consider the model's performance in the current snapshot during parameter updates, resulting in a lack of temporal dependency management. Recently, HiPPO (High-order Polynomial Projection Operators) algorithm has gained attention for their ability to optimize and preserve sequence history in State Space Model (SSM). To address the aforementioned limitations in dynamic graph representation learning, we propose a novel method called Multi-view Dynamic Graph Embeddings with State Space Model Gradient Update (DyGSSM). Our approach combines Graph Convolution Networks (GCN) for local feature extraction and random walk with Gated Recurrent Unit (GRU) for global feature extraction in each snapshot. We then integrate the local and global features using a cross-attention mechanism. Additionally, we incorporate an SSM based on HiPPO algorithm to account for long-term dependencies when updating model parameters, ensuring that model performance in each snapshot informs subsequent updates. Experiments on five public datasets show that our method outperforms existing baseline and state-of-the-art (SOTA) methods in 17 out of 20 cases.

