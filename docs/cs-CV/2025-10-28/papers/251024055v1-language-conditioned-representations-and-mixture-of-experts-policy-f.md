---
layout: default
title: Language-Conditioned Representations and Mixture-of-Experts Policy for Robust Multi-Task Robotic Manipulation
---

# Language-Conditioned Representations and Mixture-of-Experts Policy for Robust Multi-Task Robotic Manipulation

**arXiv**: [2510.24055v1](https://arxiv.org/abs/2510.24055) | [PDF](https://arxiv.org/pdf/2510.24055.pdf)

**作者**: Xiucheng Zhang, Yang Jiang, Hongwei Qing, Jiashuo Bai

---

## 💡 一句话要点

**提出语言条件表示与专家混合策略以解决多任务机器人操作中的感知模糊和任务冲突**

**关键词**: `多任务机器人操作` `语言条件表示` `专家混合策略` `模仿学习` `视觉语言融合`

## 📋 核心要点

1. 多任务机器人模仿学习中存在感知模糊和任务冲突问题
2. 结合语言条件视觉表示模块和专家混合密度策略，提升任务区分和动作分布建模
3. 在真实机器人基准上，平均成功率提升21%，达到79%

## 📄 摘要（原文）

> Perceptual ambiguity and task conflict limit multitask robotic manipulation
> via imitation learning. We propose a framework combining a Language-Conditioned
> Visual Representation (LCVR) module and a Language-conditioned
> Mixture-ofExperts Density Policy (LMoE-DP). LCVR resolves perceptual
> ambiguities by grounding visual features with language instructions, enabling
> differentiation between visually similar tasks. To mitigate task conflict,
> LMoE-DP uses a sparse expert architecture to specialize in distinct, multimodal
> action distributions, stabilized by gradient modulation. On real-robot
> benchmarks, LCVR boosts Action Chunking with Transformers (ACT) and Diffusion
> Policy (DP) success rates by 33.75% and 25%, respectively. The full framework
> achieves a 79% average success, outperforming the advanced baseline by 21%. Our
> work shows that combining semantic grounding and expert specialization enables
> robust, efficient multi-task manipulation

