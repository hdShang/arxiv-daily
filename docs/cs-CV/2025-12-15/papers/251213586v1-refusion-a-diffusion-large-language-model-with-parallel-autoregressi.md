---
layout: default
title: ReFusion: A Diffusion Large Language Model with Parallel Autoregressive Decoding
---

# ReFusion: A Diffusion Large Language Model with Parallel Autoregressive Decoding

**arXiv**: [2512.13586v1](https://arxiv.org/abs/2512.13586) | [PDF](https://arxiv.org/pdf/2512.13586.pdf)

**作者**: Jia-Nan Li, Jian Guan, Wei Wu, Chongxuan Li

---

## 💡 一句话要点

**提出ReFusion以解决掩码扩散模型在并行解码中的计算与生成一致性问题**

**关键词**: `并行解码` `掩码扩散模型` `自回归模型` `槽级规划` `KV缓存重用` `语言模型加速`

## 📋 核心要点

1. 核心问题：掩码扩散模型存在高计算开销和生成不连贯的缺陷，阻碍并行解码效率。
2. 方法要点：通过槽级并行解码，采用规划-填充策略，在槽级别进行扩散规划和自回归填充。
3. 实验或效果：在七个基准测试中，性能提升34%，速度平均加速18倍以上，接近自回归模型性能。

## 📄 摘要（原文）

> Autoregressive models (ARMs) are hindered by slow sequential inference. While masked diffusion models (MDMs) offer a parallel alternative, they suffer from critical drawbacks: high computational overhead from precluding Key-Value (KV) caching, and incoherent generation arising from learning dependencies over an intractable space of token combinations. To address these limitations, we introduce ReFusion, a novel masked diffusion model that achieves superior performance and efficiency by elevating parallel decoding from the token level to a higher slot level, where each slot is a fixed-length, contiguous sub-sequence. This is achieved through an iterative ``plan-and-infill'' decoding process: a diffusion-based planning step first identifies a set of weakly dependent slots, and an autoregressive infilling step then decodes these selected slots in parallel. The slot-based design simultaneously unlocks full KV cache reuse with a unified causal framework and reduces the learning complexity from the token combination space to a manageable slot-level permutation space. Extensive experiments on seven diverse benchmarks show that ReFusion not only overwhelmingly surpasses prior MDMs with 34% performance gains and an over 18$\times$ speedup on average, but also bridges the performance gap to strong ARMs while maintaining a 2.33$\times$ average speedup.

