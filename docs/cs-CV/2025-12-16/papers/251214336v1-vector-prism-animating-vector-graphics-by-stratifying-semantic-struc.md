---
layout: default
title: Vector Prism: Animating Vector Graphics by Stratifying Semantic Structure
---

# Vector Prism: Animating Vector Graphics by Stratifying Semantic Structure

**arXiv**: [2512.14336v1](https://arxiv.org/abs/2512.14336) | [PDF](https://arxiv.org/pdf/2512.14336.pdf)

**作者**: Jooyeol Yun, Jaegul Choo

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: yeolj00.github.io/personal-projects/vector-prism

---

## 💡 一句话要点

**提出Vector Prism框架，通过恢复SVG语义结构解决矢量图形动画自动化难题**

**关键词**: `矢量图形动画` `语义结构恢复` `视觉语言模型` `统计聚合` `SVG处理` `网页设计自动化` `多模态交互`

## 📋 核心要点

1. 现有视觉语言模型处理SVG时，常因低级形状碎片化而无法识别应一起移动的语义部件，导致动画不连贯。
2. 提出Vector Prism框架，通过统计聚合多个弱部件预测来恢复SVG的语义结构，并重组为语义组。
3. 实验显示，该方法在SVG动画生成上显著优于现有方法，实现了更连贯的动画效果和可解释的交互。

## 📝 摘要（中文）

可缩放矢量图形（SVG）是现代网页设计的核心，随着网络环境日益动态化，对其动画化的需求持续增长。尽管在代码生成和运动规划方面取得了进展，但自动化矢量图形动画对视觉语言模型（VLMs）仍然具有挑战性。VLMs经常错误处理SVG，因为视觉上连贯的部分通常被分割成低级形状，这些形状几乎无法指导哪些元素应该一起移动。本文介绍了一个框架，该框架恢复了可靠SVG动画所需的语义结构，并揭示了当前VLM系统忽略的缺失层。这是通过对多个弱部件预测进行统计聚合实现的，使系统能够从噪声预测中稳定推断语义。通过将SVG重新组织为语义组，我们的方法使VLMs能够生成更加连贯的动画。我们的实验表明，与现有方法相比取得了显著提升，这表明语义恢复是解锁稳健SVG动画并支持VLMs与矢量图形之间更可解释交互的关键步骤。

## 🔬 方法详解

Vector Prism框架的核心是通过语义恢复来增强SVG动画生成。整体框架包括：首先，从视觉语言模型获取多个弱部件预测；然后，通过统计聚合这些预测，稳定推断出SVG的语义结构；最后，将SVG重新组织为语义组，为动画生成提供高层指导。关键技术创新在于利用统计方法从噪声预测中恢复语义，解决了现有方法因低级形状碎片化而忽略语义层的问题。与现有方法的主要区别在于，它不直接依赖VLM的原始输出，而是通过语义恢复步骤，使VLM能够基于语义组生成更连贯的动画。

## 📊 实验亮点

实验结果表明，Vector Prism框架在SVG动画生成任务上取得了显著提升，与现有方法相比，生成的动画更加连贯，语义恢复步骤是关键因素，支持了更可解释的模型交互。

## 🎯 应用场景

该研究主要应用于网页设计和动态内容生成领域，可自动化生成SVG动画，提升网页交互性和用户体验。潜在价值包括简化动画制作流程、支持更复杂的矢量图形动画，以及促进视觉语言模型在图形处理中的实际应用。

## 📄 摘要（原文）

> Scalable Vector Graphics (SVG) are central to modern web design, and the demand to animate them continues to grow as web environments become increasingly dynamic. Yet automating the animation of vector graphics remains challenging for vision-language models (VLMs) despite recent progress in code generation and motion planning. VLMs routinely mis-handle SVGs, since visually coherent parts are often fragmented into low-level shapes that offer little guidance of which elements should move together. In this paper, we introduce a framework that recovers the semantic structure required for reliable SVG animation and reveals the missing layer that current VLM systems overlook. This is achieved through a statistical aggregation of multiple weak part predictions, allowing the system to stably infer semantics from noisy predictions. By reorganizing SVGs into semantic groups, our approach enables VLMs to produce animations with far greater coherence. Our experiments demonstrate substantial gains over existing approaches, suggesting that semantic recovery is the key step that unlocks robust SVG animation and supports more interpretable interactions between VLMs and vector graphics.

