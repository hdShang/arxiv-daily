---
layout: default
title: Beyond Attention: Learning Spatio-Temporal Dynamics with Emergent Interpretable Topologies
---

# Beyond Attention: Learning Spatio-Temporal Dynamics with Emergent Interpretable Topologies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00770" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00770v1</a>
  <a href="https://arxiv.org/pdf/2506.00770.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00770v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00770v1', 'Beyond Attention: Learning Spatio-Temporal Dynamics with Emergent Interpretable Topologies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sai Vamsi Alisetti, Vikas Kalagi, Sanjukta Krishnagopal

**分类**: cs.LG, cs.AI, cs.SI

**发布日期**: 2025-06-01

**备注**: 13 pages, 10 figures, workshop

---

## 💡 一句话要点

**提出InterGAT以解决图注意力网络的局限性**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `时空预测` `图注意力网络` `可解释性` `深度学习` `GRU` `动态图` `机器学习`

## 📋 核心要点

1. 现有的图注意力网络在处理时空预测时存在依赖固定邻接结构的问题，导致归纳偏差和计算开销，影响模型的可解释性。
2. 本文提出的InterGAT通过引入可学习的对称节点交互矩阵，捕捉潜在的空间关系，避免了固定图拓扑的限制。
3. 实验结果表明，InterGAT-GRU在多个数据集上显著提高了预测准确性，并且训练时间大幅减少，展示了其高效性和可解释性。

## 📝 摘要（中文）

时空预测在交通预测、能源需求建模和天气监测等应用中至关重要。尽管图注意力网络（GAT）在建模空间依赖性方面广受欢迎，但其依赖于预定义的邻接结构和动态注意力分数，导致了归纳偏差和计算开销，影响了解释性。本文提出InterGAT，作为GAT的简化替代方案，采用完全可学习的对称节点交互矩阵，捕捉潜在的空间关系，而无需依赖固定的图拓扑。我们的框架InterGAT-GRU结合了基于GRU的时间解码器，在预测准确性上超越了基线GAT-GRU，在SZ-Taxi数据集上至少提高了21%，在Los-Loop数据集上提高了6%。此外，与GAT-GRU基线相比，训练时间减少了60-70%。

## 🔬 方法详解

**问题定义**：本文旨在解决时空预测中的空间依赖性建模问题，现有的GAT方法依赖于固定的邻接结构，导致模型的归纳偏差和计算开销，影响了可解释性。

**核心思路**：InterGAT通过引入一个完全可学习的对称节点交互矩阵，捕捉潜在的空间关系，避免了对固定图拓扑的依赖，从而提升了模型的灵活性和可解释性。

**技术框架**：整体架构包括一个可学习的节点交互矩阵和一个基于GRU的时间解码器。模型首先通过交互矩阵捕捉空间关系，然后通过GRU进行时间序列预测。

**关键创新**：最重要的技术创新在于引入了可学习的对称节点交互矩阵，替代了GAT中的掩蔽注意力机制，使得模型能够自适应地学习空间关系，提升了预测性能和可解释性。

**关键设计**：模型的关键设计包括对称节点交互矩阵的初始化、损失函数的选择以及GRU的结构设置。通过这些设计，模型在训练过程中能够有效捕捉时空动态特征。

## 📊 实验亮点

实验结果显示，InterGAT-GRU在SZ-Taxi数据集上预测准确性提高至少21%，在Los-Loop数据集上提高6%。此外，训练时间相比GAT-GRU基线减少了60-70%，展示了该方法在效率和性能上的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括交通预测、能源需求建模和天气监测等。通过提高时空预测的准确性和效率，InterGAT可以为城市管理、资源调配和环境监测等实际问题提供更为有效的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Spatio-temporal forecasting is critical in applications such as traffic prediction, energy demand modeling, and weather monitoring. While Graph Attention Networks (GATs) are popular for modeling spatial dependencies, they rely on predefined adjacency structures and dynamic attention scores, introducing inductive biases and computational overhead that can obscure interpretability.
>   We propose InterGAT, a simplified alternative to GAT that replaces masked attention with a fully learnable, symmetric node interaction matrix, capturing latent spatial relationships without relying on fixed graph topologies. Our framework, InterGAT-GRU, which incorporates a GRU-based temporal decoder, outperforms the baseline GAT-GRU in forecasting accuracy, achieving at least a 21% improvement on the SZ-Taxi dataset and a 6% improvement on the Los-Loop dataset across all forecasting horizons (15 to 60 minutes). Additionally, we observed reduction in training time by 60-70% compared to GAT-GRU baseline.
>   Crucially, the learned interaction matrix reveals interpretable structure: it recovers sparse, topology-aware attention patterns that align with community structure. Spectral and clustering analyses show that the model captures both localized and global dynamics, offering insights into the functional topology driving predictions. This highlights how structure learning can simultaneously support prediction, computational efficiency, and topological interpretabil-ity in dynamic graph-based domains.

