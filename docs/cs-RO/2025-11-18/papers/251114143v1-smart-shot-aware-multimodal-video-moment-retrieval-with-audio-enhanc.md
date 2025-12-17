---
layout: default
title: SMART: Shot-Aware Multimodal Video Moment Retrieval with Audio-Enhanced MLLM
---

# SMART: Shot-Aware Multimodal Video Moment Retrieval with Audio-Enhanced MLLM

**arXiv**: [2511.14143v1](https://arxiv.org/abs/2511.14143) | [PDF](https://arxiv.org/pdf/2511.14143.pdf)

**作者**: An Yu, Weiheng Lu, Jian Li, Zhenfei Zhang, Yunhang Shen, Felix X. -F. Ye, Ming-Ching Chang

---

## 💡 一句话要点

**提出SMART框架，通过音频增强和镜头感知压缩解决视频时刻检索中的细粒度定位问题。**

**关键词**: `视频时刻检索` `多模态大语言模型` `音频增强` `镜头感知压缩` `细粒度定位`

## 📋 核心要点

1. 核心问题：现有视频时刻检索方法依赖粗粒度时序和单一视觉模态，难以处理复杂视频。
2. 方法要点：集成音频线索和镜头级结构，采用镜头感知令牌压缩以减少冗余并保留细节。
3. 实验或效果：在Charades-STA和QVHighlights数据集上，性能超越现有方法，指标显著提升。

## 📄 摘要（原文）

> Video Moment Retrieval is a task in video understanding that aims to localize a specific temporal segment in an untrimmed video based on a natural language query. Despite recent progress in moment retrieval from videos using both traditional techniques and Multimodal Large Language Models (MLLM), most existing methods still rely on coarse temporal understanding and a single visual modality, limiting performance on complex videos. To address this, we introduce \textit{S}hot-aware \textit{M}ultimodal \textit{A}udio-enhanced \textit{R}etrieval of \textit{T}emporal \textit{S}egments (SMART), an MLLM-based framework that integrates audio cues and leverages shot-level temporal structure. SMART enriches multimodal representations by combining audio and visual features while applying \textbf{Shot-aware Token Compression}, which selectively retains high-information tokens within each shot to reduce redundancy and preserve fine-grained temporal details. We also refine prompt design to better utilize audio-visual cues. Evaluations on Charades-STA and QVHighlights show that SMART achieves significant improvements over state-of-the-art methods, including a 1.61\% increase in R1@0.5 and 2.59\% gain in R1@0.7 on Charades-STA.

