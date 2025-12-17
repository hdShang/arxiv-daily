---
layout: default
title: Learning What to Attend First: Modality-Importance-Guided Reasoning for Reliable Multimodal Emotion Understanding
---

# Learning What to Attend First: Modality-Importance-Guided Reasoning for Reliable Multimodal Emotion Understanding

**arXiv**: [2512.02699v1](https://arxiv.org/abs/2512.02699) | [PDF](https://arxiv.org/pdf/2512.02699.pdf)

**作者**: Hyeongseop Rha, Jeong Hun Yeo, Junil Won, Se Jin Park, Yong Man Ro

---

## 💡 一句话要点

**提出MIGR框架以解决多模态情感理解中的推理漂移问题**

**关键词**: `多模态情感理解` `推理漂移` `模态重要性` `大语言模型` `可靠性优化`

## 📋 核心要点

1. 核心问题：现有方法存在推理漂移，模型过度依赖生成文本或视觉线索，导致解释与情感不一致。
2. 方法要点：引入模态重要性机制，识别情感主导模态，并重组推理序列，从关键模态开始解释。
3. 实验或效果：在DFEW基准上，将正确预测但解释不一致的比例从18.10%降至7.37%，提升推理可靠性。

## 📄 摘要（原文）

> In this paper, we present Modality-Importance-Guided Reasoning (MIGR), a framework designed to improve the reliability of reasoning-based multimodal emotion understanding in multimodal large language models. Although existing methods have advanced emotion understanding, they often suffer from reasoning drift: models gradually rely on their own generated text instead of multimodal evidence, and their explanations are overly shaped by visually initiated reasoning paths. To address these issues, we introduce Modality Importance (MI), a simple yet effective mechanism for identifying the emotion-dominant modality. Using MI, MIGR reorganizes reasoning sequences so that explanations begin from the modality most critical to the target emotion, preventing early reasoning from being misled by less informative cues. Our two-stage framework-comprising modality-aligned supervised fine-tuning and modality-aware reward optimization-encourages models to generate emotionally grounded, causally relevant, and coherence-preserving explanations. Experimental results on the DFEW benchmark show that MIGR substantially improves reasoning reliability, decreasing instances of correct predictions accompanied by emotionally inconsistent explanations from 18.10% to 7.37%. These results confirm the benefit of initiating reasoning from the emotion-dominant modality.

