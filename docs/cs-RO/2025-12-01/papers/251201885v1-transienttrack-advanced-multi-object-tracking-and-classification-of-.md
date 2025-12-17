---
layout: default
title: TransientTrack: Advanced Multi-Object Tracking and Classification of Cancer Cells with Transient Fluorescent Signals
---

# TransientTrack: Advanced Multi-Object Tracking and Classification of Cancer Cells with Transient Fluorescent Signals

**arXiv**: [2512.01885v1](https://arxiv.org/abs/2512.01885) | [PDF](https://arxiv.org/pdf/2512.01885.pdf)

**作者**: Florian Bürger, Martim Dias Gomes, Nica Gutu, Adrián E. Granada, Noémie Moreau, Katarzyna Bozek

---

## 💡 一句话要点

**提出TransientTrack框架，用于基于瞬态荧光信号的癌细胞多目标跟踪与分类。**

**关键词**: `细胞跟踪` `瞬态荧光信号` `Transformer网络` `多目标跟踪` `卡尔曼滤波` `单细胞分析`

## 📋 核心要点

1. 核心问题：现有细胞跟踪方法难以处理瞬态荧光信号，且无法检测细胞死亡等关键事件。
2. 方法要点：结合Transformer网络、多阶段匹配和卡尔曼滤波，直接利用检测嵌入进行轻量级跟踪。
3. 实验或效果：在单细胞水平分析化疗药物疗效，实现强性能跟踪并捕获细胞分裂与死亡。

## 📄 摘要（原文）

> Tracking cells in time-lapse videos is an essential technique for monitoring cell population dynamics at a single-cell level. Current methods for cell tracking are developed on videos with mostly single, constant signals and do not detect pivotal events such as cell death. Here, we present TransientTrack, a deep learning-based framework for cell tracking in multi-channel microscopy video data with transient fluorescent signals that fluctuate over time following processes such as the circadian rhythm of cells. By identifying key cellular events - mitosis (cell division) and apoptosis (cell death) our method allows us to build complete trajectories, including cell lineage information. TransientTrack is lightweight and performs matching on cell detection embeddings directly, without the need for quantification of tracking-specific cell features. Furthermore, our approach integrates Transformer Networks, multi-stage matching using all detection boxes, and the interpolation of missing tracklets with the Kalman Filter. This unified framework achieves strong performance across diverse conditions, effectively tracking cells and capturing cell division and death. We demonstrate the use of TransientTrack in an analysis of the efficacy of a chemotherapeutic drug at a single-cell level. The proposed framework could further advance quantitative studies of cancer cell dynamics, enabling detailed characterization of treatment response and resistance mechanisms. The code is available at https://github.com/bozeklab/TransientTrack.

