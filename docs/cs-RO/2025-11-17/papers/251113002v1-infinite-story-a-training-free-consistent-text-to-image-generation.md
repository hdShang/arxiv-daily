---
layout: default
title: Infinite-Story: A Training-Free Consistent Text-to-Image Generation
---

# Infinite-Story: A Training-Free Consistent Text-to-Image Generation

**arXiv**: [2511.13002v1](https://arxiv.org/abs/2511.13002) | [PDF](https://arxiv.org/pdf/2511.13002.pdf)

**作者**: Jihun Park, Kyoungmin Lee, Jongmin Gim, Hyeonseo Jo, Minseok Oh, Wonhyeok Choi, Kyumin Hwang, Jaeyeul Kim, Minwoo Choi, Sunghoon Im

---

## 💡 一句话要点

**提出Infinite-Story训练免费框架，解决多提示故事生成中的身份与风格不一致问题**

**关键词**: `文本到图像生成` `一致性生成` `训练免费方法` `注意力机制` `多提示故事` `快速推理`

## 📋 核心要点

1. 核心问题：多提示文本到图像生成中身份和风格不一致，现有方法需微调或推理慢
2. 方法要点：使用身份提示替换和统一注意力指导，无需训练，确保一致性与提示保真度
3. 实验或效果：在实验中实现最先进性能，推理速度比现有最快模型快6倍以上

## 📄 摘要（原文）

> We present Infinite-Story, a training-free framework for consistent text-to-image (T2I) generation tailored for multi-prompt storytelling scenarios. Built upon a scale-wise autoregressive model, our method addresses two key challenges in consistent T2I generation: identity inconsistency and style inconsistency. To overcome these issues, we introduce three complementary techniques: Identity Prompt Replacement, which mitigates context bias in text encoders to align identity attributes across prompts; and a unified attention guidance mechanism comprising Adaptive Style Injection and Synchronized Guidance Adaptation, which jointly enforce global style and identity appearance consistency while preserving prompt fidelity. Unlike prior diffusion-based approaches that require fine-tuning or suffer from slow inference, Infinite-Story operates entirely at test time, delivering high identity and style consistency across diverse prompts. Extensive experiments demonstrate that our method achieves state-of-the-art generation performance, while offering over 6X faster inference (1.72 seconds per image) than the existing fastest consistent T2I models, highlighting its effectiveness and practicality for real-world visual storytelling.

