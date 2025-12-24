---
layout: default
title: Lightweight Defense Against Adversarial Attacks in Time Series Classification
---

# Lightweight Defense Against Adversarial Attacks in Time Series Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02073" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02073v1</a>
  <a href="https://arxiv.org/pdf/2505.02073.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02073v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02073v1', 'Lightweight Defense Against Adversarial Attacks in Time Series Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Han

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-04

**备注**: 13 pages, 8 figures. Accepted at RAFDA Workshop, PAKDD 2025 (Springer, EI & Scopus indexed). Code: https://github.com/Yi126/Lightweight-Defence

---

## 💡 一句话要点

**提出基于数据增强的轻量级对抗攻击防御方法以提升时间序列分类的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列分类` `对抗攻击` `数据增强` `鲁棒性` `机器学习`

## 📋 核心要点

1. 现有的对抗训练方法在时间序列分类中计算成本高，难以广泛应用。
2. 论文提出五种基于数据增强的防御方法，计算资源消耗显著低于传统对抗训练。
3. 实验结果表明，提出的方法在防御性能和模型泛化能力上均优于PGD-based对抗训练。

## 📝 摘要（中文）

随着时间序列分类（TSC）的重要性日益增加，确保TSC模型对抗对抗攻击的鲁棒性显得尤为重要。尽管在计算机视觉领域，对抗防御已被广泛研究，但TSC领域主要依赖于计算成本高昂的对抗训练（AT）。本文开发了五种针对时间序列的数据增强防御方法，其中计算资源消耗最高的方法与原始TSC模型相比，仅增加了14.07%的计算资源。此外，这些方法的部署过程简单。通过利用这些方法的优势，我们创建了两种组合方法，其中一种是所有提出技术的集成，不仅提供了比基于PGD的AT更好的防御性能，还增强了TSC模型的泛化能力。我们的集成方法所需的计算资源不到PGD-based AT的三分之一。这些方法推动了数据挖掘中鲁棒TSC的发展，并为未来将数据增强对抗防御与大规模预训练模型结合提供了见解。

## 🔬 方法详解

**问题定义**：本文旨在解决时间序列分类（TSC）模型在面对对抗攻击时的脆弱性，现有的对抗训练方法计算成本高，限制了其应用。

**核心思路**：论文提出了五种基于数据增强的防御方法，旨在通过增加数据多样性来提高模型的鲁棒性，同时降低计算资源消耗。

**技术框架**：整体架构包括数据增强模块、模型训练模块和防御评估模块。数据增强模块生成多样化的训练样本，模型训练模块使用这些样本进行训练，防御评估模块则评估模型在对抗攻击下的表现。

**关键创新**：最重要的技术创新在于提出了轻量级的数据增强防御方法，这些方法的计算资源消耗显著低于传统的对抗训练方法，且能有效提升模型的防御性能。

**关键设计**：在设计中，采用了多种数据增强技术，结合了不同的增强策略，以确保生成的数据能够有效提升模型的泛化能力和鲁棒性。

## 📊 实验亮点

实验结果显示，提出的集成方法在防御性能上优于PGD-based对抗训练，且计算资源消耗不到其三分之一。具体而言，集成方法在多种对抗攻击下的准确率提升显著，验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场预测、医疗监测和工业设备故障检测等时间序列分析任务。通过提高模型的鲁棒性，能够有效防止对抗攻击带来的风险，从而提升实际应用的安全性和可靠性。未来，该方法还可与大规模预训练模型结合，进一步推动时间序列特征学习的发展。

## 📄 摘要（原文）

> As time series classification (TSC) gains prominence, ensuring robust TSC models against adversarial attacks is crucial. While adversarial defense is well-studied in Computer Vision (CV), the TSC field has primarily relied on adversarial training (AT), which is computationally expensive. In this paper, five data augmentation-based defense methods tailored for time series are developed, with the most computationally intensive method among them increasing the computational resources by only 14.07% compared to the original TSC model. Moreover, the deployment process for these methods is straightforward. By leveraging these advantages of our methods, we create two combined methods. One of these methods is an ensemble of all the proposed techniques, which not only provides better defense performance than PGD-based AT but also enhances the generalization ability of TSC models. Moreover, the computational resources required for our ensemble are less than one-third of those required for PGD-based AT. These methods advance robust TSC in data mining. Furthermore, as foundation models are increasingly explored for time series feature learning, our work provides insights into integrating data augmentation-based adversarial defense with large-scale pre-trained models in future research.

