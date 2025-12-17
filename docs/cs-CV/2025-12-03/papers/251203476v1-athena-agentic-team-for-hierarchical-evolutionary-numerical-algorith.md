---
layout: default
title: ATHENA: Agentic Team for Hierarchical Evolutionary Numerical Algorithms
---

# ATHENA: Agentic Team for Hierarchical Evolutionary Numerical Algorithms

**arXiv**: [2512.03476v1](https://arxiv.org/abs/2512.03476) | [PDF](https://arxiv.org/pdf/2512.03476.pdf)

**作者**: Juan Diego Toscano, Daniel T. Chen, George Em Karniadakis

---

## 💡 一句话要点

**提出ATHENA框架以解决科学计算与科学机器学习中理论与实现间的瓶颈问题。**

**关键词**: `科学计算` `科学机器学习` `智能体框架` `上下文赌博机` `数值算法` `人机协作`

## 📋 核心要点

1. 核心问题：科学计算与科学机器学习中理论概念化与计算实现间存在显著差距，阻碍研究效率。
2. 方法要点：基于HENA循环的智能体框架，通过上下文赌博机问题驱动，结合专家蓝图生成可执行代码以优化科学奖励。
3. 实验或效果：在SciC中自主识别数学对称性，在SciML中处理不适定问题，验证误差达10^{-14}，并支持人机协作提升性能。

## 📄 摘要（原文）

> Bridging the gap between theoretical conceptualization and computational implementation is a major bottleneck in Scientific Computing (SciC) and Scientific Machine Learning (SciML). We introduce ATHENA (Agentic Team for Hierarchical Evolutionary Numerical Algorithms), an agentic framework designed as an Autonomous Lab to manage the end-to-end computational research lifecycle. Its core is the HENA loop, a knowledge-driven diagnostic process framed as a Contextual Bandit problem. Acting as an online learner, the system analyzes prior trials to select structural `actions' ($A_n$) from combinatorial spaces guided by expert blueprints (e.g., Universal Approximation, Physics-Informed constraints). These actions are translated into executable code ($S_n$) to generate scientific rewards ($R_n$). ATHENA transcends standard automation: in SciC, it autonomously identifies mathematical symmetries for exact analytical solutions or derives stable numerical solvers where foundation models fail. In SciML, it performs deep diagnosis to tackle ill-posed formulations and combines hybrid symbolic-numeric workflows (e.g., coupling PINNs with FEM) to resolve multiphysics problems. The framework achieves super-human performance, reaching validation errors of $10^{-14}$. Furthermore, collaborative ``human-in-the-loop" intervention allows the system to bridge stability gaps, improving results by an order of magnitude. This paradigm shift focuses from implementation mechanics to methodological innovation, accelerating scientific discovery.

