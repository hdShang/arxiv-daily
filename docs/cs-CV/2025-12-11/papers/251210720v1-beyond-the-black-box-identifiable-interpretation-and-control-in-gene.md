---
layout: default
title: Beyond the Black Box: Identifiable Interpretation and Control in Generative Models via Causal Minimality
---

# Beyond the Black Box: Identifiable Interpretation and Control in Generative Models via Causal Minimality

**arXiv**: [2512.10720v1](https://arxiv.org/abs/2512.10720) | [PDF](https://arxiv.org/pdf/2512.10720.pdf)

**作者**: Lingjing Kong, Shaoan Xie, Guangyi Chen, Yuewen Sun, Xiangchen Song, Eric P. Xing, Kun Zhang

---

## 💡 一句话要点

**提出基于因果最小性原则的生成模型可解释框架，实现可识别控制与概念提取**

**关键词**: `生成模型可解释性` `因果最小性` `潜在变量识别` `层次概念提取` `模型控制` `扩散模型`

## 📋 核心要点

1. 核心问题：生成模型作为黑盒阻碍理解与控制，现有方法缺乏理论保证
2. 方法要点：应用因果最小性原则，通过稀疏或压缩约束学习可解释的潜在表示
3. 实验或效果：在扩散视觉和自回归语言模型中提取层次概念图，实现细粒度模型引导

## 📄 摘要（原文）

> Deep generative models, while revolutionizing fields like image and text generation, largely operate as opaque black boxes, hindering human understanding, control, and alignment. While methods like sparse autoencoders (SAEs) show remarkable empirical success, they often lack theoretical guarantees, risking subjective insights. Our primary objective is to establish a principled foundation for interpretable generative models. We demonstrate that the principle of causal minimality -- favoring the simplest causal explanation -- can endow the latent representations of diffusion vision and autoregressive language models with clear causal interpretation and robust, component-wise identifiable control. We introduce a novel theoretical framework for hierarchical selection models, where higher-level concepts emerge from the constrained composition of lower-level variables, better capturing the complex dependencies in data generation. Under theoretically derived minimality conditions (manifesting as sparsity or compression constraints), we show that learned representations can be equivalent to the true latent variables of the data-generating process. Empirically, applying these constraints to leading generative models allows us to extract their innate hierarchical concept graphs, offering fresh insights into their internal knowledge organization. Furthermore, these causally grounded concepts serve as levers for fine-grained model steering, paving the way for transparent, reliable systems.

