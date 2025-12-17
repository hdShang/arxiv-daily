---
layout: default
title: Learning to Think Fast and Slow for Visual Language Models
---

# Learning to Think Fast and Slow for Visual Language Models

**arXiv**: [2511.16670v1](https://arxiv.org/abs/2511.16670) | [PDF](https://arxiv.org/pdf/2511.16670.pdf)

**作者**: Chenyu Lin, Cheng Chi, Jinlin Wu, Sharon Li, Kaiyang Zhou

---

## 💡 一句话要点

**提出双模式思考方法以提升视觉语言模型的推理效率**

**关键词**: `视觉语言模型` `强化学习` `双模式思考` `推理效率` `令牌优化`

## 📋 核心要点

1. 现有视觉语言模型推理链冗长，导致计算成本过高
2. 使用强化学习训练模型根据问题难度自动切换快慢思考模式
3. 模型性能媲美先进方法，同时显著提高令牌效率

## 📄 摘要（原文）

> When confronted with complex problems, we tend to think slowly; conversely, for simple questions, we think quickly. Such a two-system thinking mechanism allows us to efficiently allocate cognitive resources, enabling quick decision-making for straightforward issues while reserving deeper analytical thinking for more intricate challenges. However, existing reasoning-oriented visual language models (VLMs), whether trained with explicit chain-of-thought annotations or rule-based RL rewards, mainly pursue lengthy, detailed reasoning chains, which often lead to excessive computational costs. In this work, we propose a simple RL approach, which enables VLMs to automatically switch between fast and slow thinking modes depending on task difficulty. The approach consists of two stages: in the first stage, we label data as either requiring fast thinking or slow thinking based on the model output length, which is inspired by the observation that pre-trained VLMs typically produce answers of varying lengths for different types of questions; in the second stage, we train the model using GRPO along with the thinking mode labels to develop dual-mode thinking. Despite its simplicity, our model, named DualMindVLM, significantly outperforms the base model and achieves performance on par with state-of-the-art visual reasoning models, while maintaining exceptionally high token efficiency.

