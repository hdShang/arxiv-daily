---
layout: default
title: InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy
---

# InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy

**arXiv**: [2510.13778v1](https://arxiv.org/abs/2510.13778) | [PDF](https://arxiv.org/pdf/2510.13778.pdf)

**作者**: Xinyi Chen, Yilun Chen, Yanwei Fu, Ning Gao, Jiaya Jia, Weiyang Jin, Hao Li, Yao Mu, Jiangmiao Pang, Yu Qiao, Yang Tian, Bin Wang, Bolun Wang, Fangjing Wang, Hanqing Wang, Tai Wang, Ziqin Wang, Xueyuan Wei, Chao Wu, Shuai Yang, Jinhui Ye, Junqiu Yu, Jia Zeng, Jingjing Zhang, Jinyu Zhang, Shi Zhang, Feng Zheng, Bowen Zhou, Yangkun Zhu

---

## 💡 一句话要点

**提出InternVLA-M1框架，通过空间引导训练提升通用机器人指令跟随能力**

**关键词**: `空间基础` `视觉语言动作` `机器人控制` `通用智能` `指令跟随`

## 📋 核心要点

1. 核心问题：机器人难以将指令与视觉空间位置对齐，影响通用智能。
2. 方法要点：采用两阶段训练，先空间预训练定位，后空间引导动作生成。
3. 实验效果：在多个基准上性能提升显著，如SimperEnv提升14.6%。

## 📄 摘要（原文）

> We introduce InternVLA-M1, a unified framework for spatial grounding and
> robot control that advances instruction-following robots toward scalable,
> general-purpose intelligence. Its core idea is spatially guided
> vision-language-action training, where spatial grounding serves as the critical
> link between instructions and robot actions. InternVLA-M1 employs a two-stage
> pipeline: (i) spatial grounding pre-training on over 2.3M spatial reasoning
> data to determine ``where to act'' by aligning instructions with visual,
> embodiment-agnostic positions, and (ii) spatially guided action post-training
> to decide ``how to act'' by generating embodiment-aware actions through
> plug-and-play spatial prompting. This spatially guided training recipe yields
> consistent gains: InternVLA-M1 outperforms its variant without spatial guidance
> by +14.6% on SimplerEnv Google Robot, +17% on WidowX, and +4.3% on LIBERO
> Franka, while demonstrating stronger spatial reasoning capability in box,
> point, and trace prediction. To further scale instruction following, we built a
> simulation engine to collect 244K generalizable pick-and-place episodes,
> enabling a 6.2% average improvement across 200 tasks and 3K+ objects. In
> real-world clustered pick-and-place, InternVLA-M1 improved by 7.3%, and with
> synthetic co-training, achieved +20.6% on unseen objects and novel
> configurations. Moreover, in long-horizon reasoning-intensive scenarios, it
> surpassed existing works by over 10%. These results highlight spatially guided
> training as a unifying principle for scalable and resilient generalist robots.
> Code and models are available at
> https://github.com/InternRobotics/InternVLA-M1.

