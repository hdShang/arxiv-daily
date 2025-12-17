---
layout: default
title: Menta: A Small Language Model for On-Device Mental Health Prediction
---

# Menta: A Small Language Model for On-Device Mental Health Prediction

**arXiv**: [2512.02716v1](https://arxiv.org/abs/2512.02716) | [PDF](https://arxiv.org/pdf/2512.02716.pdf)

**作者**: Tianyi Zhang, Xiangyuan Xue, Lingyan Ruan, Shiya Fu, Feng Xia, Simon D'Alfonso, Vassilis Kostakos, Hong Jia

---

## 💡 一句话要点

**提出Menta小型语言模型，用于社交媒体数据的设备端多任务心理健康预测。**

**关键词**: `心理健康预测` `小型语言模型` `设备端部署` `社交媒体分析` `多任务学习` `LoRA微调`

## 📋 核心要点

1. 核心问题：心理健康早期检测受限，大型语言模型部署困难，小型模型在社交媒体应用未充分探索。
2. 方法要点：基于LoRA框架、跨数据集策略和平衡精度损失，联合训练六分类任务。
3. 实验或效果：相比最佳非微调小型模型平均提升15.2%，在抑郁和压力分类上优于13B参数大型模型，设备端部署仅需约3GB内存。

## 📄 摘要（原文）

> Mental health conditions affect hundreds of millions globally, yet early detection remains limited. While large language models (LLMs) have shown promise in mental health applications, their size and computational demands hinder practical deployment. Small language models (SLMs) offer a lightweight alternative, but their use for social media--based mental health prediction remains largely underexplored. In this study, we introduce Menta, the first optimized SLM fine-tuned specifically for multi-task mental health prediction from social media data. Menta is jointly trained across six classification tasks using a LoRA-based framework, a cross-dataset strategy, and a balanced accuracy--oriented loss. Evaluated against nine state-of-the-art SLM baselines, Menta achieves an average improvement of 15.2\% across tasks covering depression, stress, and suicidality compared with the best-performing non--fine-tuned SLMs. It also achieves higher accuracy on depression and stress classification tasks compared to 13B-parameter LLMs, while being approximately 3.25x smaller. Moreover, we demonstrate real-time, on-device deployment of Menta on an iPhone 15 Pro Max, requiring only approximately 3GB RAM. Supported by a comprehensive benchmark against existing SLMs and LLMs, Menta highlights the potential for scalable, privacy-preserving mental health monitoring. Code is available at: https://xxue752-nz.github.io/menta-project/

