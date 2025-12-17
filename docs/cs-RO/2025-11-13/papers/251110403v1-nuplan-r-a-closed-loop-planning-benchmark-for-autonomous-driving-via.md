---
layout: default
title: nuPlan-R: A Closed-Loop Planning Benchmark for Autonomous Driving via Reactive Multi-Agent Simulation
---

# nuPlan-R: A Closed-Loop Planning Benchmark for Autonomous Driving via Reactive Multi-Agent Simulation

**arXiv**: [2511.10403v1](https://arxiv.org/abs/2511.10403) | [PDF](https://arxiv.org/pdf/2511.10403.pdf)

**作者**: Mingxing Peng, Ruoyu Yao, Xusen Guo, Jun Ma

---

## 💡 一句话要点

**提出nuPlan-R基准，通过反应式多智能体模拟解决自动驾驶闭环规划评估问题**

**关键词**: `自动驾驶规划` `闭环评估基准` `反应式多智能体模拟` `扩散模型` `交互感知机制` `规划性能指标`

## 📋 核心要点

1. 现有基准依赖规则型反应智能体，缺乏行为多样性和真实交互
2. 引入基于扩散的反应智能体和交互感知选择机制，提升真实性与效率
3. 实验显示模型生成更真实多样行为，强化学习型规划器优势

## 📄 摘要（原文）

> Recent advances in closed-loop planning benchmarks have significantly improved the evaluation of autonomous vehicles. However, existing benchmarks still rely on rule-based reactive agents such as the Intelligent Driver Model (IDM), which lack behavioral diversity and fail to capture realistic human interactions, leading to oversimplified traffic dynamics. To address these limitations, we present nuPlan-R, a new reactive closed-loop planning benchmark that integrates learning-based reactive multi-agent simulation into the nuPlan framework. Our benchmark replaces the rule-based IDM agents with noise-decoupled diffusion-based reactive agents and introduces an interaction-aware agent selection mechanism to ensure both realism and computational efficiency. Furthermore, we extend the benchmark with two additional metrics to enable a more comprehensive assessment of planning performance. Extensive experiments demonstrate that our reactive agent model produces more realistic, diverse, and human-like traffic behaviors, leading to a benchmark environment that better reflects real-world interactive driving. We further reimplement a collection of rule-based, learning-based, and hybrid planning approaches within our nuPlan-R benchmark, providing a clearer reflection of planner performance in complex interactive scenarios and better highlighting the advantages of learning-based planners in handling complex and dynamic scenarios. These results establish nuPlan-R as a new standard for fair, reactive, and realistic closed-loop planning evaluation. We will open-source the code for the new benchmark.

