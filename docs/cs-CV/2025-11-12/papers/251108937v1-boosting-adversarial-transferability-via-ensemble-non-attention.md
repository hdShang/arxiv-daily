---
layout: default
title: Boosting Adversarial Transferability via Ensemble Non-Attention
---

# Boosting Adversarial Transferability via Ensemble Non-Attention

**arXiv**: [2511.08937v1](https://arxiv.org/abs/2511.08937) | [PDF](https://arxiv.org/pdf/2511.08937.pdf)

**作者**: Yipeng Zou, Qin Liu, Jie Wu, Yu Peng, Guo Chen, Hui Zhou, Guanghui Ye

---

## 💡 一句话要点

**提出NAMEA集成非注意力方法以提升跨架构对抗迁移性**

**关键词**: `对抗迁移性` `集成攻击` `非注意力区域` `元学习` `跨架构攻击`

## 📋 核心要点

1. 核心问题：异构模型梯度方向差异大，集成攻击迁移性差
2. 方法要点：融合注意力与非注意力区域梯度，利用元学习优化
3. 实验或效果：在ImageNet上超越AdaEA和SMER，平均提升15.0%和9.6%

## 📄 摘要（原文）

> Ensemble attacks integrate the outputs of surrogate models with diverse architectures, which can be combined with various gradient-based attacks to improve adversarial transferability. However, previous work shows unsatisfactory attack performance when transferring across heterogeneous model architectures. The main reason is that the gradient update directions of heterogeneous surrogate models differ widely, making it hard to reduce the gradient variance of ensemble models while making the best of individual model. To tackle this challenge, we design a novel ensemble attack, NAMEA, which for the first time integrates the gradients from the non-attention areas of ensemble models into the iterative gradient optimization process. Our design is inspired by the observation that the attention areas of heterogeneous models vary sharply, thus the non-attention areas of ViTs are likely to be the focus of CNNs and vice versa. Therefore, we merge the gradients respectively from the attention and non-attention areas of ensemble models so as to fuse the transfer information of CNNs and ViTs. Specifically, we pioneer a new way of decoupling the gradients of non-attention areas from those of attention areas, while merging gradients by meta-learning. Empirical evaluations on ImageNet dataset indicate that NAMEA outperforms AdaEA and SMER, the state-of-the-art ensemble attacks by an average of 15.0% and 9.6%, respectively. This work is the first attempt to explore the power of ensemble non-attention in boosting cross-architecture transferability, providing new insights into launching ensemble attacks.

