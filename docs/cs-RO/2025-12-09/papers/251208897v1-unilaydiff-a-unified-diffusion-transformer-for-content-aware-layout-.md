---
layout: default
title: UniLayDiff: A Unified Diffusion Transformer for Content-Aware Layout Generation
---

# UniLayDiff: A Unified Diffusion Transformer for Content-Aware Layout Generation

**arXiv**: [2512.08897v1](https://arxiv.org/abs/2512.08897) | [PDF](https://arxiv.org/pdf/2512.08897.pdf)

**作者**: Zeyang Liu, Le Wang, Sanping Zhou, Yuxuan Wu, Xiaolong Sun, Gang Hua, Haoxiang Li

---

## 💡 一句话要点

**提出UniLayDiff统一扩散Transformer，以单模型解决内容感知布局生成的多任务挑战。**

**关键词**: `内容感知布局生成` `扩散Transformer` `多模态学习` `统一模型` `条件生成`

## 📋 核心要点

1. 核心问题：现有方法无法统一处理元素类型、尺寸或关系等多样约束的布局生成子任务。
2. 方法要点：将布局约束作为独立模态，采用多模态扩散Transformer框架捕获背景、元素与约束的交互。
3. 实验或效果：在无条件到多种条件生成任务中达到最先进性能，首次统一全范围内容感知布局生成。

## 📄 摘要（原文）

> Content-aware layout generation is a critical task in graphic design automation, focused on creating visually appealing arrangements of elements that seamlessly blend with a given background image. The variety of real-world applications makes it highly challenging to develop a single model capable of unifying the diverse range of input-constrained generation sub-tasks, such as those conditioned by element types, sizes, or their relationships. Current methods either address only a subset of these tasks or necessitate separate model parameters for different conditions, failing to offer a truly unified solution. In this paper, we propose UniLayDiff: a Unified Diffusion Transformer, that for the first time, addresses various content-aware layout generation tasks with a single, end-to-end trainable model. Specifically, we treat layout constraints as a distinct modality and employ Multi-Modal Diffusion Transformer framework to capture the complex interplay between the background image, layout elements, and diverse constraints. Moreover, we integrate relation constraints through fine-tuning the model with LoRA after pretraining the model on other tasks. Such a schema not only achieves unified conditional generation but also enhances overall layout quality. Extensive experiments demonstrate that UniLayDiff achieves state-of-the-art performance across from unconditional to various conditional generation tasks and, to the best of our knowledge, is the first model to unify the full range of content-aware layout generation tasks.

