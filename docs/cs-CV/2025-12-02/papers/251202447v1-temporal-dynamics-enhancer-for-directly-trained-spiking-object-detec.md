---
layout: default
title: Temporal Dynamics Enhancer for Directly Trained Spiking Object Detectors
---

# Temporal Dynamics Enhancer for Directly Trained Spiking Object Detectors

**arXiv**: [2512.02447v1](https://arxiv.org/abs/2512.02447) | [PDF](https://arxiv.org/pdf/2512.02447.pdf)

**作者**: Fan Luo, Zeyu Gao, Xinhao Luo, Kai Zhao, Yanfeng Lu

---

## 💡 一句话要点

**提出Temporal Dynamics Enhancer以增强脉冲神经网络在目标检测中的时序建模能力**

**关键词**: `脉冲神经网络` `目标检测` `时序建模` `能耗优化` `注意力机制`

## 📋 核心要点

1. 现有SNN输入策略导致神经元接收相似刺激，限制模型表达能力
2. TDE包含Spiking Encoder和Attention Gating Module，增强时序信息建模
3. 实验显示TDE在PASCAL VOC和EvDET200K数据集上性能提升，SDA降低能耗

## 📄 摘要（原文）

> Spiking Neural Networks (SNNs), with their brain-inspired spatiotemporal dynamics and spike-driven computation, have emerged as promising energy-efficient alternatives to Artificial Neural Networks (ANNs). However, existing SNNs typically replicate inputs directly or aggregate them into frames at fixed intervals. Such strategies lead to neurons receiving nearly identical stimuli across time steps, severely limiting the model's expressive power, particularly in complex tasks like object detection. In this work, we propose the Temporal Dynamics Enhancer (TDE) to strengthen SNNs' capacity for temporal information modeling. TDE consists of two modules: a Spiking Encoder (SE) that generates diverse input stimuli across time steps, and an Attention Gating Module (AGM) that guides the SE generation based on inter-temporal dependencies. Moreover, to eliminate the high-energy multiplication operations introduced by the AGM, we propose a Spike-Driven Attention (SDA) to reduce attention-related energy consumption. Extensive experiments demonstrate that TDE can be seamlessly integrated into existing SNN-based detectors and consistently outperforms state-of-the-art methods, achieving mAP50-95 scores of 57.7% on the static PASCAL VOC dataset and 47.6% on the neuromorphic EvDET200K dataset. In terms of energy consumption, the SDA consumes only 0.240 times the energy of conventional attention modules.

