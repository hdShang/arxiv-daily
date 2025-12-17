---
layout: default
title: Revolutionizing Mixed Precision Quantization: Towards Training-free Automatic Proxy Discovery via Large Language Models
---

# Revolutionizing Mixed Precision Quantization: Towards Training-free Automatic Proxy Discovery via Large Language Models

**arXiv**: [2512.07419v1](https://arxiv.org/abs/2512.07419) | [PDF](https://arxiv.org/pdf/2512.07419.pdf)

**作者**: Haidong Kang, Jun Du, Lihong Lin

---

## 💡 一句话要点

**提出基于大语言模型的训练无关自动代理发现框架，以革新混合精度量化设计范式。**

**关键词**: `混合精度量化` `大语言模型` `训练无关优化` `自动代理发现` `强化学习` `深度学习压缩`

## 📋 核心要点

1. 核心问题：混合精度量化依赖人工设计代理或高成本优化，效率低且不灵活。
2. 方法要点：利用大语言模型自动发现代理，通过直接策略优化增强推理，形成正反馈循环。
3. 实验或效果：在主流基准测试中实现最先进性能，为混合精度量化社区提供新视角。

## 📄 摘要（原文）

> Mixed-Precision Quantization (MPQ) liberates the Deep Neural Networks (DNNs) from the Out-Of-Memory (OOM) bottleneck, which garnered increasing research attention. However, conventional methods either searched from costly differentiable optimization, which is neither efficient nor flexible, or learned a quantized DNN from the proxy (i.e., HAWQ) manually designed by human experts, which is labor-intensive and requires huge expert knowledge. Can we design a proxy without involving any human experts and training? In this paper, we provide an affirmative answer by proposing a novel Large Language Models (LLMs)-driven Training-free Automatic Proxy (dubbed TAP) discovery framework, which reforms the design paradigm of MPQ by utilizing LLMs to find superior TAP tailored for MPQ, automatically. In addition, to bridge the gap between black-box LLMs and the tough MPQ task, we ingeniously propose simple Direct Policy Optimization (DPO) based reinforcement learning to enhance LLMs' reasoning by optimizing prompts, which can construct a positive feedback loop between the LLM and the MPQ task, enabling LLMs to generate better TAP in the next evolution. Extensive experiments on mainstream benchmarks demonstrate that TAP achieves state-of-the-art performance. Finally, we truly believe that our TAP will significantly contribute to the MPQ community by providing a new perspective on LLM-driven design algorithms.

