---
layout: default
title: McSc: Motion-Corrective Preference Alignment for Video Generation with Self-Critic Hierarchical Reasoning
---

# McSc: Motion-Corrective Preference Alignment for Video Generation with Self-Critic Hierarchical Reasoning

**arXiv**: [2511.22974v1](https://arxiv.org/abs/2511.22974) | [PDF](https://arxiv.org/pdf/2511.22974.pdf)

**作者**: Qiushi Yang, Yingjie Chen, Yuan Yao, Yifang Men, Huaizhuo Liu, Miaomiao Cui

---

## 💡 一句话要点

**提出McSc框架以解决文本到视频生成中人类偏好对齐的挑战，通过运动校正优化动态内容。**

**关键词**: `文本到视频生成` `偏好对齐` `强化学习` `运动校正` `自批判推理` `层次奖励监督`

## 📋 核心要点

1. 核心问题：现有方法依赖昂贵人工标注或代理指标，忽略人类偏好逻辑和运动与视觉质量冲突维度。
2. 方法要点：采用三阶段强化学习，包括自批判维度推理、层次比较推理和运动校正直接偏好优化。
3. 实验或效果：McSc在人类偏好对齐上表现优异，能生成高动态视频。

## 📄 摘要（原文）

> Text-to-video (T2V) generation has achieved remarkable progress in producing high-quality videos aligned with textual prompts. However, aligning synthesized videos with nuanced human preference remains challenging due to the subjective and multifaceted nature of human judgment. Existing video preference alignment methods rely on costly human annotations or utilize proxy metrics to predict preference, which lacks the understanding of human preference logic. Moreover, they usually directly align T2V models with the overall preference distribution, ignoring potential conflict dimensions like motion dynamics and visual quality, which may bias models towards low-motion content. To address these issues, we present Motion-corrective alignment with Self-critic hierarchical Reasoning (McSc), a three-stage reinforcement learning framework for robust preference modeling and alignment. Firstly, Self-critic Dimensional Reasoning (ScDR) trains a generative reward model (RM) to decompose preferences into per-dimension assessments, using self-critic reasoning chains for reliable learning. Secondly, to achieve holistic video comparison, we introduce Hierarchical Comparative Reasoning (HCR) for structural multi-dimensional reasoning with hierarchical reward supervision. Finally, using RM-preferred videos, we propose Motion-corrective Direct Preference Optimization (McDPO) to optimize T2V models, while dynamically re-weighting alignment objective to mitigate bias towards low-motion content. Experiments show that McSc achieves superior performance in human preference alignment and generates videos with high-motion dynamic.

