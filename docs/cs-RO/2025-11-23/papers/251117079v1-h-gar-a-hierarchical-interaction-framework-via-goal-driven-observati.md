---
layout: default
title: H-GAR: A Hierarchical Interaction Framework via Goal-Driven Observation-Action Refinement for Robotic Manipulation
---

# H-GAR: A Hierarchical Interaction Framework via Goal-Driven Observation-Action Refinement for Robotic Manipulation

**arXiv**: [2511.17079v1](https://arxiv.org/abs/2511.17079) | [PDF](https://arxiv.org/pdf/2511.17079.pdf)

**作者**: Yijie Zhu, Rui Shao, Ziyang Liu, Jie He, Jizhihui Liu, Jiuru Wang, Zitong Yu

---

## 💡 一句话要点

**提出H-GAR分层框架，通过目标驱动优化观察与动作，提升机器人操作性能。**

**关键词**: `机器人操作` `分层交互框架` `目标驱动预测` `观察-动作交互` `动作细化`

## 📋 核心要点

1. 现有方法在机器人操作中，常以整体方式生成观察与动作，导致预测语义错位和行为不连贯。
2. H-GAR采用分层方法，先生成目标观察和粗略动作，再通过协同模块细化动作和合成中间观察。
3. 在仿真和真实机器人任务中，H-GAR实现了最先进的性能，验证了其有效性。

## 📄 摘要（原文）

> Unified video and action prediction models hold great potential for robotic manipulation, as future observations offer contextual cues for planning, while actions reveal how interactions shape the environment. However, most existing approaches treat observation and action generation in a monolithic and goal-agnostic manner, often leading to semantically misaligned predictions and incoherent behaviors. To this end, we propose H-GAR, a Hierarchical interaction framework via Goal-driven observation-Action Refinement.To anchor prediction to the task objective, H-GAR first produces a goal observation and a coarse action sketch that outline a high-level route toward the goal. To enable explicit interaction between observation and action under the guidance of the goal observation for more coherent decision-making, we devise two synergistic modules. (1) Goal-Conditioned Observation Synthesizer (GOS) synthesizes intermediate observations based on the coarse-grained actions and the predicted goal observation. (2) Interaction-Aware Action Refiner (IAAR) refines coarse actions into fine-grained, goal-consistent actions by leveraging feedback from the intermediate observations and a Historical Action Memory Bank that encodes prior actions to ensure temporal consistency. By integrating goal grounding with explicit action-observation interaction in a coarse-to-fine manner, H-GAR enables more accurate manipulation. Extensive experiments on both simulation and real-world robotic manipulation tasks demonstrate that H-GAR achieves state-of-the-art performance.

