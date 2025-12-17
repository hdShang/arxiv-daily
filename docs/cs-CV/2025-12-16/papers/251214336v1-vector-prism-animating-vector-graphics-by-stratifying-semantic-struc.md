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

**提出Vector Prism框架，通过恢复SVG语义结构解决视觉语言模型动画生成中的碎片化问题**

🎯 **匹配领域**: **强化学习**

**关键词**: `矢量图形动画` `语义结构恢复` `视觉语言模型` `统计聚合` `SVG处理` `网页设计自动化` `多模态交互` `弱预测整合`

## 📋 核心要点

1. 现有视觉语言模型处理SVG动画时，常因图形元素被分割为低级形状而无法识别语义连贯部分，导致动画生成碎片化。
2. 提出Vector Prism框架，通过统计聚合多个弱预测来恢复SVG的语义结构，并将图形重组成语义组以指导动画生成。
3. 实验显示，该方法在SVG动画生成中显著提升了连贯性，验证了语义恢复对增强VLM与矢量图形交互的关键作用。

## 📝 摘要（中文）

可缩放矢量图形（SVG）在现代网页设计中至关重要，随着网络环境日益动态化，对其动画化的需求持续增长。尽管在代码生成和运动规划方面取得了进展，但自动化矢量图形动画对视觉语言模型（VLMs）仍然具有挑战性。VLMs经常错误处理SVG，因为视觉上连贯的部分通常被分割成低级形状，这些形状几乎无法指导哪些元素应该一起移动。本文引入了一个框架，该框架恢复了可靠SVG动画所需的语义结构，并揭示了当前VLM系统忽略的缺失层。这是通过对多个弱部分预测进行统计聚合实现的，使系统能够从噪声预测中稳定推断语义。通过将SVG重新组织成语义组，我们的方法使VLMs能够生成更具连贯性的动画。实验表明，与现有方法相比，我们的方法取得了显著提升，这表明语义恢复是解锁稳健SVG动画并支持VLMs与矢量图形之间更可解释交互的关键步骤。

## 🔬 方法详解

Vector Prism框架的核心是通过分层语义结构来恢复SVG的语义信息。整体框架包括：首先，利用视觉语言模型生成多个弱部分预测，这些预测可能包含噪声；然后，通过统计聚合技术（如聚类或投票机制）将这些弱预测整合，稳定推断出SVG的语义组；最后，基于恢复的语义结构重新组织SVG元素，为动画生成提供高层指导。关键技术创新点在于引入了语义恢复层，解决了现有方法因忽略语义而导致的碎片化问题。与现有方法的主要区别在于，现有VLM系统直接处理低级形状，而Vector Prism通过中间语义层桥接，使动画生成更具连贯性和可解释性。

## 📊 实验亮点

实验结果表明，Vector Prism在SVG动画生成任务中相比基线方法取得了显著性能提升，具体表现为动画连贯性增强和错误率降低，验证了语义恢复对提升视觉语言模型处理矢量图形能力的有效性。

## 🎯 应用场景

该研究可应用于网页设计、动态图形生成、教育工具和交互式媒体等领域，通过自动化SVG动画提升用户体验和设计效率，支持更智能的视觉内容创作。

## 📄 摘要（原文）

> Scalable Vector Graphics (SVG) are central to modern web design, and the demand to animate them continues to grow as web environments become increasingly dynamic. Yet automating the animation of vector graphics remains challenging for vision-language models (VLMs) despite recent progress in code generation and motion planning. VLMs routinely mis-handle SVGs, since visually coherent parts are often fragmented into low-level shapes that offer little guidance of which elements should move together. In this paper, we introduce a framework that recovers the semantic structure required for reliable SVG animation and reveals the missing layer that current VLM systems overlook. This is achieved through a statistical aggregation of multiple weak part predictions, allowing the system to stably infer semantics from noisy predictions. By reorganizing SVGs into semantic groups, our approach enables VLMs to produce animations with far greater coherence. Our experiments demonstrate substantial gains over existing approaches, suggesting that semantic recovery is the key step that unlocks robust SVG animation and supports more interpretable interactions between VLMs and vector graphics.

