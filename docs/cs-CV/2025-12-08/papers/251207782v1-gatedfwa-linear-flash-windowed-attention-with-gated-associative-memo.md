---
layout: default
title: GatedFWA: Linear Flash Windowed Attention with Gated Associative Memory
---

# GatedFWA: Linear Flash Windowed Attention with Gated Associative Memory

**arXiv**: [2512.07782v1](https://arxiv.org/abs/2512.07782) | [PDF](https://arxiv.org/pdf/2512.07782.pdf)

**作者**: Jiaxu Liu, Yuhe Bai, Christos-Savvas Bouganis

---

## 💡 一句话要点

**提出GatedFWA以解决滑动窗口注意力在自回归模型中内存更新不稳定和梯度问题，保持线性效率。**

**关键词**: `自回归模型` `注意力机制` `线性复杂度` `内存门控` `梯度稳定` `语言建模`

## 📋 核心要点

1. 核心问题：滑动窗口注意力在关联内存解释下更新无界，Softmax注意力导致内存收缩和梯度消失。
2. 方法要点：引入可学习的门控机制，通过衰减偏置稳定内存更新，实现可控梯度流。
3. 实验或效果：在语言建模基准上，GatedFWA保持高吞吐量，集成压缩方法，泛化至多种自回归领域。

## 📄 摘要（原文）

> Modern autoregressive models rely on attention, yet the Softmax full attention in Transformers scales quadratically with sequence length. Sliding Window Attention (SWA) achieves linear-time encoding/decoding by constraining the attention pattern, but under an \textit{Associative Memory} interpretation, its difference-style update renders the training objective effectively \emph{unbounded}. In contrast, Softmax attention normalizes updates, leading to \emph{memory shrinkage and gradient vanishing}. We propose GatedFWA: a Memory-\underline{Gated} (\underline{F}lash) \underline{W}indowed \underline{A}ttention mechanism that preserves SWAs efficiency while stabilizing memory updates and making gradient flow controllable. In essence, GatedFWA accumulate a per-token/head gate into a decay bias added to the attention logits, acting as a learnable contraction in the memory recurrence. We implement a fused one-pass gate preprocessing and a FlashAttention-compatible kernel that injects the gate under a sliding mask, ensuring I/O efficiency and numerical stability. On language modelling benchmarks, GatedFWA delivers competitive throughput with negligible overhead and better use of global context, and it integrates cleanly with token compression/selection methods such as NSA and generalizes to various autoregressive domains.

