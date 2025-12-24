---
layout: default
title: "CLoE: Curriculum Learning on Endoscopic Images for Robust MES Classification"
---

# CLoE: Curriculum Learning on Endoscopic Images for Robust MES Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13280" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13280v1</a>
  <a href="https://arxiv.org/pdf/2508.13280.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13280v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13280v1', 'CLoE: Curriculum Learning on Endoscopic Images for Robust MES Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeynep Ozdemir, Hacer Yalim Keles, Omer Ozgur Tanriover

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-18

**备注**: 16 pages, 4 figures, 9 tables

**🔗 代码/项目**: [GITHUB](https://github.com/zeynepozdemir/CLoE)

---

## 💡 一句话要点

**提出CLoE框架以解决内窥镜图像MES分类中的标签噪声问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `内窥镜图像` `课程学习` `MES分类` `标签噪声` `图像质量评估` `深度学习` `医疗影像分析`

## 📋 核心要点

1. 现有MES分类方法面临标签噪声和观察者间变异性的问题，导致分类准确性不足。
2. CLoE框架通过课程学习策略，结合图像质量评估和ResizeMix增强，提升了分类的鲁棒性。
3. 在LIMUC和HyperKvasir数据集上，CLoE显著提高了模型性能，ConvNeXt-Tiny在LIMUC上达到82.5%的准确率。

## 📝 摘要（中文）

从内窥镜图像中评估疾病严重性在溃疡性结肠炎的评估中至关重要，Mayo内窥镜亚分数（MES）被广泛用于评估炎症。然而，由于观察者间的标签噪声和分数的序数特性，MES分类仍然具有挑战性。我们提出了CLoE，一个考虑标签可靠性和序数结构的课程学习框架。通过在波士顿肠道准备评分（BBPS）标签上训练的轻量模型估计图像质量，作为注释置信度的代理，从简单（干净）到困难（噪声）对样本进行排序。该课程进一步结合ResizeMix增强技术以提高鲁棒性。在LIMUC和HyperKvasir数据集上的实验表明，CLoE在强监督和自监督基线之上始终提高了性能。例如，ConvNeXt-Tiny在LIMUC上达到82.5%的准确率和0.894的QWK，且计算成本低。这些结果突显了在标签不确定性下改善序数分类的难度感知训练策略的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决内窥镜图像中MES分类的标签噪声和序数特性问题。现有方法往往忽视标签的可靠性和观察者间的变异性，导致分类性能不佳。

**核心思路**：CLoE框架采用课程学习策略，通过图像质量评估来排序样本，从而使模型在训练过程中逐步适应更复杂的样本。这种设计旨在提高模型对标签不确定性的鲁棒性。

**技术框架**：CLoE的整体架构包括两个主要模块：一是基于BBPS标签的轻量模型用于估计图像质量，二是结合ResizeMix增强技术来提高样本的多样性和模型的泛化能力。

**关键创新**：CLoE的主要创新在于将课程学习与标签可靠性评估相结合，形成了一种新的训练策略。这与传统方法的直接训练方式有本质区别，能够更好地处理标签噪声问题。

**关键设计**：在模型设计中，使用了轻量级网络来快速评估图像质量，并通过ResizeMix技术增强样本多样性。此外，损失函数设计考虑了序数特性，以更好地适应MES分类的需求。

## 📊 实验亮点

在LIMUC数据集上，使用CLoE框架的ConvNeXt-Tiny模型达到了82.5%的准确率和0.894的Kappa加权系数，显著优于现有的强监督和自监督基线。这表明CLoE在处理标签不确定性方面具有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、自动化诊断系统和临床决策支持。通过提高MES分类的准确性，CLoE框架可以帮助医生更好地评估患者的病情，从而优化治疗方案，提升患者的治疗效果。未来，该方法也可扩展到其他领域的序数分类任务中。

## 📄 摘要（原文）

> Estimating disease severity from endoscopic images is essential in assessing ulcerative colitis, where the Mayo Endoscopic Subscore (MES) is widely used to grade inflammation. However, MES classification remains challenging due to label noise from inter-observer variability and the ordinal nature of the score, which standard models often ignore. We propose CLoE, a curriculum learning framework that accounts for both label reliability and ordinal structure. Image quality, estimated via a lightweight model trained on Boston Bowel Preparation Scale (BBPS) labels, is used as a proxy for annotation confidence to order samples from easy (clean) to hard (noisy). This curriculum is further combined with ResizeMix augmentation to improve robustness. Experiments on the LIMUC and HyperKvasir datasets, using both CNNs and Transformers, show that CLoE consistently improves performance over strong supervised and self-supervised baselines. For instance, ConvNeXt-Tiny reaches 82.5\% accuracy and a QWK of 0.894 on LIMUC with low computational cost. These results highlight the potential of difficulty-aware training strategies for improving ordinal classification under label uncertainty. Code will be released at https://github.com/zeynepozdemir/CLoE.

