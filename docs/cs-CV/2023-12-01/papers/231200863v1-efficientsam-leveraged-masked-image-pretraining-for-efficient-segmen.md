---
layout: default
title: "EfficientSAM: Leveraged Masked Image Pretraining for Efficient Segment Anything"
---

# EfficientSAM: Leveraged Masked Image Pretraining for Efficient Segment Anything

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00863" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00863v1</a>
  <a href="https://arxiv.org/pdf/2312.00863.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00863v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00863v1', 'EfficientSAM: Leveraged Masked Image Pretraining for Efficient Segment Anything')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunyang Xiong, Bala Varadarajan, Lemeng Wu, Xiaoyu Xiang, Fanyi Xiao, Chenchen Zhu, Xiaoliang Dai, Dilin Wang, Fei Sun, Forrest Iandola, Raghuraman Krishnamoorthi, Vikas Chandra

**分类**: cs.CV

**发布日期**: 2023-12-01

---

## 💡 一句话要点

**提出EfficientSAM以解决SAM模型计算成本高的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `轻量级模型` `视觉表示学习` `实例分割` `掩码图像预训练` `计算效率` `Transformer模型` `SA-1B数据集`

## 📋 核心要点

1. 现有的SAM模型由于计算成本高，限制了其在实际应用中的广泛使用。
2. 本文提出EfficientSAMs，通过masked image pretraining（SAMI）来学习有效的视觉表示，构建轻量级的SAM模型。
3. 实验结果表明，EfficientSAMs在多个视觉任务上表现优异，特别是在零-shot实例分割任务上，相较于其他模型有约4 AP的提升。

## 📝 摘要（中文）

Segment Anything Model (SAM)作为一种强大的视觉应用工具，其卓越的零-shot迁移能力和高适应性得益于在大规模高质量SA-1B数据集上训练的超大Transformer模型。然而，SAM模型的巨大计算成本限制了其在更广泛实际应用中的使用。为了解决这一问题，本文提出了EfficientSAMs，这是一种轻量级的SAM模型，能够在大幅降低复杂度的同时保持良好的性能。我们的方法基于masked image pretraining，即SAMI，旨在通过重建SAM图像编码器的特征来有效学习视觉表示。经过多项视觉任务的评估，EfficientSAMs在零-shot实例分割等任务上表现优异，相较于其他快速SAM模型有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决Segment Anything Model (SAM)在实际应用中由于计算成本过高的问题。现有的SAM模型虽然性能卓越，但其庞大的计算需求限制了其应用范围。

**核心思路**：论文提出的EfficientSAMs通过引入masked image pretraining（SAMI），有效地学习视觉表示，从而构建轻量级的SAM模型，降低计算复杂度。

**技术框架**：整体架构包括SAMI预训练的轻量级图像编码器和掩码解码器，首先通过SAMI进行特征重建，然后在SA-1B数据集上进行微调，以适应“segment anything”任务。

**关键创新**：最重要的创新点在于引入了SAMI作为预训练方法，使得轻量级模型在性能上超越了其他掩码图像预训练方法，特别是在零-shot任务上表现突出。

**关键设计**：在模型设计中，采用了轻量级网络结构，优化了损失函数以适应特定任务需求，同时在训练过程中注重特征重建的有效性。通过这些设计，EfficientSAMs在保持性能的同时显著降低了计算复杂度。

## 📊 实验亮点

实验结果显示，EfficientSAMs在零-shot实例分割任务上相较于其他快速SAM模型有显著提升，具体表现为在COCO/LVIS数据集上约提升4 AP。这一结果表明，SAMI预训练方法在多项视觉任务中均具有优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、智能监控、医疗影像分析等多个视觉任务。EfficientSAMs的轻量级特性使其能够在资源受限的环境中高效运行，具有广泛的实际价值和未来影响，能够推动更多视觉应用的落地。

## 📄 摘要（原文）

> Segment Anything Model (SAM) has emerged as a powerful tool for numerous vision applications. A key component that drives the impressive performance for zero-shot transfer and high versatility is a super large Transformer model trained on the extensive high-quality SA-1B dataset. While beneficial, the huge computation cost of SAM model has limited its applications to wider real-world applications. To address this limitation, we propose EfficientSAMs, light-weight SAM models that exhibits decent performance with largely reduced complexity. Our idea is based on leveraging masked image pretraining, SAMI, which learns to reconstruct features from SAM image encoder for effective visual representation learning. Further, we take SAMI-pretrained light-weight image encoders and mask decoder to build EfficientSAMs, and finetune the models on SA-1B for segment anything task. We perform evaluations on multiple vision tasks including image classification, object detection, instance segmentation, and semantic object detection, and find that our proposed pretraining method, SAMI, consistently outperforms other masked image pretraining methods. On segment anything task such as zero-shot instance segmentation, our EfficientSAMs with SAMI-pretrained lightweight image encoders perform favorably with a significant gain (e.g., ~4 AP on COCO/LVIS) over other fast SAM models.

