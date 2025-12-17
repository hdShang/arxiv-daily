---
layout: default
title: VisCoP: Visual Probing for Video Domain Adaptation of Vision Language Models
---

# VisCoP: Visual Probing for Video Domain Adaptation of Vision Language Models

**arXiv**: [2510.13808v1](https://arxiv.org/abs/2510.13808) | [PDF](https://arxiv.org/pdf/2510.13808.pdf)

**作者**: Dominick Reilly, Manish Kumar Govind, Le Xue, Srijan Das

---

## 💡 一句话要点

**提出VisCoP方法，通过视觉探针实现视觉语言模型的高效视频领域适应**

**关键词**: `视觉语言模型` `领域适应` `视觉探针` `视频理解` `参数高效微调`

## 📋 核心要点

1. 核心问题：视觉语言模型在分布偏移的新领域性能下降，现有方法易导致灾难性遗忘或特征学习不足
2. 方法要点：在视觉编码器中添加可学习视觉探针，最小化预训练参数修改，实现高效领域适应
3. 实验或效果：在跨视角、跨模态和跨任务设置中，VisCoP优于现有方法，保持源域知识

## 📄 摘要（原文）

> Large Vision-Language Models (VLMs) excel at general visual reasoning tasks
> but exhibit sharp performance degradation when applied to novel domains with
> substantial distribution shifts from pretraining data. Existing domain
> adaptation approaches finetune different VLM components, but this often results
> in limited domain-specific feature learning or catastrophic forgetting of prior
> capabilities. To address these issues, we introduce Vision Contextualized
> Probing (VisCoP), which augments the VLM's vision encoder with a compact set of
> learnable visual probes. These probes enable efficient domain-specific
> adaptation with minimal modification to pretrained parameters. We evaluate
> VisCoP across three challenging domain adaptation settings-cross-view
> (exocentric to egocentric), cross-modal (RGB to depth), and cross-task (human
> understanding to robot control). Experiments show that VisCoP consistently
> outperforms existing adaptation strategies, achieving superior performance on
> target domains while effectively retaining source-domain knowledge.

