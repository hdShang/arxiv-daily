---
layout: default
title: DINOv3 as a Frozen Encoder for CRPS-Oriented Probabilistic Rainfall Nowcasting
---

# DINOv3 as a Frozen Encoder for CRPS-Oriented Probabilistic Rainfall Nowcasting

**arXiv**: [2511.10894v1](https://arxiv.org/abs/2511.10894) | [PDF](https://arxiv.org/pdf/2511.10894.pdf)

**作者**: Luciano Araujo Dourado Filho, Almir Moreira da Silva Neto, Anthony Miyaguchi, Rodrigo Pereira David, Rodrigo Tripodi Calumby, Lukáš Picek

---

## 💡 一句话要点

**提出基于DINOv3的冻结编码器方法，用于概率降雨临近预报。**

**关键词**: `概率降雨临近预报` `DINOv3编码器` `连续排序概率得分` `视频投影器` `3D-UNET基准` `Weather4Cast基准`

## 📋 核心要点

1. 核心问题：实现高效的概率降雨临近预报，预测4小时累积降雨分布。
2. 方法要点：使用预训练DINOv3编码器，结合视频投影器和轻量概率头优化CRPS。
3. 实验效果：在Weather4Cast 2025基准上，CRPS达3.5102，比最佳3D-UNET提升约26%。

## 📄 摘要（原文）

> This paper proposes a competitive and computationally efficient approach to probabilistic rainfall nowcasting. A video projector (V-JEPA Vision Transformer) associated to a lightweight probabilistic head is attached to a pre-trained satellite vision encoder (DINOv3\text{-}SAT493M) to map encoder tokens into a discrete empirical CDF (eCDF) over 4-hour accumulated rainfall. The projector-head is optimized end-to-end over the Continuous Ranked Probability Score (CRPS). As an alternative, 3D-UNET baselines trained with an aggregate Rank Probability Score and a per-pixel Gamma-Hurdle objective are used. On the Weather4Cast 2025 benchmark, the proposed method achieved a promising performance, with a CRPS of 3.5102 (CRPS), which represents $\approx$26\% in effectiveness gain against the best 3D-UNET.

