---
layout: default
title: COOPER: A Unified Model for Cooperative Perception and Reasoning in Spatial Intelligence
---

# COOPER: A Unified Model for Cooperative Perception and Reasoning in Spatial Intelligence

**arXiv**: [2512.04563v1](https://arxiv.org/abs/2512.04563) | [PDF](https://arxiv.org/pdf/2512.04563.pdf)

**作者**: Zefeng Zhang, Xiangzhao Hao, Hengzhu Tang, Zhenyu Zhang, Jiawei Sheng, Xiaodong Li, Zhenyang Li, Li Gao, Daiting Shi, Dawei Yin, Tingwen Liu

---

## 💡 一句话要点

**提出COOPER统一模型，通过深度与分割辅助模态及自适应交错推理增强空间智能。**

**关键词**: `多模态大语言模型` `空间推理` `辅助模态生成` `自适应推理` `深度感知` `分割增强`

## 📋 核心要点

1. 核心问题：当前MLLMs在3D感知空间推理方面存在不足，感知与推理常被孤立处理。
2. 方法要点：利用深度和分割作为辅助模态，分两阶段训练以生成辅助模态并实现自适应交错推理。
3. 实验或效果：在空间推理任务上平均提升6.91%，仅辅助模态生成变体在距离和大小估计上增益7.92%。

## 📄 摘要（原文）

> Visual Spatial Reasoning is crucial for enabling Multimodal Large Language Models (MLLMs) to understand object properties and spatial relationships, yet current models still struggle with 3D-aware reasoning. Existing approaches typically enhance either perception, by augmenting RGB inputs with auxiliary modalities such as depth and segmentation, or reasoning, by training on spatial VQA datasets and applying reinforcement learning, and thus treat these two aspects in isolation. In this work, we investigate whether a unified MLLM can develop an intrinsic ability to enhance spatial perception and, through adaptive interleaved reasoning, achieve stronger spatial intelligence. We propose \textbf{COOPER}, a unified MLLM that leverages depth and segmentation as auxiliary modalities and is trained in two stages to acquire auxiliary modality generation and adaptive, interleaved reasoning capabilities. COOPER achieves an average \textbf{6.91\%} improvement in spatial reasoning while maintaining general performance. Moreover, even a variant trained only for auxiliary modality generation attains a \textbf{7.92\%} gain on distance and size estimation, suggesting that learning to generate auxiliary modalities helps internalize spatial knowledge and strengthen spatial understanding.

