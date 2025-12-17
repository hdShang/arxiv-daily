---
layout: default
title: DMVFC: Deep Learning Based Functionally Consistent Tractography Fiber Clustering Using Multimodal Diffusion MRI and Functional MRI
---

# DMVFC: Deep Learning Based Functionally Consistent Tractography Fiber Clustering Using Multimodal Diffusion MRI and Functional MRI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.24770" class="toolbar-btn" target="_blank">📄 arXiv: 2510.24770v2</a>
  <a href="https://arxiv.org/pdf/2510.24770.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.24770v2" onclick="toggleFavorite(this, '2510.24770v2', 'DMVFC: Deep Learning Based Functionally Consistent Tractography Fiber Clustering Using Multimodal Diffusion MRI and Functional MRI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bocheng Guo, Jin Wang, Yijie Li, Junyi Wang, Mingyu Gao, Puming Feng, Yuqian Chen, Jarrett Rushmore, Nikos Makris, Yogesh Rathi, Lauren J O'Donnell, Fan Zhang

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-10-24 (更新: 2025-11-03)

**备注**: 14 pages

---

## 💡 一句话要点

**提出DMVFC，利用多模态MRI数据进行功能一致的纤维束聚类**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `纤维束聚类` `扩散MRI` `功能MRI` `多模态融合` `深度学习` `白质分割` `多视图学习`

## 📋 核心要点

1. 传统纤维束聚类主要依赖几何特征，忽略了功能和微观结构信息，导致功能一致性较差。
2. DMVFC框架通过多视图预训练和协同微调，整合dMRI和fMRI数据，提取纤维的几何、微观结构和功能特征。
3. 实验表明，DMVFC在功能一致的白质分割方面优于现有方法，提升了纤维束聚类的性能。

## 📝 摘要（中文）

本研究提出了一种基于深度学习的纤维束聚类框架，即深度多视图纤维聚类（DMVFC），它利用多模态扩散MRI（dMRI）和功能MRI（fMRI）数据，实现功能一致的白质分割。现有的纤维聚类策略主要依赖纤维的几何特征，忽略了纤维束的功能和微观结构信息。DMVFC能够有效地整合白质纤维的几何和微观结构特征，以及沿纤维束的fMRI BOLD信号。DMVFC包括两个主要组成部分：(1) 一个多视图预训练模块，用于分别从纤维几何、微观结构测量和功能信号等信息源计算嵌入特征；(2) 一个协同微调模块，用于同时优化嵌入的差异。实验结果表明，与两种最先进的纤维聚类方法相比，DMVFC在实现功能上有意义且一致的白质分割方面表现出优越的性能。

## 🔬 方法详解

**问题定义**：现有的纤维束聚类方法主要依赖于纤维的几何形状，忽略了纤维束的功能信息和微观结构信息。这导致聚类结果在功能上的一致性较差，无法充分利用多模态MRI数据蕴含的丰富信息。因此，如何有效地整合dMRI和fMRI数据，实现功能一致的白质分割是一个关键问题。

**核心思路**：DMVFC的核心思路是利用深度学习框架，通过多视图学习的方式，分别提取纤维的几何特征、微观结构特征和功能特征，然后将这些特征进行融合，从而实现功能一致的纤维束聚类。这种方法能够充分利用多模态MRI数据的信息，提高聚类结果的功能一致性。

**技术框架**：DMVFC框架主要包括两个模块：多视图预训练模块和协同微调模块。首先，多视图预训练模块分别从纤维几何、微观结构测量和功能信号等信息源计算嵌入特征。然后，协同微调模块同时优化这些嵌入的差异，从而实现多模态信息的融合。整个框架通过深度学习模型进行端到端的训练。

**关键创新**：DMVFC的关键创新在于提出了一个多视图学习框架，能够有效地整合dMRI和fMRI数据，实现功能一致的纤维束聚类。与传统的基于几何特征的聚类方法相比，DMVFC能够更好地利用多模态MRI数据的信息，提高聚类结果的功能一致性。此外，协同微调模块的设计也能够有效地优化不同模态之间的特征差异。

**关键设计**：在多视图预训练模块中，可以使用不同的深度学习模型来提取不同模态的特征，例如，可以使用图神经网络来提取纤维的几何特征，使用卷积神经网络来提取fMRI信号的特征。在协同微调模块中，可以使用对比学习等方法来优化不同模态之间的特征差异。损失函数的设计需要考虑不同模态之间的权重，以及聚类结果的功能一致性。

## 📊 实验亮点

实验结果表明，DMVFC在功能一致的白质分割方面优于两种最先进的纤维聚类方法。具体来说，DMVFC能够产生更具有功能意义和一致性的白质分割结果，这表明DMVFC能够有效地整合dMRI和fMRI数据，提高纤维束聚类的性能。虽然论文中没有给出具体的性能数据和提升幅度，但结论明确表明DMVFC的优越性。

## 🎯 应用场景

DMVFC可应用于研究健康和疾病状态下大脑的结构连接，例如，可以用于研究神经退行性疾病（如阿尔茨海默病）中白质纤维束的变化，或者用于研究脑损伤后白质纤维束的重塑。该方法还可以用于指导神经外科手术，提高手术的精确性和安全性。此外，DMVFC还可以促进我们对大脑功能的理解，为开发新的神经疾病治疗方法提供依据。

## 📄 摘要（原文）

> Tractography fiber clustering using diffusion MRI (dMRI) is a crucial method for white matter (WM) parcellation to enable analysis of brains structural connectivity in health and disease. Current fiber clustering strategies primarily use the fiber geometric characteristics (i.e., the spatial trajectories) to group similar fibers into clusters, while neglecting the functional and microstructural information of the fiber tracts. There is increasing evidence that neural activity in the WM can be measured using functional MRI (fMRI), providing potentially valuable multimodal information for fiber clustering to enhance its functional coherence. Furthermore, microstructural features such as fractional anisotropy (FA) can be computed from dMRI as additional information to ensure the anatomical coherence of the clusters. In this paper, we develop a novel deep learning fiber clustering framework, namely Deep Multi-view Fiber Clustering (DMVFC), which uses joint multi-modal dMRI and fMRI data to enable functionally consistent WM parcellation. DMVFC can effectively integrate the geometric and microstructural characteristics of the WM fibers with the fMRI BOLD signals along the fiber tracts. DMVFC includes two major components: (1) a multi-view pretraining module to compute embedding features from each source of information separately, including fiber geometry, microstructure measures, and functional signals, and (2) a collaborative fine-tuning module to simultaneously refine the differences of embeddings. In the experiments, we compare DMVFC with two state-of-the-art fiber clustering methods and demonstrate superior performance in achieving functionally meaningful and consistent WM parcellation results.

