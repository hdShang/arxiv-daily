---
layout: default
title: A Comprehensive Study on Visual Token Redundancy for Discrete Diffusion-based Multimodal Large Language Models
---

# A Comprehensive Study on Visual Token Redundancy for Discrete Diffusion-based Multimodal Large Language Models

**arXiv**: [2511.15098v1](https://arxiv.org/abs/2511.15098) | [PDF](https://arxiv.org/pdf/2511.15098.pdf)

**作者**: Duo Li, Zuhao Yang, Xiaoqin Zhang, Ling Shao, Shijian Lu

---

## 💡 一句话要点

**研究视觉令牌冗余以优化离散扩散多模态大语言模型效率**

**关键词**: `离散扩散模型` `多模态大语言模型` `视觉令牌冗余` `剪枝优化` `推理加速` `信息损失恢复`

## 📋 核心要点

1. 核心问题：离散扩散MLLMs推理时计算开销大，忽视视觉令牌冗余。
2. 方法要点：分析冗余演化，验证剪枝对信息损失和恢复的影响。
3. 实验或效果：发现不同架构和任务下冗余特性，提出针对性加速策略。

## 📄 摘要（原文）

> Discrete diffusion-based multimodal large language models (dMLLMs) have emerged as a promising alternative to autoregressive MLLMs thanks to their advantages in parallel decoding and bidirectional context modeling, but most existing dMLLMs incur significant computational overhead during inference due to the full-sequence attention computation in each denoising step. Pioneer studies attempt to resolve this issue from a modality-agnostic perspective via key-value cache optimization or efficient sampling but most of them overlook modality-specific visual token redundancy. In this work, we conduct a comprehensive study on how visual token redundancy evolves with different dMLLM architectures and tasks and how visual token pruning affects dMLLM responses and efficiency. Specifically, our study reveals that visual redundancy emerges only in from-scratch dMLLMs while handling long-answer tasks. In addition, we validate that visual token pruning introduces non-negligible information loss in dMLLMs and only from-scratch dMLLMs can recover the lost information progressively during late denoising steps. Furthermore, our study shows that layer-skipping is promising for accelerating AR-to-diffusion dMLLMs, whereas progressive or late-step pruning is more effective for from-scratch dMLLMs. Overall, this work offers a new perspective on efficiency optimization for dMLLMs, greatly advancing their applicability across various multimodal understanding tasks.

