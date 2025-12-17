---
layout: default
title: VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation
---

# VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation

**arXiv**: [2510.23497v1](https://arxiv.org/abs/2510.23497) | [PDF](https://arxiv.org/pdf/2510.23497.pdf)

**作者**: Walid Bousselham, Hilde Kuehne, Cordelia Schmid

---

## 💡 一句话要点

**提出VOLD框架，通过在线策略蒸馏将LLMs推理能力迁移至VLMs，解决高质量图像-文本推理数据稀缺问题。**

**关键词**: `视觉语言模型` `推理迁移` `在线策略蒸馏` `强化学习` `分布对齐` `教师-学生模型`

## 📋 核心要点

1. 核心问题：高质量图像-文本推理数据稀缺，阻碍视觉语言模型复杂推理能力发展。
2. 方法要点：结合强化学习与在线策略蒸馏，利用文本教师模型指导学生模型推理轨迹。
3. 实验效果：在多个基准测试中显著超越基线模型，并提升当前最优性能。

## 📄 摘要（原文）

> Training vision-language models (VLMs) for complex reasoning remains a
> challenging task, i.a. due to the scarcity of high-quality image-text reasoning
> data. Conversely, text-based reasoning resources are abundant and scalable, but
> it is still an open question how to leveraging them for VLM reasoning. To
> address this problem, we propose VOLD, a framework to transfer reasoning
> capabilities from text-only teacher models to VLM student models. To this end,
> VOLD combines reinforcement learning via Group Relative Policy Optimization
> (GRPO) with on-policy distillation, which allows the student reasoning traces
> to be guided by the teacher model, resulting in a significant gain over using
> GRPO alone. We further show that a cold-start alignment is essential for an
> effective transfer during the online training phase in this scenario and that
> without sufficient distributional alignment between teacher and student,
> on-policy distillation fails to provide meaningful guidance. We evaluate VOLD
> across diverse benchmarks including MMMU-Pro, MathVision, MathVista, and
> LogicVista, showing that VOLD outperforms the baseline model significantly and
> improves over the state of the art by a margin. Our ablation shows the
> importance of a cold-start alignment via SFT for on-policy distillation with a
> text-only teacher.

