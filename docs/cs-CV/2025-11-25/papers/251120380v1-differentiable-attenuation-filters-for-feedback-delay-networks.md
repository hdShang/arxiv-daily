---
layout: default
title: Differentiable Attenuation Filters for Feedback Delay Networks
---

# Differentiable Attenuation Filters for Feedback Delay Networks

**arXiv**: [2511.20380v1](https://arxiv.org/abs/2511.20380) | [PDF](https://arxiv.org/pdf/2511.20380.pdf)

**作者**: Ilias Ibnyahya, Joshua D. Reiss

---

## 💡 一句话要点

**提出可微分衰减滤波器以优化反馈延迟网络的音频混响设计**

**关键词**: `反馈延迟网络` `可微分滤波器` `音频混响` `参数均衡器` `梯度学习`

## 📋 核心要点

1. 传统图形均衡器在反馈延迟网络中需大量滤波器，导致计算成本高
2. 使用二阶节无限脉冲响应滤波器作为参数均衡器，实现频率相关衰减控制
3. 方法可微分、参数共享，显著减少优化参数并提升性能，降低计算开销

## 📄 摘要（原文）

> We introduce a novel method for designing attenuation filters in digital audio reverberation systems based on Feedback Delay Net- works (FDNs). Our approach uses Second Order Sections (SOS) of Infinite Impulse Response (IIR) filters arranged as parametric equalizers (PEQ), enabling fine control over frequency-dependent reverberation decay. Unlike traditional graphic equalizer designs, which require numerous filters per delay line, we propose a scal- able solution where the number of filters can be adjusted. The fre- quency, gain, and quality factor (Q) parameters are shared parame- ters across delay lines and only the gain is adjusted based on delay length. This design not only reduces the number of optimization parameters, but also remains fully differentiable and compatible with gradient-based learning frameworks. Leveraging principles of analog filter design, our method allows for efficient and accu- rate filter fitting using supervised learning. Our method delivers a flexible and differentiable design, achieving state-of-the-art per- formance while significantly reducing computational cost.

