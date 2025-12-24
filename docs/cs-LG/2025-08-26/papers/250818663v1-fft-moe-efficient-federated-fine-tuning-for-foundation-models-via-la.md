---
layout: default
title: "FFT-MoE: Efficient Federated Fine-Tuning for Foundation Models via Large-scale Sparse MoE under Heterogeneous Edge"
---

# FFT-MoE: Efficient Federated Fine-Tuning for Foundation Models via Large-scale Sparse MoE under Heterogeneous Edge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18663" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18663v1</a>
  <a href="https://arxiv.org/pdf/2508.18663.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18663v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18663v1', 'FFT-MoE: Efficient Federated Fine-Tuning for Foundation Models via Large-scale Sparse MoE under Heterogeneous Edge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gang Hu, Yinglei Teng, Pengfei Wu, Nan Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-26

**备注**: 9 pages, 6 figures

---

## 💡 一句话要点

**提出FFT-MoE以解决异构边缘环境下的联邦微调问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `稀疏专家混合` `模型微调` `异构环境` `非IID数据` `隐私保护` `边缘计算`

## 📋 核心要点

1. 现有的LoRA-based FFT方法在异构FL环境中存在结构不兼容和对非IID数据适应性不足的问题，影响了模型的收敛和泛化能力。
2. 本文提出FFT-MoE框架，通过稀疏Mixture of Experts适配器替代LoRA，允许客户端根据本地资源动态选择专家，实现个性化微调。
3. 在大量的实验中，FFT-MoE在IID和非IID条件下均表现出优越的泛化性能和训练效率，超越了现有的FFT基线方法。

## 📝 摘要（中文）

随着基础模型（FM）推动人工通用智能（AGI）的进步，在隐私和资源限制下对其进行微调变得愈加重要，尤其是在高质量训练数据分布于边缘设备时。联邦学习（FL）通过联邦微调（FFT）提供了一种有效的解决方案，允许在不共享原始数据的情况下进行模型协作适应。现有的基于LoRA的FFT方法在异构FL环境中面临结构不兼容和对非独立同分布（non-IID）数据适应性不足等挑战。为此，本文提出了FFT-MoE框架，通过稀疏专家混合（MoE）适配器替代LoRA，使每个客户端能够训练轻量级的门控网络，选择性激活个性化的专家子集，从而实现对本地资源预算的细粒度适应，同时保持聚合兼容性。实验结果表明，FFT-MoE在泛化性能和训练效率上均优于现有的FFT基线。

## 🔬 方法详解

**问题定义**：本文旨在解决在异构边缘环境下进行联邦微调时，LoRA方法的结构不兼容性和对非IID数据的适应性不足的问题。这些问题导致模型收敛困难和泛化能力下降。

**核心思路**：提出FFT-MoE框架，通过引入稀疏Mixture of Experts适配器，允许每个客户端根据本地资源动态选择激活的专家，从而实现个性化的微调和更好的聚合兼容性。

**技术框架**：FFT-MoE的整体架构包括客户端的轻量级门控网络、稀疏专家适配器和异构性感知辅助损失函数。客户端通过门控网络选择激活的专家，适配器则负责处理具体的任务。

**关键创新**：最重要的创新在于用稀疏MoE适配器替代LoRA，解决了结构不兼容和非IID数据适应性的问题，同时引入的辅助损失函数确保了专家的多样性和平衡利用。

**关键设计**：在设计中，门控网络的结构轻量化以适应边缘设备的资源限制，损失函数动态调整路由分布，以实现专家的均衡利用和多样性。

## 📊 实验亮点

实验结果显示，FFT-MoE在泛化性能和训练效率上均显著优于现有的FFT基线，尤其在非IID条件下，提升幅度达到XX%（具体数据待补充），展示了其在异构环境下的强大适应能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能手机、物联网设备和边缘计算平台等，能够在保护用户隐私的同时实现高效的模型微调。未来，该方法可能推动更多基于联邦学习的智能应用，提升模型在实际场景中的表现。

## 📄 摘要（原文）

> As FMs drive progress toward Artificial General Intelligence (AGI), fine-tuning them under privacy and resource constraints has become increasingly critical particularly when highquality training data resides on distributed edge devices. Federated Learning (FL) offers a compelling solution through Federated Fine-Tuning (FFT), which enables collaborative model adaptation without sharing raw data. Recent approaches incorporate Parameter-Efficient Fine-Tuning (PEFT) techniques such as Low Rank Adaptation (LoRA) to reduce computational overhead. However, LoRA-based FFT faces two major limitations in heterogeneous FL environments: structural incompatibility across clients with varying LoRA configurations and limited adaptability to non-IID data distributions, which hinders convergence and generalization. To address these challenges, we propose FFT MoE, a novel FFT framework that replaces LoRA with sparse Mixture of Experts (MoE) adapters. Each client trains a lightweight gating network to selectively activate a personalized subset of experts, enabling fine-grained adaptation to local resource budgets while preserving aggregation compatibility. To further combat the expert load imbalance caused by device and data heterogeneity, we introduce a heterogeneity-aware auxiliary loss that dynamically regularizes the routing distribution to ensure expert diversity and balanced utilization. Extensive experiments spanning both IID and non-IID conditions demonstrate that FFT MoE consistently outperforms state of the art FFT baselines in generalization performance and training efficiency.

