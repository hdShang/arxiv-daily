---
layout: default
title: A Generalization of Input-Output Linearization via Dynamic Switching Between Melds of Output Functions
---

# A Generalization of Input-Output Linearization via Dynamic Switching Between Melds of Output Functions

**arXiv**: [2510.17448v1](https://arxiv.org/abs/2510.17448) | [PDF](https://arxiv.org/pdf/2510.17448.pdf)

**作者**: Mirko Mizzoni, Pieter van Goor, Barbara Bazzana, Antonio Franchi

---

## 💡 一句话要点

**提出通过动态切换输出函数集合实现非线性系统反馈线性化的通用框架。**

**关键词**: `非线性系统控制` `反馈线性化` `输出切换` `稳定性分析` `机器人控制`

## 📋 核心要点

1. 核心问题：非线性系统控制中如何安全切换不同输出集合以保持系统稳定性。
2. 方法要点：引入meld概念，定义可线性化输出子集，并证明切换条件下的状态有界性。
3. 实验或效果：在机器人操纵器数值模拟中验证理论，确保输出跟踪和指数稳定。

## 📄 摘要（原文）

> This letter presents a systematic framework for switching between different
> sets of outputs for the control of nonlinear systems via feedback
> linearization. We introduce the concept of a meld to formally define a valid,
> feedback-linearizable subset of outputs that can be selected from a larger deck
> of possible outputs. The main contribution is a formal proof establishing that
> under suitable dwell-time and compatibility conditions, it is possible to
> switch between different melds while guaranteeing the uniform boundedness of
> the system state. We further show that the error dynamics of the active outputs
> remain exponentially stable within each switching interval and that outputs
> common to consecutive melds are tracked seamlessly through transitions. The
> proposed theory is valid for any feedback linearizable nonlinear system, such
> as, e.g., robots, aerial and terrestrial vehicles, etc.. We demonstrate it on a
> simple numerical simulation of a robotic manipulator.

