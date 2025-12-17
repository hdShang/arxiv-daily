---
layout: default
title: Enhancing Vision-Language Models for Autonomous Driving through Task-Specific Prompting and Spatial Reasoning
---

# Enhancing Vision-Language Models for Autonomous Driving through Task-Specific Prompting and Spatial Reasoning

**arXiv**: [2510.24152v1](https://arxiv.org/abs/2510.24152) | [PDF](https://arxiv.org/pdf/2510.24152.pdf)

**作者**: Aodi Wu, Xubo Luo

---

## 💡 一句话要点

**提出任务特定提示与空间推理框架，以增强视觉语言模型在自动驾驶场景理解中的性能。**

**关键词**: `视觉语言模型` `自动驾驶` `任务特定提示` `空间推理` `多视图图像` `模型优化`

## 📋 核心要点

1. 自动驾驶场景理解中，视觉语言模型需处理多任务干扰问题。
2. 采用混合提示路由、任务特定提示、视觉组装和推理参数优化方法。
3. 在Qwen2.5-VL-72B上实现平均准确率70.87%至72.85%，提升模型鲁棒性。

## 📄 摘要（原文）

> This technical report presents our solution for the RoboSense Challenge at
> IROS 2025, which evaluates Vision-Language Models (VLMs) on autonomous driving
> scene understanding across perception, prediction, planning, and corruption
> detection tasks. We propose a systematic framework built on four core
> components. First, a Mixture-of-Prompts router classifies questions and
> dispatches them to task-specific expert prompts, eliminating interference
> across diverse question types. Second, task-specific prompts embed explicit
> coordinate systems, spatial reasoning rules, role-playing,
> Chain-of-Thought/Tree-of-Thought reasoning, and few-shot examples tailored to
> each task. Third, a visual assembly module composes multi-view images with
> object crops, magenta markers, and adaptive historical frames based on question
> requirements. Fourth, we configure model inference parameters (temperature,
> top-p, message roles) per task to optimize output quality. Implemented on
> Qwen2.5-VL-72B, our approach achieves 70.87% average accuracy on Phase-1 (clean
> data) and 72.85% on Phase-2 (corrupted data), demonstrating that structured
> prompting and spatial grounding substantially enhance VLM performance on
> safety-critical autonomous driving tasks. Code and prompt are available at
> https://github.com/wuaodi/UCAS-CSU-phase2.

