---
layout: default
title: SPEED-Q: Staged Processing with Enhanced Distillation towards Efficient Low-bit On-device VLM Quantization
---

# SPEED-Q: Staged Processing with Enhanced Distillation towards Efficient Low-bit On-device VLM Quantization

**arXiv**: [2511.08914v1](https://arxiv.org/abs/2511.08914) | [PDF](https://arxiv.org/pdf/2511.08914.pdf)

**作者**: Tianyu Guo, Shanwei Zhao, Shiai Zhu, Chenguang Ma

---

## 💡 一句话要点

**提出SPEED-Q框架以解决边缘设备上视觉语言模型的低比特量化难题**

**关键词**: `视觉语言模型` `低比特量化` `边缘设备部署` `蒸馏训练` `分阶段处理` `模型压缩`

## 📋 核心要点

1. 核心问题：视觉与语言组件量化敏感度差异大，低比特量化导致训练不稳定
2. 方法要点：采用分阶段敏感度自适应机制和蒸馏增强策略，提升量化性能与稳定性
3. 实验或效果：在2比特设置下准确率比现有方法高6倍，2/4比特均优于先前方法

## 📄 摘要（原文）

> Deploying Vision-Language Models (VLMs) on edge devices (e.g., smartphones and robots) is crucial for enabling low-latency and privacy-preserving intelligent applications. Given the resource constraints of these devices, quantization offers a promising solution by improving memory efficiency and reducing bandwidth requirements, thereby facilitating the deployment of VLMs. However, existing research has rarely explored aggressive quantization on VLMs, particularly for the models ranging from 1B to 2B parameters, which are more suitable for resource-constrained edge devices. In this paper, we propose SPEED-Q, a novel Staged Processing with Enhanced Distillation framework for VLM low-bit weight-only quantization that systematically addresses the following two critical obstacles: (1) significant discrepancies in quantization sensitivity between vision (ViT) and language (LLM) components in VLMs; (2) training instability arising from the reduced numerical precision inherent in low-bit quantization. In SPEED-Q, a staged sensitivity adaptive mechanism is introduced to effectively harmonize performance across different modalities. We further propose a distillation-enhanced quantization strategy to stabilize the training process and reduce data dependence. Together, SPEED-Q enables accurate, stable, and data-efficient quantization of complex VLMs. SPEED-Q is the first framework tailored for quantizing entire small-scale billion-parameter VLMs to low bits. Extensive experiments across multiple benchmarks demonstrate that SPEED-Q achieves up to 6x higher accuracy than existing quantization methods under 2-bit settings and consistently outperforms prior on-device VLMs under both 2-bit and 4-bit settings. Our code and models are available at https://github.com/antgroup/SPEED-Q.

