---
layout: default
title: V-OCBF: Learning Safety Filters from Offline Data via Value-Guided Offline Control Barrier Functions
---

# V-OCBF: Learning Safety Filters from Offline Data via Value-Guided Offline Control Barrier Functions

**arXiv**: [2512.10822v1](https://arxiv.org/abs/2512.10822) | [PDF](https://arxiv.org/pdf/2512.10822.pdf)

**作者**: Mumuksh Tayal, Manan Tayal, Aditya Singh, Shishir Kolathaya, Ravi Prakash

---

## 💡 一句话要点

**提出V-OCBF框架，从离线数据学习神经控制屏障函数以保障自主系统安全**

**关键词**: `离线强化学习` `控制屏障函数` `安全保证` `无模型学习` `实时控制` `自主系统`

## 📋 核心要点

1. 核心问题：现有离线安全强化学习方法无法保证前向不变性，而控制屏障函数依赖专家设计或系统动态知识
2. 方法要点：通过递归有限差分屏障更新实现无模型学习，结合期望分位数目标避免分布外动作查询
3. 实验或效果：在多个案例中显著减少安全违规，保持任务性能，支持离线合成安全关键控制器

## 📄 摘要（原文）

> Ensuring safety in autonomous systems requires controllers that satisfy hard, state-wise constraints without relying on online interaction. While existing Safe Offline RL methods typically enforce soft expected-cost constraints, they do not guarantee forward invariance. Conversely, Control Barrier Functions (CBFs) provide rigorous safety guarantees but usually depend on expert-designed barrier functions or full knowledge of the system dynamics. We introduce Value-Guided Offline Control Barrier Functions (V-OCBF), a framework that learns a neural CBF entirely from offline demonstrations. Unlike prior approaches, V-OCBF does not assume access to the dynamics model; instead, it derives a recursive finite-difference barrier update, enabling model-free learning of a barrier that propagates safety information over time. Moreover, V-OCBF incorporates an expectile-based objective that avoids querying the barrier on out-of-distribution actions and restricts updates to the dataset-supported action set. The learned barrier is then used with a Quadratic Program (QP) formulation to synthesize real-time safe control. Across multiple case studies, V-OCBF yields substantially fewer safety violations than baseline methods while maintaining strong task performance, highlighting its scalability for offline synthesis of safety-critical controllers without online interaction or hand-engineered barriers.

