---
layout: default
title: T2T-VICL: Unlocking the Boundaries of Cross-Task Visual In-Context Learning via Implicit Text-Driven VLMs
---

# T2T-VICL: Unlocking the Boundaries of Cross-Task Visual In-Context Learning via Implicit Text-Driven VLMs

**arXiv**: [2511.16107v1](https://arxiv.org/abs/2511.16107) | [PDF](https://arxiv.org/pdf/2511.16107.pdf)

**作者**: Shao-Jun Xia, Huixin Zhang, Zhengzhong Tu

---

## 💡 一句话要点

**提出T2T-VICL以解决视觉语言模型跨任务视觉上下文学习问题**

**关键词**: `视觉上下文学习` `跨任务学习` `视觉语言模型` `文本提示生成` `推理框架`

## 📋 核心要点

1. 核心问题：视觉语言模型能否在不同视觉任务间实现上下文学习
2. 方法要点：设计文本提示生成与选择机制，构建跨任务数据集
3. 实验或效果：在多个跨任务场景中取得领先或次优性能

## 📄 摘要（原文）

> In large language models (LLM), in-context learning (ICL) refers to performing new tasks by conditioning on small demonstrations provided in the input context. Recent advances in visual in-context learning (VICL) demonstrate promising capabilities for solving downstream tasks by unified vision-language models (VLMs). When the visual prompt and the target images originate from different visual tasks, can VLMs still enable VICL? In the paper, we propose a fully collaborative pipeline, i.e. T2T-VICL, for VLMs to investigate the potential of cross-task VICL. Fundamentally, we design a mechanism to generate and select text prompts that best implicitly describe the differences between two distinct low-level vision tasks, and construct the first cross-task VICL dataset. Building upon this, we propose a novel inference framework that combines perceptual score-based reasoning with traditional evaluation metrics to perform cross-task VICL. Our approach achieves top-tier results across nine cross-task scenarios and second-tier performance in ten additional scenarios, unlocking the boundaries of cross-task VICL within VLMs.

