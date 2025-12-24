---
layout: default
title: "SAC-MIL: Spatial-Aware Correlated Multiple Instance Learning for Histopathology Whole Slide Image Classification"
---

# SAC-MIL: Spatial-Aware Correlated Multiple Instance Learning for Histopathology Whole Slide Image Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03973" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03973v1</a>
  <a href="https://arxiv.org/pdf/2509.03973.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03973v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03973v1', 'SAC-MIL: Spatial-Aware Correlated Multiple Instance Learning for Histopathology Whole Slide Image Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Bai, Zitong Yu, Haowen Tian, Xijing Wang, Shuo Yan, Lin Wang, Honglin Li, Xitong Ling, Bo Zhang, Zheng Zhang, Wufan Wang, Hui Gao, Xiangyang Gong, Wendong Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**提出空间感知相关多示例学习(SAC-MIL)用于病理全切片图像分类。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `全切片图像分类` `多示例学习` `空间感知` `位置编码` `实例相关性`

## 📋 核心要点

1. 现有WSI分类方法难以有效利用实例间的空间关系，且基于Transformer的方法部署复杂。
2. SAC-MIL通过位置编码模块嵌入空间信息，并使用SAC块进行高效的全实例相关性建模。
3. 实验表明，SAC-MIL在多个数据集上取得了SOTA性能，且易于部署，具有实际应用价值。

## 📝 摘要（中文）

本文提出了一种空间感知相关多示例学习(SAC-MIL)方法，用于执行全切片图像(WSI)分类。SAC-MIL包含一个位置编码模块和一个SAC块，分别用于编码位置信息和执行全示例相关性计算。位置编码模块利用切片内的实例坐标来编码空间关系，而非输入WSI序列中的实例索引，从而能够处理训练和测试序列长度不同的外推问题。SAC块是一种基于MLP的方法，以相对于序列长度的线性时间复杂度执行全实例相关性。由于MLP结构简单，易于部署，无需像基于Transformer的方法那样使用自定义CUDA内核。SAC-MIL在CAMELYON-16、TCGA-LUNG和TCGA-BRAC数据集上取得了最先进的性能。代码将在接收后发布。

## 🔬 方法详解

**问题定义**：全切片图像(WSI)分类旨在根据病理切片图像预测患者的疾病状态。现有方法，特别是基于多示例学习(MIL)的方法，通常忽略了实例之间的空间关系，或者使用复杂的Transformer结构，导致计算成本高昂且部署困难。因此，如何有效利用实例间的空间信息，并降低计算复杂度，是WSI分类面临的关键问题。

**核心思路**：SAC-MIL的核心思路是利用实例在WSI中的坐标信息来编码空间关系，并设计一个高效的模块来建模实例之间的相关性。通过位置编码模块，将实例的位置信息嵌入到特征中，从而使模型能够感知实例的空间分布。SAC块则通过MLP结构，在保证线性时间复杂度的前提下，实现全实例相关性建模。

**技术框架**：SAC-MIL的整体框架包括以下几个主要模块：1) 特征提取模块：用于从WSI的各个实例中提取视觉特征。2) 位置编码模块：利用实例的坐标信息，生成位置编码向量，并将其与视觉特征融合。3) SAC块：通过MLP结构，建模所有实例之间的相关性，生成聚合特征。4) 分类器：基于聚合特征，预测WSI的类别。

**关键创新**：SAC-MIL的关键创新在于：1) 提出了位置编码模块，能够有效编码实例的空间信息，并解决训练和测试序列长度不同的外推问题。2) 设计了SAC块，通过MLP结构，实现了线性时间复杂度的全实例相关性建模，避免了Transformer结构的复杂性。

**关键设计**：位置编码模块使用正弦和余弦函数来生成位置编码向量，并将其与视觉特征进行拼接。SAC块包含多个MLP层，用于建模实例之间的相关性。损失函数采用标准的交叉熵损失函数。具体的网络结构和参数设置需要在论文的实验部分查找。

## 📊 实验亮点

SAC-MIL在CAMELYON-16、TCGA-LUNG和TCGA-BRAC三个公开数据集上取得了state-of-the-art的性能。具体提升幅度未知，需要在论文中查找实验结果的详细数据，包括与其他基线方法的对比。

## 🎯 应用场景

SAC-MIL可应用于多种病理图像分析任务，如癌症诊断、预后预测和治疗方案选择。该方法能够有效利用病理切片中的空间信息，提高诊断准确率，辅助医生进行更精准的决策。此外，SAC-MIL的低计算复杂度使其更易于部署到实际临床环境中，具有广阔的应用前景。

## 📄 摘要（原文）

> We propose Spatial-Aware Correlated Multiple Instance Learning (SAC-MIL) for performing WSI classification. SAC-MIL consists of a positional encoding module to encode position information and a SAC block to perform full instance correlations. The positional encoding module utilizes the instance coordinates within the slide to encode the spatial relationships instead of the instance index in the input WSI sequence. The positional encoding module can also handle the length extrapolation issue where the training and testing sequences have different lengths. The SAC block is an MLP-based method that performs full instance correlation in linear time complexity with respect to the sequence length. Due to the simple structure of MLP, it is easy to deploy since it does not require custom CUDA kernels, compared to Transformer-based methods for WSI classification. SAC-MIL has achieved state-of-the-art performance on the CAMELYON-16, TCGA-LUNG, and TCGA-BRAC datasets. The code will be released upon acceptance.

