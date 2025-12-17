---
layout: default
title: Grounding Everything in Tokens for Multimodal Large Language Models
---

# Grounding Everything in Tokens for Multimodal Large Language Models

**arXiv**: [2512.10554v1](https://arxiv.org/abs/2512.10554) | [PDF](https://arxiv.org/pdf/2512.10554.pdf)

**作者**: Xiangxuan Ren, Zhongdao Wang, Liping Hou, Pin Tang, Guoqing Wang, Chao Ma

---

## 💡 一句话要点

**提出GETok方法，通过可学习令牌增强多模态大语言模型在2D空间中的对象定位能力。**

**关键词**: `多模态大语言模型` `对象定位` `空间表示` `可学习令牌` `指代任务`

## 📋 核心要点

1. 核心问题：MLLMs的序列语言令牌难以在2D图像空间准确接地对象。
2. 方法要点：使用网格令牌和偏移令牌构建空间表示，直接嵌入空间关系。
3. 实验或效果：在多种指代任务中优于现有方法，支持监督微调和强化学习。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have made significant advancements in vision understanding and reasoning. However, the autoregressive Transformer architecture used by MLLMs requries tokenization on input images, which limits their ability to accurately ground objects within the 2D image space. This raises an important question: how can sequential language tokens be improved to better ground objects in 2D spatial space for MLLMs? To address this, we present a spatial representation method for grounding objects, namely GETok, that integrates a specialized vocabulary of learnable tokens into MLLMs. GETok first uses grid tokens to partition the image plane into structured spatial anchors, and then exploits offset tokens to enable precise and iterative refinement of localization predictions. By embedding spatial relationships directly into tokens, GETok significantly advances MLLMs in native 2D space reasoning without modifying the autoregressive architecture. Extensive experiments demonstrate that GETok achieves superior performance over the state-of-the-art methods across various referring tasks in both supervised fine-tuning and reinforcement learning settings.

