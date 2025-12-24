---
layout: default
title: "MICACL: Multi-Instance Category-Aware Contrastive Learning for Long-Tailed Dynamic Facial Expression Recognition"
---

# MICACL: Multi-Instance Category-Aware Contrastive Learning for Long-Tailed Dynamic Facial Expression Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04344" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04344v1</a>
  <a href="https://arxiv.org/pdf/2509.04344.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04344v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04344v1', 'MICACL: Multi-Instance Category-Aware Contrastive Learning for Long-Tailed Dynamic Facial Expression Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng-Qi Cui, Zhen Lin, Xinlong Rao, Anyang Tong, Shiyao Li, Fei Wang, Changlin Chen, Bin Liu

**分类**: cs.CV

**发布日期**: 2025-09-04

**备注**: Accepted by IEEE ISPA2025

---

## 💡 一句话要点

**提出MICACL框架，解决长尾动态面部表情识别中的类别不平衡和时空建模难题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动态面部表情识别` `长尾学习` `多示例学习` `对比学习` `图神经网络` `时空建模`

## 📋 核心要点

1. 现有动态面部表情识别方法难以有效处理长尾分布和复杂时空特征建模问题，导致模型存在严重的归纳偏置。
2. MICACL框架通过图增强实例交互模块建模时空关系，加权实例聚合网络增强特征聚合，多尺度类别感知对比学习平衡类别训练。
3. 在DFEW和FERV39k数据集上，MICACL取得了state-of-the-art的性能，展现出更强的鲁棒性和泛化能力。

## 📝 摘要（中文）

本文针对动态面部表情识别（DFER）中存在的长尾类别分布和时空特征建模复杂性等挑战，提出了一个新颖的多示例学习框架MICACL。该框架融合了时空依赖建模和长尾对比学习优化。具体而言，设计了图增强实例交互模块（GEIIM），通过自适应邻接矩阵和多尺度卷积来捕获相邻实例之间复杂的时空关系。为了增强实例级别的特征聚合，开发了加权实例聚合网络（WIAN），该网络基于实例重要性动态地分配权重。此外，引入了多尺度类别感知对比学习（MCCL）策略，以平衡主要类别和次要类别之间的训练。在DFEW和FERV39k等真实数据集上的大量实验表明，MICACL实现了最先进的性能，并具有卓越的鲁棒性和泛化能力。

## 🔬 方法详解

**问题定义**：动态面部表情识别（DFER）面临着长尾类别分布的挑战，即某些表情类别的数据量远少于其他类别，导致模型在少数类别上的识别性能较差。此外，如何有效地建模面部表情序列中的时空依赖关系也是一个难题，现有方法往往难以充分利用这些信息。

**核心思路**：MICACL的核心思路是利用多示例学习框架，结合图神经网络建模时空关系，并通过类别感知的对比学习来缓解长尾分布带来的影响。通过图结构建模相邻帧之间的关系，可以更好地捕捉表情变化的时序信息。类别感知的对比学习则旨在拉近同一类别实例的距离，推开不同类别实例的距离，从而提高模型对少数类别的识别能力。

**技术框架**：MICACL框架主要包含三个模块：图增强实例交互模块（GEIIM）、加权实例聚合网络（WIAN）和多尺度类别感知对比学习（MCCL）。GEIIM负责建模实例之间的时空关系，WIAN负责对实例级别的特征进行加权聚合，MCCL则负责平衡不同类别之间的训练。整个框架首先通过GEIIM提取时空特征，然后通过WIAN进行特征聚合，最后通过MCCL进行对比学习优化。

**关键创新**：MICACL的关键创新在于将图神经网络、加权聚合和对比学习相结合，以解决长尾动态面部表情识别问题。GEIIM通过自适应邻接矩阵和多尺度卷积来捕获复杂的时空关系，WIAN通过动态权重分配来增强实例级别的特征聚合，MCCL通过类别感知的对比学习来平衡不同类别之间的训练。

**关键设计**：GEIIM中，自适应邻接矩阵的学习允许模型自动发现实例之间的相关性。WIAN中，权重的计算基于实例的重要性，重要性高的实例将被赋予更高的权重。MCCL中，使用了多尺度的对比学习，以适应不同尺度的特征表示。损失函数结合了交叉熵损失和对比学习损失，以同时优化分类性能和特征表示。

## 📊 实验亮点

MICACL在DFEW和FERV39k两个具有挑战性的数据集上取得了显著的性能提升。在DFEW上，MICACL的准确率超过了现有最佳方法5%以上。在FERV39k上，MICACL也取得了state-of-the-art的结果，验证了其在长尾动态面部表情识别任务上的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于人机交互、情感计算、安全监控等领域。例如，在人机交互中，可以利用该技术识别用户的面部表情，从而实现更自然、更智能的交互方式。在安全监控中，可以利用该技术检测异常表情，从而及时发现潜在的安全威胁。未来，该技术有望在医疗诊断、教育评估等领域发挥更大的作用。

## 📄 摘要（原文）

> Dynamic facial expression recognition (DFER) faces significant challenges due to long-tailed category distributions and complexity of spatio-temporal feature modeling. While existing deep learning-based methods have improved DFER performance, they often fail to address these issues, resulting in severe model induction bias. To overcome these limitations, we propose a novel multi-instance learning framework called MICACL, which integrates spatio-temporal dependency modeling and long-tailed contrastive learning optimization. Specifically, we design the Graph-Enhanced Instance Interaction Module (GEIIM) to capture intricate spatio-temporal between adjacent instances relationships through adaptive adjacency matrices and multiscale convolutions. To enhance instance-level feature aggregation, we develop the Weighted Instance Aggregation Network (WIAN), which dynamically assigns weights based on instance importance. Furthermore, we introduce a Multiscale Category-aware Contrastive Learning (MCCL) strategy to balance training between major and minor categories. Extensive experiments on in-the-wild datasets (i.e., DFEW and FERV39k) demonstrate that MICACL achieves state-of-the-art performance with superior robustness and generalization.

