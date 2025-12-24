---
layout: default
title: "Why Settle for Mid: A Probabilistic Viewpoint to Spatial Relationship Alignment in Text-to-image Models"
---

# Why Settle for Mid: A Probabilistic Viewpoint to Spatial Relationship Alignment in Text-to-image Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23418" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23418v1</a>
  <a href="https://arxiv.org/pdf/2506.23418.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23418v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23418v1', 'Why Settle for Mid: A Probabilistic Viewpoint to Spatial Relationship Alignment in Text-to-image Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Parham Rezaei, Arash Marioriyad, Mahdieh Soleymani Baghshah, Mohammad Hossein Rohban

**分类**: cs.CV

**发布日期**: 2025-06-29

**备注**: 12 main pages, 18 figures, and 16 tables

---

## 💡 一句话要点

**提出概率框架以解决文本到图像模型的空间关系对齐问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `文本到图像生成` `空间关系对齐` `概率模型` `评估指标` `生成方法` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有文本到图像模型在组合生成中面临空间关系错位的问题，难以准确反映输入提示中的细节。
2. 本文提出了一种基于概率的框架，通过优越性概率（PoS）建模对象的相对空间位置，改善空间关系对齐。
3. 实验结果显示，PSE指标与人类判断的对齐程度更高，PSG方法在多个评估指标上超越了现有最先进的方法。

## 📝 摘要（中文）

尽管文本到图像模型能够生成高质量、真实且多样的图像，但在组合生成方面仍面临挑战，尤其是在准确表示输入提示中指定的细节方面。一个普遍存在的问题是空间关系的错位，模型常常无法忠实生成反映输入提示中对象之间空间配置的图像。为了解决这一挑战，本文提出了一种新的概率框架，用于建模场景中对象的相对空间位置，利用了优越性概率（PoS）的概念。我们做出了两项重要贡献：首先，提出了一种新的评估指标PoS基础评估（PSE），用于评估文本与图像之间的2D和3D空间关系的对齐程度；其次，提出了PoS基础生成（PSG），一种在推理时改善T2I模型中2D和3D空间关系对齐的方法，无需微调。实验表明，PSE指标与人类判断的对齐程度优于传统的中心基准指标，PSG显著提升了文本到图像模型生成指定空间配置图像的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到图像模型在组合生成中空间关系错位的问题。现有方法在生成图像时，常常无法准确反映输入提示中对象之间的空间配置，导致生成结果不符合人类的直观理解。

**核心思路**：论文提出了一种新的概率框架，利用优越性概率（PoS）来建模对象的相对空间位置。通过引入PoS基础评估（PSE）和PoS基础生成（PSG）方法，改善了空间关系的对齐。

**技术框架**：整体架构包括两个主要模块：首先是PSE评估模块，用于评估文本与图像之间的空间关系对齐；其次是PSG生成模块，在推理阶段通过奖励函数优化生成过程。

**关键创新**：最重要的创新在于提出了PSE评估指标和PSG生成方法。PSE与传统的中心基准指标相比，更能反映人类的判断，而PSG则在不需要微调的情况下，显著改善了空间关系的对齐。

**关键设计**：PSG方法采用了基于词性（Part-of-Speech）的奖励函数，能够通过两种方式使用：一种是作为梯度引导机制，应用于去噪步骤中的交叉注意力图；另一种是作为搜索策略，评估一组初始噪声向量以选择最佳向量。实验中，PSE指标与人类判断的对齐程度显著提高，展示了其在复杂空间关系准确性评估中的可靠性。

## 📊 实验亮点

实验结果表明，PSE指标在空间关系对齐方面与人类判断的对齐程度显著提高，且PSG方法在多个评估指标上超越了现有最先进的方法，提升幅度达到XX%。具体而言，PSG在生成图像的空间配置准确性上表现优异，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、图像生成、虚拟现实和增强现实等。通过改善文本到图像模型的空间关系对齐能力，可以提升生成图像的质量和准确性，进而推动相关领域的技术进步和应用落地。未来，该方法可能会在艺术创作、游戏设计和自动化内容生成等方面产生深远影响。

## 📄 摘要（原文）

> Despite the ability of text-to-image models to generate high-quality, realistic, and diverse images, they face challenges in compositional generation, often struggling to accurately represent details specified in the input prompt. A prevalent issue in compositional generation is the misalignment of spatial relationships, as models often fail to faithfully generate images that reflect the spatial configurations specified between objects in the input prompts. To address this challenge, we propose a novel probabilistic framework for modeling the relative spatial positioning of objects in a scene, leveraging the concept of Probability of Superiority (PoS). Building on this insight, we make two key contributions. First, we introduce a novel evaluation metric, PoS-based Evaluation (PSE), designed to assess the alignment of 2D and 3D spatial relationships between text and image, with improved adherence to human judgment. Second, we propose PoS-based Generation (PSG), an inference-time method that improves the alignment of 2D and 3D spatial relationships in T2I models without requiring fine-tuning. PSG employs a Part-of-Speech PoS-based reward function that can be utilized in two distinct ways: (1) as a gradient-based guidance mechanism applied to the cross-attention maps during the denoising steps, or (2) as a search-based strategy that evaluates a set of initial noise vectors to select the best one. Extensive experiments demonstrate that the PSE metric exhibits stronger alignment with human judgment compared to traditional center-based metrics, providing a more nuanced and reliable measure of complex spatial relationship accuracy in text-image alignment. Furthermore, PSG significantly enhances the ability of text-to-image models to generate images with specified spatial configurations, outperforming state-of-the-art methods across multiple evaluation metrics and benchmarks.

