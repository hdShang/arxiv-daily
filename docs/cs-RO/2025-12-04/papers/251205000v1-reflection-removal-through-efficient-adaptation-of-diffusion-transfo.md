---
layout: default
title: Reflection Removal through Efficient Adaptation of Diffusion Transformers
---

# Reflection Removal through Efficient Adaptation of Diffusion Transformers

**arXiv**: [2512.05000v1](https://arxiv.org/abs/2512.05000) | [PDF](https://arxiv.org/pdf/2512.05000.pdf)

**作者**: Daniyar Zakarin, Thiemo Wandel, Anton Obukhov, Dengxin Dai

---

## 💡 一句话要点

**提出基于扩散变换器的框架，通过高效适应解决单图像反射去除问题。**

**关键词**: `单图像反射去除` `扩散变换器` `物理渲染合成` `LoRA适应` `零样本基准`

## 📋 核心要点

1. 核心问题：单图像反射去除，依赖任务特定架构且数据不足。
2. 方法要点：利用预训练扩散变换器基础模型，结合物理渲染合成数据和LoRA高效适应。
3. 实验或效果：在领域内和零样本基准测试中实现最先进性能，验证了方法的可扩展性和高保真度。

## 📄 摘要（原文）

> We introduce a diffusion-transformer (DiT) framework for single-image reflection removal that leverages the generalization strengths of foundation diffusion models in the restoration setting. Rather than relying on task-specific architectures, we repurpose a pre-trained DiT-based foundation model by conditioning it on reflection-contaminated inputs and guiding it toward clean transmission layers. We systematically analyze existing reflection removal data sources for diversity, scalability, and photorealism. To address the shortage of suitable data, we construct a physically based rendering (PBR) pipeline in Blender, built around the Principled BSDF, to synthesize realistic glass materials and reflection effects. Efficient LoRA-based adaptation of the foundation model, combined with the proposed synthetic data, achieves state-of-the-art performance on in-domain and zero-shot benchmarks. These results demonstrate that pretrained diffusion transformers, when paired with physically grounded data synthesis and efficient adaptation, offer a scalable and high-fidelity solution for reflection removal. Project page: https://hf.co/spaces/huawei-bayerlab/windowseat-reflection-removal-web

