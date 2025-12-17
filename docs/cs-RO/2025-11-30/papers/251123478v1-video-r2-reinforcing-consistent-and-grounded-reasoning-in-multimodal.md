---
layout: default
title: Video-R2: Reinforcing Consistent and Grounded Reasoning in Multimodal Language Models
---

# Video-R2: Reinforcing Consistent and Grounded Reasoning in Multimodal Language Models

**arXiv**: [2511.23478v1](https://arxiv.org/abs/2511.23478) | [PDF](https://arxiv.org/pdf/2511.23478.pdf)

**作者**: Muhammad Maaz, Hanoona Rasheed, Fahad Shahbaz Khan, Salman Khan

---

## 💡 一句话要点

**提出Video-R2模型，通过强化学习增强多模态语言模型在视频推理中的一致性和视觉基础性。**

**关键词**: `视频推理` `多模态语言模型` `强化学习` `时间对齐` `视觉基础性` `基准测试`

## 📋 核心要点

1. 核心问题：当前模型在视频推理中常出现逻辑不一致或视觉证据弱的问题，依赖语言先验而非视觉内容。
2. 方法要点：采用时间感知监督微调和基于时间对齐奖励的组相对策略优化，提升时间对齐和推理一致性。
3. 实验或效果：在11个基准测试中，Video-R2在一致性、视觉注意力和准确性方面均优于现有模型。

## 📄 摘要（原文）

> Reasoning over dynamic visual content remains a central challenge for multimodal large language models. Recent thinking models generate explicit reasoning traces for interpretability; however, their reasoning often appears convincing while being logically inconsistent or weakly grounded in visual evidence. We identify and formalize these issues through two diagnostic metrics: Think Answer Consistency (TAC), which measures the alignment between reasoning and answers, and Video Attention Score (VAS), which captures the extent to which reasoning depends on visual versus textual cues. Analysis across 11 video reasoning benchmarks shows that current models rely heavily on linguistic priors rather than visual content. To address this, we propose a reinforcement learning approach that enhances both temporal precision and reasoning consistency. Our approach combines timestamp aware supervised fine tuning with Group Relative Policy Optimization (GRPO) guided by a novel Temporal Alignment Reward (TAR). This dual step post training stage encourages temporally aligned and causally coherent video reasoning. The resulting model, Video R2, achieves consistently higher TAC, VAS, and accuracy across multiple benchmarks, demonstrating that improvements in temporal alignment and reasoning coherence lead to more accurate and trustworthy video understanding. Our code, dataset, and model will be open sourced.

