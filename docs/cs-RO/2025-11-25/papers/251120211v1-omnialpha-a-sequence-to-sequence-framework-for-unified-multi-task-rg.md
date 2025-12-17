---
layout: default
title: OmniAlpha: A Sequence-to-Sequence Framework for Unified Multi-Task RGBA Generation
---

# OmniAlpha: A Sequence-to-Sequence Framework for Unified Multi-Task RGBA Generation

**arXiv**: [2511.20211v1](https://arxiv.org/abs/2511.20211) | [PDF](https://arxiv.org/pdf/2511.20211.pdf)

**作者**: Hao Yu, Jiabo Zhan, Zile Wang, Jinglin Wang, Huaisong Zhang, Hongyu Li, Xinrui Chen, Yongxian Wei, Chun Yuan

---

## 💡 一句话要点

**提出OmniAlpha统一框架以解决RGBA图像生成与编辑的多任务需求**

**关键词**: `RGBA图像生成` `多任务学习` `扩散变换器` `序列到序列框架` `AlphaLayers数据集`

## 📋 核心要点

1. 核心问题：现有RGBA生成模型碎片化，缺乏统一多任务能力。
2. 方法要点：采用MSRoPE-BiL增强DiT，支持多RGBA层并发处理。
3. 实验效果：在AIM-500上SAD降低84.8%，人类偏好胜率超90%。

## 📄 摘要（原文）

> Generative models have excelled in RGB synthesis, but real-world applications require RGBA manipulation. This has led to a fragmented landscape: specialized, single-task models handle alpha but lack versatility, while unified multi-task frameworks are confined to the RGB domain. To bridge this critical gap, we propose OmniAlpha, the first unified, multi-task generative framework for sequence-to-sequence RGBA image generation and editing. Its architecture features MSRoPE-BiL, a novel RoPE method with a bi-directionally extendable layer axis for its Diffusion Transformer (DiT) backbone, enabling the concurrent processing of multiple input and target RGBA layers. To power this framework, we introduce AlphaLayers, a new dataset of 1,000 high-quality, multi-layer triplets, built via a novel automated synthesis and filter pipeline. Jointly training OmniAlpha on this dataset across a comprehensive suite of 21 diverse tasks, extensive experiments demonstrate that our unified approach consistently outperforms strong, specialized baselines. Most notably, OmniAlpha achieves a dramatic 84.8% relative reduction in SAD for mask-free matting on AIM-500 and wins over 90% of human preferences in layer-conditioned completion. Our work proves that a unified, multi-task model can learn a superior shared representation for RGBA, paving the way for more powerful, layer-aware generative systems.

