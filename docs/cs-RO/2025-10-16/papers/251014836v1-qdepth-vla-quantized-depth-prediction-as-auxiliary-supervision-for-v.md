---
layout: default
title: QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models
---

# QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models

**arXiv**: [2510.14836v1](https://arxiv.org/abs/2510.14836) | [PDF](https://arxiv.org/pdf/2510.14836.pdf)

**作者**: Yixuan Li, Yuhui Chen, Mingcai Zhou, Haoran Li

---

## 💡 一句话要点

**提出QDepth-VLA框架，通过量化深度预测增强VLA模型的空间推理能力**

**关键词**: `视觉-语言-动作模型` `深度预测` `空间推理` `量化表示` `辅助监督`

## 📋 核心要点

1. 现有VLA模型缺乏对3D结构的理解，影响精细操作任务性能
2. 引入辅助深度预测任务，使用VQ-VAE编码量化深度图以学习深度感知表示
3. 在仿真和真实任务中验证，提升空间推理和操作任务表现

## 📄 摘要（原文）

> Spatial perception and reasoning are crucial for Vision-Language-Action (VLA)
> models to accomplish fine-grained manipulation tasks. However, existing
> approaches often lack the ability to understand and reason over the essential
> 3D structures necessary for precise control. To address this limitation, we
> propose QDepth-VLA, a general framework that augments VLA models with an
> auxiliary depth prediction task. A dedicated depth expert is designed to
> predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder,
> enabling the model to learn depth-aware representations that capture critical
> geometric cues. Experimental results on the simulation benchmarks and
> real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning
> and competitive performance on manipulation tasks.

