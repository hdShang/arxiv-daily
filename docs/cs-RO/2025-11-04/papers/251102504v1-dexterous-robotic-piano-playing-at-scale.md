---
layout: default
title: Dexterous Robotic Piano Playing at Scale
---

# Dexterous Robotic Piano Playing at Scale

**arXiv**: [2511.02504v1](https://arxiv.org/abs/2511.02504) | [PDF](https://arxiv.org/pdf/2511.02504.pdf)

**作者**: Le Chen, Yi Zhao, Jan Schneider, Quankai Gao, Simon Guist, Cheng Qian, Juho Kannala, Bernhard Schölkopf, Joni Pajarinen, Dieter Büchler

---

## 💡 一句话要点

**提出OmniPianist方法，通过无演示学习实现大规模灵巧机器人钢琴演奏**

**关键词**: `机器人钢琴演奏` `最优运输` `强化学习` `模仿学习` `灵巧操作` `大规模训练`

## 📋 核心要点

1. 核心问题：双手机器人钢琴演奏任务高维、接触丰富，需快速精确控制。
2. 方法要点：结合最优运输自动指法、大规模强化学习和流匹配变换器模仿学习。
3. 实验或效果：训练超2000个代理，构建百万轨迹数据集，实现近千首曲目演奏。

## 📄 摘要（原文）

> Endowing robot hands with human-level dexterity has been a long-standing goal
> in robotics. Bimanual robotic piano playing represents a particularly
> challenging task: it is high-dimensional, contact-rich, and requires fast,
> precise control. We present OmniPianist, the first agent capable of performing
> nearly one thousand music pieces via scalable, human-demonstration-free
> learning. Our approach is built on three core components. First, we introduce
> an automatic fingering strategy based on Optimal Transport (OT), allowing the
> agent to autonomously discover efficient piano-playing strategies from scratch
> without demonstrations. Second, we conduct large-scale Reinforcement Learning
> (RL) by training more than 2,000 agents, each specialized in distinct music
> pieces, and aggregate their experience into a dataset named RP1M++, consisting
> of over one million trajectories for robotic piano playing. Finally, we employ
> a Flow Matching Transformer to leverage RP1M++ through large-scale imitation
> learning, resulting in the OmniPianist agent capable of performing a wide range
> of musical pieces. Extensive experiments and ablation studies highlight the
> effectiveness and scalability of our approach, advancing dexterous robotic
> piano playing at scale.

