---
layout: default
title: EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation
---

# EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation

**arXiv**: [2511.05397v1](https://arxiv.org/abs/2511.05397) | [PDF](https://arxiv.org/pdf/2511.05397.pdf)

**作者**: Samarth Chopra, Alex McMoil, Ben Carnovale, Evan Sokolson, Rajkumar Kubendran, Samuel Dickerson

---

## 💡 一句话要点

**提出EverydayVLA模型，结合低成本硬件以解决机器人操作在复杂场景中的可靠性问题**

**关键词**: `视觉语言动作模型` `低成本机器人` `自适应重规划` `6自由度操作` `机器人基础模型`

## 📋 核心要点

1. 核心问题：现有VLA模型依赖昂贵硬件，在陌生或杂乱场景中表现不佳
2. 方法要点：统一模型输出离散和连续动作，自适应集成监控不确定性触发重规划
3. 实验或效果：在LIBERO基准匹配SOTA，真实世界测试中分布内外性能提升显著

## 📄 摘要（原文）

> While Vision-Language-Action (VLA) models map visual inputs and language
> instructions directly to robot actions, they often rely on costly hardware and
> struggle in novel or cluttered scenes. We introduce EverydayVLA, a 6-DOF
> manipulator that can be assembled for under $300, capable of modest payloads
> and workspace. A single unified model jointly outputs discrete and continuous
> actions, and our adaptive-horizon ensemble monitors motion uncertainty to
> trigger on-the-fly re-planning for safe, reliable operation. On LIBERO,
> EverydayVLA matches state-of-the-art success rates, and in real-world tests it
> outperforms prior methods by 49% in-distribution and 34.9% out-of-distribution.
> By combining a state-of-the-art VLA with cost-effective hardware, EverydayVLA
> democratizes access to a robotic foundation model and paves the way for
> economical use in homes and research labs alike. Experiment videos and details:
> https://everydayvla.github.io/

