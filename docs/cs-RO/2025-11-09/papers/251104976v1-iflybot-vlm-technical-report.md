---
layout: default
title: iFlyBot-VLM Technical Report
---

# iFlyBot-VLM Technical Report

**arXiv**: [2511.04976v1](https://arxiv.org/abs/2511.04976) | [PDF](https://arxiv.org/pdf/2511.04976.pdf)

**作者**: Xin Nie, Zhiyuan Cheng, Yuan Zhang, Chao Ji, Jiajia Wu, Yuhan Zhang, Jia Pan

---

## 💡 一句话要点

**提出iFlyBot-VLM以解决具身智能中视觉感知与运动控制的跨模态语义鸿沟**

**关键词**: `视觉语言模型` `具身智能` `跨模态语义` `操作语言` `感知-动作闭环` `基准评估`

## 📋 核心要点

1. 核心问题：高维环境感知与低层机器人运动控制间的语义鸿沟阻碍具身智能发展
2. 方法要点：将视觉空间信息抽象为可转移的操作语言，实现感知-动作闭环协调
3. 实验或效果：在10个主流基准数据集上取得最优性能，并保持模型通用能力

## 📄 摘要（原文）

> We introduce iFlyBot-VLM, a general-purpose Vision-Language Model (VLM) used
> to improve the domain of Embodied Intelligence. The central objective of
> iFlyBot-VLM is to bridge the cross-modal semantic gap between high-dimensional
> environmental perception and low-level robotic motion control. To this end, the
> model abstracts complex visual and spatial information into a body-agnostic and
> transferable Operational Language, thereby enabling seamless perception-action
> closed-loop coordination across diverse robotic platforms. The architecture of
> iFlyBot-VLM is systematically designed to realize four key functional
> capabilities essential for embodied intelligence: 1) Spatial Understanding and
> Metric Reasoning; 2) Interactive Target Grounding; 3) Action Abstraction and
> Control Parameter Generation; 4) Task Planning and Skill Sequencing. We
> envision iFlyBot-VLM as a scalable and generalizable foundation model for
> embodied AI, facilitating the progression from specialized task-oriented
> systems toward generalist, cognitively capable agents. We conducted evaluations
> on 10 current mainstream embodied intelligence-related VLM benchmark datasets,
> such as Blink and Where2Place, and achieved optimal performance while
> preserving the model's general capabilities. We will publicly release both the
> training data and model weights to foster further research and development in
> the field of Embodied Intelligence.

