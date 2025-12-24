---
layout: default
title: A New Spatiotemporal Correlation Anomaly Detection Method that Integrates Contrastive Learning and Few-Shot Learning in Wireless Sensor Networks
---

# A New Spatiotemporal Correlation Anomaly Detection Method that Integrates Contrastive Learning and Few-Shot Learning in Wireless Sensor Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00420" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00420v1</a>
  <a href="https://arxiv.org/pdf/2506.00420.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00420v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00420v1', 'A New Spatiotemporal Correlation Anomaly Detection Method that Integrates Contrastive Learning and Few-Shot Learning in Wireless Sensor Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Miao Ye, Suxiao Wang, Jiaguang Han, Yong Wang, Xiaoli Wang, Jingxuan Wei, Peng Wen, Jing Cui

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-31

---

## 💡 一句话要点

**提出MTAD-RD以解决无线传感器网络异常检测中的样本不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `无线传感器网络` `异常检测` `对比学习` `少样本学习` `时空相关特征` `深度学习` `图神经网络`

## 📋 核心要点

1. 现有无线传感器网络异常检测方法在样本标签缺失和样本不平衡方面存在显著挑战，限制了检测性能。
2. 本文提出的MTAD-RD模型通过增强的网络结构和两阶段训练策略，有效提取时空相关特征并解决样本不足问题。
3. 在真实数据集上的实验结果显示，MTAD-RD方法的F1分数达到90.97%，显著优于现有的监督学习方法。

## 📝 摘要（中文）

在无线传感器网络（WSNs）中，检测数据异常对于评估其可靠性和稳定性至关重要。现有的异常检测方法面临提取时空相关特征有限、缺乏样本标签、异常样本稀少及样本分布不平衡等挑战。为此，本文提出了一种新的时空相关检测模型MTAD-RD，该模型从模型架构和两阶段训练策略的角度出发，设计了增强的保留网络、特征融合模块和图注意力网络模块，以提取节点间的相关信息。通过对真实公共数据集的实验，MTAD-RD方法实现了90.97%的F1分数，优于现有的监督学习方法。

## 🔬 方法详解

**问题定义**：本文旨在解决无线传感器网络中异常检测面临的样本标签缺失、异常样本稀少及样本分布不平衡等问题。现有方法在提取时空相关特征时表现不足，影响了检测效果。

**核心思路**：MTAD-RD模型通过设计增强的保留网络和两阶段训练策略，利用对比学习和少样本学习的结合，提升特征提取能力并有效应对样本不足的问题。

**技术框架**：该模型的整体架构包括增强的保留网络（RetNet）、多粒度特征融合模块和图注意力网络模块，能够提取节点间的相关信息，并从时间序列数据中获取全局信息。训练过程分为两个阶段：首先进行对比学习以提取可迁移特征，然后使用基于缓存的样本采样器进行少样本学习。

**关键创新**：最重要的创新在于结合了对比学习和少样本学习的两阶段训练策略，解决了样本标签缺失和样本不平衡的问题，提升了模型的泛化能力。

**关键设计**：设计了特定的联合损失函数以联合训练双图判别网络，同时通过增强的网络结构和模块化设计提高了模型的推理效率。

## 📊 实验亮点

在真实公共数据集上的实验中，MTAD-RD方法实现了90.97%的F1分数，显著优于现有的监督学习方法，展示了其在异常检测任务中的优越性能和有效性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在智能城市、环境监测和工业自动化等领域。通过提高无线传感器网络的异常检测能力，可以有效保障系统的稳定性和安全性，促进智能系统的可靠运行。

## 📄 摘要（原文）

> Detecting anomalies in the data collected by WSNs can provide crucial evidence for assessing the reliability and stability of WSNs. Existing methods for WSN anomaly detection often face challenges such as the limited extraction of spatiotemporal correlation features, the absence of sample labels, few anomaly samples, and an imbalanced sample distribution. To address these issues, a spatiotemporal correlation detection model (MTAD-RD) considering both model architecture and a two-stage training strategy perspective is proposed. In terms of model structure design, the proposed MTAD-RD backbone network includes a retentive network (RetNet) enhanced by a cross-retention (CR) module, a multigranular feature fusion module, and a graph attention network module to extract internode correlation information. This proposed model can integrate the intermodal correlation features and spatial features of WSN neighbor nodes while extracting global information from time series data. Moreover, its serialized inference characteristic can remarkably reduce inference overhead. For model training, a two-stage training approach was designed. First, a contrastive learning proxy task was designed for time series data with graph structure information in WSNs, enabling the backbone network to learn transferable features from unlabeled data using unsupervised contrastive learning methods, thereby addressing the issue of missing sample labels in the dataset. Then, a caching-based sample sampler was designed to divide samples into few-shot and contrastive learning data. A specific joint loss function was developed to jointly train the dual-graph discriminator network to address the problem of sample imbalance effectively. In experiments carried out on real public datasets, the designed MTAD-RD anomaly detection method achieved an F1 score of 90.97%, outperforming existing supervised WSN anomaly detection methods.

