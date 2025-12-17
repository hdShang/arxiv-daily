---
layout: default
title: Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary
---

# Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary

**arXiv**: [2511.22963v1](https://arxiv.org/abs/2511.22963) | [PDF](https://arxiv.org/pdf/2511.22963.pdf)

**作者**: Zhirui Liu, Kaiyang Ji, Ke Yang, Jingyi Yu, Ye Shi, Jingya Wang

---

## 💡 一句话要点

**提出Humanoid-LLA模型，通过统一运动词汇和物理感知微调，实现人形机器人自由语言指令的全身控制。**

**关键词**: `人形机器人控制` `语言指令执行` `统一运动词汇` `物理感知微调` `强化学习` `全身动作生成`

## 📋 核心要点

1. 核心问题：现有方法在语言条件全身控制中，常牺牲运动多样性或物理可行性，难以处理复杂指令。
2. 方法要点：构建统一运动词汇对齐人类与人形运动基元，结合词汇导向控制器和物理感知强化学习微调。
3. 实验或效果：在仿真和真实Unitree G1机器人上评估，显示强语言泛化能力，运动自然性、稳定性和成功率优于现有方法。

## 📄 摘要（原文）

> Enabling humanoid robots to follow free-form language commands is critical for seamless human-robot interaction, collaborative task execution, and general-purpose embodied intelligence. While recent advances have improved low-level humanoid locomotion and robot manipulation, language-conditioned whole-body control remains a significant challenge. Existing methods are often limited to simple instructions and sacrifice either motion diversity or physical plausibility. To address this, we introduce Humanoid-LLA, a Large Language Action Model that maps expressive language commands to physically executable whole-body actions for humanoid robots. Our approach integrates three core components: a unified motion vocabulary that aligns human and humanoid motion primitives into a shared discrete space; a vocabulary-directed controller distilled from a privileged policy to ensure physical feasibility; and a physics-informed fine-tuning stage using reinforcement learning with dynamics-aware rewards to enhance robustness and stability. Extensive evaluations in simulation and on a real-world Unitree G1 humanoid show that Humanoid-LLA delivers strong language generalization while maintaining high physical fidelity, outperforming existing language-conditioned controllers in motion naturalness, stability, and execution success rate.

