---
layout: default
title: NeuroSketch: An Effective Framework for Neural Decoding via Systematic Architectural Optimization
---

# NeuroSketch: An Effective Framework for Neural Decoding via Systematic Architectural Optimization

**arXiv**: [2512.09524v1](https://arxiv.org/abs/2512.09524) | [PDF](https://arxiv.org/pdf/2512.09524.pdf)

**作者**: Gaorui Zhang, Zhizhang Yuan, Jialan Yang, Junru Chen, Li Meng, Yang Yang

---

## 💡 一句话要点

**提出NeuroSketch框架，通过系统架构优化提升脑机接口中的神经解码性能。**

**关键词**: `神经解码` `脑机接口` `架构优化` `CNN-2D` `多模态实验`

## 📋 核心要点

1. 核心问题：神经解码中模型架构探索不足，影响性能提升。
2. 方法要点：从基础架构研究到宏观微观优化，基于CNN-2D进行系统设计。
3. 实验或效果：在多种模态、信号和任务上验证，达到SOTA性能。

## 📄 摘要（原文）

> Neural decoding, a critical component of Brain-Computer Interface (BCI), has recently attracted increasing research interest. Previous research has focused on leveraging signal processing and deep learning methods to enhance neural decoding performance. However, the in-depth exploration of model architectures remains underexplored, despite its proven effectiveness in other tasks such as energy forecasting and image classification. In this study, we propose NeuroSketch, an effective framework for neural decoding via systematic architecture optimization. Starting with the basic architecture study, we find that CNN-2D outperforms other architectures in neural decoding tasks and explore its effectiveness from temporal and spatial perspectives. Building on this, we optimize the architecture from macro- to micro-level, achieving improvements in performance at each step. The exploration process and model validations take over 5,000 experiments spanning three distinct modalities (visual, auditory, and speech), three types of brain signals (EEG, SEEG, and ECoG), and eight diverse decoding tasks. Experimental results indicate that NeuroSketch achieves state-of-the-art (SOTA) performance across all evaluated datasets, positioning it as a powerful tool for neural decoding. Our code and scripts are available at https://github.com/Galaxy-Dawn/NeuroSketch.

