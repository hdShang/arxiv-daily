---
layout: default
title: TBT-Former: Learning Temporal Boundary Distributions for Action Localization
---

# TBT-Former: Learning Temporal Boundary Distributions for Action Localization

**arXiv**: [2512.01298v1](https://arxiv.org/abs/2512.01298) | [PDF](https://arxiv.org/pdf/2512.01298.pdf)

**作者**: Thisara Rathnayaka, Uthayasanker Thayasivam

---

## 💡 一句话要点

**提出TBT-Former，通过增强Transformer骨干、跨尺度特征融合和边界分布回归，解决动作定位中边界模糊和多尺度信息融合问题。**

**关键词**: `时序动作定位` `Transformer架构` `特征金字塔网络` `边界分布回归` `视频理解` `深度学习`

## 📋 核心要点

1. 核心问题：动作定位模型在模糊边界和多尺度信息融合上存在挑战，影响定位精度。
2. 方法要点：采用高容量Transformer骨干、跨尺度特征金字塔网络和基于广义焦点损失的边界分布回归头。
3. 实验或效果：在THUMOS14和EPIC-Kitchens 100数据集上达到新性能水平，在ActivityNet-1.3上保持竞争力。

## 📄 摘要（原文）

> Temporal Action Localization (TAL) remains a fundamental challenge in video understanding, aiming to identify the start time, end time, and category of all action instances within untrimmed videos. While recent single-stage, anchor-free models like ActionFormer have set a high standard by leveraging Transformers for temporal reasoning, they often struggle with two persistent issues: the precise localization of actions with ambiguous or "fuzzy" temporal boundaries and the effective fusion of multi-scale contextual information. In this paper, we introduce the Temporal Boundary Transformer (TBT-Former), a new architecture that directly addresses these limitations. TBT-Former enhances the strong ActionFormer baseline with three core contributions: (1) a higher-capacity scaled Transformer backbone with an increased number of attention heads and an expanded Multi-Layer Perceptron (MLP) dimension for more powerful temporal feature extraction; (2) a cross-scale feature pyramid network (FPN) that integrates a top-down pathway with lateral connections, enabling richer fusion of high-level semantics and low-level temporal details; and (3) a novel boundary distribution regression head. Inspired by the principles of Generalized Focal Loss (GFL), this new head recasts the challenging task of boundary regression as a more flexible probability distribution learning problem, allowing the model to explicitly represent and reason about boundary uncertainty. Within the paradigm of Transformer-based architectures, TBT-Former advances the formidable benchmark set by its predecessors, establishing a new level of performance on the highly competitive THUMOS14 and EPIC-Kitchens 100 datasets, while remaining competitive on the large-scale ActivityNet-1.3. Our code is available at https://github.com/aaivu/In21-S7-CS4681-AML-Research-Projects/tree/main/projects/210536K-Multi-Modal-Learning_Video-Understanding

