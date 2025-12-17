---
layout: default
title: FOLK: Fast Open-Vocabulary 3D Instance Segmentation via Label-guided Knowledge Distillation
---

# FOLK: Fast Open-Vocabulary 3D Instance Segmentation via Label-guided Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08849" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08849v1</a>
  <a href="https://arxiv.org/pdf/2510.08849.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08849v1" onclick="toggleFavorite(this, '2510.08849v1', 'FOLK: Fast Open-Vocabulary 3D Instance Segmentation via Label-guided Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongrui Wu, Zhicheng Gao, Jin Cao, Kelu Yao, Wen Shen, Zhihua Wei

**分类**: cs.CV

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**提出FOLK，通过标签引导的知识蒸馏实现快速开放词汇3D实例分割**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇3D实例分割` `知识蒸馏` `3D点云` `视觉-语言模型` `机器人` `场景理解`

## 📋 核心要点

1. 现有开放词汇3D实例分割方法依赖2D-3D映射，易受遮挡噪声影响，且计算成本高昂。
2. FOLK通过知识蒸馏，将2D教师模型的开放词汇知识迁移到3D学生模型，直接在3D点云上进行分类。
3. 实验表明，FOLK在ScanNet200数据集上取得了SOTA性能，AP50达到35.7，推理速度显著提升。

## 📝 摘要（中文）

本文提出了一种快速开放词汇3D实例分割方法，名为FOLK，它通过标签引导的知识蒸馏实现。现有方法通常将3D实例映射到2D RGB-D图像，然后利用视觉-语言模型(VLM)进行分类，但这种映射策略会引入2D遮挡噪声，并在推理过程中产生巨大的计算和内存开销，从而降低推理速度。为了解决上述问题，FOLK设计了一个教师模型来提取高质量的实例嵌入，并将其开放词汇知识提炼到3D学生模型中。这样，在推理过程中，经过蒸馏的3D模型可以直接从3D点云中分类实例，避免遮挡造成的噪声，并显著加快推理过程。具体来说，首先设计一个教师模型，为每个3D实例生成一个2D CLIP嵌入，结合了可见性和视点多样性，作为蒸馏的学习目标。然后，开发一个3D学生模型，直接为每个3D实例生成3D嵌入。在训练过程中，提出了一种标签引导的蒸馏算法，将标签一致的2D嵌入中的开放词汇知识提炼到学生模型中。在ScanNet200和Replica数据集上进行的实验表明，FOLK在ScanNet200数据集上实现了最先进的性能，AP50得分为35.7，同时运行速度比以前的方法快约6.0倍至152.2倍。

## 🔬 方法详解

**问题定义**：开放词汇3D实例分割旨在分割和分类超出标注标签空间的实例。现有方法的痛点在于，将3D实例映射到2D图像的过程中引入了遮挡噪声，并且使用视觉-语言模型进行分类时，计算和内存开销巨大，导致推理速度慢。

**核心思路**：FOLK的核心思路是利用知识蒸馏，训练一个3D学生模型，使其能够直接从3D点云中学习并进行开放词汇的实例分割。通过将2D教师模型的知识迁移到3D学生模型，避免了2D-3D映射带来的噪声和计算负担。

**技术框架**：FOLK包含一个2D教师模型和一个3D学生模型。教师模型负责提取高质量的实例嵌入，并生成用于知识蒸馏的目标。学生模型则直接在3D点云上进行特征提取和分类。训练过程采用标签引导的蒸馏算法，确保学生模型学习到与标签一致的知识。推理阶段，仅使用3D学生模型，实现快速的实例分割。

**关键创新**：FOLK的关键创新在于：1) 直接在3D空间进行开放词汇实例分割，避免了2D-3D映射带来的问题；2) 提出了标签引导的知识蒸馏算法，有效提升了学生模型的性能；3) 设计了结合可见性和视点多样性的2D CLIP嵌入作为蒸馏目标。

**关键设计**：教师模型使用CLIP模型提取2D实例的嵌入，并结合可见性和视点信息进行增强。学生模型采用3D神经网络，例如PointNet++或类似结构，直接从3D点云中提取特征。标签引导的蒸馏算法使用交叉熵损失或KL散度损失来衡量教师模型和学生模型输出之间的差异，并根据标签信息调整损失权重。

## 📊 实验亮点

FOLK在ScanNet200数据集上取得了显著的性能提升，AP50得分达到35.7，超越了现有方法。更重要的是，FOLK的推理速度比之前的方法快6.0倍到152.2倍，实现了速度和精度的双重提升。这些结果表明，FOLK是一种高效且有效的开放词汇3D实例分割方法。

## 🎯 应用场景

FOLK在机器人导航、自动驾驶、场景理解等领域具有广泛的应用前景。它可以帮助机器人理解周围环境，识别未知的物体，并进行更智能的交互。此外，该方法还可以应用于三维重建、虚拟现实等领域，提升用户体验。

## 📄 摘要（原文）

> Open-vocabulary 3D instance segmentation seeks to segment and classify instances beyond the annotated label space. Existing methods typically map 3D instances to 2D RGB-D images, and then employ vision-language models (VLMs) for classification. However, such a mapping strategy usually introduces noise from 2D occlusions and incurs substantial computational and memory costs during inference, slowing down the inference speed. To address the above problems, we propose a Fast Open-vocabulary 3D instance segmentation method via Label-guided Knowledge distillation (FOLK). Our core idea is to design a teacher model that extracts high-quality instance embeddings and distills its open-vocabulary knowledge into a 3D student model. In this way, during inference, the distilled 3D model can directly classify instances from the 3D point cloud, avoiding noise caused by occlusions and significantly accelerating the inference process. Specifically, we first design a teacher model to generate a 2D CLIP embedding for each 3D instance, incorporating both visibility and viewpoint diversity, which serves as the learning target for distillation. We then develop a 3D student model that directly produces a 3D embedding for each 3D instance. During training, we propose a label-guided distillation algorithm to distill open-vocabulary knowledge from label-consistent 2D embeddings into the student model. FOLK conducted experiments on the ScanNet200 and Replica datasets, achieving state-of-the-art performance on the ScanNet200 dataset with an AP50 score of 35.7, while running approximately 6.0x to 152.2x faster than previous methods. All codes will be released after the paper is accepted.

