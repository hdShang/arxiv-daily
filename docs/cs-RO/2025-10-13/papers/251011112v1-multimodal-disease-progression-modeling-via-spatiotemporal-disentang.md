---
layout: default
title: Multimodal Disease Progression Modeling via Spatiotemporal Disentanglement and Multiscale Alignment
---

# Multimodal Disease Progression Modeling via Spatiotemporal Disentanglement and Multiscale Alignment

**arXiv**: [2510.11112v1](https://arxiv.org/abs/2510.11112) | [PDF](https://arxiv.org/pdf/2510.11112.pdf)

**作者**: Chen Liu, Wenfang Yao, Kejing Yin, William K. Cheung, Jing Qin

---

## 💡 一句话要点

**提出DiPro框架，通过时空解耦和多尺度对齐解决多模态疾病进展建模问题**

**关键词**: `多模态学习` `疾病进展建模` `时空解耦` `多尺度对齐` `电子健康记录` `胸部X光序列`

## 📋 核心要点

1. 核心问题：连续CXR序列冗余和EHR与成像数据时间不对齐阻碍疾病进展建模
2. 方法要点：解耦CXR静态与动态特征，并分层对齐EHR数据以建模进展路径
3. 实验或效果：在MIMIC数据集上实现疾病识别和ICU预测的先进性能

## 📄 摘要（原文）

> Longitudinal multimodal data, including electronic health records (EHR) and
> sequential chest X-rays (CXRs), is critical for modeling disease progression,
> yet remains underutilized due to two key challenges: (1) redundancy in
> consecutive CXR sequences, where static anatomical regions dominate over
> clinically-meaningful dynamics, and (2) temporal misalignment between sparse,
> irregular imaging and continuous EHR data. We introduce $\texttt{DiPro}$, a
> novel framework that addresses these challenges through region-aware
> disentanglement and multi-timescale alignment. First, we disentangle static
> (anatomy) and dynamic (pathology progression) features in sequential CXRs,
> prioritizing disease-relevant changes. Second, we hierarchically align these
> static and dynamic CXR features with asynchronous EHR data via local (pairwise
> interval-level) and global (full-sequence) synchronization to model coherent
> progression pathways. Extensive experiments on the MIMIC dataset demonstrate
> that $\texttt{DiPro}$ could effectively extract temporal clinical dynamics and
> achieve state-of-the-art performance on both disease progression identification
> and general ICU prediction tasks.

