---
layout: default
title: Understanding the Gain from Data Filtering in Multimodal Contrastive Learning
---

# Understanding the Gain from Data Filtering in Multimodal Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14230" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14230v1</a>
  <a href="https://arxiv.org/pdf/2512.14230.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14230v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14230v1', 'Understanding the Gain from Data Filtering in Multimodal Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Divyansh Pareek, Sewoong Oh, Simon S. Du

**分类**: cs.LG, stat.ML

**发布日期**: 2025-12-16

**备注**: 40 pages, 8 figures, 1 table. This work is accepted to the Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025

---

## 💡 一句话要点

**提出教师模型过滤以提升多模态对比学习效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `对比学习` `数据过滤` `教师模型` `深度学习`

## 📋 核心要点

1. 现有多模态学习方法在处理低质量数据时效果不佳，导致模型性能下降。
2. 论文提出基于教师模型的过滤方法，通过预训练模型评估数据质量，从而提升对比学习效果。
3. 实验结果表明，使用教师模型过滤后，模型误差显著降低，验证了数据过滤的有效性。

## 📝 摘要（中文）

现代多模态表示学习的成功依赖于互联网规模的数据集。然而，由于大量原始网络数据的低质量，数据筛选成为训练流程中的关键步骤。基于教师模型的过滤方法利用预训练模型计算质量评分，已成为一种成功的解决方案。本文通过标准双模态数据生成模型，表征了过滤后的对比学习性能，证明了数据过滤的可行性和有效性。具体而言，未过滤情况下的误差被上下界限为$rac{1}{η	ext{sqrt}{n}}$，而使用教师模型过滤后的误差在大$η$范围内上界为$rac{1}{	ext{sqrt}{ηn}}$，在小$η$范围内上界为$rac{1}{	ext{sqrt}{n}}$。

## 🔬 方法详解

**问题定义**：本文解决的问题是如何在多模态对比学习中有效处理低质量数据。现有方法在面对大量低质量数据时，模型性能受到严重影响，导致学习效果不佳。

**核心思路**：论文的核心思路是利用预训练的教师模型对数据进行过滤，通过计算质量评分来筛选出高质量的数据对，从而提升对比学习的效果。这样的设计能够有效减少低质量数据对模型训练的干扰。

**技术框架**：整体架构包括数据采集、教师模型训练、数据过滤和对比学习四个主要模块。首先，收集原始数据，然后训练教师模型，接着利用该模型对数据进行质量评分，最后在高质量数据上进行对比学习。

**关键创新**：最重要的技术创新点在于提出了基于教师模型的过滤机制，显著提高了对比学习的性能。与现有方法相比，该方法能够更有效地利用高质量数据，降低模型误差。

**关键设计**：在参数设置上，论文定义了数据匹配的比例$η$，并通过线性对比学习框架进行实验。损失函数设计上，采用了对比损失，确保模型能够学习到更具区分性的特征。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14230v1/figures/hist_scores.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14230v1/figures/error_vs_eta_10000000_first95trials.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14230v1/figures/plot_dfn.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，使用教师模型过滤后，模型的误差在大$η$范围内上界为$rac{1}{	ext{sqrt}{ηn}}$，在小$η$范围内上界为$rac{1}{	ext{sqrt}{n}}$，相较于未过滤情况下的误差$rac{1}{η	ext{sqrt}{n}}$，显著降低了模型的误差，验证了数据过滤的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理和多模态数据分析等。通过提升多模态对比学习的效果，能够在图像与文本的结合、视频理解等任务中实现更高的准确性和鲁棒性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The success of modern multimodal representation learning relies on internet-scale datasets. Due to the low quality of a large fraction of raw web data, data curation has become a critical step in the training pipeline. Filtering using a trained model (i.e., teacher-based filtering) has emerged as a successful solution, leveraging a pre-trained model to compute quality scores. To explain the empirical success of teacher-based filtering, we characterize the performance of filtered contrastive learning under the standard bimodal data generation model. Denoting $η\in(0,1]$ as the fraction of data with correctly matched modalities among $n$ paired samples, we utilize a linear contrastive learning setup to show a provable benefit of data filtering: $(i)$ the error without filtering is upper and lower bounded by $\frac{1}{η\sqrt{n}}$, and $(ii)$ the error with teacher-based filtering is upper bounded by $\frac{1}{\sqrt{ηn}}$ in the large $η$ regime, and by $\frac{1}{\sqrt{n}}$ in the small $η$ regime.

