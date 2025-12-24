---
layout: default
title: Industrial Synthetic Segment Pre-training
---

# Industrial Synthetic Segment Pre-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13099" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13099v2</a>
  <a href="https://arxiv.org/pdf/2505.13099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13099v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13099v2', 'Industrial Synthetic Segment Pre-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shinichi Mae, Ryousuke Yamada, Hirokatsu Kataoka

**分类**: cs.CV

**发布日期**: 2025-05-19 (更新: 2025-05-20)

---

## 💡 一句话要点

**提出工业合成分割预训练数据集以解决图像数据不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实例分割` `合成数据集` `工业应用` `视觉模型` `数据效率` `监督学习` `领域适应`

## 📋 核心要点

1. 现有方法在工业应用中面临法律限制和领域差距，导致性能下降。
2. 本文提出的InsCore数据集通过合成生成工业特征的实例分割图像，无需真实图像和人工标注。
3. 实验表明，使用InsCore预训练的模型在多个工业数据集上表现优于传统方法，提升显著。

## 📝 摘要（中文）

在实例分割领域，基于真实图像数据集的预训练已被广泛证明有效。然而，工业应用面临法律和伦理限制，以及网络图像与工业图像之间的领域差距等挑战。为了解决这些问题，本文提出了实例核心分割数据集（InsCore），该数据集基于公式驱动的监督学习生成完全标注的合成实例分割图像。实验结果表明，使用InsCore预训练的模型在五个工业数据集上的表现优于在COCO和ImageNet-21k上训练的模型，以及微调后的SAM，平均提升6.2个百分点，展示了该方法的数据效率。

## 🔬 方法详解

**问题定义**：本文旨在解决工业应用中实例分割模型对真实图像和人工标注的依赖问题。现有方法在法律和领域适应性上存在显著不足，导致性能下降。

**核心思路**：提出实例核心分割数据集（InsCore），通过公式驱动的监督学习生成合成图像，反映工业数据的特征，避免了对真实图像的依赖。

**技术框架**：InsCore数据集的生成流程包括数据合成、标注生成和特征反映三个主要模块，确保生成的图像具有复杂遮挡、密集层次掩膜和多样的非刚性形状。

**关键创新**：InsCore的最大创新在于其完全合成的特性，避免了法律和伦理问题，同时在工业数据特征的反映上优于传统的真实图像数据集。

**关键设计**：在数据合成过程中，采用了特定的参数设置和损失函数，以确保生成图像的质量和多样性，网络结构设计上注重对工业特征的捕捉。

## 📊 实验亮点

实验结果显示，使用InsCore预训练的模型在五个工业数据集上的实例分割性能平均提升6.2个百分点，超越了在COCO和ImageNet-21k上训练的模型以及微调后的SAM，展现出极高的数据效率，仅使用10万张合成图像。

## 🎯 应用场景

该研究的潜在应用领域包括制造业、自动化检测和机器人视觉等，能够为工业界提供一种无需真实图像和人工标注的高效实例分割解决方案。未来，InsCore有望推动工业视觉模型的普及和应用，降低数据获取成本。

## 📄 摘要（原文）

> Pre-training on real-image datasets has been widely proven effective for improving instance segmentation. However, industrial applications face two key challenges: (1) legal and ethical restrictions, such as ImageNet's prohibition of commercial use, and (2) limited transferability due to the domain gap between web images and industrial imagery. Even recent vision foundation models, including the segment anything model (SAM), show notable performance degradation in industrial settings. These challenges raise critical questions: Can we build a vision foundation model for industrial applications without relying on real images or manual annotations? And can such models outperform even fine-tuned SAM on industrial datasets? To address these questions, we propose the Instance Core Segmentation Dataset (InsCore), a synthetic pre-training dataset based on formula-driven supervised learning (FDSL). InsCore generates fully annotated instance segmentation images that reflect key characteristics of industrial data, including complex occlusions, dense hierarchical masks, and diverse non-rigid shapes, distinct from typical web imagery. Unlike previous methods, InsCore requires neither real images nor human annotations. Experiments on five industrial datasets show that models pre-trained with InsCore outperform those trained on COCO and ImageNet-21k, as well as fine-tuned SAM, achieving an average improvement of 6.2 points in instance segmentation performance. This result is achieved using only 100k synthetic images, more than 100 times fewer than the 11 million images in SAM's SA-1B dataset, demonstrating the data efficiency of our approach. These findings position InsCore as a practical and license-free vision foundation model for industrial applications.

