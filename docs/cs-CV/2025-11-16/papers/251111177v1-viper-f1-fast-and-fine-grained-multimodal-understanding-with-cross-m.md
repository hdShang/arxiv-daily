---
layout: default
title: Viper-F1: Fast and Fine-Grained Multimodal Understanding with Cross-Modal State-Space Modulation
---

# Viper-F1: Fast and Fine-Grained Multimodal Understanding with Cross-Modal State-Space Modulation

**arXiv**: [2511.11177v1](https://arxiv.org/abs/2511.11177) | [PDF](https://arxiv.org/pdf/2511.11177.pdf)

**作者**: Quoc-Huy Trinh, Mustapha Abdullahi, Do Duy Hung Trinh, Bo Zhao, Debesh Jha

---

## 💡 一句话要点

**提出Viper-F1以解决多模态模型高计算成本和细粒度视觉理解不足的问题。**

**关键词**: `多模态理解` `状态空间模型` `视觉语言模型` `高效推理` `细粒度视觉定位`

## 📋 核心要点

1. 多模态大模型计算成本高，在资源受限场景部署困难。
2. 使用液态状态空间动态替代注意力机制，并引入令牌-网格相关模块增强视觉定位。
3. 实验显示模型在多个基准测试中实现高效、准确的细粒度理解。

## 📄 摘要（原文）

> Recent advances in multimodal large language models (MLLMs) have enabled impressive progress in vision-language understanding, yet their high computational cost limits deployment in resource-constrained scenarios such as robotic manipulation, personal assistants, and smart cameras. Most existing methods rely on Transformer-based cross-attention, whose quadratic complexity hinders efficiency. Moreover, small vision-language models often struggle to precisely capture fine-grained, task-relevant visual regions, leading to degraded performance on fine-grained reasoning tasks that limit their effectiveness in the real world. To address these issues, we introduce Viper-F1, a Hybrid State-Space Vision-Language Model that replaces attention with efficient Liquid State-Space Dynamics. To further enhance visual grounding, we propose a Token-Grid Correlation Module, which computes lightweight correlations between text tokens and image patches and modulates the state-space dynamics via FiLM conditioning. This enables the model to selectively emphasize visual regions relevant to the textual prompt while maintaining linear-time inference. Experimental results across multiple benchmarks demonstrate that Viper-F1 achieves accurate, fine-grained understanding with significantly improved efficiency.

