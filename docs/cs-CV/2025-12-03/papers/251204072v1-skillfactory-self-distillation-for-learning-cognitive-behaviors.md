---
layout: default
title: SkillFactory: Self-Distillation For Learning Cognitive Behaviors
---

# SkillFactory: Self-Distillation For Learning Cognitive Behaviors

**arXiv**: [2512.04072v1](https://arxiv.org/abs/2512.04072) | [PDF](https://arxiv.org/pdf/2512.04072.pdf)

**作者**: Zayne Sprague, Jack Lu, Manya Wadhwa, Sedrick Keh, Mengye Ren, Greg Durrett

---

## 💡 一句话要点

**提出SkillFactory方法，通过自蒸馏在监督微调阶段学习认知技能，以增强强化学习模型性能。**

**关键词**: `认知技能学习` `自蒸馏` `监督微调` `强化学习` `模型泛化`

## 📋 核心要点

1. 核心问题：如何让模型利用基础模型未展现的认知技能，如验证答案、回溯和重试。
2. 方法要点：使用模型自身样本重排生成“银”监督微调数据，无需从更强模型蒸馏。
3. 实验效果：SkillFactory初始化提升模型在强化学习后对更难任务的泛化能力和鲁棒性。

## 📄 摘要（原文）

> Reasoning models leveraging long chains of thought employ various cognitive skills, such as verification of their answers, backtracking, retrying by an alternate method, and more. Previous work has shown that when a base language model exhibits these skills, training that model further with reinforcement learning (RL) can learn to leverage them. How can we get models to leverage skills that aren't exhibited by base models? Our work, SkillFactory, is a method for fine-tuning models to roughly learn these skills during a supervised fine-tuning (SFT) stage prior to RL. Our approach does not rely on distillation from a stronger model, but instead uses samples from the model itself, rearranged to provide training data in the format of those skills. These "silver" SFT traces may be imperfect, but are nevertheless effective for priming a model to acquire skills during RL. Our evaluation shows that (1) starting from SkillFactory SFT initialization helps a model to generalize to harder variants of a task post-RL, despite lower performance pre-RL; (2) cognitive skills are indeed used by the model; (3) RLed SkillFactory models are more robust to regression on out-of-domain tasks than RLed base models. Our work suggests that inductive biases learned prior to RL help models learn robust cognitive skill use.

