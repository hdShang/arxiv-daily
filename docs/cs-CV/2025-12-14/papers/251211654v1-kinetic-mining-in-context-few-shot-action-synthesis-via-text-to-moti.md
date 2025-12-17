---
layout: default
title: Kinetic Mining in Context: Few-Shot Action Synthesis via Text-to-Motion Distillation
---

# Kinetic Mining in Context: Few-Shot Action Synthesis via Text-to-Motion Distillation

**arXiv**: [2512.11654v1](https://arxiv.org/abs/2512.11654) | [PDF](https://arxiv.org/pdf/2512.11654.pdf)

**作者**: Luca Cazzola, Ahed Alboody

---

## 💡 一句话要点

**提出KineMIC框架，通过文本到运动蒸馏解决少样本动作合成问题。**

**关键词**: `少样本动作合成` `文本到运动蒸馏` `骨骼动作识别` `扩散模型微调` `数据增强`

## 📋 核心要点

1. 核心问题：通用文本到运动模型生成的动作不适合骨骼动作识别，存在领域差距。
2. 方法要点：利用CLIP文本嵌入建立语义对应，指导扩散模型微调为动作到运动生成器。
3. 实验或效果：在NTU RGB+D 120子集上，仅用每类10样本，提升准确率23.1%。

## 📄 摘要（原文）

> The acquisition cost for large, annotated motion datasets remains a critical bottleneck for skeletal-based Human Activity Recognition (HAR). Although Text-to-Motion (T2M) generative models offer a compelling, scalable source of synthetic data, their training objectives, which emphasize general artistic motion, and dataset structures fundamentally differ from HAR's requirements for kinematically precise, class-discriminative actions. This disparity creates a significant domain gap, making generalist T2M models ill-equipped for generating motions suitable for HAR classifiers. To address this challenge, we propose KineMIC (Kinetic Mining In Context), a transfer learning framework for few-shot action synthesis. KineMIC adapts a T2M diffusion model to an HAR domain by hypothesizing that semantic correspondences in the text encoding space can provide soft supervision for kinematic distillation. We operationalize this via a kinetic mining strategy that leverages CLIP text embeddings to establish correspondences between sparse HAR labels and T2M source data. This process guides fine-tuning, transforming the generalist T2M backbone into a specialized few-shot Action-to-Motion generator. We validate KineMIC using HumanML3D as the source T2M dataset and a subset of NTU RGB+D 120 as the target HAR domain, randomly selecting just 10 samples per action class. Our approach generates significantly more coherent motions, providing a robust data augmentation source that delivers a +23.1% accuracy points improvement. Animated illustrations and supplementary materials are available at (https://lucazzola.github.io/publications/kinemic).

