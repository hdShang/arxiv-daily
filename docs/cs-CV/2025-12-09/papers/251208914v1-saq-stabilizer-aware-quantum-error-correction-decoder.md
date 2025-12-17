---
layout: default
title: SAQ: Stabilizer-Aware Quantum Error Correction Decoder
---

# SAQ: Stabilizer-Aware Quantum Error Correction Decoder

**arXiv**: [2512.08914v1](https://arxiv.org/abs/2512.08914) | [PDF](https://arxiv.org/pdf/2512.08914.pdf)

**作者**: David Zenati, Eliya Nachmani

---

## 💡 一句话要点

**提出SAQ-Decoder框架，结合Transformer学习与约束感知后处理，实现近最大似然精度和线性计算可扩展性，以解决量子纠错解码的精度-效率权衡问题。**

**关键词**: `量子纠错解码` `Transformer架构` `可微逻辑损失` `线性计算可扩展性` `toric码` `最大似然精度`

## 📋 核心要点

1. 量子纠错解码面临精度与效率的权衡，现有方法如MWPM和神经网络解码器在性能或复杂度上存在不足。
2. SAQ-Decoder采用双流Transformer架构处理综合征和逻辑信息，结合可微逻辑损失直接优化逻辑错误率。
3. 在toric码上实现近最优性能，独立噪声和去极化噪声下的错误阈值接近最大似然界限，优于现有基线。

## 📄 摘要（原文）

> Quantum Error Correction (QEC) decoding faces a fundamental accuracy-efficiency tradeoff. Classical methods like Minimum Weight Perfect Matching (MWPM) exhibit variable performance across noise models and suffer from polynomial complexity, while tensor network decoders achieve high accuracy but at prohibitively high computational cost. Recent neural decoders reduce complexity but lack the accuracy needed to compete with computationally expensive classical methods. We introduce SAQ-Decoder, a unified framework combining transformer-based learning with constraint aware post-processing that achieves both near Maximum Likelihood (ML) accuracy and linear computational scalability with respect to the syndrome size. Our approach combines a dual-stream transformer architecture that processes syndromes and logical information with asymmetric attention patterns, and a novel differentiable logical loss that directly optimizes Logical Error Rates (LER) through smooth approximations over finite fields. SAQ-Decoder achieves near-optimal performance, with error thresholds of 10.99% (independent noise) and 18.6% (depolarizing noise) on toric codes that approach the ML bounds of 11.0% and 18.9% while outperforming existing neural and classical baselines in accuracy, complexity, and parameter efficiency. Our findings establish that learned decoders can simultaneously achieve competitive decoding accuracy and computational efficiency, addressing key requirements for practical fault-tolerant quantum computing systems.

