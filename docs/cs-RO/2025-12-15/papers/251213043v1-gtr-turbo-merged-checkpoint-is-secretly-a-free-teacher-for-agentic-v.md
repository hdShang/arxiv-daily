---
layout: default
title: GTR-Turbo: Merged Checkpoint is Secretly a Free Teacher for Agentic VLM Training
---

# GTR-Turbo: Merged Checkpoint is Secretly a Free Teacher for Agentic VLM Training

**arXiv**: [2512.13043v1](https://arxiv.org/abs/2512.13043) | [PDF](https://arxiv.org/pdf/2512.13043.pdf)

**作者**: Tong Wei, Yijun Yang, Changhao Zhang, Junliang Xing, Yuanchun Shi, Zongqing Lu, Deheng Ye

---

## 💡 一句话要点

**提出GTR-Turbo，通过合并检查点作为免费教师，高效提升多模态智能体训练性能。**

**关键词**: `多模态智能体` `强化学习` `检查点合并` `蒸馏训练` `视觉语言模型` `高效训练`

## 📋 核心要点

1. 核心问题：多模态智能体强化学习面临稀疏奖励和长程信用分配难题，依赖昂贵教师模型。
2. 方法要点：在训练中合并检查点权重作为免费教师，通过监督微调或软标签蒸馏指导后续强化学习。
3. 实验或效果：在视觉任务中提升基线模型准确率10-30%，训练时间减少50%，计算成本降低60%。

## 📄 摘要（原文）

> Multi-turn reinforcement learning (RL) for multi-modal agents built upon vision-language models (VLMs) is hampered by sparse rewards and long-horizon credit assignment. Recent methods densify the reward by querying a teacher that provides step-level feedback, e.g., Guided Thought Reinforcement (GTR) and On-Policy Distillation, but rely on costly, often privileged models as the teacher, limiting practicality and reproducibility. We introduce GTR-Turbo, a highly efficient upgrade to GTR, which matches the performance without training or querying an expensive teacher model. Specifically, GTR-Turbo merges the weights of checkpoints produced during the ongoing RL training, and then uses this merged model as a "free" teacher to guide the subsequent RL via supervised fine-tuning or soft logit distillation. This design removes dependence on privileged VLMs (e.g., GPT or Gemini), mitigates the "entropy collapse" observed in prior work, and keeps training stable. Across diverse visual agentic tasks, GTR-Turbo improves the accuracy of the baseline model by 10-30% while reducing wall-clock training time by 50% and compute cost by 60% relative to GTR.

