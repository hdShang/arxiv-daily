---
layout: default
title: FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via neural Action Tokenization
---

# FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via neural Action Tokenization

**arXiv**: [2512.04952v1](https://arxiv.org/abs/2512.04952) | [PDF](https://arxiv.org/pdf/2512.04952.pdf)

**作者**: Yicheng Liu, Shiduo Zhang, Zibin Dong, Baijun Ye, Tianyuan Yuan, Xiaopeng Yu, Linqi Yin, Chenhao Lu, Junhao Shi, Luca Jiang-Tao Yu, Liangtao Zheng, Tao Jiang, Jingjing Gong, Xipeng Qiu, Hang Zhao

---

## 💡 一句话要点

**提出FASTer框架以解决机器人视觉语言动作模型中动作标记化在重建保真度与推理效率间的权衡问题。**

**关键词**: `视觉语言动作模型` `动作标记化` `自回归解码` `机器人学习` `推理效率` `泛化能力`

## 📋 核心要点

1. 核心问题：自回归视觉语言动作模型的动作标记化存在重建保真度与推理效率的权衡。
2. 方法要点：FASTerVQ将动作块编码为单通道图像以捕获时空依赖，FASTerVLA基于此采用块级自回归解码和轻量动作专家。
3. 实验或效果：在模拟和真实基准测试中，FASTerVQ提供高质量重建和强泛化，FASTerVLA在推理速度和任务性能上超越先前最优模型。

## 📄 摘要（原文）

> Autoregressive vision-language-action (VLA) models have recently demonstrated strong capabilities in robotic manipulation. However, their core process of action tokenization often involves a trade-off between reconstruction fidelity and inference efficiency. We introduce FASTer, a unified framework for efficient and generalizable robot learning that integrates a learnable tokenizer with an autoregressive policy built upon it. FASTerVQ encodes action chunks as single-channel images, capturing global spatio-temporal dependencies while maintaining a high compression ratio. FASTerVLA builds on this tokenizer with block-wise autoregressive decoding and a lightweight action expert, achieving both faster inference and higher task performance. Extensive experiments across simulated and real-world benchmarks show that FASTerVQ delivers superior reconstruction quality, high token utilization, and strong cross-task and cross-embodiment generalization, while FASTerVLA further improves overall capability, surpassing previous state-of-the-art VLA models in both inference speed and task performance.

