---
layout: default
title: CounterVQA: Evaluating and Improving Counterfactual Reasoning in Vision-Language Models for Video Understanding
---

# CounterVQA: Evaluating and Improving Counterfactual Reasoning in Vision-Language Models for Video Understanding

**arXiv**: [2511.19923v1](https://arxiv.org/abs/2511.19923) | [PDF](https://arxiv.org/pdf/2511.19923.pdf)

**作者**: Yuefei Chen, Jiang Liu, Xiaodong Lin, Ruixiang Tang

---

## 💡 一句话要点

**提出CounterVQA基准和CFGPT方法以增强视频语言模型的反事实推理能力**

**关键词**: `视频语言模型` `反事实推理` `基准评估` `蒸馏训练` `视频理解`

## 📋 核心要点

1. 核心问题：视频语言模型在反事实推理方面存在不足，尤其在复杂因果链上表现不佳
2. 方法要点：开发CFGPT后训练方法，从语言模态蒸馏反事实推理能力到视觉模态
3. 实验或效果：在CounterVQA基准上评估，CFGPT在所有难度级别均带来一致改进

## 📄 摘要（原文）

> Vision Language Models (VLMs) have recently shown significant advancements in video understanding, especially in feature alignment, event reasoning, and instruction-following tasks. However, their capability for counterfactual reasoning, inferring alternative outcomes under hypothetical conditions, remains underexplored. This capability is essential for robust video understanding, as it requires identifying underlying causal structures and reasoning about unobserved possibilities, rather than merely recognizing observed patterns. To systematically evaluate this capability, we introduce CounterVQA, a video-based benchmark featuring three progressive difficulty levels that assess different aspects of counterfactual reasoning. Through comprehensive evaluation of both state-of-the-art open-source and closed-source models, we uncover a substantial performance gap: while these models achieve reasonable accuracy on simple counterfactual questions, performance degrades significantly on complex multi-hop causal chains. To address these limitations, we develop a post-training method, CFGPT, that enhances a model's visual counterfactual reasoning ability by distilling its counterfactual reasoning capability from the language modality, yielding consistent improvements across all CounterVQA difficulty levels. Dataset and code will be further released.

