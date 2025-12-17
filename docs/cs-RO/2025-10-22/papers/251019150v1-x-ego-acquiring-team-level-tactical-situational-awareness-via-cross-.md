---
layout: default
title: X-Ego: Acquiring Team-Level Tactical Situational Awareness via Cross-Egocentric Contrastive Video Representation Learning
---

# X-Ego: Acquiring Team-Level Tactical Situational Awareness via Cross-Egocentric Contrastive Video Representation Learning

**arXiv**: [2510.19150v1](https://arxiv.org/abs/2510.19150) | [PDF](https://arxiv.org/pdf/2510.19150.pdf)

**作者**: Yunzhe Wang, Soham Hans, Volkan Ustun

---

## 💡 一句话要点

**提出跨自我中心对比学习以提升团队战术感知，应用于电子竞技视频分析**

**关键词**: `跨自我中心学习` `多智能体视频理解` `团队战术感知` `电子竞技基准` `对比学习` `位置预测`

## 📋 核心要点

1. 核心问题：现有视频理解依赖第三人称视角，忽略多智能体同步自我中心学习。
2. 方法要点：引入跨自我中心对比学习，对齐队友自我中心视觉流以增强战术感知。
3. 实验或效果：在队友-对手位置预测任务中，验证方法提升单视角位置推断能力。

## 📄 摘要（原文）

> Human team tactics emerge from each player's individual perspective and their
> ability to anticipate, interpret, and adapt to teammates' intentions. While
> advances in video understanding have improved the modeling of team interactions
> in sports, most existing work relies on third-person broadcast views and
> overlooks the synchronous, egocentric nature of multi-agent learning. We
> introduce X-Ego-CS, a benchmark dataset consisting of 124 hours of gameplay
> footage from 45 professional-level matches of the popular e-sports game
> Counter-Strike 2, designed to facilitate research on multi-agent
> decision-making in complex 3D environments. X-Ego-CS provides cross-egocentric
> video streams that synchronously capture all players' first-person perspectives
> along with state-action trajectories. Building on this resource, we propose
> Cross-Ego Contrastive Learning (CECL), which aligns teammates' egocentric
> visual streams to foster team-level tactical situational awareness from an
> individual's perspective. We evaluate CECL on a teammate-opponent location
> prediction task, demonstrating its effectiveness in enhancing an agent's
> ability to infer both teammate and opponent positions from a single
> first-person view using state-of-the-art video encoders. Together, X-Ego-CS and
> CECL establish a foundation for cross-egocentric multi-agent benchmarking in
> esports. More broadly, our work positions gameplay understanding as a testbed
> for multi-agent modeling and tactical learning, with implications for
> spatiotemporal reasoning and human-AI teaming in both virtual and real-world
> domains. Code and dataset are available at https://github.com/HATS-ICT/x-ego.

