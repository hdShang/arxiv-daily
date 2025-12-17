---
layout: default
title: SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL
---

# SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL

**arXiv**: [2512.04069v1](https://arxiv.org/abs/2512.04069) | [PDF](https://arxiv.org/pdf/2512.04069.pdf)

**作者**: Siyi Chen, Mikaela Angelina Uy, Chan Hee Song, Faisal Ladhak, Adithyavairavan Murali, Qing Qu, Stan Birchfield, Valts Blukis, Jonathan Tremblay

---

## 💡 一句话要点

**提出双交互强化学习框架以增强视觉语言模型的多工具空间推理能力**

**关键词**: `视觉语言模型` `空间推理` `强化学习` `多工具协调` `机器人操作`

## 📋 核心要点

1. 视觉语言模型在度量精确空间推理方面存在不足，多工具协调面临搜索空间大的挑战
2. 采用双阶段训练框架，结合单工具专家演示与前沿模型轨迹，通过强化学习优化工具使用
3. 在空间理解基准测试中实现最先进性能，并展示真实世界机器人操作的可靠性

## 📄 摘要（原文）

> Vision Language Models (VLMs) demonstrate strong qualitative visual understanding, but struggle with metrically precise spatial reasoning required for embodied applications. The agentic paradigm promises that VLMs can use a wide variety of tools that could augment these capabilities, such as depth estimators, segmentation models, and pose estimators. Yet it remains an open challenge how to realize this vision without solely relying on handcrafted prompting strategies or enforcing fixed, predefined tool pipelines that limit VLMs' ability to discover optimal tool-use patterns. Reinforcement Learning could overcome this gap, but has so far been limited to reasoning with a single visual tool due to the large search space in multi-tool reasoning. We introduce Double Interactive Reinforcement Learning (DIRL), a two-phase training framework where VLMs learn to coordinate multiple tools through interactive exploration and feedback. In the teaching phase, we combine demonstrations from a single tool specialist trained via interactive RL with traces from a frontier model using all tools. In the exploration phase, the model further refines multi-tool coordination through continued RL. Our model, SpaceTools, with tool-augmented spatial reasoning ability, achieves state-of-the-art performance on spatial understanding benchmarks (RoboSpatial-Home, BLINK, BOP-ASK) and demonstrates reliable real-world manipulation using a 7-DOF robot as a tool. DIRL provides substantial improvements over the vanilla SFT (+12% on RoboSpatial) and RL (+16% on RoboSpatial) baselines. Project page: https://spacetools.github.io/.

