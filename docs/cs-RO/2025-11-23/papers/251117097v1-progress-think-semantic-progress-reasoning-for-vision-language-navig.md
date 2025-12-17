---
layout: default
title: Progress-Think: Semantic Progress Reasoning for Vision-Language Navigation
---

# Progress-Think: Semantic Progress Reasoning for Vision-Language Navigation

**arXiv**: [2511.17097v1](https://arxiv.org/abs/2511.17097) | [PDF](https://arxiv.org/pdf/2511.17097.pdf)

**作者**: Shuo Wang, Yucheng Wang, Guoxin Lian, Yongcai Wang, Maiyue Chen, Kaihui Wang, Bo Zhang, Zhizhong Su, Yutian Zhou, Wanting Li, Deying Li, Zhaoxin Fan

---

## 💡 一句话要点

**提出语义进展推理方法以提升视觉语言导航的连贯性**

**关键词**: `视觉语言导航` `语义进展推理` `自对齐预训练` `强化学习优化` `多步指令理解`

## 📋 核心要点

1. 核心问题：现有方法忽视观察与指令序列的单调共进特性，导致导航不一致。
2. 方法要点：通过三阶段框架实现语义进展预测，无需昂贵标注。
3. 实验效果：在R2R-CE和RxR-CE数据集上实现最先进的成功率和效率。

## 📄 摘要（原文）

> Vision-Language Navigation requires agents to act coherently over long horizons by understanding not only local visual context but also how far they have advanced within a multi-step instruction. However, recent Vision-Language-Action models focus on direct action prediction and earlier progress methods predict numeric achievements; both overlook the monotonic co-progression property of the observation and instruction sequences. Building on this insight, Progress-Think introduces semantic progress reasoning, predicting instruction-style progress from visual observations to enable more accurate navigation. To achieve this without expensive annotations, we propose a three-stage framework. In the initial stage, Self-Aligned Progress Pretraining bootstraps a reasoning module via a novel differentiable alignment between visual history and instruction prefixes. Then, Progress-Guided Policy Pretraining injects learned progress states into the navigation context, guiding the policy toward consistent actions. Finally, Progress-Policy Co-Finetuning jointly optimizes both modules with tailored progress-aware reinforcement objectives. Experiments on R2R-CE and RxR-CE show state-of-the-art success and efficiency, demonstrating that semantic progress yields a more consistent representation of navigation advancement.

