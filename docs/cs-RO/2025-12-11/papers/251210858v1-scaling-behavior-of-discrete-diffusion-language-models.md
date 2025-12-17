---
layout: default
title: Scaling Behavior of Discrete Diffusion Language Models
---

# Scaling Behavior of Discrete Diffusion Language Models

**arXiv**: [2512.10858v1](https://arxiv.org/abs/2512.10858) | [PDF](https://arxiv.org/pdf/2512.10858.pdf)

**作者**: Dimitri von Rütte, Janis Fluri, Omead Pooladzandi, Bernhard Schölkopf, Thomas Hofmann, Antonio Orvieto

---

## 💡 一句话要点

**研究离散扩散语言模型的缩放行为，揭示噪声类型对计算效率的影响**

**关键词**: `离散扩散语言模型` `缩放行为` `噪声类型` `计算效率` `大规模训练` `语言模型对比`

## 📋 核心要点

1. 核心问题：离散扩散语言模型（DLMs）的缩放行为未充分探索，与自回归模型（ALMs）对比未知
2. 方法要点：通过平滑插值掩码与均匀扩散，研究不同噪声类型及超参数（如批大小和学习率）的影响
3. 实验或效果：均匀扩散在数据受限时计算效率更高，模型规模扩展至100亿参数，验证预测缩放行为

## 📄 摘要（原文）

> Modern LLM pre-training consumes vast amounts of compute and training data, making the scaling behavior, or scaling laws, of different models a key distinguishing factor. Discrete diffusion language models (DLMs) have been proposed as an alternative to autoregressive language models (ALMs). However, their scaling behavior has not yet been fully explored, with prior work suggesting that they require more data and compute to match the performance of ALMs.
>   We study the scaling behavior of DLMs on different noise types by smoothly interpolating between masked and uniform diffusion while paying close attention to crucial hyperparameters such as batch size and learning rate. Our experiments reveal that the scaling behavior of DLMs strongly depends on the noise type and is considerably different from ALMs. While all noise types converge to similar loss values in compute-bound scaling, we find that uniform diffusion requires more parameters and less data for compute-efficient training compared to masked diffusion, making them a promising candidate in data-bound settings. We scale our uniform diffusion model up to 10B parameters trained for $10^{22}$ FLOPs, confirming the predicted scaling behavior and making it the largest publicly known uniform diffusion model to date.

