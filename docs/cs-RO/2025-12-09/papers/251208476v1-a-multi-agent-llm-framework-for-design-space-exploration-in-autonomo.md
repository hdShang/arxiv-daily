---
layout: default
title: A Multi-Agent LLM Framework for Design Space Exploration in Autonomous Driving Systems
---

# A Multi-Agent LLM Framework for Design Space Exploration in Autonomous Driving Systems

**arXiv**: [2512.08476v1](https://arxiv.org/abs/2512.08476) | [PDF](https://arxiv.org/pdf/2512.08476.pdf)

**作者**: Po-An Shih, Shao-Hua Wang, Yung-Che Li, Chia-Heng Tu, Chih-Han Chang

---

## 💡 一句话要点

**提出基于多智能体LLM的设计空间探索框架，以自动化自动驾驶系统设计优化。**

**关键词**: `自动驾驶系统` `设计空间探索` `多智能体LLM` `多模态推理` `自动化设计`

## 📋 核心要点

1. 核心问题：传统设计空间探索方法难以处理多模态执行输出和复杂性能权衡，依赖人工评估。
2. 方法要点：利用多智能体LLM集成多模态推理与3D仿真工具，自动化解释执行输出并生成设计点。
3. 实验或效果：在机器人出租车案例中，相比遗传算法基线，在相同探索预算下识别更多帕累托最优、成本效益高的解决方案。

## 📄 摘要（原文）

> Designing autonomous driving systems requires efficient exploration of large hardware/software configuration spaces under diverse environmental conditions, e.g., with varying traffic, weather, and road layouts. Traditional design space exploration (DSE) approaches struggle with multi-modal execution outputs and complex performance trade-offs, and often require human involvement to assess correctness based on execution outputs. This paper presents a multi-agent, large language model (LLM)-based DSE framework, which integrates multi-modal reasoning with 3D simulation and profiling tools to automate the interpretation of execution outputs and guide the exploration of system designs. Specialized LLM agents are leveraged to handle user input interpretation, design point generation, execution orchestration, and analysis of both visual and textual execution outputs, which enables identification of potential bottlenecks without human intervention. A prototype implementation is developed and evaluated on a robotaxi case study (an SAE Level 4 autonomous driving application). Compared with a genetic algorithm baseline, the proposed framework identifies more Pareto-optimal, cost-efficient solutions with reduced navigation time under the same exploration budget. Experimental results also demonstrate the efficiency of the adoption of the LLM-based approach for DSE. We believe that this framework paves the way to the design automation of autonomous driving systems.

