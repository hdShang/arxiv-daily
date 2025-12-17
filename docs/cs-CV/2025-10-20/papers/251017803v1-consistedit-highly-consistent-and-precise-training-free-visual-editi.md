---
layout: default
title: ConsistEdit: Highly Consistent and Precise Training-free Visual Editing
---

# ConsistEdit: Highly Consistent and Precise Training-free Visual Editing

**arXiv**: [2510.17803v1](https://arxiv.org/abs/2510.17803) | [PDF](https://arxiv.org/pdf/2510.17803.pdf)

**作者**: Zixin Yin, Ling-Hao Chen, Lionel Ni, Xili Dai

---

## 💡 一句话要点

**提出ConsistEdit方法，基于MM-DiT实现高一致性和精确的无训练视觉编辑**

**关键词**: `无训练视觉编辑` `注意力控制` `MM-DiT模型` `多轮编辑` `视频编辑`

## 📋 核心要点

1. 当前无训练注意力控制方法在编辑强度与源一致性间难以平衡，影响多轮和视频编辑
2. 通过视觉专用注意力控制、掩码引导预融合和QKV差异化操作，提升编辑一致性和对齐性
3. 实验显示在图像和视频编辑任务中达到SOTA，支持多轮、多区域和渐进结构控制

## 📄 摘要（原文）

> Recent advances in training-free attention control methods have enabled
> flexible and efficient text-guided editing capabilities for existing generation
> models. However, current approaches struggle to simultaneously deliver strong
> editing strength while preserving consistency with the source. This limitation
> becomes particularly critical in multi-round and video editing, where visual
> errors can accumulate over time. Moreover, most existing methods enforce global
> consistency, which limits their ability to modify individual attributes such as
> texture while preserving others, thereby hindering fine-grained editing.
> Recently, the architectural shift from U-Net to MM-DiT has brought significant
> improvements in generative performance and introduced a novel mechanism for
> integrating text and vision modalities. These advancements pave the way for
> overcoming challenges that previous methods failed to resolve. Through an
> in-depth analysis of MM-DiT, we identify three key insights into its attention
> mechanisms. Building on these, we propose ConsistEdit, a novel attention
> control method specifically tailored for MM-DiT. ConsistEdit incorporates
> vision-only attention control, mask-guided pre-attention fusion, and
> differentiated manipulation of the query, key, and value tokens to produce
> consistent, prompt-aligned edits. Extensive experiments demonstrate that
> ConsistEdit achieves state-of-the-art performance across a wide range of image
> and video editing tasks, including both structure-consistent and
> structure-inconsistent scenarios. Unlike prior methods, it is the first
> approach to perform editing across all inference steps and attention layers
> without handcraft, significantly enhancing reliability and consistency, which
> enables robust multi-round and multi-region editing. Furthermore, it supports
> progressive adjustment of structural consistency, enabling finer control.

