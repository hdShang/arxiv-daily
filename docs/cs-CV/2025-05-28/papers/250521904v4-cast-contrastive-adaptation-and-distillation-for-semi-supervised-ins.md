---
layout: default
title: "CAST: Contrastive Adaptation and Distillation for Semi-Supervised Instance Segmentation"
---

# CAST: Contrastive Adaptation and Distillation for Semi-Supervised Instance Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21904" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21904v4</a>
  <a href="https://arxiv.org/pdf/2505.21904.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21904v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21904v4', 'CAST: Contrastive Adaptation and Distillation for Semi-Supervised Instance Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pardis Taghavi, Tian Liu, Renjie Li, Reza Langari, Zhengzhong Tu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-28 (更新: 2025-10-08)

---

## 💡 一句话要点

**提出CAST框架以解决半监督实例分割问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实例分割` `半监督学习` `知识蒸馏` `对比学习` `视觉基础模型`

## 📋 核心要点

1. 现有的实例分割方法依赖于大量的逐像素标注，成本高且计算复杂，限制了其应用。
2. CAST框架通过半监督知识蒸馏，结合有限的标注和丰富的未标注数据，进行领域适应和知识转移。
3. 在Cityscapes和ADE20K上，CAST显著提高了模型性能，超越了现有的最先进方法，展示了其有效性。

## 📝 摘要（中文）

实例分割需要昂贵的逐像素标注和计算密集型模型。我们提出CAST，一个半监督知识蒸馏框架，利用有限的标注和丰富的未标注数据，将预训练的视觉基础模型压缩为紧凑的专家。CAST分为三个阶段：通过对比校准进行视觉基础模型的领域适应、通过统一的多目标损失进行知识转移，以及学生模型的精炼以减轻伪标签偏差。CAST的核心是实例感知的逐像素对比损失，融合了掩膜和类别得分，以提取信息丰富的负样本并强化实例间的边界。在Cityscapes和ADE20K数据集上，我们的学生模型在大小上减少约11倍，分别提高了+8.5和+7.1的AP，超越了适应后的教师模型，并在两个基准上进一步超越了最先进的半监督知识蒸馏方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决实例分割中对逐像素标注的高依赖性和计算复杂性的问题。现有方法在标注成本和模型效率上存在显著不足。

**核心思路**：CAST框架通过半监督知识蒸馏，利用有限的标注数据和丰富的未标注数据，进行领域适应和知识转移，从而提升模型性能。

**技术框架**：CAST的整体架构分为三个主要阶段：第一阶段是通过自训练和对比校准进行视觉基础模型的领域适应；第二阶段是通过统一的多目标损失进行知识转移；第三阶段是学生模型的精炼，以减轻伪标签的偏差。

**关键创新**：CAST的核心创新在于引入了实例感知的逐像素对比损失，这一损失函数融合了掩膜和类别得分，能够有效提取信息丰富的负样本并强化实例间的边界，从而提升了模型的对比信号。

**关键设计**：CAST的设计中，采用了统一的多目标损失函数来协调不同任务的学习，同时在学生模型的训练中引入了对比损失，以确保教师模型和学生模型的嵌入对齐。

## 📊 实验亮点

CAST框架在Cityscapes和ADE20K数据集上表现出色，学生模型在大小上减少约11倍，分别提高了+8.5和+7.1的AP，超越了适应后的教师模型，并在两个基准上进一步超越了最先进的半监督知识蒸馏方法，显示出显著的性能提升。

## 🎯 应用场景

该研究在自动驾驶、医学影像分析和视频监控等领域具有广泛的应用潜力。通过减少对标注数据的依赖，CAST能够加速模型的训练过程，并提高实例分割任务的效率和准确性，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Instance segmentation demands costly per-pixel annotations and computationally expensive models. We introduce CAST, a semi-supervised knowledge distillation (SSKD) framework that compresses pre-trained vision foundation models (VFM) into compact experts using limited labeled and abundant unlabeled data. CAST unfolds in three stages: (1) domain adaptation of the VFM(s) via self-training with contrastive calibration, (2) knowledge transfer through a unified multi-objective loss, and (3) student refinement to mitigate residual pseudo-label bias. Central to CAST is an \emph{instance-aware pixel-wise contrastive loss} that fuses mask and class scores to extract informative negatives and enforce clear inter-instance margins. By maintaining this contrastive signal across both adaptation and distillation, we align teacher and student embeddings and fully leverage unlabeled images. On Cityscapes and ADE20K, our ~11x smaller student improves over its zero-shot VFM teacher(s) by +8.5 and +7.1 AP, surpasses adapted teacher(s) by +3.4 and +1.5 AP, and further outperforms state-of-the-art SSKD methods on both benchmarks.

