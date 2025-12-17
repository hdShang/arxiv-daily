---
layout: default
title: Realizing Fully-Integrated, Low-Power, Event-Based Pupil Tracking with Neuromorphic Hardware
---

# Realizing Fully-Integrated, Low-Power, Event-Based Pupil Tracking with Neuromorphic Hardware

**arXiv**: [2511.20175v1](https://arxiv.org/abs/2511.20175) | [PDF](https://arxiv.org/pdf/2511.20175.pdf)

**作者**: Federico Paredes-Valles, Yoshitaka Miyatani, Kirk Y. W. Scheper

---

## 💡 一句话要点

**提出集成事件感知与神经形态计算的穿戴式瞳孔追踪系统，实现超低功耗实时跟踪**

**关键词**: `事件视觉` `神经形态计算` `穿戴式系统` `瞳孔追踪` `低功耗设计` `实时推断`

## 📋 核心要点

1. 穿戴式平台难以实现高频率、低功耗的稳健眼动追踪
2. 集成事件传感器与神经形态芯片，采用量化不确定性的脉冲神经网络
3. 在原型上实现100Hz双眼追踪，平均功耗低于5mW每眼

## 📄 摘要（原文）

> Eye tracking is fundamental to numerous applications, yet achieving robust, high-frequency tracking with ultra-low power consumption remains challenging for wearable platforms. While event-based vision sensors offer microsecond resolution and sparse data streams, they have lacked fully integrated, low-power processing solutions capable of real-time inference. In this work, we present the first battery-powered, wearable pupil-center-tracking system with complete on-device integration, combining event-based sensing and neuromorphic processing on the commercially available Speck2f system-on-chip with lightweight coordinate decoding on a low-power microcontroller. Our solution features a novel uncertainty-quantifying spiking neural network with gated temporal decoding, optimized for strict memory and bandwidth constraints, complemented by systematic deployment mechanisms that bridge the reality gap. We validate our system on a new multi-user dataset and demonstrate a wearable prototype with dual neuromorphic devices achieving robust binocular pupil tracking at 100 Hz with an average power consumption below 5 mW per eye. Our work demonstrates that end-to-end neuromorphic computing enables practical, always-on eye tracking for next-generation energy-efficient wearable systems.

