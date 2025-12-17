---
layout: default
title: Delays in Spiking Neural Networks: A State Space Model Approach
---

# Delays in Spiking Neural Networks: A State Space Model Approach

**arXiv**: [2512.01906v1](https://arxiv.org/abs/2512.01906) | [PDF](https://arxiv.org/pdf/2512.01906.pdf)

**作者**: Sanja Karilanova, Subhrakanti Dey, Ayça Özçelikkale

---

## 💡 一句话要点

**提出基于状态空间模型的延迟机制，以增强脉冲神经网络处理时序数据的能力。**

**关键词**: `脉冲神经网络` `延迟机制` `状态空间模型` `时序数据处理` `神经形态硬件`

## 📋 核心要点

1. 核心问题：脉冲神经网络中延迟机制对捕获复杂时序依赖至关重要，但现有方法可能计算效率低。
2. 方法要点：通过额外状态变量引入延迟，使神经元能访问有限输入历史，兼容LIF等标准模型。
3. 实验或效果：在SHD数据集上匹配现有延迟SNN性能，计算高效，且在小网络中显著提升性能。

## 📄 摘要（原文）

> Spiking neural networks (SNNs) are biologically inspired, event-driven models that are suitable for processing temporal data and offer energy-efficient computation when implemented on neuromorphic hardware. In SNNs, richer neuronal dynamic allows capturing more complex temporal dependencies, with delays playing a crucial role by allowing past inputs to directly influence present spiking behavior. We propose a general framework for incorporating delays into SNNs through additional state variables. The proposed mechanism enables each neuron to access a finite temporal input history. The framework is agnostic to neuron models and hence can be seamlessly integrated into standard spiking neuron models such as LIF and adLIF. We analyze how the duration of the delays and the learnable parameters associated with them affect the performance. We investigate the trade-offs in the network architecture due to additional state variables introduced by the delay mechanism. Experiments on the Spiking Heidelberg Digits (SHD) dataset show that the proposed mechanism matches the performance of existing delay-based SNNs while remaining computationally efficient. Moreover, the results illustrate that the incorporation of delays may substantially improve performance in smaller networks.

