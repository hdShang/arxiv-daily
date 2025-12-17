---
layout: default
title: Controlling changes to attention logits
---

# Controlling changes to attention logits

**arXiv**: [2511.21377v1](https://arxiv.org/abs/2511.21377) | [PDF](https://arxiv.org/pdf/2511.21377.pdf)

**作者**: Ben Anson, Laurence Aitchison

---

## 💡 一句话要点

**提出参数依赖学习率方法以解决Transformer注意力权重不稳定问题**

**关键词**: `Transformer稳定性` `注意力机制` `学习率调整` `权重控制` `MLA兼容性`

## 📋 核心要点

1. 核心问题：Transformer中查询和键权重易增长过大，导致训练不稳定
2. 方法要点：通过参数依赖学习率控制注意力logits变化，无需QK归一化
3. 实验或效果：在MLA设置中优于其他方法，性能与QK归一化竞争

## 📄 摘要（原文）

> Stability of neural network weights is critical when training transformer models. The query and key weights are particularly problematic, as they tend to grow large without any intervention. Applying normalization to queries and keys, known as `QK norm', fixes stability issues in practice, but is not always applicable. For example, QK norm is not compatible with Multi Latent Attention (MLA) because QK norm requires full materialization of queries and keys during inference, which is not done in MLA. In this paper we suggest that controlling the changes to logits is important for stability. We show that these changes are controllable by assigning parameter-dependent learning rates to the query and key weights. We find that our cheap intervention allows us to increase the base learning rate of the network, outperform other methods in the MLA setting, and achieve performance competitive with QK norm when using Multi-head Attention.

