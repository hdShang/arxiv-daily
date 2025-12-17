---
layout: default
title: Spatial-SSRL: Enhancing Spatial Understanding via Self-Supervised Reinforcement Learning
---

# Spatial-SSRL: Enhancing Spatial Understanding via Self-Supervised Reinforcement Learning

**arXiv**: [2510.27606v1](https://arxiv.org/abs/2510.27606) | [PDF](https://arxiv.org/pdf/2510.27606.pdf)

**作者**: Yuhong Liu, Beichen Zhang, Yuhang Zang, Yuhang Cao, Long Xing, Xiaoyi Dong, Haodong Duan, Dahua Lin, Jiaqi Wang

---

## 💡 一句话要点

**提出Spatial-SSRL以增强大型视觉语言模型的空间理解能力**

**关键词**: `自监督强化学习` `空间理解` `大型视觉语言模型` `可验证信号` `RGB-D图像`

## 📋 核心要点

1. 核心问题：大型视觉语言模型在空间理解方面存在不足，现有方法依赖高成本监督。
2. 方法要点：通过自监督强化学习，从普通图像自动生成五种可验证的空间结构任务。
3. 实验或效果：在七个基准测试中，平均准确率提升超过3.89%，保持通用视觉能力。

## 📄 摘要（原文）

> Spatial understanding remains a weakness of Large Vision-Language Models
> (LVLMs). Existing supervised fine-tuning (SFT) and recent reinforcement
> learning with verifiable rewards (RLVR) pipelines depend on costly supervision,
> specialized tools, or constrained environments that limit scale. We introduce
> Spatial-SSRL, a self-supervised RL paradigm that derives verifiable signals
> directly from ordinary RGB or RGB-D images. Spatial-SSRL automatically
> formulates five pretext tasks that capture 2D and 3D spatial structure:
> shuffled patch reordering, flipped patch recognition, cropped patch inpainting,
> regional depth ordering, and relative 3D position prediction. These tasks
> provide ground-truth answers that are easy to verify and require no human or
> LVLM annotation. Training on our tasks substantially improves spatial reasoning
> while preserving general visual capabilities. On seven spatial understanding
> benchmarks in both image and video settings, Spatial-SSRL delivers average
> accuracy gains of 4.63% (3B) and 3.89% (7B) over the Qwen2.5-VL baselines. Our
> results show that simple, intrinsic supervision enables RLVR at scale and
> provides a practical route to stronger spatial intelligence in LVLMs.

