---
layout: default
title: E3AD: An Emotion-Aware Vision-Language-Action Model for Human-Centric End-to-End Autonomous Driving
---

# E3AD: An Emotion-Aware Vision-Language-Action Model for Human-Centric End-to-End Autonomous Driving

**arXiv**: [2512.04733v1](https://arxiv.org/abs/2512.04733) | [PDF](https://arxiv.org/pdf/2512.04733.pdf)

**作者**: Yihong Tang, Haicheng Liao, Tong Nie, Junlin He, Ao Qu, Kehua Chen, Wei Ma, Zhenning Li, Lijun Sun, Chengzhong Xu

---

## 💡 一句话要点

**提出E3AD模型，通过情感感知的视觉-语言-动作框架解决开放域端到端自动驾驶中乘客情感忽略问题。**

**关键词**: `端到端自动驾驶` `视觉-语言-动作模型` `情感感知` `空间推理` `开放域驾驶`

## 📋 核心要点

1. 核心问题：现有端到端自动驾驶系统忽视乘客情感状态，影响舒适度和接受度。
2. 方法要点：引入连续VAD情感模型和双通路空间推理模块，增强语义理解和空间认知。
3. 实验或效果：在真实数据集上提升视觉定位和路径规划，情感估计达到SOTA相关性。

## 📄 摘要（原文）

> End-to-end autonomous driving (AD) systems increasingly adopt vision-language-action (VLA) models, yet they typically ignore the passenger's emotional state, which is central to comfort and AD acceptance. We introduce Open-Domain End-to-End (OD-E2E) autonomous driving, where an autonomous vehicle (AV) must interpret free-form natural-language commands, infer the emotion, and plan a physically feasible trajectory. We propose E3AD, an emotion-aware VLA framework that augments semantic understanding with two cognitively inspired components: a continuous Valenc-Arousal-Dominance (VAD) emotion model that captures tone and urgency from language, and a dual-pathway spatial reasoning module that fuses egocentric and allocentric views for human-like spatial cognition. A consistency-oriented training scheme, combining modality pretraining with preference-based alignment, further enforces coherence between emotional intent and driving actions. Across real-world datasets, E3AD improves visual grounding and waypoint planning and achieves state-of-the-art (SOTA) VAD correlation for emotion estimation. These results show that injecting emotion into VLA-style driving yields more human-aligned grounding, planning, and human-centric feedback.

