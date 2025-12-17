---
layout: default
title: Enhanced Motion Forecasting with Plug-and-Play Multimodal Large Language Models
---

# Enhanced Motion Forecasting with Plug-and-Play Multimodal Large Language Models

**arXiv**: [2510.17274v1](https://arxiv.org/abs/2510.17274) | [PDF](https://arxiv.org/pdf/2510.17274.pdf)

**作者**: Katie Luo, Jingwei Ji, Tong He, Runsheng Xu, Yichen Xie, Dragomir Anguelov, Mingxing Tan

---

## 💡 一句话要点

**提出Plug-and-Forecast方法，通过多模态大语言模型增强运动预测模型以处理复杂场景**

**关键词**: `运动预测` `多模态大语言模型` `蒸馏嵌入` `自动驾驶` `零样本推理`

## 📋 核心要点

1. 核心问题：现有自动驾驶运动预测模型在多样化真实场景中泛化成本高且效果有限
2. 方法要点：设计提示从MLLMs提取结构化场景理解，蒸馏为可学习嵌入以增强预测模型
3. 实验或效果：在Waymo和nuScenes数据集上验证，无需微调即显著提升预测性能

## 📄 摘要（原文）

> Current autonomous driving systems rely on specialized models for perceiving
> and predicting motion, which demonstrate reliable performance in standard
> conditions. However, generalizing cost-effectively to diverse real-world
> scenarios remains a significant challenge. To address this, we propose
> Plug-and-Forecast (PnF), a plug-and-play approach that augments existing motion
> forecasting models with multimodal large language models (MLLMs). PnF builds on
> the insight that natural language provides a more effective way to describe and
> handle complex scenarios, enabling quick adaptation to targeted behaviors. We
> design prompts to extract structured scene understanding from MLLMs and distill
> this information into learnable embeddings to augment existing behavior
> prediction models. Our method leverages the zero-shot reasoning capabilities of
> MLLMs to achieve significant improvements in motion prediction performance,
> while requiring no fine-tuning -- making it practical to adopt. We validate our
> approach on two state-of-the-art motion forecasting models using the Waymo Open
> Motion Dataset and the nuScenes Dataset, demonstrating consistent performance
> improvements across both benchmarks.

