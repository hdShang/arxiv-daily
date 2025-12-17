---
layout: default
title: From CAD to POMDP: Probabilistic Planning for Robotic Disassembly of End-of-Life Products
---

# From CAD to POMDP: Probabilistic Planning for Robotic Disassembly of End-of-Life Products

**arXiv**: [2511.23407v1](https://arxiv.org/abs/2511.23407) | [PDF](https://arxiv.org/pdf/2511.23407.pdf)

**作者**: Jan Baumgärtner, Malte Hansjosten, David Hald, Adrian Hauptmannl, Alexander Puchta, Jürgen Fleischer

---

## 💡 一句话要点

**提出基于POMDP的概率规划框架，用于机器人对不确定状态报废产品的拆卸任务。**

**关键词**: `机器人拆卸规划` `部分可观测马尔可夫决策过程` `概率规划` `强化学习` `贝叶斯滤波` `报废产品处理`

## 📋 核心要点

1. 核心问题：报废产品因磨损或维修导致状态不确定，传统确定性规划方法失效。
2. 方法要点：将拆卸建模为POMDP，从CAD数据自动生成模型，结合强化学习和贝叶斯滤波处理不确定性。
3. 实验或效果：在两种机器人系统上验证，相比基线减少平均拆卸时间和方差，适应模型偏差。

## 📄 摘要（原文）

> To support the circular economy, robotic systems must not only assemble new products but also disassemble end-of-life (EOL) ones for reuse, recycling, or safe disposal. Existing approaches to disassembly sequence planning often assume deterministic and fully observable product models, yet real EOL products frequently deviate from their initial designs due to wear, corrosion, or undocumented repairs. We argue that disassembly should therefore be formulated as a Partially Observable Markov Decision Process (POMDP), which naturally captures uncertainty about the product's internal state. We present a mathematical formulation of disassembly as a POMDP, in which hidden variables represent uncertain structural or physical properties. Building on this formulation, we propose a task and motion planning framework that automatically derives specific POMDP models from CAD data, robot capabilities, and inspection results. To obtain tractable policies, we approximate this formulation with a reinforcement-learning approach that operates on stochastic action outcomes informed by inspection priors, while a Bayesian filter continuously maintains beliefs over latent EOL conditions during execution. Using three products on two robotic systems, we demonstrate that this probabilistic planning framework outperforms deterministic baselines in terms of average disassembly time and variance, generalizes across different robot setups, and successfully adapts to deviations from the CAD model, such as missing or stuck parts.

