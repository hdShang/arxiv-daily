---
layout: default
title: TeDA: Boosting Vision-Lanuage Models for Zero-Shot 3D Object Retrieval via Testing-time Distribution Alignment
---

# TeDA: Boosting Vision-Lanuage Models for Zero-Shot 3D Object Retrieval via Testing-time Distribution Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02325" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02325v1</a>
  <a href="https://arxiv.org/pdf/2505.02325.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02325v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02325v1', 'TeDA: Boosting Vision-Lanuage Models for Zero-Shot 3D Object Retrieval via Testing-time Distribution Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhichuan Wang, Yang Zhou, Jinhai Xiang, Yulong Wang, Xinwei He

**分类**: cs.CV

**发布日期**: 2025-05-05

**备注**: Accepted by ICMR 2025

**🔗 代码/项目**: [GITHUB](https://github.com/wangzhichuan123/TeDA)

---

## 💡 一句话要点

**提出TeDA以解决未知类别3D物体检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D物体检索` `视觉-语言模型` `零-shot学习` `多模态融合` `自增强策略`

## 📋 核心要点

1. 现有方法在3D物体检索中面临训练数据不足和类别未知的挑战，导致泛化能力不足。
2. 提出的TeDA框架通过将3D物体投影为多视图图像，并利用CLIP进行特征提取，解决了2D与3D分布差异的问题。
3. 实验结果显示，TeDA在多个基准测试中显著优于现有方法，验证了其在未知类别检索中的有效性。

## 📝 摘要（中文）

学习具有区分性的3D表示以适应未知测试类别是许多现实世界3D应用的新兴需求。现有方法因缺乏广泛概念的3D训练数据而难以实现这一目标。预训练的大型视觉-语言模型（如CLIP）在零-shot泛化能力上表现出色，但在提取适合的3D表示时受到2D训练与3D测试分布之间巨大差距的限制。为了解决这些挑战，本文提出了测试时分布对齐（TeDA）框架，首次研究了视觉-语言模型在3D特征学习中的测试时适应。TeDA将3D物体投影为多视图图像，利用CLIP提取特征，并通过自增强方式对自信的查询-目标样本对进行迭代优化，从而优化3D查询嵌入。此外，TeDA还整合了多模态语言模型（InternVL）生成的文本描述，以增强对3D物体的理解。大量实验表明，TeDA在四个开放集3D物体检索基准上显著超越了现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决在未知类别下进行3D物体检索的问题。现有方法因缺乏足够的3D训练数据和2D与3D分布之间的差距，难以实现良好的泛化能力。

**核心思路**：TeDA框架通过在测试时对预训练的2D视觉-语言模型CLIP进行适应，利用多视图图像提取3D特征，并通过自增强策略优化查询嵌入，以提高检索性能。

**技术框架**：TeDA的整体架构包括三个主要模块：首先，将3D物体投影为多视图图像；其次，使用CLIP提取这些图像的特征；最后，通过自信的查询-目标样本对进行迭代优化，以提升3D查询的嵌入表示。

**关键创新**：TeDA是首个研究视觉-语言模型在3D特征学习中的测试时适应的工作，创新性地将2D与3D特征提取结合，填补了现有方法的空白。

**关键设计**：在模型设计中，TeDA采用了迭代优化策略，利用自信的样本对进行特征增强，同时整合了多模态语言模型生成的文本描述，以丰富3D物体的理解。

## 📊 实验亮点

在四个开放集3D物体检索基准上，TeDA的表现显著优于现有最先进的方法，具体提升幅度达到XX%，验证了其在未知类别检索中的有效性。此外，在Objaverse-LVIS数据集上使用深度图的实验进一步支持了TeDA的有效性。

## 🎯 应用场景

该研究在自动驾驶、机器人抓取、虚拟现实等领域具有广泛的应用潜力。通过提高未知类别3D物体的检索能力，TeDA能够促进智能系统在复杂环境中的决策与操作，提升其适应性和智能化水平。

## 📄 摘要（原文）

> Learning discriminative 3D representations that generalize well to unknown testing categories is an emerging requirement for many real-world 3D applications. Existing well-established methods often struggle to attain this goal due to insufficient 3D training data from broader concepts. Meanwhile, pre-trained large vision-language models (e.g., CLIP) have shown remarkable zero-shot generalization capabilities. Yet, they are limited in extracting suitable 3D representations due to substantial gaps between their 2D training and 3D testing distributions. To address these challenges, we propose Testing-time Distribution Alignment (TeDA), a novel framework that adapts a pretrained 2D vision-language model CLIP for unknown 3D object retrieval at test time. To our knowledge, it is the first work that studies the test-time adaptation of a vision-language model for 3D feature learning. TeDA projects 3D objects into multi-view images, extracts features using CLIP, and refines 3D query embeddings with an iterative optimization strategy by confident query-target sample pairs in a self-boosting manner. Additionally, TeDA integrates textual descriptions generated by a multimodal language model (InternVL) to enhance 3D object understanding, leveraging CLIP's aligned feature space to fuse visual and textual cues. Extensive experiments on four open-set 3D object retrieval benchmarks demonstrate that TeDA greatly outperforms state-of-the-art methods, even those requiring extensive training. We also experimented with depth maps on Objaverse-LVIS, further validating its effectiveness. Code is available at https://github.com/wangzhichuan123/TeDA.

