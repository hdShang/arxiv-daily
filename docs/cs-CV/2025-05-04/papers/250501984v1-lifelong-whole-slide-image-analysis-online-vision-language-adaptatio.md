---
layout: default
title: "Lifelong Whole Slide Image Analysis: Online Vision-Language Adaptation and Past-to-Present Gradient Distillation"
---

# Lifelong Whole Slide Image Analysis: Online Vision-Language Adaptation and Past-to-Present Gradient Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01984" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01984v1</a>
  <a href="https://arxiv.org/pdf/2505.01984.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01984v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01984v1', 'Lifelong Whole Slide Image Analysis: Online Vision-Language Adaptation and Past-to-Present Gradient Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Doanh C. Bui, Hoai Luan Pham, Vu Trung Duong Le, Tuan Hai Vu, Van Duy Tran, Khang Nguyen, Yasuhiko Nakashima

**分类**: cs.CV

**发布日期**: 2025-05-04

**备注**: IEEE Access (2025)

**DOI**: [10.1109/ACCESS.2025.3580470](https://doi.org/10.1109/ACCESS.2025.3580470)

---

## 💡 一句话要点

**提出ADaFGrad以解决WSI分析中的持续学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全切片图像` `持续学习` `梯度蒸馏` `视觉-语言模型` `癌症诊断`

## 📋 核心要点

1. 现有方法在处理全切片图像时面临存储和计算资源的巨大挑战，难以实现有效的持续学习。
2. 论文提出的ADaFGrad方法通过结合视觉-语言模型和梯度蒸馏机制，提升了WSI分析的终身学习能力。
3. 实验结果显示，ADaFGrad在类增量学习场景中准确率提升了+5.068%，并在知识保留方面表现优异。

## 📝 摘要（中文）

全切片图像（WSIs）在癌症诊断和预后中发挥着重要作用，因为它们提供了细胞级别的组织细节。然而，WSIs的快速增长带来了存储、处理和模型训练等方面的挑战。因此，开发针对WSI分析的终身学习方法至关重要。本研究提出了ADaFGrad，一种旨在增强WSI分析的终身学习的方法。通过利用病理视觉-语言基础模型，构建了一个框架，使得切片的区域组织特征与预定义的文本原型缓冲区之间能够进行交互。此外，提出了一种梯度蒸馏机制，模拟了在持续学习环境中，分类头参数相对于分类逻辑的梯度。实验结果表明，ADaFGrad在仅经过少量训练周期后，超越了现有的WSI特定和传统的持续学习方法，准确率提高了+5.068%。

## 🔬 方法详解

**问题定义**：本论文旨在解决全切片图像（WSI）分析中的持续学习问题。现有方法在处理大规模WSI时，面临存储、处理和模型训练的挑战，导致知识遗忘和性能下降。

**核心思路**：论文提出的ADaFGrad方法通过结合病理视觉-语言基础模型与梯度蒸馏机制，增强了WSI分析的终身学习能力。这种设计使得模型能够在不同时间点有效地利用历史知识。

**技术框架**：ADaFGrad的整体架构包括两个主要模块：一是基于视觉-语言模型的特征交互框架，二是梯度蒸馏机制。特征交互模块负责提取切片的区域特征并与文本原型进行关联，而梯度蒸馏模块则在持续学习中保持模型的知识。

**关键创新**：ADaFGrad的核心创新在于引入了梯度蒸馏机制，该机制能够有效模拟分类逻辑的梯度，从而在不同迭代中保持模型的学习能力。这与传统方法的知识遗忘问题形成鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数以平衡新旧知识的学习，同时优化了网络结构以适应大规模WSI数据的处理需求。

## 📊 实验亮点

实验结果表明，ADaFGrad在类增量学习场景中准确率提升了+5.068%，并在知识保留方面表现优异，显示出最小的遗忘率。此外，ADaFGrad的准确率比基线提高了+40.084%，验证了所提模块的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医院和临床环境中的癌症诊断工具。通过实现高效的WSI分析，ADaFGrad能够帮助病理学家更准确地进行癌症诊断，从而提高患者的治疗效果。此外，随着数据量的不断增加，该方法的持续学习能力将使其在未来的医疗应用中具有重要价值。

## 📄 摘要（原文）

> Whole Slide Images (WSIs) play a crucial role in accurate cancer diagnosis and prognosis, as they provide tissue details at the cellular level. However, the rapid growth of computational tasks involving WSIs poses significant challenges. Given that WSIs are gigapixels in size, they present difficulties in terms of storage, processing, and model training. Therefore, it is essential to develop lifelong learning approaches for WSI analysis. In scenarios where slides are distributed across multiple institutes, we aim to leverage them to develop a unified online model as a computational tool for cancer diagnosis in clinical and hospital settings. In this study, we introduce ADaFGrad, a method designed to enhance lifelong learning for whole-slide image (WSI) analysis. First, we leverage pathology vision-language foundation models to develop a framework that enables interaction between a slide's regional tissue features and a predefined text-based prototype buffer. Additionally, we propose a gradient-distillation mechanism that mimics the gradient of a logit with respect to the classification-head parameters across past and current iterations in a continual-learning setting. We construct a sequence of six TCGA datasets for training and evaluation. Experimental results show that ADaFGrad outperforms both state-of-the-art WSI-specific and conventional continual-learning methods after only a few training epochs, exceeding them by up to +5.068% in the class-incremental learning scenario while exhibiting the least forgetting (i.e., retaining the most knowledge from previous tasks). Moreover, ADaFGrad surpasses its baseline by as much as +40.084% in accuracy, further demonstrating the effectiveness of the proposed modules.

