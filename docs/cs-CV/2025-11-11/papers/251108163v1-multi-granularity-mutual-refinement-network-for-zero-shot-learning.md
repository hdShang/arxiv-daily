---
layout: default
title: Multi-Granularity Mutual Refinement Network for Zero-Shot Learning
---

# Multi-Granularity Mutual Refinement Network for Zero-Shot Learning

**arXiv**: [2511.08163v1](https://arxiv.org/abs/2511.08163) | [PDF](https://arxiv.org/pdf/2511.08163.pdf)

**作者**: Ning Wang, Long Yu, Cong Hua, Guangming Zhu, Lin Mei, Syed Afaq Ali Shah, Mohammed Bennamoun, Liang Zhang

---

## 💡 一句话要点

**提出多粒度互精炼网络以增强零样本学习中的视觉特征可迁移性**

**关键词**: `零样本学习` `多粒度特征` `视觉语义交互` `特征融合` `区域特征挖掘`

## 📋 核心要点

1. 核心问题：现有零样本学习方法忽视局部区域特征间的内在交互，影响视觉特征可迁移性。
2. 方法要点：通过解耦多粒度特征提取和跨粒度特征融合，强化区域特征的判别性和交互。
3. 实验或效果：在三个基准数据集上验证了方法的优越性和竞争力，代码已开源。

## 📄 摘要（原文）

> Zero-shot learning (ZSL) aims to recognize unseen classes with zero samples by transferring semantic knowledge from seen classes. Current approaches typically correlate global visual features with semantic information (i.e., attributes) or align local visual region features with corresponding attributes to enhance visual-semantic interactions. Although effective, these methods often overlook the intrinsic interactions between local region features, which can further improve the acquisition of transferable and explicit visual features. In this paper, we propose a network named Multi-Granularity Mutual Refinement Network (Mg-MRN), which refine discriminative and transferable visual features by learning decoupled multi-granularity features and cross-granularity feature interactions. Specifically, we design a multi-granularity feature extraction module to learn region-level discriminative features through decoupled region feature mining. Then, a cross-granularity feature fusion module strengthens the inherent interactions between region features of varying granularities. This module enhances the discriminability of representations at each granularity level by integrating region representations from adjacent hierarchies, further improving ZSL recognition performance. Extensive experiments on three popular ZSL benchmark datasets demonstrate the superiority and competitiveness of our proposed Mg-MRN method. Our code is available at https://github.com/NingWang2049/Mg-MRN.

