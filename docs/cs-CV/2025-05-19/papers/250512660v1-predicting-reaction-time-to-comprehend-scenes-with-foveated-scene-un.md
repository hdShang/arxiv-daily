---
layout: default
title: Predicting Reaction Time to Comprehend Scenes with Foveated Scene Understanding Maps
---

# Predicting Reaction Time to Comprehend Scenes with Foveated Scene Understanding Maps

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12660" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12660v1</a>
  <a href="https://arxiv.org/pdf/2505.12660.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12660v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12660v1', 'Predicting Reaction Time to Comprehend Scenes with Foveated Scene Understanding Maps')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziqi Wen, Jonathan Skaza, Shravan Murlidaran, William Y. Wang, Miguel P. Eckstein

**分类**: cs.CV

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出F-SUM模型以解决场景理解反应时间预测问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `场景理解` `反应时间预测` `视觉语言模型` `注视特性` `图像可计算模型` `人机交互` `视觉注意力`

## 📋 核心要点

1. 现有模型在预测人类场景理解反应时间方面存在不足，尤其缺乏图像可计算的预测工具。
2. 本文提出的F-SUM模型通过结合注视特性与视觉语言模型，生成空间分布的场景理解图，提供了新的预测方式。
3. 实验结果表明，F-SUM评分与人类反应时间和描述准确性之间存在显著相关性，优于传统图像指标。

## 📝 摘要（中文）

尽管已有模型能够预测人类在目标搜索和视觉辨别等任务中的反应时间，但针对场景理解时间的图像可计算预测器的开发仍然是一个开放的挑战。本文提出了一种新颖的图像可计算模型，结合了人类视觉系统的注视特性与视觉语言模型（VLM），生成了基于注视位置的场景理解空间分布图（Foveated Scene Understanding Map, F-SUM）。该模型的F-SUM评分与人类反应时间和描述准确性显著相关，超越了传统图像指标的效果，展示了注视视觉处理在理解难度中的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效预测人类在场景理解中的反应时间这一具体问题。现有方法在这一领域缺乏图像可计算的预测工具，导致预测精度不足。

**核心思路**：论文的核心思路是将人类视觉系统的注视特性与视觉语言模型相结合，生成基于注视位置的场景理解图，从而更好地反映人类的理解过程。

**技术框架**：整体架构包括数据输入、视觉语言模型生成场景描述、结合注视特性生成F-SUM图、计算F-SUM评分等主要模块。

**关键创新**：最重要的技术创新在于提出了Foveated Scene Understanding Map（F-SUM），这是一个基于注视位置的空间理解图，能够更准确地反映人类的理解过程，与现有方法相比具有本质区别。

**关键设计**：在模型设计中，关键参数包括注视位置的选择、视觉语言模型的训练损失函数，以及F-SUM评分的计算方式。这些设计确保了模型能够有效捕捉场景理解的动态特性。

## 📊 实验亮点

实验结果显示，F-SUM评分与人类反应时间的相关性达到0.47，与所需的眼动次数相关性为0.51，且在时间限制下的描述准确性相关性为-0.56。这些结果显著超越了传统图像指标，如杂乱度和视觉复杂性，展示了F-SUM模型的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、自动驾驶、虚拟现实等，能够帮助系统更好地理解用户的视觉注意力和反应时间，从而优化用户体验和系统性能。未来，该模型有望在智能视觉系统中得到广泛应用，提升其理解和响应能力。

## 📄 摘要（原文）

> Although models exist that predict human response times (RTs) in tasks such as target search and visual discrimination, the development of image-computable predictors for scene understanding time remains an open challenge. Recent advances in vision-language models (VLMs), which can generate scene descriptions for arbitrary images, combined with the availability of quantitative metrics for comparing linguistic descriptions, offer a new opportunity to model human scene understanding. We hypothesize that the primary bottleneck in human scene understanding and the driving source of variability in response times across scenes is the interaction between the foveated nature of the human visual system and the spatial distribution of task-relevant visual information within an image. Based on this assumption, we propose a novel image-computable model that integrates foveated vision with VLMs to produce a spatially resolved map of scene understanding as a function of fixation location (Foveated Scene Understanding Map, or F-SUM), along with an aggregate F-SUM score. This metric correlates with average (N=17) human RTs (r=0.47) and number of saccades (r=0.51) required to comprehend a scene (across 277 scenes). The F-SUM score also correlates with average (N=16) human description accuracy (r=-0.56) in time-limited presentations. These correlations significantly exceed those of standard image-based metrics such as clutter, visual complexity, and scene ambiguity based on language entropy. Together, our work introduces a new image-computable metric for predicting human response times in scene understanding and demonstrates the importance of foveated visual processing in shaping comprehension difficulty.

