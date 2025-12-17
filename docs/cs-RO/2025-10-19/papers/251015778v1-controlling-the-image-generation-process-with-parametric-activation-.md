---
layout: default
title: Controlling the image generation process with parametric activation functions
---

# Controlling the image generation process with parametric activation functions

**arXiv**: [2510.15778v1](https://arxiv.org/abs/2510.15778) | [PDF](https://arxiv.org/pdf/2510.15778.pdf)

**作者**: Ilia Pavlov

---

## 💡 一句话要点

**提出参数化激活函数系统，以交互方式控制图像生成模型的输出。**

**关键词**: `图像生成` `参数化激活函数` `模型交互控制` `StyleGAN2` `BigGAN` `可解释性`

## 📋 核心要点

1. 核心问题：图像生成模型内部机制缺乏可解释性和直接交互工具。
2. 方法要点：允许用户替换生成网络激活函数为参数化版本并设置参数。
3. 实验或效果：在StyleGAN2和BigGAN上演示，分别使用FFHQ和ImageNet数据集。

## 📄 摘要（原文）

> As image generative models continue to increase not only in their fidelity
> but also in their ubiquity the development of tools that leverage direct
> interaction with their internal mechanisms in an interpretable way has received
> little attention In this work we introduce a system that allows users to
> develop a better understanding of the model through interaction and
> experimentation By giving users the ability to replace activation functions of
> a generative network with parametric ones and a way to set the parameters of
> these functions we introduce an alternative approach to control the networks
> output We demonstrate the use of our method on StyleGAN2 and BigGAN networks
> trained on FFHQ and ImageNet respectively.

