---
layout: default
title: How Does RL Post-training Induce Skill Composition? A Case Study on Countdown
---

# How Does RL Post-training Induce Skill Composition? A Case Study on Countdown

**arXiv**: [2512.01775v1](https://arxiv.org/abs/2512.01775) | [PDF](https://arxiv.org/pdf/2512.01775.pdf)

**作者**: Simon Park, Simran Kaur, Sanjeev Arora

---

## 💡 一句话要点

**研究RL后训练如何诱导技能组合，以Countdown任务为例揭示组合泛化机制**

**关键词**: `强化学习后训练` `组合泛化` `Countdown任务` `表达式树分析` `技能组合` `泛化诊断`

## 📋 核心要点

1. 核心问题：RL后训练是否促进组合泛化，而非仅长度泛化，技能组合结构如何影响学习
2. 方法要点：将Countdown任务解构为表达式树，分析子树作为可重用技能，追踪树形与成功率
3. 实验或效果：发现OOD泛化能力，学习顺序受树形结构影响，右重结构泛化脆弱

## 📄 摘要（原文）

> While reinforcement learning (RL) successfully enhances reasoning in large language models, its role in fostering compositional generalization (the ability to synthesize novel skills from known components) is often conflated with mere length generalization. To this end, we study what RL post-training teaches about skill composition and how the structure of the composition affects the skill transfer. We focus on the Countdown task (given n numbers and a target, form an expression that evaluates to the target) and analyze model solutions as expression trees, where each subtree corresponds to a reusable subtask and thus can be viewed as a ``skill.'' Tracking tree shapes and their success rates over training, we find: (i) out-of-distribution (OOD) generalization to larger n and to unseen tree shapes, indicating compositional reuse of subtasks; (ii) a structure-dependent hierarchy of learnability -- models master shallow balanced trees (workload is balanced between subtasks) before deep unbalanced ones, with persistent fragility on right-heavy structures (even when the composition depth is the same as some left-heavy structures). Our diagnostic reveals what is learned, in what order, and where generalization fails, clarifying how RL-only post-training induces OOD generalization beyond what standard metrics such as pass@k reveal.

