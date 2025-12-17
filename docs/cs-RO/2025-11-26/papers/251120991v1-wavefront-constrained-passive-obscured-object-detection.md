---
layout: default
title: Wavefront-Constrained Passive Obscured Object Detection
---

# Wavefront-Constrained Passive Obscured Object Detection

**arXiv**: [2511.20991v1](https://arxiv.org/abs/2511.20991) | [PDF](https://arxiv.org/pdf/2511.20991.pdf)

**作者**: Zhiwen Zheng, Yiwei Ouyang, Zhao Huang, Tao Zhang, Xiaoshuai Zhang, Huiyu Zhou, Wenwen Tang, Shaowei Jiang, Jin Liu, Xingru Huang

---

## 💡 一句话要点

**提出WavePCNet以解决视场外遮挡物体检测中的波前传播建模问题**

**关键词**: `波前传播建模` `遮挡物体检测` `相干光传播` `物理驱动网络` `鲁棒性增强`

## 📋 核心要点

1. 核心问题：现有方法难以捕捉相干光传播物理，低信噪比下易收敛到非物理解
2. 方法要点：集成TriWCP和动量记忆机制，模拟波前传播并抑制扰动积累
3. 实验或效果：在四个物理数据集上验证，准确性和鲁棒性优于现有方法

## 📄 摘要（原文）

> Accurately localizing and segmenting obscured objects from faint light patterns beyond the field of view is highly challenging due to multiple scattering and medium-induced perturbations. Most existing methods, based on real-valued modeling or local convolutional operations, are inadequate for capturing the underlying physics of coherent light propagation. Moreover, under low signal-to-noise conditions, these methods often converge to non-physical solutions, severely compromising the stability and reliability of the observation. To address these challenges, we propose a novel physics-driven Wavefront Propagating Compensation Network (WavePCNet) to simulate wavefront propagation and enhance the perception of obscured objects. This WavePCNet integrates the Tri-Phase Wavefront Complex-Propagation Reprojection (TriWCP) to incorporate complex amplitude transfer operators to precisely constrain coherent propagation behavior, along with a momentum memory mechanism to effectively suppress the accumulation of perturbations. Additionally, a High-frequency Cross-layer Compensation Enhancement is introduced to construct frequency-selective pathways with multi-scale receptive fields and dynamically model structural consistency across layers, further boosting the model's robustness and interpretability under complex environmental conditions. Extensive experiments conducted on four physically collected datasets demonstrate that WavePCNet consistently outperforms state-of-the-art methods across both accuracy and robustness.

