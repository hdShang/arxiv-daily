---
layout: default
title: "Adapting SAM with Dynamic Similarity Graphs for Few-Shot Parameter-Efficient Small Dense Object Detection: A Case Study of Chickpea Pods in Field Conditions"
---

# Adapting SAM with Dynamic Similarity Graphs for Few-Shot Parameter-Efficient Small Dense Object Detection: A Case Study of Chickpea Pods in Field Conditions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25805" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25805v1</a>
  <a href="https://arxiv.org/pdf/2509.25805.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25805v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25805v1', 'Adapting SAM with Dynamic Similarity Graphs for Few-Shot Parameter-Efficient Small Dense Object Detection: A Case Study of Chickpea Pods in Field Conditions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xintong Jiang, Yixue Liu, Mohamed Debbagh, Yu Tian, Valerio Hoyos-Villegas, Viacheslav Adamchuk, Shangpeng Sun

**分类**: cs.CV

**发布日期**: 2025-09-30

**备注**: 23 pages, 11 figures, 4 tables

---

## 💡 一句话要点

**提出基于动态相似图的SAM自适应方法，用于少样本密集小目标检测，以田间鹰嘴豆荚为例。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少样本学习` `参数高效微调` `动态相似图` `目标检测` `农业视觉` `SAM自适应` `密集小目标`

## 📋 核心要点

1. 农业场景下小目标密集检测面临数据稀缺和环境复杂双重挑战，现有方法难以兼顾精度与效率。
2. 论文提出动态相似图自适应（DSGA）模块，结合LoRA，在少量样本下有效提升SAM的分割性能。
3. 实验表明，该方法在鹰嘴豆荚数据集上显著优于传统微调方法，结构度量提升17.31%，自适应F度量提升62.36%。

## 📝 摘要（中文）

本研究针对农业计算机视觉任务中，基础模型在有限训练数据和复杂田间条件下进行参数高效微调的挑战，提出了一种基于动态相似性的图自适应（DSGA）模块，用于在极端数据约束下自适应分割一切模型（SAM），以实现复杂农业环境中密集小目标的前景和实例精确分割。DSGA通过可学习的多项式衰减初始化权重排序机制构建动态相似图，并进行自适应局部特征聚合，仅用400万可训练参数（占原始SAM的4.26%）就建立了鲁棒的空间和动态相似性表示。将这种基于图的特征自适应与低秩自适应（LoRA）集成，创建了一个互补的优化框架，有效捕获图像嵌入中的局部和全局依赖关系，同时保持模型稳定性和参数效率。在具有挑战性的鹰嘴豆荚数据集上的实验结果表明，DSGA与LoRA在2、4、8和10个样本下，在多个指标上均优于基线SAM微调，并且随着样本数量的增加，性能逐渐提高。定量指标显示，结构度量提高了17.31%，自适应F度量提高了62.36%。全面的消融研究和通过Grad-CAM和t-SNE进行的可视化分析验证了该框架在特征区分方面的有效性。该自适应方法展示了自动化农业监测应用的实用性，在具有10到120个豆荚的图像中，实现了准确的豆荚计数，调整后的R平方值为0.8987。

## 🔬 方法详解

**问题定义**：论文旨在解决农业环境中，特别是田间条件下，对密集小目标（如鹰嘴豆荚）进行精确分割和计数的问题。现有方法在数据量有限的情况下，难以充分利用大型预训练模型（如SAM）的潜力，且微调过程参数量大，效率低，容易过拟合。

**核心思路**：论文的核心思路是利用动态相似图来捕捉图像中目标之间的空间和动态关系，并结合低秩自适应（LoRA）方法，实现对SAM模型的参数高效微调。通过动态相似图，模型能够更好地理解目标之间的上下文信息，从而提高分割精度。LoRA则保证了在少量数据下，模型能够稳定训练，避免过拟合。

**技术框架**：整体框架包括以下几个主要模块：1) SAM模型：作为基础分割模型；2) 动态相似图自适应（DSGA）模块：用于构建动态相似图并进行特征自适应；3) 低秩自适应（LoRA）：用于参数高效微调；4) 分割头：用于最终的分割结果预测。流程上，首先使用SAM提取图像特征，然后通过DSGA模块构建动态相似图并进行特征增强，接着使用LoRA对SAM进行微调，最后通过分割头输出分割结果。

**关键创新**：论文最重要的技术创新点在于提出了动态相似图自适应（DSGA）模块。该模块通过可学习的多项式衰减初始化权重排序机制，能够动态地捕捉图像中目标之间的相似性关系，并根据这些关系进行特征聚合。与传统的静态图或注意力机制相比，DSGA能够更灵活地适应不同场景下的目标分布，从而提高分割精度。

**关键设计**：DSGA模块的关键设计包括：1) 可学习的多项式衰减初始化权重：用于对不同节点之间的相似性进行加权，使得模型能够更加关注重要的相似性关系；2) 自适应局部特征聚合：根据动态相似图，对每个节点的局部特征进行聚合，从而增强特征的表达能力；3) LoRA的秩设置为较小的值，以保证参数效率和模型稳定性。损失函数采用常用的分割损失函数，如Dice Loss或Cross-Entropy Loss。

## 📊 实验亮点

实验结果表明，提出的DSGA与LoRA结合的方法在鹰嘴豆荚数据集上取得了显著的性能提升。与基线SAM微调相比，结构度量（Structure-measure）提高了17.31%，自适应F度量（adaptive F-measure）提高了62.36%。此外，消融实验验证了DSGA模块和LoRA的有效性。在不同样本数量下，该方法均优于其他对比方法，表明其具有良好的泛化能力。

## 🎯 应用场景

该研究成果可应用于精准农业领域，例如作物生长监测、产量预测、病虫害检测等。通过自动化识别和计数农作物目标，可以帮助农民更好地管理农田，提高生产效率，减少资源浪费。此外，该方法还可以扩展到其他小目标密集检测场景，如医学图像分析、遥感图像处理等。

## 📄 摘要（原文）

> Parameter-Efficient Fine-Tuning (PEFT) of foundation models for agricultural computer vision tasks remains challenging due to limited training data and complex field conditions. This study introduces a Dynamic Similarity-based Graph Adaptation (DSGA) module to adapt the Segment Anything Model (SAM) under extreme data constraints for precise foreground and instance segmentation of small dense objects in complex agricultural environments. Through dynamic similarity graph construction with a learnable polynomial decay-initialized weight ranking mechanism and adaptive local feature aggregation, DSGA establishes robust spatial and dynamic similarity representation with only 4.00M trainable parameters, which is 4.26% of the original SAM. Integrating this graph-based feature adaptation with Low-Rank Adaptation (LoRA) creates a complementary optimization framework that effectively captures both local and global dependencies in image embeddings while preserving model stability and parameter efficiency. Experimental results on a challenging chickpea pod dataset demonstrated that DSGA with LoRA achieved superior performance across multiple metrics evaluated under 2, 4, 8 and 10 shots, with progressive performance gains as shot count increased. Quantitative metrics showed a 17.31% improvement in Structure-measure and a 62.36% gain in adaptive F-measure compared to the baseline SAM fine-tuning. Comprehensive ablation studies and visualization analyses through Grad-CAM and t-SNE validated the framework's effectiveness in feature discrimination. The proposed adaptation demonstrated practical utility for automated agricultural monitoring applications, achieving accurate pod-counting with an adjusted R-squared of 0.8987 for images with 10 to 120 pods under challenging field conditions.

