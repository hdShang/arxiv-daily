---
layout: default
title: RVLF: A Reinforcing Vision-Language Framework for Gloss-Free Sign Language Translation
---

# RVLF: A Reinforcing Vision-Language Framework for Gloss-Free Sign Language Translation

**arXiv**: [2512.07273v1](https://arxiv.org/abs/2512.07273) | [PDF](https://arxiv.org/pdf/2512.07273.pdf)

**作者**: Zhi Rao, Yucheng Zhou, Benjia Zhou, Yiqing Huang, Sergio Escalera, Jun Wan

---

## 💡 一句话要点

**提出RVLF框架以解决无注释手语翻译中的表示不足和语义对齐问题**

**关键词**: `无注释手语翻译` `视觉语言模型` `强化学习` `语义对齐` `GRPO优化`

## 📋 核心要点

1. 核心问题：无注释手语翻译存在视觉表示不足和句子级语义错配，影响翻译质量。
2. 方法要点：结合大型视觉语言模型与强化学习，通过语义表示学习和GRPO优化提升翻译性能。
3. 实验或效果：在多个数据集上BLEU-4分数显著提升，验证了GRPO优化的有效性。

## 📄 摘要（原文）

> Gloss-free sign language translation (SLT) is hindered by two key challenges: **inadequate sign representation** that fails to capture nuanced visual cues, and **sentence-level semantic misalignment** in current LLM-based methods, which limits translation quality. To address these issues, we propose a three-stage **r**einforcing **v**ision-**l**anguage **f**ramework (**RVLF**). We build a large vision-language model (LVLM) specifically designed for sign language, and then combine it with reinforcement learning (RL) to adaptively enhance translation performance. First, for a sufficient representation of sign language, RVLF introduces an effective semantic representation learning mechanism that fuses skeleton-based motion cues with semantically rich visual features extracted via DINOv2, followed by instruction tuning to obtain a strong SLT-SFT baseline. Then, to improve sentence-level semantic misalignment, we introduce a GRPO-based optimization strategy that fine-tunes the SLT-SFT model with a reward function combining translation fidelity (BLEU) and sentence completeness (ROUGE), yielding the optimized model termed SLT-GRPO. Our conceptually simple framework yields substantial gains under the gloss-free SLT setting without pre-training on any external large-scale sign language datasets, improving BLEU-4 scores by +5.1, +1.11, +1.4, and +1.61 on the CSL-Daily, PHOENIX-2014T, How2Sign, and OpenASL datasets, respectively. To the best of our knowledge, this is the first work to incorporate GRPO into SLT. Extensive experiments and ablation studies validate the effectiveness of GRPO-based optimization in enhancing both translation quality and semantic consistency.

