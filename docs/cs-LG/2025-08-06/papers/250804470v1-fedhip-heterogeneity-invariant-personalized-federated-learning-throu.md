---
layout: default
title: "FedHiP: Heterogeneity-Invariant Personalized Federated Learning Through Closed-Form Solutions"
---

# FedHiP: Heterogeneity-Invariant Personalized Federated Learning Through Closed-Form Solutions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04470" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04470v1</a>
  <a href="https://arxiv.org/pdf/2508.04470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04470v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04470v1', 'FedHiP: Heterogeneity-Invariant Personalized Federated Learning Through Closed-Form Solutions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianheng Tang, Zhirui Yang, Jingchao Wang, Kejia Fan, Jinfeng Xu, Huiping Zhuang, Anfeng Liu, Houbing Herbert Song, Leye Wang, Yunhuai Liu

**分类**: cs.LG

**发布日期**: 2025-08-06

**备注**: 11 pages, 5 figures, 3 tables

---

## 💡 一句话要点

**提出FedHiP以解决个性化联邦学习中的数据异质性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化联邦学习` `数据异质性` `无梯度训练` `解析解决方案` `自监督学习` `特征提取` `模型个性化`

## 📋 核心要点

1. 现有个性化联邦学习方法在面对客户端数据异质性时，收敛性和性能受到严重影响，主要依赖于梯度更新的方式存在局限性。
2. 本文提出的FedHiP方案通过解析解决方案避免了基于梯度的更新，利用冻结的基础模型进行特征提取，设计了无梯度的解析分类器。
3. 实验结果表明，FedHiP在多个基准数据集上表现优异，准确率较现有最先进方法提升了至少5.79%-20.97%。

## 📝 摘要（中文）

近年来，个性化联邦学习（PFL）作为一种流行的范式，通过协作训练为每个客户端提供个性化模型。然而，现有PFL方法面临着数据异质性（即非独立同分布数据）带来的显著挑战，严重影响了收敛性和性能。本文提出了一种名为FedHiP的异质性不变个性化联邦学习方案，通过解析（即封闭形式）解决方案来避免基于梯度的更新。我们利用自监督预训练的趋势，采用冻结的基础模型进行无梯度特征提取，并开发了无梯度训练的解析分类器。FedHiP方案包括三个阶段：解析本地训练、解析全局聚合和解析本地个性化，确保每个个性化模型在数据分布的非IID情况下保持一致。大量实验验证了FedHiP方案的优越性，准确率比最先进的基线提高了至少5.79%-20.97%。

## 🔬 方法详解

**问题定义**：本文旨在解决个性化联邦学习中由于数据异质性导致的收敛性和性能下降问题。现有方法依赖于梯度更新，难以有效应对非IID数据的挑战。

**核心思路**：FedHiP方案的核心在于通过解析解决方案替代传统的梯度更新，利用自监督学习的基础模型进行特征提取，从而实现无梯度训练。

**技术框架**：FedHiP的整体架构包括三个主要阶段：解析本地训练、解析全局聚合和解析本地个性化。每个阶段都采用解析方法，确保模型在不同客户端数据分布下保持一致性。

**关键创新**：FedHiP的最大创新在于其异质性不变性，即无论数据如何分布，每个个性化模型都保持相同。这一特性与传统方法的依赖梯度更新形成鲜明对比。

**关键设计**：在设计中，使用了冻结的基础模型作为特征提取器，避免了梯度计算的复杂性。损失函数和网络结构经过优化，以支持解析分类器的有效训练。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，FedHiP在多个基准数据集上的准确率提升显著，较现有最先进的基线方法提高了至少5.79%-20.97%。这一结果表明，FedHiP在处理数据异质性方面具有明显优势，验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融和智能家居等多个需要个性化模型的场景。通过提高个性化模型的性能，FedHiP能够为用户提供更精准的服务，推动智能系统的进一步发展。未来，随着数据隐私和安全问题的日益重要，FedHiP的无梯度特性将为保护用户数据提供新的解决方案。

## 📄 摘要（原文）

> Lately, Personalized Federated Learning (PFL) has emerged as a prevalent paradigm to deliver personalized models by collaboratively training while simultaneously adapting to each client's local applications. Existing PFL methods typically face a significant challenge due to the ubiquitous data heterogeneity (i.e., non-IID data) across clients, which severely hinders convergence and degrades performance. We identify that the root issue lies in the long-standing reliance on gradient-based updates, which are inherently sensitive to non-IID data. To fundamentally address this issue and bridge the research gap, in this paper, we propose a Heterogeneity-invariant Personalized Federated learning scheme, named FedHiP, through analytical (i.e., closed-form) solutions to avoid gradient-based updates. Specifically, we exploit the trend of self-supervised pre-training, leveraging a foundation model as a frozen backbone for gradient-free feature extraction. Following the feature extractor, we further develop an analytic classifier for gradient-free training. To support both collective generalization and individual personalization, our FedHiP scheme incorporates three phases: analytic local training, analytic global aggregation, and analytic local personalization. The closed-form solutions of our FedHiP scheme enable its ideal property of heterogeneity invariance, meaning that each personalized model remains identical regardless of how non-IID the data are distributed across all other clients. Extensive experiments on benchmark datasets validate the superiority of our FedHiP scheme, outperforming the state-of-the-art baselines by at least 5.79%-20.97% in accuracy.

