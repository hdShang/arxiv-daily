---
layout: default
title: Multimodal Mixture-of-Experts for ISAC in Low-Altitude Wireless Networks
---

# Multimodal Mixture-of-Experts for ISAC in Low-Altitude Wireless Networks

**arXiv**: [2512.01750v1](https://arxiv.org/abs/2512.01750) | [PDF](https://arxiv.org/pdf/2512.01750.pdf)

**作者**: Kai Zhang, Wentao Yu, Hengtao He, Shenghui Song, Jun Zhang, Khaled B. Letaief

---

## 💡 一句话要点

**提出基于专家混合框架的多模态ISAC方法，以解决低空无线网络中动态环境下的自适应融合问题。**

**关键词**: `多模态融合` `专家混合模型` `低空无线网络` `集成感知与通信` `自适应融合` `稀疏计算`

## 📋 核心要点

1. 核心问题：现有多模态融合方法在低空动态环境中无法适应信道异质性和模态可靠性变化。
2. 方法要点：采用专家混合框架，每个模态由专用专家网络处理，轻量门控模块自适应分配融合权重。
3. 实验或效果：在三个典型ISAC任务上，框架在学习性能和训练样本效率上优于传统基线。

## 📄 摘要（原文）

> Integrated sensing and communication (ISAC) is a key enabler for low-altitude wireless networks (LAWNs), providing simultaneous environmental perception and data transmission in complex aerial scenarios. By combining heterogeneous sensing modalities such as visual, radar, lidar, and positional information, multimodal ISAC can improve both situational awareness and robustness of LAWNs. However, most existing multimodal fusion approaches use static fusion strategies that treat all modalities equally and cannot adapt to channel heterogeneity or time-varying modality reliability in dynamic low-altitude environments. To address this fundamental limitation, we propose a mixture-of-experts (MoE) framework for multimodal ISAC in LAWNs. Each modality is processed by a dedicated expert network, and a lightweight gating module adaptively assigns fusion weights according to the instantaneous informativeness and reliability of each modality. To improve scalability under the stringent energy constraints of aerial platforms, we further develop a sparse MoE variant that selectively activates only a subset of experts, thereby reducing computation overhead while preserving the benefits of adaptive fusion. Comprehensive simulations on three typical ISAC tasks in LAWNs demonstrate that the proposed frameworks consistently outperform conventional multimodal fusion baselines in terms of learning performance and training sample efficiency.

