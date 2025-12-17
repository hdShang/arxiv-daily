---
layout: default
title: Over-the-Air Semantic Alignment with Stacked Intelligent Metasurfaces
---

# Over-the-Air Semantic Alignment with Stacked Intelligent Metasurfaces

**arXiv**: [2512.05657v1](https://arxiv.org/abs/2512.05657) | [PDF](https://arxiv.org/pdf/2512.05657.pdf)

**作者**: Mario Edoardo Pandolfo, Kyriakos Stylianopoulos, George C. Alexandropoulos, Paolo Di Lorenzo

---

## 💡 一句话要点

**提出基于堆叠智能超表面的空中语义对齐框架，以降低设备计算负担。**

**关键词**: `语义通信` `堆叠智能超表面` `潜在空间对齐` `波域处理` `异构模型`

## 📋 核心要点

1. 语义通信中异构模型导致潜在表示错位，影响性能。
2. 利用堆叠智能超表面作为可训练线性算子，在波域直接对齐潜在空间。
3. 实验显示在高低信噪比下均能保持高任务准确性和鲁棒性。

## 📄 摘要（原文）

> Semantic communication systems aim to transmit task-relevant information between devices capable of artificial intelligence, but their performance can degrade when heterogeneous transmitter-receiver models produce misaligned latent representations. Existing semantic alignment methods typically rely on additional digital processing at the transmitter or receiver, increasing overall device complexity. In this work, we introduce the first over-the-air semantic alignment framework based on stacked intelligent metasurfaces (SIM), which enables latent-space alignment directly in the wave domain, reducing substantially the computational burden at the device level. We model SIMs as trainable linear operators capable of emulating both supervised linear aligners and zero-shot Parseval-frame-based equalizers. To realize these operators physically, we develop a gradient-based optimization procedure that tailors the metasurface transfer function to a desired semantic mapping. Experiments with heterogeneous vision transformer (ViT) encoders show that SIMs can accurately reproduce both supervised and zero-shot semantic equalizers, achieving up to 90% task accuracy in regimes with high signal-to-noise ratio (SNR), while maintaining strong robustness even at low SNR values.

