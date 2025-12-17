---
layout: default
title: Periodic Skill Discovery
---

# Periodic Skill Discovery

**arXiv**: [2511.03187v1](https://arxiv.org/abs/2511.03187) | [PDF](https://arxiv.org/pdf/2511.03187.pdf)

**作者**: Jonghae Park, Daesol Cho, Jusuk Lee, Dongseok Shim, Inkyu Jang, H. Jin Kim

---

## 💡 一句话要点

**提出周期性技能发现框架，以无监督方式学习机器人任务中的周期性行为。**

**关键词**: `无监督强化学习` `技能发现` `周期性行为` `机器人任务` `潜空间编码`

## 📋 核心要点

1. 当前无监督技能发现方法忽视技能周期性，难以适应机器人运动任务。
2. PSD通过编码器将状态映射到圆形潜空间，自然编码周期性。
3. 实验显示PSD能学习多样周期性技能，并在下游任务如跨栏中表现优异。

## 📄 摘要（原文）

> Unsupervised skill discovery in reinforcement learning (RL) aims to learn
> diverse behaviors without relying on external rewards. However, current methods
> often overlook the periodic nature of learned skills, focusing instead on
> increasing the mutual dependence between states and skills or maximizing the
> distance traveled in latent space. Considering that many robotic tasks --
> particularly those involving locomotion -- require periodic behaviors across
> varying timescales, the ability to discover diverse periodic skills is
> essential. Motivated by this, we propose Periodic Skill Discovery (PSD), a
> framework that discovers periodic behaviors in an unsupervised manner. The key
> idea of PSD is to train an encoder that maps states to a circular latent space,
> thereby naturally encoding periodicity in the latent representation. By
> capturing temporal distance, PSD can effectively learn skills with diverse
> periods in complex robotic tasks, even with pixel-based observations. We
> further show that these learned skills achieve high performance on downstream
> tasks such as hurdling. Moreover, integrating PSD with an existing skill
> discovery method offers more diverse behaviors, thus broadening the agent's
> repertoire. Our code and demos are available at
> https://jonghaepark.github.io/psd/

