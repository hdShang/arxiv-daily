---
layout: default
title: Dynamic Reflections: Probing Video Representations with Text Alignment
---

# Dynamic Reflections: Probing Video Representations with Text Alignment

**arXiv**: [2511.02767v1](https://arxiv.org/abs/2511.02767) | [PDF](https://arxiv.org/pdf/2511.02767.pdf)

**作者**: Tyler Zhu, Tengda Han, Leonidas Guibas, Viorica Pătrăucean, Maks Ovsjanikov

---

## 💡 一句话要点

**提出视频-文本对齐方法以探究视频编码器的表示能力**

**关键词**: `视频-文本对齐` `跨模态表示` `时序推理` `零样本评估` `视频编码器`

## 📋 核心要点

1. 核心问题：视频数据的时序特性在跨模态对齐中未被充分探索
2. 方法要点：引入参数化测试时缩放定律，分析视觉和文本数据丰富度的影响
3. 实验或效果：发现对齐与下游任务性能相关，提供零样本评估基准

## 📄 摘要（原文）

> The alignment of representations from different modalities has recently been
> shown to provide insights on the structural similarities and downstream
> capabilities of different encoders across diverse data types. While significant
> progress has been made in aligning images with text, the temporal nature of
> video data remains largely unexplored in this context. In this work, we conduct
> the first comprehensive study of video-text representation alignment, probing
> the capabilities of modern video and language encoders. Our findings reveal
> several key insights. First, we demonstrate that cross-modal alignment highly
> depends on the richness of both visual (static images vs. multi-frame videos)
> and text (single caption vs. a collection) data provided at test time,
> especially when using state-of-the-art video encoders. We propose parametric
> test-time scaling laws that capture this behavior and show remarkable
> predictive power against empirical observations. Secondly, we investigate the
> correlation between semantic alignment and performance on both semantic and
> non-semantic downstream tasks, providing initial evidence that strong alignment
> against text encoders may be linked to general-purpose video representation and
> understanding. Finally, we correlate temporal reasoning with cross-modal
> alignment providing a challenging test-bed for vision and language models.
> Overall, our work introduces video-text alignment as an informative zero-shot
> way to probe the representation power of different encoders for spatio-temporal
> data. Project page can be found at https://video-prh.github.io/

