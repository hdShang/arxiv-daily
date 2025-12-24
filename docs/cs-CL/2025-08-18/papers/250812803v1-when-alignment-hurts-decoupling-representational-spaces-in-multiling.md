---
layout: default
title: "When Alignment Hurts: Decoupling Representational Spaces in Multilingual Models"
---

# When Alignment Hurts: Decoupling Representational Spaces in Multilingual Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12803" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12803v1</a>
  <a href="https://arxiv.org/pdf/2508.12803.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12803v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12803v1', 'When Alignment Hurts: Decoupling Representational Spaces in Multilingual Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmed Elshabrawy, Hour Kaing, Haiyue Song, Alham Fikri Aji, Hideki Tanaka, Masao Utiyama, Raj Dabre

**分类**: cs.CL

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出在线变分探测框架以解决多语言模型的表示空间解耦问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `表示空间` `生成建模` `阿拉伯方言` `因果干预` `在线变分探测` `机器翻译`

## 📋 核心要点

1. 现有方法假设高资源标准语言的对齐能够帮助低资源方言的建模，但过度的表示纠缠反而会造成负面影响。
2. 论文提出了一种在线变分探测框架，能够在微调过程中持续估计标准方言的子空间，实现与该空间的有效解耦。
3. 在25种阿拉伯方言的实验中，该方法在生成质量上提升了最高4.9 chrF++，尽管在标准语言性能上存在一定的权衡。

## 📝 摘要（中文）

本研究挑战了高资源标准语言与低资源方言之间的过度对齐假设，表明与主流方言（如现代标准阿拉伯语）过度纠缠会阻碍生成建模。我们首次进行了全面的因果研究，分析并直接干预大型语言模型的内部表示几何。提出的在线变分探测框架在微调过程中持续估计标准方言的子空间，从而实现与该空间的投影解耦。尽管在标准语言性能上存在权衡，但在25种方言的生成质量上提升了最高4.9 chrF++和平均2.0的效果，提供了因果证据，证明高资源方言的子空间主导性会限制相关方言的生成能力。

## 🔬 方法详解

**问题定义**：本研究旨在解决高资源标准语言与低资源方言之间的过度对齐问题，现有方法未能有效处理这种表示空间的纠缠，导致生成模型性能下降。

**核心思路**：提出在线变分探测框架，通过持续估计标准方言的子空间，实现与该空间的投影解耦，从而改善生成模型的表现。

**技术框架**：该框架包括数据输入、模型微调、子空间估计和生成输出四个主要模块。通过对模型内部表示的干预，调整生成过程中的表示分配。

**关键创新**：最重要的技术创新在于将几何探测与信息论探测相结合，提出了子空间级别的因果干预方法，显著区别于传统的微调方法。

**关键设计**：在参数设置上，采用了动态调整的学习率和损失函数，确保在微调过程中能够有效地进行子空间的估计与解耦。

## 📊 实验亮点

实验结果显示，采用在线变分探测框架后，在25种阿拉伯方言的生成质量上提升了最高4.9 chrF++和平均2.0的效果，相较于标准微调方法，显著改善了生成能力，尽管在标准语言性能上有所权衡。

## 🎯 应用场景

该研究的潜在应用领域包括多语言机器翻译、跨方言生成任务以及其他需要处理多种语言变体的自然语言处理任务。通过优化表示空间的分配，能够提高生成模型在低资源语言上的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Alignment with high-resource standard languages is often assumed to aid the modeling of related low-resource varieties. We challenge this assumption by demonstrating that excessive representational entanglement with a dominant variety, such as Modern Standard Arabic (MSA) in relation to Arabic dialects, can actively hinder generative modeling. We present the first comprehensive causal study of this phenomenon by analyzing and directly intervening in the internal representation geometry of large language models (LLMs). Our key contribution is an online variational probing framework that continuously estimates the subspace of the standard variety during fine-tuning, enabling projection-based decoupling from this space. While our study uses Arabic as a case due to its unusually rich parallel resources across 25 dialects, the broader motivation is methodological: dialectal MT serves as a controlled proxy for generative tasks where comparable multi-variety corpora are unavailable. Across 25 dialects, our intervention improves generation quality by up to +4.9 chrF++ and +2.0 on average compared to standard fine-tuning, despite a measured tradeoff in standard-language performance. These results provide causal evidence that subspace dominance by high-resource varieties can restrict generative capacity for related varieties. More generally, we unify geometric and information-theoretic probing with subspace-level causal interventions, offering practical tools for improving generative modeling in closely related language families and, more broadly, for controlling representational allocation in multilingual and multi-domain LLMs. Code will be released.

