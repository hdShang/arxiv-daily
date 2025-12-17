---
layout: default
title: From Structure to Detail: Hierarchical Distillation for Efficient Diffusion Model
---

# From Structure to Detail: Hierarchical Distillation for Efficient Diffusion Model

**arXiv**: [2511.08930v1](https://arxiv.org/abs/2511.08930) | [PDF](https://arxiv.org/pdf/2511.08930.pdf)

**作者**: Hanbo Cheng, Peng Wang, Kaixiang Lei, Qi Li, Zhen Zou, Pengfei Hu, Jun Du

---

## 💡 一句话要点

**提出分层蒸馏框架以解决扩散模型推理延迟问题**

**关键词**: `扩散模型` `模型蒸馏` `推理加速` `对抗训练` `图像生成`

## 📋 核心要点

1. 扩散模型推理延迟高，轨迹与分布蒸馏方法存在权衡问题
2. 分层蒸馏结合轨迹蒸馏提供结构草图，分布蒸馏进行细节优化
3. 在ImageNet等任务中实现单步FID 2.26，媲美多步教师模型

## 📄 摘要（原文）

> The inference latency of diffusion models remains a critical barrier to their real-time application. While trajectory-based and distribution-based step distillation methods offer solutions, they present a fundamental trade-off. Trajectory-based methods preserve global structure but act as a "lossy compressor", sacrificing high-frequency details. Conversely, distribution-based methods can achieve higher fidelity but often suffer from mode collapse and unstable training. This paper recasts them from independent paradigms into synergistic components within our novel Hierarchical Distillation (HD) framework. We leverage trajectory distillation not as a final generator, but to establish a structural ``sketch", providing a near-optimal initialization for the subsequent distribution-based refinement stage. This strategy yields an ideal initial distribution that enhances the ceiling of overall performance. To further improve quality, we introduce and refine the adversarial training process. We find standard discriminator structures are ineffective at refining an already high-quality generator. To overcome this, we introduce the Adaptive Weighted Discriminator (AWD), tailored for the HD pipeline. By dynamically allocating token weights, AWD focuses on local imperfections, enabling efficient detail refinement. Our approach demonstrates state-of-the-art performance across diverse tasks. On ImageNet $256\times256$, our single-step model achieves an FID of 2.26, rivaling its 250-step teacher. It also achieves promising results on the high-resolution text-to-image MJHQ benchmark, proving its generalizability. Our method establishes a robust new paradigm for high-fidelity, single-step diffusion models.

