---
layout: default
title: Learning Parameterized Skills from Demonstrations
---

# Learning Parameterized Skills from Demonstrations

**arXiv**: [2510.24095v1](https://arxiv.org/abs/2510.24095) | [PDF](https://arxiv.org/pdf/2510.24095.pdf)

**作者**: Vedant Gupta, Haotian Fu, Calvin Luo, Yiding Jiang, George Konidaris

---

## 💡 一句话要点

**提出DEPS算法从专家演示中学习参数化技能，以提升未见任务的泛化能力。**

**关键词**: `参数化技能学习` `专家演示` `变分推理` `信息论正则化` `多任务泛化` `元策略学习`

## 📋 核心要点

1. 核心问题：从多任务专家演示中学习参数化技能，避免潜在变量模型的退化问题。
2. 方法要点：结合时间变分推理和信息论正则化，联合学习技能策略和元策略。
3. 实验效果：在LIBERO和MetaWorld基准上优于多任务和技能学习基线方法。

## 📄 摘要（原文）

> We present DEPS, an end-to-end algorithm for discovering parameterized skills
> from expert demonstrations. Our method learns parameterized skill policies
> jointly with a meta-policy that selects the appropriate discrete skill and
> continuous parameters at each timestep. Using a combination of temporal
> variational inference and information-theoretic regularization methods, we
> address the challenge of degeneracy common in latent variable models, ensuring
> that the learned skills are temporally extended, semantically meaningful, and
> adaptable. We empirically show that learning parameterized skills from
> multitask expert demonstrations significantly improves generalization to unseen
> tasks. Our method outperforms multitask as well as skill learning baselines on
> both LIBERO and MetaWorld benchmarks. We also demonstrate that DEPS discovers
> interpretable parameterized skills, such as an object grasping skill whose
> continuous arguments define the grasp location.

