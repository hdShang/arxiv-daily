---
layout: default
title: "Federated Distillation on Edge Devices: Efficient Client-Side Filtering for Non-IID Data"
---

# Federated Distillation on Edge Devices: Efficient Client-Side Filtering for Non-IID Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14769" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14769v1</a>
  <a href="https://arxiv.org/pdf/2508.14769.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14769v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14769v1', 'Federated Distillation on Edge Devices: Efficient Client-Side Filtering for Non-IID Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmed Mujtaba, Gleb Radchenko, Radu Prodan, Marc Masana

**分类**: cs.LG, cs.DC

**发布日期**: 2025-08-20

**备注**: This paper was accepted at the International Conference on Federated Learning Technologies and Applications, 2025. The final version is available at IEEE Xplore

---

## 💡 一句话要点

**提出EdgeFD以解决边缘设备上的非IID数据过滤问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `联邦学习` `边缘计算` `知识蒸馏` `非IID数据` `KMeans算法` `隐私保护` `机器学习` `数据过滤`

## 📋 核心要点

1. 现有的联邦蒸馏方法依赖复杂的知识共享策略，导致客户端需要进行高计算量的统计密度比估计，增加了处理延迟。
2. 本文提出的EdgeFD方法通过引入基于KMeans的密度比估计器，简化了客户端的数据过滤过程，消除了对服务器端过滤的需求。
3. 实验结果显示，EdgeFD在多种数据分布下的表现优于现有技术，准确率接近IID场景，且计算开销显著降低，适合边缘设备应用。

## 📝 摘要（中文）

联邦蒸馏作为一种新兴的协作机器学习方法，通过交换模型输出（软逻辑）而非完整模型参数，提供了更好的隐私保护和减少通信。然而，现有方法依赖复杂的选择性知识共享策略，要求客户端通过计算密集的统计密度比估计器识别分布内代理数据。此外，服务器端对模糊知识的过滤增加了延迟。为了解决这些挑战，本文提出了一种高效的EdgeFD方法，简化了客户端的密度比估计，并消除了服务器端过滤的需求。EdgeFD采用基于KMeans的密度比估计器，有效过滤客户端的分布内和分布外代理数据，显著提高了知识共享的质量。实验结果表明，EdgeFD在强非IID、弱非IID和IID数据分布下均优于现有方法，准确率接近IID场景，且计算开销显著降低，适合资源受限的边缘设备部署。

## 🔬 方法详解

**问题定义**：本文旨在解决现有联邦蒸馏方法在处理非IID数据时的复杂性和延迟问题。现有方法需要客户端进行高计算量的密度比估计，并依赖服务器端的模糊知识过滤，导致效率低下。

**核心思路**：EdgeFD通过引入基于KMeans的密度比估计器，简化了客户端的计算过程，直接在客户端进行数据过滤，避免了服务器端的延迟。该方法有效提高了知识共享的质量，尤其是在非IID数据场景下。

**技术框架**：EdgeFD的整体架构包括数据收集、KMeans密度比估计、数据过滤和知识共享四个主要模块。客户端首先收集数据，然后使用KMeans算法进行密度比估计，接着过滤不合适的代理数据，最后将有效的知识共享给服务器。

**关键创新**：EdgeFD的主要创新在于使用KMeans算法作为密度比估计器，显著降低了计算复杂度，并消除了对服务器端过滤的需求。这一设计使得方法在资源受限的边缘设备上更具可行性。

**关键设计**：在EdgeFD中，KMeans算法的参数设置经过优化，以确保在不同数据分布下的有效性。此外，损失函数设计考虑了知识共享的质量，确保在过滤过程中尽可能保留有用的信息。整体网络结构经过调整，以适应边缘设备的计算能力。

## 📊 实验亮点

实验结果表明，EdgeFD在强非IID、弱非IID和IID数据分布下的准确率均接近IID场景，且在计算开销上显著低于现有最先进的方法，展示了其在边缘设备上的优越性能和实用性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其适用于需要保护隐私的边缘计算场景，如智能手机、物联网设备和边缘服务器等。通过提高非IID数据处理的效率，EdgeFD能够在医疗、金融和智能城市等领域实现更安全和高效的协作学习。

## 📄 摘要（原文）

> Federated distillation has emerged as a promising collaborative machine learning approach, offering enhanced privacy protection and reduced communication compared to traditional federated learning by exchanging model outputs (soft logits) rather than full model parameters. However, existing methods employ complex selective knowledge-sharing strategies that require clients to identify in-distribution proxy data through computationally expensive statistical density ratio estimators. Additionally, server-side filtering of ambiguous knowledge introduces latency to the process. To address these challenges, we propose a robust, resource-efficient EdgeFD method that reduces the complexity of the client-side density ratio estimation and removes the need for server-side filtering. EdgeFD introduces an efficient KMeans-based density ratio estimator for effectively filtering both in-distribution and out-of-distribution proxy data on clients, significantly improving the quality of knowledge sharing. We evaluate EdgeFD across diverse practical scenarios, including strong non-IID, weak non-IID, and IID data distributions on clients, without requiring a pre-trained teacher model on the server for knowledge distillation. Experimental results demonstrate that EdgeFD outperforms state-of-the-art methods, consistently achieving accuracy levels close to IID scenarios even under heterogeneous and challenging conditions. The significantly reduced computational overhead of the KMeans-based estimator is suitable for deployment on resource-constrained edge devices, thereby enhancing the scalability and real-world applicability of federated distillation. The code is available online for reproducibility.

