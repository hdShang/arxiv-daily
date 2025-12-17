---
layout: default
title: When a Robot is More Capable than a Human: Learning from Constrained Demonstrators
---

# When a Robot is More Capable than a Human: Learning from Constrained Demonstrators

**arXiv**: [2510.09096v1](https://arxiv.org/abs/2510.09096) | [PDF](https://arxiv.org/pdf/2510.09096.pdf)

**作者**: Xinhu Li, Ayush Jain, Zhaojing Yang, Yigit Korkmaz, Erdem Bıyık

---

## 💡 一句话要点

**提出从受限专家演示中学习更优策略的方法，通过状态奖励推断和探索提升机器人性能。**

**关键词**: `模仿学习` `机器人学习` `奖励推断` `状态奖励` `轨迹优化` `受限演示`

## 📋 核心要点

1. 核心问题：专家演示因控制受限导致策略次优，机器人能否学习优于演示的策略。
2. 方法要点：推断状态奖励信号，通过时间插值自标注奖励，探索更高效轨迹。
3. 实验效果：在真实机器人上任务完成时间比行为克隆快10倍，样本效率更高。

## 📄 摘要（原文）

> Learning from demonstrations enables experts to teach robots complex tasks
> using interfaces such as kinesthetic teaching, joystick control, and
> sim-to-real transfer. However, these interfaces often constrain the expert's
> ability to demonstrate optimal behavior due to indirect control, setup
> restrictions, and hardware safety. For example, a joystick can move a robotic
> arm only in a 2D plane, even though the robot operates in a higher-dimensional
> space. As a result, the demonstrations collected by constrained experts lead to
> suboptimal performance of the learned policies. This raises a key question: Can
> a robot learn a better policy than the one demonstrated by a constrained
> expert? We address this by allowing the agent to go beyond direct imitation of
> expert actions and explore shorter and more efficient trajectories. We use the
> demonstrations to infer a state-only reward signal that measures task progress,
> and self-label reward for unknown states using temporal interpolation. Our
> approach outperforms common imitation learning in both sample efficiency and
> task completion time. On a real WidowX robotic arm, it completes the task in 12
> seconds, 10x faster than behavioral cloning, as shown in real-robot videos on
> https://sites.google.com/view/constrainedexpert .

