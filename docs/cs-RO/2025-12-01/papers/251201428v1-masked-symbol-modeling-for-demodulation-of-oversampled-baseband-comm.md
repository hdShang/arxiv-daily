---
layout: default
title: Masked Symbol Modeling for Demodulation of Oversampled Baseband Communication Signals in Impulsive Noise-Dominated Channels
---

# Masked Symbol Modeling for Demodulation of Oversampled Baseband Communication Signals in Impulsive Noise-Dominated Channels

**arXiv**: [2512.01428v1](https://arxiv.org/abs/2512.01428) | [PDF](https://arxiv.org/pdf/2512.01428.pdf)

**作者**: Oguz Bedir, Nurullah Sevim, Mostafa Ibrahim, Sabit Ekin

---

## 💡 一句话要点

**提出掩码符号建模以在脉冲噪声主导信道中解调过采样基带通信信号**

**关键词**: `掩码符号建模` `Transformer网络` `基带信号解调` `脉冲噪声信道` `上下文感知物理层`

## 📋 核心要点

1. 核心问题：过采样基带信号中脉冲整形重叠导致的符号间贡献被视为噪声，而非上下文信息源。
2. 方法要点：借鉴BERT，提出掩码符号建模框架，用Transformer预测掩码符号，学习波形潜在语法。
3. 实验或效果：应用于脉冲噪声干扰下的解调任务，模型利用学习上下文推断受损段，提升解调性能。

## 📄 摘要（原文）

> Recent breakthroughs in natural language processing show that attention mechanism in Transformer networks, trained via masked-token prediction, enables models to capture the semantic context of the tokens and internalize the grammar of language. While the application of Transformers to communication systems is a burgeoning field, the notion of context within physical waveforms remains under-explored. This paper addresses that gap by re-examining inter-symbol contribution (ISC) caused by pulse-shaping overlap. Rather than treating ISC as a nuisance, we view it as a deterministic source of contextual information embedded in oversampled complex baseband signals. We propose Masked Symbol Modeling (MSM), a framework for the physical (PHY) layer inspired by Bidirectional Encoder Representations from Transformers methodology. In MSM, a subset of symbol aligned samples is randomly masked, and a Transformer predicts the missing symbol identifiers using the surrounding "in-between" samples. Through this objective, the model learns the latent syntax of complex baseband waveforms. We illustrate MSM's potential by applying it to the task of demodulating signals corrupted by impulsive noise, where the model infers corrupted segments by leveraging the learned context. Our results suggest a path toward receivers that interpret, rather than merely detect communication signals, opening new avenues for context-aware PHY layer design.

