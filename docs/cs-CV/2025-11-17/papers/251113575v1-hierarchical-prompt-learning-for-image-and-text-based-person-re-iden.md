---
layout: default
title: Hierarchical Prompt Learning for Image- and Text-Based Person Re-Identification
---

# Hierarchical Prompt Learning for Image- and Text-Based Person Re-Identification

**arXiv**: [2511.13575v1](https://arxiv.org/abs/2511.13575) | [PDF](https://arxiv.org/pdf/2511.13575.pdf)

**作者**: Linhan Zhou, Shuang Li, Neng Dong, Yonghang Tai, Yafei Zhang, Huafeng Li

---

## 💡 一句话要点

**提出分层提示学习框架以统一优化图像和文本行人重识别任务**

**关键词**: `行人重识别` `分层提示学习` `跨模态检索` `任务路由Transformer` `伪文本令牌`

## 📋 核心要点

1. 核心问题：图像和文本行人重识别任务分离导致表示纠缠和性能不佳
2. 方法要点：使用任务路由Transformer和分层提示生成，结合伪文本令牌增强语义对齐
3. 实验或效果：在多个基准测试中实现图像和文本行人重识别的先进性能

## 📄 摘要（原文）

> Person re-identification (ReID) aims to retrieve target pedestrian images given either visual queries (image-to-image, I2I) or textual descriptions (text-to-image, T2I). Although both tasks share a common retrieval objective, they pose distinct challenges: I2I emphasizes discriminative identity learning, while T2I requires accurate cross-modal semantic alignment. Existing methods often treat these tasks separately, which may lead to representation entanglement and suboptimal performance. To address this, we propose a unified framework named Hierarchical Prompt Learning (HPL), which leverages task-aware prompt modeling to jointly optimize both tasks. Specifically, we first introduce a Task-Routed Transformer, which incorporates dual classification tokens into a shared visual encoder to route features for I2I and T2I branches respectively. On top of this, we develop a hierarchical prompt generation scheme that integrates identity-level learnable tokens with instance-level pseudo-text tokens. These pseudo-tokens are derived from image or text features via modality-specific inversion networks, injecting fine-grained, instance-specific semantics into the prompts. Furthermore, we propose a Cross-Modal Prompt Regularization strategy to enforce semantic alignment in the prompt token space, ensuring that pseudo-prompts preserve source-modality characteristics while enhancing cross-modal transferability. Extensive experiments on multiple ReID benchmarks validate the effectiveness of our method, achieving state-of-the-art performance on both I2I and T2I tasks.

