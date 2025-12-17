---
layout: default
title: Using Non-Expert Data to Robustify Imitation Learning via Offline Reinforcement Learning
---

# Using Non-Expert Data to Robustify Imitation Learning via Offline Reinforcement Learning

**arXiv**: [2510.19495v1](https://arxiv.org/abs/2510.19495) | [PDF](https://arxiv.org/pdf/2510.19495.pdf)

**作者**: Kevin Huang, Rosario Scalise, Cleah Winston, Ayush Agrawal, Yunchu Zhang, Rohan Baijal, Markus Grotz, Byron Boots, Benjamin Burchfiel, Hongkai Dai, Masha Itkina, Paarth Shah, Abhishek Gupta

---

## 💡 一句话要点

**提出离线强化学习方法以利用非专家数据增强模仿学习的鲁棒性**

**关键词**: `模仿学习` `离线强化学习` `非专家数据` `机器人操作` `策略鲁棒性`

## 📋 核心要点

1. 模仿学习依赖高质量专家数据，难以适应真实世界多样场景
2. 通过离线强化学习算法改进，利用非专家数据扩展策略分布支持
3. 在机器人操作任务中，显著提升策略的恢复能力和泛化性能

## 📄 摘要（原文）

> Imitation learning has proven effective for training robots to perform
> complex tasks from expert human demonstrations. However, it remains limited by
> its reliance on high-quality, task-specific data, restricting adaptability to
> the diverse range of real-world object configurations and scenarios. In
> contrast, non-expert data -- such as play data, suboptimal demonstrations,
> partial task completions, or rollouts from suboptimal policies -- can offer
> broader coverage and lower collection costs. However, conventional imitation
> learning approaches fail to utilize this data effectively. To address these
> challenges, we posit that with right design decisions, offline reinforcement
> learning can be used as a tool to harness non-expert data to enhance the
> performance of imitation learning policies. We show that while standard offline
> RL approaches can be ineffective at actually leveraging non-expert data under
> the sparse data coverage settings typically encountered in the real world,
> simple algorithmic modifications can allow for the utilization of this data,
> without significant additional assumptions. Our approach shows that broadening
> the support of the policy distribution can allow imitation algorithms augmented
> by offline RL to solve tasks robustly, showing considerably enhanced recovery
> and generalization behavior. In manipulation tasks, these innovations
> significantly increase the range of initial conditions where learned policies
> are successful when non-expert data is incorporated. Moreover, we show that
> these methods are able to leverage all collected data, including partial or
> suboptimal demonstrations, to bolster task-directed policy performance. This
> underscores the importance of algorithmic techniques for using non-expert data
> for robust policy learning in robotics.

