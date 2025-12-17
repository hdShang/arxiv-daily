---
layout: default
title: MedReason-R1: Learning to Reason for CT Diagnosis with Reinforcement Learning and Local Zoom
---

# MedReason-R1: Learning to Reason for CT Diagnosis with Reinforcement Learning and Local Zoom

**arXiv**: [2510.19626v1](https://arxiv.org/abs/2510.19626) | [PDF](https://arxiv.org/pdf/2510.19626.pdf)

**作者**: Yifan Li, Fenghe Tang, Yingtai Li, Shaohua Kevin Zhou

---

## 💡 一句话要点

**提出MedReason-R1模型，结合强化学习与局部放大，提升CT疾病诊断性能。**

**关键词**: `医学视觉语言模型` `CT疾病诊断` `强化学习` `局部放大` `数据集构建` `诊断推理`

## 📋 核心要点

1. 通用视觉语言模型在医学图像诊断中表现不佳，因缺乏高质量数据集和忽略从粗到细诊断过程。
2. 构建CT-RATE-VQA数据集，并设计MedReason-R1模型，嵌入局部放大区域以增强诊断细节。
3. 引入GRPO强化学习框架，无需昂贵人工标注，在CT诊断中达到先进性能并保持泛化能力。

## 📄 摘要（原文）

> General-purpose large Vision-Language Models (VLMs) demonstrate strong
> capabilities in generating detailed descriptions for natural images. However,
> their performance in the medical domain remains suboptimal, even for relatively
> straightforward tasks, primarily due to the lack of large-scale, high-quality,
> specialized medical imaging datasets and the neglect of the diagnostic process
> that progresses from coarse to fine-grained. To address the first issue, we
> construct the CT-RATE-VQA dataset, which has 84K QA pairs. For the second
> issue, we propose MedReason-R1, a medical VLM with explicit reasoning process
> for disease diagnosis. MedReason-R1 incorporates a novel strategy that embeds
> zoom-in disease region-of-interest areas into the image, highlighting the
> crucial role of both global localization and disease-specific details in
> enhancing the model's diagnostic performance. Furthermore, we introduce the
> GRPO reinforcement learning framework to MedReason-R1, which enables effective
> reasoning without relying on costly manual annotations. Compared to recent
> general-purpose and medical VLMs, MedReason-R1 achieves state-of-the-art
> performance in CT disease diagnosis while retaining generalization. The code,
> checkpoints, and dataset are available at:
> https://github.com/Leevan001/MedReason-R1

