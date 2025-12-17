---
layout: default
title: Back to Basics: Motion Representation Matters for Human Motion Generation Using Diffusion Model
---

# Back to Basics: Motion Representation Matters for Human Motion Generation Using Diffusion Model

**arXiv**: [2512.04499v1](https://arxiv.org/abs/2512.04499) | [PDF](https://arxiv.org/pdf/2512.04499.pdf)

**作者**: Yuduo Jin, Brandon Haworth

---

## 💡 一句话要点

**评估运动表示与损失函数对基于扩散模型的人体运动生成的影响**

**关键词**: `人体运动生成` `扩散模型` `运动表示` `损失函数` `训练优化`

## 📋 核心要点

1. 核心问题：研究运动表示和损失函数在人体运动生成扩散模型中的基础作用
2. 方法要点：基于代理运动扩散模型（MDM）进行实证研究，应用v损失作为预测目标
3. 实验或效果：比较六种常见运动表示的性能，分析不同配置对训练时间的影响

## 📄 摘要（原文）

> Diffusion models have emerged as a widely utilized and successful methodology in human motion synthesis. Task-oriented diffusion models have significantly advanced action-to-motion, text-to-motion, and audio-to-motion applications. In this paper, we investigate fundamental questions regarding motion representations and loss functions in a controlled study, and we enumerate the impacts of various decisions in the workflow of the generative motion diffusion model. To answer these questions, we conduct empirical studies based on a proxy motion diffusion model (MDM). We apply v loss as the prediction objective on MDM (vMDM), where v is the weighted sum of motion data and noise. We aim to enhance the understanding of latent data distributions and provide a foundation for improving the state of conditional motion diffusion models. First, we evaluate the six common motion representations in the literature and compare their performance in terms of quality and diversity metrics. Second, we compare the training time under various configurations to shed light on how to speed up the training process of motion diffusion models. Finally, we also conduct evaluation analysis on a large motion dataset. The results of our experiments indicate clear performance differences across motion representations in diverse datasets. Our results also demonstrate the impacts of distinct configurations on model training and suggest the importance and effectiveness of these decisions on the outcomes of motion diffusion models.

