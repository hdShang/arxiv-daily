---
layout: default
title: TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models
---

# TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models

**arXiv**: [2511.05275v1](https://arxiv.org/abs/2511.05275) | [PDF](https://arxiv.org/pdf/2511.05275.pdf)

**作者**: Hokyun Im, Euijin Jeong, Jianlong Fu, Andrey Kolobov, Youngwoon Lee

---

## 💡 一句话要点

**提出TwinVLA框架，通过组合单臂VLA实现数据高效的双臂操作。**

**关键词**: `双臂操作` `视觉语言动作模型` `模块化组合` `数据效率` `机器人学习`

## 📋 核心要点

1. 问题：双臂操作需大量双臂数据，但公开数据集多为单臂演示。
2. 方法：组合两个预训练单臂VLA，构建模块化双臂模型。
3. 效果：在真实与仿真任务中，优于单块模型，缩小与顶尖模型差距。

## 📄 摘要（原文）

> Vision-language-action models (VLAs) trained on large-scale robotic datasets
> have demonstrated strong performance on manipulation tasks, including bimanual
> tasks. However, because most public datasets focus on single-arm
> demonstrations, adapting VLAs for bimanual tasks typically requires substantial
> additional bimanual data and fine-tuning. To address this challenge, we
> introduce TwinVLA, a modular framework that composes two copies of a pretrained
> single-arm VLA into a coordinated bimanual VLA. Unlike monolithic
> cross-embodiment models trained on mixtures of single-arm and bimanual data,
> TwinVLA improves both data efficiency and performance by composing pretrained
> single-arm policies. Across diverse bimanual tasks in real-world and simulation
> settings, TwinVLA outperforms a comparably-sized monolithic RDT-1B model
> without requiring any bimanual pretraining. Furthermore, it narrows the gap to
> state-of-the-art model, $\pi_0$ which rely on extensive proprietary bimanual
> data and compute cost. These results establish our modular composition approach
> as a data-efficient and scalable path toward high-performance bimanual
> manipulation, leveraging public single-arm data.

