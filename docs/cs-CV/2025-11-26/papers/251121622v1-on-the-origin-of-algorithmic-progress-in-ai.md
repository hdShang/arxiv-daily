---
layout: default
title: On the Origin of Algorithmic Progress in AI
---

# On the Origin of Algorithmic Progress in AI

**arXiv**: [2511.21622v1](https://arxiv.org/abs/2511.21622) | [PDF](https://arxiv.org/pdf/2511.21622.pdf)

**作者**: Hans Gundlach, Alex Fogelson, Jayson Lynch, Ana Trisovic, Jonathan Rosenfeld, Anmol Sandhu, Neil Thompson

---

## 💡 一句话要点

**揭示算法效率增益与计算规模相关，解释AI训练效率提升**

**关键词**: `算法效率` `计算规模依赖` `扩展实验` `FLOP效率` `Transformer` `LSTM`

## 📋 核心要点

1. 核心问题：算法效率增益远低于预期，2012-2023年FLOP效率提升22,000倍中仅部分可解释
2. 方法要点：通过小规模消融实验和扩展实验，分析算法在计算规模下的效率差异
3. 实验或效果：LSTM到Transformer的转换贡献主要增益，效率增益达6,930倍

## 📄 摘要（原文）

> Algorithms have been estimated to increase AI training FLOP efficiency by a factor of 22,000 between 2012 and 2023 [Ho et al., 2024]. Running small-scale ablation experiments on key innovations from this time period, we are able to account for less than 10x of these gains. Surveying the broader literature, we estimate that additional innovations not included in our ablations account for less than 10x, yielding a total under 100x. This leads us to conduct scaling experiments, which reveal that much of this efficiency gap can be explained by algorithms with scale-dependent efficiency improvements. In particular, we conduct scaling experiments between LSTMs and Transformers, finding exponent differences in their compute-optimal scaling law while finding little scaling difference for many other innovations. These experiments demonstrate that - contrary to standard assumptions - an algorithm's efficiency gains are tied to compute scale. Using experimental extrapolation and literature estimates, we account for 6,930x efficiency gains over the same time period, with the scale-dependent LSTM-to-Transformer transition accounting for the majority of gains. Our results indicate that algorithmic progress for small models has been far slower than previously assumed, and that measures of algorithmic efficiency are strongly reference-dependent.

