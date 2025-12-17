---
layout: default
title: See, Think, Learn: A Self-Taught Multimodal Reasoner
---

# See, Think, Learn: A Self-Taught Multimodal Reasoner

**arXiv**: [2512.02456v1](https://arxiv.org/abs/2512.02456) | [PDF](https://arxiv.org/pdf/2512.02456.pdf)

**作者**: Sourabh Sharma, Sonam Gupta, Sadbhawna

---

## 💡 一句话要点

**提出See-Think-Learn自训练框架以增强视觉语言模型的多模态推理能力**

**关键词**: `视觉语言模型` `自训练` `多模态推理` `结构化推理` `负样本增强`

## 📋 核心要点

1. 核心问题：视觉语言模型在感知与推理方面存在不足，且现有方法依赖高成本标注或忽略感知。
2. 方法要点：引入结构化推理模板，先提取视觉属性再指导推理，通过自训练循环联合优化感知与推理。
3. 实验或效果：在多个领域实验中优于基线，定性分析显示其生成高质量推理依据。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have achieved remarkable progress in integrating visual perception with language understanding. However, effective multimodal reasoning requires both accurate perception and robust reasoning, and weakness in either limits the performance of VLMs. Prior efforts to enhance reasoning often depend on high-quality chain-of-thought (CoT) data, obtained via labor-intensive human annotations, costly proprietary models, or self-training methods that overlook perception. To address these limitations, we propose a simple yet effective self-training framework called See-Think-Learn (STL). At its core, STL introduces a structured reasoning template that encourages the model to see before thinking, first extracting visual attributes in textual form, then using them to guide reasoning. The framework jointly improves perception and reasoning by having the model generate and learn from its own structured rationales in a self-training loop. Furthermore, we augment the training data with negative rationales, i.e. explanations that justify why certain answer choices are incorrect, to enhance the model's ability to distinguish between correct and misleading responses. This fosters more discriminative and robust learning. Experiments across diverse domains show that STL consistently outperforms baselines trained directly only on answers or self-generated reasoning, while qualitative analysis confirms the high quality of its rationales. STL thus provides a cost-effective solution to enhance multimodal reasoning ability of VLMs.

