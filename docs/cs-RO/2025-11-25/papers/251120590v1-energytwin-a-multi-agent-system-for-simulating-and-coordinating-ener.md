---
layout: default
title: EnergyTwin: A Multi-Agent System for Simulating and Coordinating Energy Microgrids
---

# EnergyTwin: A Multi-Agent System for Simulating and Coordinating Energy Microgrids

**arXiv**: [2511.20590v1](https://arxiv.org/abs/2511.20590) | [PDF](https://arxiv.org/pdf/2511.20590.pdf)

**作者**: Jakub Muszyński, Ignacy Walużenicz, Patryk Zan, Zofia Wrona, Maria Ganzha, Marcin Paprzycki, Costin Bădică

---

## 💡 一句话要点

**提出EnergyTwin多代理系统，用于模拟和协调能源微电网以提高自给和韧性。**

**关键词**: `微电网模拟` `多代理系统` `能源协调` `预测规划` `数字孪生`

## 📋 核心要点

1. 微电网需协调异构能源资源，现有工具缺乏物理基础与分散决策结合。
2. EnergyTwin结合物理模型与预测驱动滚动规划，代理通过合约交互实现分散控制。
3. 校园场景实验显示，预测规划提升自给率、电池储备，减少低韧性状态暴露。

## 📄 摘要（原文）

> Microgrids are deployed to reduce purchased grid energy, limit exposure to volatile tariffs, and ensure service continuity during disturbances. This requires coordinating heterogeneous distributed energy resources across multiple time scales and under variable conditions. Among existing tools, typically, power-system simulators capture physical behaviour but assume centralized control, while multi-agent frameworks model decentralized decision-making but represent energy with no physical grounding. In this context, the EnergyTwin is introduced, an agent-based microgrid simulation environment that couples physically grounded models with forecast-informed, rolling-horizon planning, and negotiations. Each asset is modeled as an agent, interacting with a central agent that obtains forecasts, formulates predictions, and allocates energy through contract-based interactions. EnergyTwin targets tertiary-layer decision making and is extensible for digital-twin use. Its feasibility was evaluated in a university campus microgrid scenario where multiple planning strategies were compared. Achieved results show that forecast-driven rolling-horizon planning increases local energy self-sufficiency, maintains higher battery reserves, and reduces exposure to low-resilience operating states. They demonstrate also potential of EnergyTwin as platform supporting research on resilient, negotiation-driven microgrids.

