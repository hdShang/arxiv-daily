---
layout: default
title: mmWalk: Towards Multi-modal Multi-view Walking Assistance
---

# mmWalk: Towards Multi-modal Multi-view Walking Assistance

**arXiv**: [2510.11520v1](https://arxiv.org/abs/2510.11520) | [PDF](https://arxiv.org/pdf/2510.11520.pdf)

**作者**: Kedi Ying, Ruiping Liu, Chongyan Chen, Mingzhe Tao, Hao Shi, Kailun Yang, Jiaming Zhang, Rainer Stiefelhagen

---

## 💡 一句话要点

**提出mmWalk多模态多视图数据集以解决盲人或低视力者户外安全导航问题**

**关键词**: `多模态数据集` `户外导航` `视觉语言模型` `可访问性特征` `风险评估`

## 📋 核心要点

1. 核心问题：盲人或低视力者在复杂环境中行走缺乏整体场景理解，导致导航困难。
2. 方法要点：构建模拟多模态数据集，集成多视图传感器和可访问性特征，包含12万帧同步数据。
3. 实验或效果：评估视觉语言模型在风险任务中表现不佳，微调模型在真实数据集上验证有效性。

## 📄 摘要（原文）

> Walking assistance in extreme or complex environments remains a significant
> challenge for people with blindness or low vision (BLV), largely due to the
> lack of a holistic scene understanding. Motivated by the real-world needs of
> the BLV community, we build mmWalk, a simulated multi-modal dataset that
> integrates multi-view sensor and accessibility-oriented features for outdoor
> safe navigation. Our dataset comprises 120 manually controlled,
> scenario-categorized walking trajectories with 62k synchronized frames. It
> contains over 559k panoramic images across RGB, depth, and semantic modalities.
> Furthermore, to emphasize real-world relevance, each trajectory involves
> outdoor corner cases and accessibility-specific landmarks for BLV users.
> Additionally, we generate mmWalkVQA, a VQA benchmark with over 69k visual
> question-answer triplets across 9 categories tailored for safe and informed
> walking assistance. We evaluate state-of-the-art Vision-Language Models (VLMs)
> using zero- and few-shot settings and found they struggle with our risk
> assessment and navigational tasks. We validate our mmWalk-finetuned model on
> real-world datasets and show the effectiveness of our dataset for advancing
> multi-modal walking assistance.

