---
layout: default
title: Do Reasoning Vision-Language Models Inversely Scale in Test-Time Compute? A Distractor-centric Empirical Analysis
---

# Do Reasoning Vision-Language Models Inversely Scale in Test-Time Compute? A Distractor-centric Empirical Analysis

**arXiv**: [2511.21397v1](https://arxiv.org/abs/2511.21397) | [PDF](https://arxiv.org/pdf/2511.21397.pdf)

**作者**: Jiyun Bae, Hyunjong Ok, Sangwoo Mo, Jaeho Lee

---

## 💡 一句话要点

**提出Idis数据集分析视觉干扰物对多模态推理模型的影响，揭示逆缩放现象。**

**关键词**: `视觉语言模型` `干扰物分析` `逆缩放现象` `视觉问答数据集` `推理长度` `偏见缓解`

## 📋 核心要点

1. 核心问题：视觉干扰物如何影响多模态模型在测试时的推理缩放。
2. 方法要点：构建Idis数据集，系统变化语义、数值和空间维度的干扰物。
3. 实验或效果：视觉干扰物降低准确率但不增加推理长度，提出提示策略缓解偏见。

## 📄 摘要（原文）

> How does irrelevant information (i.e., distractors) affect test-time scaling in vision-language models (VLMs)? Prior studies on language models have reported an inverse scaling effect, where textual distractors lead to longer but less effective reasoning. To investigate whether similar phenomena occur in multimodal settings, we introduce Idis (Images with distractors), a visual question-answering dataset that systematically varies distractors along semantic, numerical, and spatial dimensions. Our analyses reveal that visual distractors differ fundamentally from textual ones: although inverse scaling persists, adding visual distractors reduces accuracy without increasing reasoning length. We further show that tracking attribute counts within reasoning traces provides key insights into how distractors, reasoning length, and accuracy interact. Finally, we demonstrate that these trends extend to established visual bias benchmarks such as Waterbirds, and we propose a simple prompting strategy to mitigate bias-driven predictions in reasoning models.

