---
layout: default
title: A versatile foundation model for cine cardiac magnetic resonance image analysis tasks
---

# A versatile foundation model for cine cardiac magnetic resonance image analysis tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00679" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00679v2</a>
  <a href="https://arxiv.org/pdf/2506.00679.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00679v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00679v2', 'A versatile foundation model for cine cardiac magnetic resonance image analysis tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunguan Fu, Wenjia Bai, Weixi Yi, Charlotte Manisty, Anish N Bhuva, Thomas A Treibel, James C Moon, Matthew J Clarkson, Rhodri Huw Davies, Yipeng Hu

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-05-31 (更新: 2025-08-31)

**🔗 代码/项目**: [GITHUB](https://github.com/mathpluscode/CineMA)

---

## 💡 一句话要点

**提出CineMA模型以解决心脏磁共振图像分析问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心脏磁共振` `图像分析` `卷积神经网络` `变换器` `多任务学习` `临床应用` `模型公平性`

## 📋 核心要点

1. 现有的心脏磁共振图像分析方法在准确性和适应性方面存在不足，难以满足临床需求。
2. CineMA模型采用多视角卷积-变换器掩码自编码器架构，旨在提高心脏图像分析的效率和准确性。
3. 实验结果表明，CineMA在心室边界描绘和疾病检测中均优于传统CNN，且在不同人群中表现一致。

## 📝 摘要（中文）

本文提出了一种多功能基础模型CineMA，能够执行多种临床相关的图像分析任务，包括分割、标志定位、诊断和预后评估。该模型在74916名受试者的1500万幅影像上进行训练，并在超过4500幅来自八个独立数据集的图像上进行了验证。CineMA在心室边界描绘和射血分数估计等任务中，表现优于传统卷积神经网络（CNN），即使在仅使用一半微调数据的情况下，性能提升依然显著。此外，CineMA还能够检测系统性疾病（如糖尿病、高血压和癌症）中的心脏变化，并预测死亡率。最后，研究还评估了模型的公平性，显示其在不同人口子群体中的一致性表现。

## 🔬 方法详解

**问题定义**：本文旨在解决心脏磁共振图像分析中的准确性和适应性不足的问题。现有方法多依赖于传统卷积神经网络（CNN），在处理复杂的临床任务时表现不佳，尤其是在多样化人群中的应用。

**核心思路**：CineMA模型结合了卷积神经网络和变换器的优势，采用多视角卷积-变换器掩码自编码器架构，以提高模型在多种图像分析任务中的表现。该设计旨在增强模型的学习效率和适应性，使其能够处理更复杂的临床任务。

**技术框架**：CineMA的整体架构包括数据预处理、特征提取、任务特定的输出层等多个模块。模型首先通过多视角卷积层提取图像特征，然后通过变换器模块进行特征融合，最后输出分割、定位和诊断结果。

**关键创新**：CineMA的主要创新在于其结合了卷积神经网络和变换器的特性，形成了一种新的图像分析框架。这种设计使得模型在处理复杂的心脏图像时，能够更好地捕捉空间和时间特征，从而显著提高分析准确性。

**关键设计**：模型的训练使用了1500万幅影像，损失函数采用了多任务学习策略，以平衡不同任务的学习。此外，模型在微调阶段表现出良好的鲁棒性，即使在使用一半数据的情况下，依然保持了高性能。

## 📊 实验亮点

CineMA在心室边界描绘和射血分数估计中表现优于传统CNN，且在疾病检测中也显示出更高的准确性。模型在多个独立数据集上的验证结果表明，其在不同人群中的一致性表现，进一步增强了其临床应用的可靠性。

## 🎯 应用场景

CineMA模型在心脏磁共振图像分析中的应用潜力巨大，能够支持临床工作流程，提升心血管疾病的诊断和预后评估效率。未来，该模型还可扩展到其他医学影像分析领域，推动个性化医疗的发展。

## 📄 摘要（原文）

> Here we present a versatile foundation model that can perform a range of clinically-relevant image analysis tasks, including segmentation, landmark localisation, diagnosis, and prognostication. A multi-view convolution-transformer masked autoencoder, named as CineMA, was trained on 15 million cine images from 74,916 subjects. The model was validated on multiple image analysis tasks and compared to existing models on >4,500 images from eight independent datasets with diverse population characteristics, representing the largest benchmark study for cine CMR so far. CineMA consistently outperformed conventional convolutional neural networks (CNNs) in delineating ventricular boundaries and estimating ejection fraction, a key measure of cardiac function. The improved performance was preserved, even when the model only used half of fine-tuning data. CineMA also surpassed CNNs in disease detection and matched their performance in long-axis function measurement. Interestingly, we found that CineMA can also detect cardiac changes in systemic diseases, such as diabetes, hypertension and cancer, and can also predict mortality. Finally, we assessed model fairness and demonstrated consistent model performance across demographic subgroups. These findings highlight CineMA's accuracy, learning efficiency, adaptability, and fairness, underscoring its potential as a foundation model for automated cardiac image analysis to support clinical workflow and cardiovascular research. All training and inference code and models are made publicly available at https://github.com/mathpluscode/CineMA.

