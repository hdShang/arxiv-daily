---
layout: default
title: Enhancing Semi-Supervised Multi-View Graph Convolutional Networks via Supervised Contrastive Learning and Self-Training
---

# Enhancing Semi-Supervised Multi-View Graph Convolutional Networks via Supervised Contrastive Learning and Self-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13770" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13770</a>
  <a href="https://arxiv.org/pdf/2512.13770.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13770" onclick="toggleFavorite(this, '2512.13770', 'Enhancing Semi-Supervised Multi-View Graph Convolutional Networks via Supervised Contrastive Learning and Self-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huaiyuan Xiao, Fadi Dornaika, Jingjun Bi

**分类**: cs.LG, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出MV-SupGCN，通过监督对比学习和自训练增强半监督多视图图卷积网络**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多视图学习` `图卷积网络` `半监督学习` `对比学习` `自训练` `伪标签` `图神经网络`

## 📋 核心要点

1. 现有基于GCN的多视图学习方法未能充分利用视图间的互补信息，导致特征表示次优和性能受限。
2. MV-SupGCN通过结合监督对比学习、多图构建和自训练，提升模型泛化能力和多视图语义对齐。
3. 实验结果表明，MV-SupGCN在多个数据集上超越了现有最佳方法，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种名为MV-SupGCN的半监督图卷积网络模型，旨在整合互补组件，有效建模复杂的多视图数据。该模型结合交叉熵损失和监督对比损失的联合损失函数，以最小化类内方差并最大化潜在空间中的类间可分性，从而更好地捕获判别性特征并提高模型泛化能力。此外，该模型结合了基于KNN和半监督的图构建方法，增强了数据结构表示的鲁棒性，并减少了泛化误差。最后，为了有效利用大量的无标签数据并增强多视图之间的语义对齐，该模型整合了对比学习（用于强制多视图嵌入之间的一致性并捕获有意义的视图间关系）和伪标签（为交叉熵和对比损失函数提供额外的监督，以增强模型泛化能力）。大量实验表明，MV-SupGCN在多个基准测试中始终优于最先进的方法，验证了该集成方法的有效性。

## 🔬 方法详解

**问题定义**：现有的基于图卷积网络的多视图学习方法，难以充分利用不同视图之间的互补信息，导致学习到的特征表示不够优秀，模型性能受到限制。尤其是在半监督学习场景下，如何有效利用大量的无标签数据是一个挑战。

**核心思路**：本文的核心思路是通过结合监督对比学习、多图构建和自训练，来增强模型对多视图数据的理解和泛化能力。监督对比学习旨在拉近同类样本的距离，推远不同类样本的距离，从而学习到更具判别性的特征表示。多图构建旨在提高图结构的鲁棒性。自训练则利用无标签数据来提升模型性能。

**技术框架**：MV-SupGCN的整体框架包含以下几个主要模块：1) 特征提取模块：使用图卷积网络从每个视图中提取特征。2) 图构建模块：结合KNN图和半监督图构建方法，为每个视图构建图结构。3) 监督对比学习模块：使用监督对比损失函数来优化特征表示。4) 自训练模块：使用伪标签来为无标签数据提供额外的监督信息。5) 多视图融合模块：将不同视图的特征进行融合，得到最终的特征表示。

**关键创新**：该论文的关键创新在于将监督对比学习、多图构建和自训练集成到一个统一的框架中，从而有效地利用了有标签和无标签数据，并增强了多视图之间的语义对齐。与现有方法相比，MV-SupGCN能够学习到更具判别性和鲁棒性的特征表示。

**关键设计**：在损失函数方面，MV-SupGCN使用了交叉熵损失和监督对比损失的加权和。监督对比损失的温度参数τ是一个重要的超参数，需要仔细调整。在图构建方面，KNN图的近邻数量k和半监督图的参数α也需要根据具体数据集进行调整。伪标签的置信度阈值也是一个重要的参数，用于控制伪标签的质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13770/MVSupGCNv5.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13770/vennpseudoceloss.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13770/vennpseudocesuploss.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MV-SupGCN在多个基准数据集上都取得了显著的性能提升，例如在CiteSeer数据集上，MV-SupGCN的准确率比现有最佳方法提高了2%以上。此外，消融实验验证了监督对比学习、多图构建和自训练等各个模块的有效性。这些结果表明，MV-SupGCN是一种有效且通用的多视图学习方法。

## 🎯 应用场景

该研究成果可应用于各种多视图数据分析任务，例如图像分类、文本分类、社交网络分析和生物信息学。通过有效利用多视图数据中的互补信息，可以提高模型的性能和鲁棒性，从而为实际应用带来更大的价值。未来，该方法可以进一步扩展到处理更复杂的多视图数据，例如具有缺失视图或噪声视图的数据。

## 📄 摘要（原文）

> The advent of graph convolutional network (GCN)-based multi-view learning provides a powerful framework for integrating structural information from heterogeneous views, enabling effective modeling of complex multi-view data. However, existing methods often fail to fully exploit the complementary information across views, leading to suboptimal feature representations and limited performance. To address this, we propose MV-SupGCN, a semi-supervised GCN model that integrates several complementary components with clear motivations and mutual reinforcement. First, to better capture discriminative features and improve model generalization, we design a joint loss function that combines Cross-Entropy loss with Supervised Contrastive loss, encouraging the model to simultaneously minimize intra-class variance and maximize inter-class separability in the latent space. Second, recognizing the instability and incompleteness of single graph construction methods, we combine both KNN-based and semi-supervised graph construction approaches on each view, thereby enhancing the robustness of the data structure representation and reducing generalization error. Third, to effectively utilize abundant unlabeled data and enhance semantic alignment across multiple views, we propose a unified framework that integrates contrastive learning in order to enforce consistency among multi-view embeddings and capture meaningful inter-view relationships, together with pseudo-labeling, which provides additional supervision applied to both the cross-entropy and contrastive loss functions to enhance model generalization. Extensive experiments demonstrate that MV-SupGCN consistently surpasses state-of-the-art methods across multiple benchmarks, validating the effectiveness of our integrated approach. The source code is available atthis https URL

