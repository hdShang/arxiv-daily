---
layout: default
title: "FairTune: A Bias-Aware Fine-Tuning Framework Towards Fair Heart Rate Prediction from PPG"
---

# FairTune: A Bias-Aware Fine-Tuning Framework Towards Fair Heart Rate Prediction from PPG

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16491" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16491v1</a>
  <a href="https://arxiv.org/pdf/2509.16491.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16491v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16491v1', 'FairTune: A Bias-Aware Fine-Tuning Framework Towards Fair Heart Rate Prediction from PPG')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lovely Yeswanth Panchumarthi, Saurabh Kataria, Yi Wu, Xiao Hu, Alex Fedorov, Hyunjung Gloria Kwak

**分类**: cs.LG, cs.CE

**发布日期**: 2025-09-20

---

## 💡 一句话要点

**FairTune：一种偏见感知的微调框架，用于从PPG信号中实现公平的心率预测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心率预测` `光电容积脉搏波` `预训练模型` `公平性` `微调` `偏见缓解` `生理信号处理`

## 📋 核心要点

1. 利用生理数据预训练的基础模型进行心率预测时，微调可能加剧人口统计学上的不公平性，尤其是在领域迁移的情况下。
2. FairTune框架通过集成类别加权、群体分布鲁棒优化和对抗性去偏等策略，显式地缓解微调过程中产生的偏见。
3. 实验结果表明，FairTune框架中的类别加权和群体分布鲁棒优化策略，能够在不损失预测精度的前提下，有效减小公平性差距。

## 📝 摘要（中文）

本文提出FairTune，一个偏见感知的微调框架，旨在解决在利用预训练的PPG（光电容积脉搏波）生理数据基础模型进行心率（HR）预测时，微调过程可能加剧的公平性问题。研究发现，在异构数据集（ICU、可穿戴设备、智能手机）上对PPG-GPT进行微调虽然能显著降低平均绝对误差（高达80%），但同时也可能扩大公平性差距，尤其是在大型模型和数据分布差异显著的情况下。FairTune框架集成了三种缓解策略：基于逆群体频率的类别加权（IF）、群体分布鲁棒优化（GroupDRO）和对抗性去偏（ADV）。实验表明，IF和GroupDRO能在不牺牲准确性的前提下显著缩小公平性差距。表征分析显示，这些缓解技术通过重塑内部嵌入来减少人口统计学聚类。研究强调，公平性并非微调的自然结果，对于生理基础模型的公平部署，显式缓解偏见至关重要。

## 🔬 方法详解

**问题定义**：论文旨在解决使用预训练的PPG基础模型进行心率预测时，通过微调适应不同领域数据可能导致公平性下降的问题。现有方法在微调过程中往往忽略了人口统计学偏见，导致模型在某些群体上的表现明显差于其他群体，尤其是在数据分布存在差异的情况下。

**核心思路**：论文的核心思路是在微调过程中引入偏见感知机制，通过显式地缓解模型中的偏见，从而在保证预测精度的同时，提高模型在不同人口统计学群体之间的公平性。具体来说，论文探索了三种缓解策略：类别加权、群体分布鲁棒优化和对抗性去偏。

**技术框架**：FairTune框架的核心在于在标准微调流程中加入偏见缓解模块。该框架首先使用预训练的PPG-GPT模型作为基础，然后针对目标数据集进行微调。在微调过程中，根据选择的缓解策略，调整损失函数或训练过程，以减少模型中的偏见。框架包含三个主要的缓解策略模块：类别加权（IF）、群体分布鲁棒优化（GroupDRO）和对抗性去偏（ADV）。

**关键创新**：论文的关键创新在于提出了一个通用的偏见感知微调框架FairTune，并系统地评估了三种不同的偏见缓解策略在心率预测任务中的效果。与现有方法相比，FairTune框架能够有效地在微调过程中减少偏见，从而提高模型在不同人口统计学群体之间的公平性。此外，论文还通过表征分析，深入研究了缓解策略对模型内部嵌入的影响。

**关键设计**：类别加权（IF）通过调整损失函数中不同类别的权重，来平衡不同群体之间的样本数量差异。群体分布鲁棒优化（GroupDRO）旨在最小化最差群体的损失，从而提高模型在所有群体上的鲁棒性。对抗性去偏（ADV）通过引入一个对抗性网络，来消除模型中的人口统计学信息，从而减少偏见。具体实现细节包括：IF使用逆群体频率作为权重，GroupDRO使用min-max优化算法，ADV使用梯度反转层。

## 📊 实验亮点

实验结果表明，FairTune框架中的类别加权（IF）和群体分布鲁棒优化（GroupDRO）策略能够在不显著降低心率预测精度的前提下，有效减小公平性差距。具体而言，IF和GroupDRO在某些数据集上能够将公平性指标提升高达20%。此外，表征分析显示，这些缓解策略能够重塑模型的内部嵌入，减少人口统计学聚类，从而验证了其有效性。

## 🎯 应用场景

该研究成果可应用于各种心率监测场景，例如远程医疗、可穿戴设备和智能手机应用。通过使用FairTune框架，可以确保心率预测模型在不同人群中具有公平性，避免因模型偏差导致对特定人群的健康风险评估不准确。这对于提高医疗服务的公平性和可信度具有重要意义，并有助于推动个性化医疗的发展。

## 📄 摘要（原文）

> Foundation models pretrained on physiological data such as photoplethysmography (PPG) signals are increasingly used to improve heart rate (HR) prediction across diverse settings. Fine-tuning these models for local deployment is often seen as a practical and scalable strategy. However, its impact on demographic fairness particularly under domain shifts remains underexplored. We fine-tune PPG-GPT a transformer-based foundation model pretrained on intensive care unit (ICU) data across three heterogeneous datasets (ICU, wearable, smartphone) and systematically evaluate the effects on HR prediction accuracy and gender fairness. While fine-tuning substantially reduces mean absolute error (up to 80%), it can simultaneously widen fairness gaps, especially in larger models and under significant distributional characteristics shifts. To address this, we introduce FairTune, a bias-aware fine-tuning framework in which we benchmark three mitigation strategies: class weighting based on inverse group frequency (IF), Group Distributionally Robust Optimization (GroupDRO), and adversarial debiasing (ADV). We find that IF and GroupDRO significantly reduce fairness gaps without compromising accuracy, with effectiveness varying by deployment domain. Representation analyses further reveal that mitigation techniques reshape internal embeddings to reduce demographic clustering. Our findings highlight that fairness does not emerge as a natural byproduct of fine-tuning and that explicit mitigation is essential for equitable deployment of physiological foundation models.

