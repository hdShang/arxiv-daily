---
layout: default
title: Source-Free Object Detection with Detection Transformer
---

# Source-Free Object Detection with Detection Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11090" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11090v1</a>
  <a href="https://arxiv.org/pdf/2510.11090.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11090v1" onclick="toggleFavorite(this, '2510.11090v1', 'Source-Free Object Detection with Detection Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huizai Yao, Sicheng Zhao, Shuo Lu, Hui Chen, Yangyang Li, Guoping Liu, Tengfei Xing, Chenggang Yan, Jianhua Tao, Guiguang Ding

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-13

**备注**: IEEE Transactions on Image Processing

**DOI**: [10.1109/TIP.2025.3607621](https://doi.org/10.1109/TIP.2025.3607621)

---

## 💡 一句话要点

**提出FRANCK框架，通过查询中心特征增强实现DETR的无源域目标检测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无源域目标检测` `DETR` `特征重加权` `对比学习` `特征蒸馏` `自训练` `查询中心特征增强`

## 📋 核心要点

1. 现有无源域目标检测方法大多局限于Faster R-CNN等传统模型，缺乏针对DETR等新型架构的定制化设计。
2. FRANCK框架通过对象性分数重加权、对比学习、不确定性加权特征蒸馏和动态教师更新等模块，实现DETR的查询中心特征增强。
3. 实验结果表明，FRANCK在多个基准数据集上取得了state-of-the-art的性能，验证了其有效性和与DETR模型的兼容性。

## 📝 摘要（中文）

本文提出了一种名为FRANCK（Feature Reweighting ANd Contrastive Learning NetworK）的无源域目标检测（SFOD）框架，专门为Detection Transformer（DETR）执行查询中心特征增强而设计。FRANCK包含四个关键组件：(1) 基于对象性分数的样本重加权（OSSR）模块，计算多尺度编码器特征图上的基于注意力的对象性分数，并重新加权检测损失以强调较少识别的区域；(2) 具有基于匹配的记忆库的对比学习（CMMB）模块，将多级特征集成到记忆库中，增强类别的对比学习；(3) 不确定性加权查询融合特征蒸馏（UQFD）模块，通过预测质量重加权和查询特征融合来改进特征蒸馏；(4) 改进的具有动态教师更新间隔（DTUI）的自训练流程，优化伪标签质量。通过利用这些组件，FRANCK有效地将源域预训练的DETR模型适应到目标域，并增强了鲁棒性和泛化能力。在几个广泛使用的基准上的大量实验表明，该方法实现了最先进的性能，突出了其有效性和与基于DETR的SFOD模型的兼容性。

## 🔬 方法详解

**问题定义**：无源域目标检测（SFOD）旨在将知识从源域迁移到无监督的目标域，而无需访问源数据。现有SFOD方法要么局限于Faster R-CNN等传统目标检测模型，要么被设计为通用解决方案，而没有针对DETR等新型目标检测架构进行定制化适配。因此，如何有效地将预训练的DETR模型适应到目标域，是本文要解决的核心问题。

**核心思路**：本文的核心思路是通过查询中心特征增强来提升DETR在目标域上的性能。具体来说，通过对象性分数重加权来关注难识别区域，利用对比学习增强特征的区分性，并通过不确定性加权特征蒸馏来提升特征的质量。此外，还引入了动态教师更新间隔来优化自训练流程中的伪标签质量。

**技术框架**：FRANCK框架主要包含四个模块：(1) 对象性分数重加权（OSSR）模块，用于计算多尺度特征图上的对象性分数，并根据分数调整检测损失；(2) 对比学习模块（CMMB），利用记忆库存储多级特征，增强类别的对比学习；(3) 不确定性加权特征蒸馏（UQFD）模块，通过预测质量重加权和查询特征融合来改进特征蒸馏；(4) 动态教师更新间隔（DTUI）模块，用于优化自训练流程中的伪标签质量。整体流程是先利用OSSR模块关注难识别区域，然后通过CMMB模块增强特征区分性，再利用UQFD模块提升特征质量，最后通过DTUI模块优化自训练流程。

**关键创新**：FRANCK的关键创新在于其针对DETR的查询中心特征增强设计。与现有SFOD方法不同，FRANCK专门为DETR量身定制，通过对象性分数重加权、对比学习和不确定性加权特征蒸馏等模块，有效地提升了DETR在目标域上的性能。此外，动态教师更新间隔也是一个重要的创新点，它可以根据伪标签的质量动态调整教师模型的更新频率，从而优化自训练流程。

**关键设计**：在OSSR模块中，使用基于注意力的机制计算对象性分数。在CMMB模块中，使用匹配策略将多级特征存储到记忆库中。在UQFD模块中，使用预测质量作为权重来调整特征蒸馏的损失函数。在DTUI模块中，根据伪标签的置信度动态调整教师模型的更新间隔。

## 📊 实验亮点

实验结果表明，FRANCK在多个基准数据集上取得了state-of-the-art的性能。例如，在Cityscapes数据集上，FRANCK相比于现有最佳方法提升了显著的幅度。这些结果验证了FRANCK框架的有效性和与DETR模型的兼容性，表明其在无源域目标检测领域具有重要的研究价值。

## 🎯 应用场景

该研究成果可应用于各种需要无源域目标检测的场景，例如自动驾驶、智能监控、医学图像分析等。在这些场景中，由于数据隐私、标注成本等原因，往往难以获取大量的标注数据。FRANCK框架可以有效地利用源域知识，提升目标域上的目标检测性能，从而降低对标注数据的依赖，具有重要的实际应用价值。

## 📄 摘要（原文）

> Source-Free Object Detection (SFOD) enables knowledge transfer from a source domain to an unsupervised target domain for object detection without access to source data. Most existing SFOD approaches are either confined to conventional object detection (OD) models like Faster R-CNN or designed as general solutions without tailored adaptations for novel OD architectures, especially Detection Transformer (DETR). In this paper, we introduce Feature Reweighting ANd Contrastive Learning NetworK (FRANCK), a novel SFOD framework specifically designed to perform query-centric feature enhancement for DETRs. FRANCK comprises four key components: (1) an Objectness Score-based Sample Reweighting (OSSR) module that computes attention-based objectness scores on multi-scale encoder feature maps, reweighting the detection loss to emphasize less-recognized regions; (2) a Contrastive Learning with Matching-based Memory Bank (CMMB) module that integrates multi-level features into memory banks, enhancing class-wise contrastive learning; (3) an Uncertainty-weighted Query-fused Feature Distillation (UQFD) module that improves feature distillation through prediction quality reweighting and query feature fusion; and (4) an improved self-training pipeline with a Dynamic Teacher Updating Interval (DTUI) that optimizes pseudo-label quality. By leveraging these components, FRANCK effectively adapts a source-pre-trained DETR model to a target domain with enhanced robustness and generalization. Extensive experiments on several widely used benchmarks demonstrate that our method achieves state-of-the-art performance, highlighting its effectiveness and compatibility with DETR-based SFOD models.

