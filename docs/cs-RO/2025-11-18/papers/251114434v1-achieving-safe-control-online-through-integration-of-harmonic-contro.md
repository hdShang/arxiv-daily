---
layout: default
title: Achieving Safe Control Online through Integration of Harmonic Control Lyapunov-Barrier Functions with Unsafe Object-Centric Action Policies
---

# Achieving Safe Control Online through Integration of Harmonic Control Lyapunov-Barrier Functions with Unsafe Object-Centric Action Policies

**arXiv**: [2511.14434v1](https://arxiv.org/abs/2511.14434) | [PDF](https://arxiv.org/pdf/2511.14434.pdf)

**作者**: Marlow Fawn, Matthias Scheutz

---

## 💡 一句话要点

**提出结合谐波控制李雅普诺夫-屏障函数与不安全策略的方法，实现机器人安全控制。**

**关键词**: `谐波控制李雅普诺夫-屏障函数` `信号时序逻辑` `机器人安全控制` `强化学习策略` `形式化保证`

## 📋 核心要点

1. 核心问题：机器人策略可能不安全，需在保持任务行为的同时确保安全。
2. 方法要点：从信号时序逻辑推导HCLBF，结合任意策略生成安全证书。
3. 实验或效果：在静止机械臂移动任务中验证，能避免与障碍物碰撞。

## 📄 摘要（原文）

> We propose a method for combining Harmonic Control Lyapunov-Barrier Functions (HCLBFs) derived from Signal Temporal Logic (STL) specifications with any given robot policy to turn an unsafe policy into a safe one with formal guarantees.  The two components are combined via HCLBF-derived safety certificates, thus producing commands that preserve both safety and task-driven behavior.  We demonstrate with a simple proof-of-concept implementation for an object-centric force-based policy trained through reinforcement learning for a movement task of a stationary robot arm that is able to avoid colliding with obstacles on a table top after combining the policy with the safety constraints.  The proposed method can be generalized to more complex specifications and dynamic task settings.

