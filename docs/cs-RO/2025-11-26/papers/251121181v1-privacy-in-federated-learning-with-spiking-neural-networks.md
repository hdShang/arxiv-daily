---
layout: default
title: Privacy in Federated Learning with Spiking Neural Networks
---

# Privacy in Federated Learning with Spiking Neural Networks

**arXiv**: [2511.21181v1](https://arxiv.org/abs/2511.21181) | [PDF](https://arxiv.org/pdf/2511.21181.pdf)

**作者**: Dogukan Aksu, Jesus Martinez del Rincon, Ihsen Alouani

---

## 💡 一句话要点

**实证研究脉冲神经网络在联邦学习中的梯度泄露隐私风险**

**关键词**: `脉冲神经网络` `联邦学习` `梯度泄露攻击` `隐私保护` `替代梯度训练` `神经形态计算`

## 📋 核心要点

1. 核心问题：联邦学习中梯度反转攻击威胁隐私，脉冲神经网络风险未知。
2. 方法要点：将梯度泄露攻击适配到脉冲域，使用替代梯度训练。
3. 实验或效果：SNN梯度重建噪声大，无法恢复时空结构，隐私风险低。

## 📄 摘要（原文）

> Spiking neural networks (SNNs) have emerged as prominent candidates for embedded and edge AI. Their inherent low power consumption makes them far more efficient than conventional ANNs in scenarios where energy budgets are tightly constrained. In parallel, federated learning (FL) has become the prevailing training paradigm in such settings, enabling on-device learning while limiting the exposure of raw data. However, gradient inversion attacks represent a critical privacy threat in FL, where sensitive training data can be reconstructed directly from shared gradients. While this vulnerability has been widely investigated in conventional ANNs, its implications for SNNs remain largely unexplored. In this work, we present the first comprehensive empirical study of gradient leakage in SNNs across diverse data domains. SNNs are inherently non-differentiable and are typically trained using surrogate gradients, which we hypothesized would be less correlated with the original input and thus less informative from a privacy perspective. To investigate this, we adapt different gradient leakage attacks to the spike domain. Our experiments reveal a striking contrast with conventional ANNs: whereas ANN gradients reliably expose salient input content, SNN gradients yield noisy, temporally inconsistent reconstructions that fail to recover meaningful spatial or temporal structure. These results indicate that the combination of event-driven dynamics and surrogate-gradient training substantially reduces gradient informativeness. To the best of our knowledge, this work provides the first systematic benchmark of gradient inversion attacks for spiking architectures, highlighting the inherent privacy-preserving potential of neuromorphic computation.

