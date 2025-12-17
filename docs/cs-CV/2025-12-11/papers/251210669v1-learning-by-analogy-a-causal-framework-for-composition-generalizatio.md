---
layout: default
title: Learning by Analogy: A Causal Framework for Composition Generalization
---

# Learning by Analogy: A Causal Framework for Composition Generalization

**arXiv**: [2512.10669v1](https://arxiv.org/abs/2512.10669) | [PDF](https://arxiv.org/pdf/2512.10669.pdf)

**作者**: Lingjing Kong, Shaoan Xie, Yang Jiao, Yetian Chen, Yanhui Guo, Simone Shao, Yan Gao, Guangyi Chen, Kun Zhang

---

## 💡 一句话要点

**提出基于因果模块化和最小变化的类比学习框架，以解决组合泛化问题。**

**关键词**: `组合泛化` `因果模块化` `分层数据生成` `类比学习` `结构可识别性`

## 📋 核心要点

1. 核心问题：组合泛化能力的数据结构和原理尚不明确，模型需理解新概念组合。
2. 方法要点：形式化类比过程，引入分层数据生成过程编码概念层次和交互机制。
3. 实验或效果：理论证明结构可识别，并在基准数据集上实现显著改进。

## 📄 摘要（原文）

> Compositional generalization -- the ability to understand and generate novel combinations of learned concepts -- enables models to extend their capabilities beyond limited experiences. While effective, the data structures and principles that enable this crucial capability remain poorly understood. We propose that compositional generalization fundamentally requires decomposing high-level concepts into basic, low-level concepts that can be recombined across similar contexts, similar to how humans draw analogies between concepts. For example, someone who has never seen a peacock eating rice can envision this scene by relating it to their previous observations of a chicken eating rice.
>   In this work, we formalize these intuitive processes using principles of causal modularity and minimal changes. We introduce a hierarchical data-generating process that naturally encodes different levels of concepts and their interaction mechanisms. Theoretically, we demonstrate that this approach enables compositional generalization supporting complex relations between composed concepts, advancing beyond prior work that assumes simpler interactions like additive effects. Critically, we also prove that this latent hierarchical structure is provably recoverable (identifiable) from observable data like text-image pairs, a necessary step for learning such a generative process. To validate our theory, we apply insights from our theoretical framework and achieve significant improvements on benchmark datasets.

