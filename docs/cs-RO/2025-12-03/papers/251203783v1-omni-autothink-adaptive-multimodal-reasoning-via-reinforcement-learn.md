---
layout: default
title: Omni-AutoThink: Adaptive Multimodal Reasoning via Reinforcement Learning
---

# Omni-AutoThink: Adaptive Multimodal Reasoning via Reinforcement Learning

**arXiv**: [2512.03783v1](https://arxiv.org/abs/2512.03783) | [PDF](https://arxiv.org/pdf/2512.03783.pdf)

**作者**: Dongchao Yang, Songxiang Liu, Disong Wang, Yuanyuan Wang, Guanglu Wan, Helen Meng

---

## 💡 一句话要点

**提出Omni-AutoThink自适应多模态推理框架，通过强化学习动态调整推理深度以解决任务难度适应性问题。**

**关键词**: `自适应推理` `多模态学习` `强化学习` `Omni模型` `任务难度适应`

## 📋 核心要点

1. 核心问题：现有Omni模型推理行为僵化，难以根据任务难度自适应调整推理深度。
2. 方法要点：采用自适应监督微调和自适应强化学习两阶段框架，优化推理行为。
3. 实验或效果：构建多模态自适应推理基准，实验显示性能显著优于基线。

## 📄 摘要（原文）

> Recent advances in Omni models have enabled unified multimodal perception and generation. However, most existing systems still exhibit rigid reasoning behaviors, either overthinking simple problems or failing to reason when necessary. To address this limitation, we propose Omni-AutoThink, a novel adaptive reasoning framework that dynamically adjusts the model's reasoning depth according to task difficulty. Our framework comprises two stages: (1) an Adaptive Supervised Fine-Tuning (Adaptive SFT) stage, which endows the Omni model with fundamental reasoning capability using large-scale reasoning-augmented data, and (2) an Adaptive Reinforcement Learning (Adaptive GRPO) stage, which optimizes reasoning behaviors based on task complexity and reward feedback. We further construct a comprehensive adaptive reasoning benchmark that spans text-only, text-audio, text-visual, and text-audio-visual modalities, providing both training and evaluation splits for multimodal reasoning assessment. Experimental results demonstrate that our proposed framework significantly improves adaptive reasoning performance compared to previous baselines. All benchmark data and code will be publicly released.

