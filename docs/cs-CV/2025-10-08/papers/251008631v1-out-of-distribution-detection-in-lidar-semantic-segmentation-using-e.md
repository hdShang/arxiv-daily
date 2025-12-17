---
layout: default
title: Out-of-Distribution Detection in LiDAR Semantic Segmentation Using Epistemic Uncertainty from Hierarchical GMMs
---

# Out-of-Distribution Detection in LiDAR Semantic Segmentation Using Epistemic Uncertainty from Hierarchical GMMs

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08631" target="_blank" class="toolbar-btn">arXiv: 2510.08631v1</a>
    <a href="https://arxiv.org/pdf/2510.08631.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08631v1" 
            onclick="toggleFavorite(this, '2510.08631v1', 'Out-of-Distribution Detection in LiDAR Semantic Segmentation Using Epistemic Uncertainty from Hierarchical GMMs')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hanieh Shojaei Miandashti, Claus Brenner

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**提出基于分层GMM不确定性的LiDAR语义分割OOD检测方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `LiDAR语义分割` `域外检测` `认知不确定性` `高斯混合模型` `分层贝叶斯` `无监督学习`

## 📋 核心要点

1. 现有OOD检测方法常将认知不确定性和偶然不确定性混淆，导致将分布内的模糊区域误判为OOD。
2. 论文提出一种无监督OOD检测方法，利用分层贝叶斯建模GMM参数得到的认知不确定性。
3. 实验表明，该方法在SemanticKITTI数据集上显著优于现有方法，在AUROC、AUPRC和FPR95指标上均有提升。

## 📝 摘要（中文）

本文提出了一种针对LiDAR点云语义分割中域外(OOD)对象检测的无监督方法。该方法旨在解决将训练中未遇到的未知对象错误分类为已知类别的问题。与依赖辅助OOD数据集的有监督方法不同，本文方法无需额外数据或训练，利用深度神经网络特征空间中高斯混合模型(GMM)参数的分层贝叶斯建模导出的认知不确定性进行OOD检测。实验结果表明，在SemanticKITTI数据集上，该方法优于现有的基于不确定性的方法，AUROC提升18%，AUPRC提升22%，FPR95从76%降低到40%。

## 🔬 方法详解

**问题定义**：论文旨在解决LiDAR点云语义分割中，模型将训练集中未见过的OOD对象错误分类为已知类别的问题。现有方法，特别是基于预测熵的方法，常常无法区分认知不确定性（模型对自身的不确定性）和偶然不确定性（数据本身的不确定性），导致将分布内的模糊区域错误地识别为OOD。

**核心思路**：论文的核心思路是利用认知不确定性来区分OOD对象。通过对深度神经网络提取的特征空间中的高斯混合模型（GMM）参数进行分层贝叶斯建模，可以更准确地估计模型对特定区域的不确定性，从而更好地区分OOD对象和分布内的模糊区域。这种方法避免了对额外OOD数据的依赖，实现了无监督的OOD检测。

**技术框架**：整体框架包括以下几个主要步骤：1) 使用深度神经网络提取LiDAR点云的特征；2) 在特征空间中拟合高斯混合模型（GMM）；3) 对GMM的参数进行分层贝叶斯建模，得到参数的后验分布；4) 利用参数的后验分布计算认知不确定性；5) 使用认知不确定性作为OOD检测的指标。

**关键创新**：最重要的技术创新点在于使用分层贝叶斯建模来估计GMM参数的认知不确定性。与直接使用预测熵的方法相比，该方法能够更准确地捕捉模型的不确定性，从而更好地区分OOD对象和分布内的模糊区域。此外，该方法是无监督的，不需要额外的OOD数据进行训练。

**关键设计**：关键设计包括：1) 使用深度神经网络（具体结构未明确说明，但应为现有的LiDAR语义分割网络）提取特征；2) 选择合适的高斯混合模型（GMM）的组件数量；3) 设计分层贝叶斯模型的先验分布，以反映对GMM参数的先验知识；4) 使用合适的推断方法（如变分推断或马尔可夫链蒙特卡洛方法）来估计GMM参数的后验分布；5) 选择合适的认知不确定性度量，例如后验分布的方差或熵。

## 📊 实验亮点

实验结果表明，该方法在SemanticKITTI数据集上显著优于现有的基于不确定性的方法。具体而言，AUROC指标提升了18%，AUPRC指标提升了22%，FPR95指标从76%降低到40%。这些结果表明，该方法能够更准确地检测OOD对象，并减少误报率。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、智能交通等领域。通过检测LiDAR数据中的OOD对象，可以提高系统的安全性和可靠性，避免因错误识别未知物体而导致的事故。例如，在自动驾驶中，可以识别出道路上的异常物体，如倒地的树木或未知的障碍物，从而及时采取避让措施。

## 📄 摘要（原文）

> In addition to accurate scene understanding through precise semantic segmentation of LiDAR point clouds, detecting out-of-distribution (OOD) objects, instances not encountered during training, is essential to prevent the incorrect assignment of unknown objects to known classes. While supervised OOD detection methods depend on auxiliary OOD datasets, unsupervised methods avoid this requirement but typically rely on predictive entropy, the entropy of the predictive distribution obtained by averaging over an ensemble or multiple posterior weight samples. However, these methods often conflate epistemic (model) and aleatoric (data) uncertainties, misclassifying ambiguous in distribution regions as OOD. To address this issue, we present an unsupervised OOD detection approach that employs epistemic uncertainty derived from hierarchical Bayesian modeling of Gaussian Mixture Model (GMM) parameters in the feature space of a deep neural network. Without requiring auxiliary data or additional training stages, our approach outperforms existing uncertainty-based methods on the SemanticKITTI dataset, achieving an 18\% improvement in AUROC, 22\% increase in AUPRC, and 36\% reduction in FPR95 (from 76\% to 40\%), compared to the predictive entropy approach used in prior works.

