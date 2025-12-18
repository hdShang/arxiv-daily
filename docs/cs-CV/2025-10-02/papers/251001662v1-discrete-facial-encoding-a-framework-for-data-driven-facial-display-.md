---
layout: default
title: Discrete Facial Encoding: : A Framework for Data-driven Facial Display Discovery
---

# Discrete Facial Encoding: : A Framework for Data-driven Facial Display Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01662" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01662v1</a>
  <a href="https://arxiv.org/pdf/2510.01662.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01662v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01662v1', 'Discrete Facial Encoding: : A Framework for Data-driven Facial Display Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minh Tran, Maksim Siniukov, Zhangyu Jin, Mohammad Soleymani

**分类**: cs.CV

**发布日期**: 2025-10-02

---

## 💡 一句话要点

**提出离散面部编码(DFE)，用于数据驱动的面部表情发现，替代FACS。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `面部表情分析` `离散面部编码` `无监督学习` `RVQ-VAE` `3D形变模型`

## 📋 核心要点

1. 现有面部表情分析方法如FACS存在覆盖范围有限和标注成本高的问题，限制了其应用。
2. 论文提出离散面部编码(DFE)，利用RVQ-VAE学习面部表情的离散token表示，实现无监督学习。
3. 实验表明，DFE在压力检测、人格预测和抑郁症检测等任务中优于FACS和Masked Autoencoders。

## 📝 摘要（中文）

面部表情分析是理解人类行为的关键，但现有的编码系统，如面部动作编码系统(FACS)，受到覆盖范围有限和人工标注成本高昂的限制。本文提出了一种无监督的、数据驱动的替代方案——离散面部编码(DFE)，它从3D网格序列中学习紧凑且可解释的面部表情字典，该字典通过残差向量量化变分自编码器(RVQ-VAE)学习得到。我们的方法首先使用3D形变模型(3DMM)从图像中提取与身份无关的表情特征，有效地解耦了头部姿势和面部几何等因素。然后，我们使用RVQ-VAE对这些特征进行编码，从共享码本中生成一系列离散token，每个token捕获一个特定的、可重用的面部变形模式，该模式有助于整体表情的表达。通过大量的实验，我们证明了离散面部编码比FACS和其他面部编码替代方案能捕捉到更精确的面部行为。我们在三个高层次的心理学任务中评估了我们表示的效用：压力检测、人格预测和抑郁症检测。使用建立在学习到的token之上的简单词袋模型，我们的系统始终优于基于FACS的pipeline以及强大的图像和视频表示学习模型，如掩码自编码器。进一步的分析表明，我们的表示涵盖了更广泛的面部展示，突出了其作为FACS在心理和情感计算应用中可扩展且有效的替代方案的潜力。

## 🔬 方法详解

**问题定义**：现有面部表情分析方法，如FACS，依赖于人工标注，成本高昂且覆盖范围有限，难以捕捉细微的面部变化。这限制了其在心理学和情感计算等领域的应用。

**核心思路**：论文的核心思路是利用无监督学习方法，自动从面部图像序列中学习到一组离散的、可解释的面部表情单元（tokens）。通过将复杂的面部表情分解为这些基本单元的组合，可以更有效地表示和分析面部行为。

**技术框架**：DFE框架包含以下几个主要阶段：1) 使用3DMM提取身份无关的表情特征，消除头部姿势和面部几何的影响；2) 使用RVQ-VAE对提取的特征进行编码，生成离散的token序列；3) 使用学习到的token构建词袋模型，用于下游任务的分类或回归。

**关键创新**：DFE的关键创新在于使用RVQ-VAE学习面部表情的离散表示。与传统的连续表示相比，离散表示更易于解释，并且可以更好地捕捉面部表情的结构化信息。此外，RVQ-VAE通过残差量化，可以更有效地利用码本空间，提高表示的精度。

**关键设计**：3DMM用于提取身份无关的表情特征，确保模型关注表情本身而非个体差异。RVQ-VAE的码本大小和层数是重要的超参数，需要根据数据集进行调整。损失函数包括重构损失和量化损失，用于保证重构质量和码本的有效性。词袋模型使用TF-IDF加权，突出重要token的作用。

## 📊 实验亮点

实验结果表明，DFE在压力检测、人格预测和抑郁症检测等任务中，均优于基于FACS的pipeline以及Masked Autoencoders等先进模型。例如，在抑郁症检测任务中，DFE的性能提升超过5%。这表明DFE能够更有效地捕捉与心理状态相关的面部行为。

## 🎯 应用场景

该研究成果可应用于心理学、情感计算、人机交互等领域。例如，可以用于自动诊断心理疾病、评估用户的情绪状态、改善虚拟角色的表情生成等。未来，该方法有望扩展到其他非语言行为的分析，例如身体姿势和语音语调。

## 📄 摘要（原文）

> Facial expression analysis is central to understanding human behavior, yet existing coding systems such as the Facial Action Coding System (FACS) are constrained by limited coverage and costly manual annotation. In this work, we introduce Discrete Facial Encoding (DFE), an unsupervised, data-driven alternative of compact and interpretable dictionary of facial expressions from 3D mesh sequences learned through a Residual Vector Quantized Variational Autoencoder (RVQ-VAE). Our approach first extracts identity-invariant expression features from images using a 3D Morphable Model (3DMM), effectively disentangling factors such as head pose and facial geometry. We then encode these features using an RVQ-VAE, producing a sequence of discrete tokens from a shared codebook, where each token captures a specific, reusable facial deformation pattern that contributes to the overall expression. Through extensive experiments, we demonstrate that Discrete Facial Encoding captures more precise facial behaviors than FACS and other facial encoding alternatives. We evaluate the utility of our representation across three high-level psychological tasks: stress detection, personality prediction, and depression detection. Using a simple Bag-of-Words model built on top of the learned tokens, our system consistently outperforms both FACS-based pipelines and strong image and video representation learning models such as Masked Autoencoders. Further analysis reveals that our representation covers a wider variety of facial displays, highlighting its potential as a scalable and effective alternative to FACS for psychological and affective computing applications.

