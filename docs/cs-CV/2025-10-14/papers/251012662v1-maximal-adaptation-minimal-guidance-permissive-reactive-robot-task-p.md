---
layout: default
title: Maximal Adaptation, Minimal Guidance: Permissive Reactive Robot Task Planning with Humans in the Loop
---

# Maximal Adaptation, Minimal Guidance: Permissive Reactive Robot Task Planning with Humans in the Loop

**arXiv**: [2510.12662v1](https://arxiv.org/abs/2510.12662) | [PDF](https://arxiv.org/pdf/2510.12662.pdf)

**作者**: Oz Gitelson, Satya Prakash Nayak, Ritam Raha, Anne-Kathrin Schmuck

---

## 💡 一句话要点

**提出人机逻辑交互框架，实现机器人在无限时域任务中与人类协作。**

**关键词**: `人机交互` `时序逻辑任务` `机器人规划` `在线适应` `协作机器人` `形式保证`

## 📋 核心要点

1. 核心问题：机器人在未知人类任务下如何可靠满足时序逻辑任务并最小化干扰。
2. 方法要点：结合最大适应性和最小可调反馈，在线调整策略并仅在必要时请求合作。
3. 实验或效果：在真实机器人任务和Overcooked-AI基准中验证，产生涌现合作行为并保持形式保证。

## 📄 摘要（原文）

> We present a novel framework for human-robot \emph{logical} interaction that
> enables robots to reliably satisfy (infinite horizon) temporal logic tasks
> while effectively collaborating with humans who pursue independent and unknown
> tasks. The framework combines two key capabilities: (i) \emph{maximal
> adaptation} enables the robot to adjust its strategy \emph{online} to exploit
> human behavior for cooperation whenever possible, and (ii) \emph{minimal
> tunable feedback} enables the robot to request cooperation by the human online
> only when necessary to guarantee progress. This balance minimizes human-robot
> interference, preserves human autonomy, and ensures persistent robot task
> satisfaction even under conflicting human goals. We validate the approach in a
> real-world block-manipulation task with a Franka Emika Panda robotic arm and in
> the Overcooked-AI benchmark, demonstrating that our method produces rich,
> \emph{emergent} cooperative behaviors beyond the reach of existing approaches,
> while maintaining strong formal guarantees.

