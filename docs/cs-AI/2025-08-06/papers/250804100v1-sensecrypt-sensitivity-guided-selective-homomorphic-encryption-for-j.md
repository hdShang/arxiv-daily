---
layout: default
title: "SenseCrypt: Sensitivity-guided Selective Homomorphic Encryption for Joint Federated Learning in Cross-Device Scenarios"
---

# SenseCrypt: Sensitivity-guided Selective Homomorphic Encryption for Joint Federated Learning in Cross-Device Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04100" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04100v1</a>
  <a href="https://arxiv.org/pdf/2508.04100.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04100v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04100v1', 'SenseCrypt: Sensitivity-guided Selective Homomorphic Encryption for Joint Federated Learning in Cross-Device Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Borui Li, Li Yan, Junhao Han, Jianmin Liu, Lei Yu

**分类**: cs.CR, cs.AI, cs.DC

**发布日期**: 2025-08-06

**备注**: 17 pages, 19 figures

---

## 💡 一句话要点

**提出SenseCrypt以解决跨设备场景下的同态加密效率问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `同态加密` `联邦学习` `跨设备场景` `隐私保护` `模型优化` `敏感性引导` `选择性加密`

## 📋 核心要点

1. 现有同态加密方法在跨设备联邦学习中存在高开销和适应成本，导致客户端延迟和性能下降。
2. 本文提出的SenseCrypt框架通过敏感性引导选择性同态加密，聚类相似数据分布的客户端以优化加密策略。
3. 实验结果显示，SenseCrypt在保证模型准确性的同时，训练时间显著减少，提升幅度达到58.4%-88.7%。

## 📝 摘要（中文）

同态加密（HE）在保护联邦学习（FL）安全性方面具有重要作用，但面临高开销和适应成本的问题。选择性同态加密方法通过全局掩码部分加密模型参数，旨在降低开销并易于适应。然而，在具有异构数据和系统能力的跨设备场景中，传统选择性同态加密方法导致客户端延迟增加，且HE开销降低效果不佳。为此，本文提出了SenseCrypt，一个基于敏感性引导的选择性同态加密框架，旨在为每个跨设备FL客户端自适应地平衡安全性和HE开销。通过对模型参数敏感性的观察，设计了隐私保护方法以聚类具有相似数据分布的客户端，并开发了评分机制来推导每个客户端可加密的无延迟模型参数比例。最终，构建并解决了一个多目标模型参数选择优化问题，最大化模型安全性并最小化HE开销。实验结果表明，SenseCrypt在确保安全性的同时，训练时间较传统HE方法减少58.4%-88.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决跨设备联邦学习中同态加密方法的高开销和客户端延迟问题。现有选择性同态加密方法在异构数据和系统能力下表现不佳，导致性能下降。

**核心思路**：SenseCrypt框架通过敏感性引导选择性同态加密，利用模型参数的敏感性来聚类具有相似数据分布的客户端，从而优化加密策略，减少HE开销。

**技术框架**：SenseCrypt的整体架构包括三个主要模块：1) 客户端聚类模块，通过隐私保护方法聚类相似数据分布的客户端；2) 评分机制模块，推导每个客户端可加密的无延迟模型参数比例；3) 多目标优化模块，解决模型参数选择问题，平衡安全性和HE开销。

**关键创新**：最重要的创新点在于引入敏感性引导的选择性同态加密策略，能够根据数据分布的相似性自适应调整加密策略，显著降低HE开销并避免客户端延迟。

**关键设计**：在设计中，采用了聚类算法对客户端进行分组，设置了评分机制来评估可加密参数比例，并构建了多目标优化问题以实现HE开销和模型安全性的平衡。

## 📊 实验亮点

实验结果表明，SenseCrypt在抵御最先进的反演攻击的同时，模型准确性与IID数据相当，训练时间较传统同态加密方法减少58.4%-88.7%，显示出显著的性能提升。

## 🎯 应用场景

SenseCrypt框架在跨设备联邦学习中具有广泛的应用潜力，特别是在需要保护用户隐私的场景，如医疗、金融和智能设备等领域。通过优化同态加密的效率，该方法能够有效提升模型训练的速度和安全性，促进更广泛的应用落地。

## 📄 摘要（原文）

> Homomorphic Encryption (HE) prevails in securing Federated Learning (FL), but suffers from high overhead and adaptation cost. Selective HE methods, which partially encrypt model parameters by a global mask, are expected to protect privacy with reduced overhead and easy adaptation. However, in cross-device scenarios with heterogeneous data and system capabilities, traditional Selective HE methods deteriorate client straggling, and suffer from degraded HE overhead reduction performance. Accordingly, we propose SenseCrypt, a Sensitivity-guided selective Homomorphic EnCryption framework, to adaptively balance security and HE overhead per cross-device FL client. Given the observation that model parameter sensitivity is effective for measuring clients' data distribution similarity, we first design a privacy-preserving method to respectively cluster the clients with similar data distributions. Then, we develop a scoring mechanism to deduce the straggler-free ratio of model parameters that can be encrypted by each client per cluster. Finally, for each client, we formulate and solve a multi-objective model parameter selection optimization problem, which minimizes HE overhead while maximizing model security without causing straggling. Experiments demonstrate that SenseCrypt ensures security against the state-of-the-art inversion attacks, while achieving normal model accuracy as on IID data, and reducing training time by 58.4%-88.7% as compared to traditional HE methods.

