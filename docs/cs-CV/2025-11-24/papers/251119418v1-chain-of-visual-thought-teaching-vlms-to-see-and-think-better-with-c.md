---
layout: default
title: Chain-of-Visual-Thought: Teaching VLMs to See and Think Better with Continuous Visual Tokens
---

# Chain-of-Visual-Thought: Teaching VLMs to See and Think Better with Continuous Visual Tokens

**arXiv**: [2511.19418v1](https://arxiv.org/abs/2511.19418) | [PDF](https://arxiv.org/pdf/2511.19418.pdf)

**作者**: Yiming Qin, Bomin Wei, Jiaxin Ge, Konstantinos Kallidromitis, Stephanie Fu, Trevor Darrell, Xudong Wang

---

## 💡 一句话要点

**提出Chain-of-Visual-Thought框架，通过连续视觉令牌增强视觉语言模型的密集感知能力**

**关键词**: `视觉语言模型` `连续视觉令牌` `密集感知` `自回归训练` `多模态推理` `性能提升`

## 📋 核心要点

1. 当前视觉语言模型在空间推理等密集视觉感知任务上表现不佳
2. COVT使用约20个连续视觉令牌编码外观、几何等属性，并自回归预测以重构密集监督信号
3. 在多个基准测试中，集成COVT的模型性能提升3%至16%，实现更精确和可解释的多模态推理

## 📄 摘要（原文）

> Vision-Language Models (VLMs) excel at reasoning in linguistic space but struggle with perceptual understanding that requires dense visual perception, e.g., spatial reasoning and geometric awareness. This limitation stems from the fact that current VLMs have limited mechanisms to capture dense visual information across spatial dimensions. We introduce Chain-of-Visual-Thought (COVT), a framework that enables VLMs to reason not only in words but also through continuous visual tokens-compact latent representations that encode rich perceptual cues. Within a small budget of roughly 20 tokens, COVT distills knowledge from lightweight vision experts, capturing complementary properties such as 2D appearance, 3D geometry, spatial layout, and edge structure. During training, the VLM with COVT autoregressively predicts these visual tokens to reconstruct dense supervision signals (e.g., depth, segmentation, edges, and DINO features). At inference, the model reasons directly in the continuous visual token space, preserving efficiency while optionally decoding dense predictions for interpretability. Evaluated across more than ten diverse perception benchmarks, including CV-Bench, MMVP, RealWorldQA, MMStar, WorldMedQA, and HRBench, integrating COVT into strong VLMs such as Qwen2.5-VL and LLaVA consistently improves performance by 3% to 16% and demonstrates that compact continuous visual thinking enables more precise, grounded, and interpretable multimodal intelligence.

