---
layout: default
title: Behavior Trees vs Executable Ontologies: a Comparative Analysis of Robot Control Paradigms
---

# Behavior Trees vs Executable Ontologies: a Comparative Analysis of Robot Control Paradigms

**arXiv**: [2511.15274v1](https://arxiv.org/abs/2511.15274) | [PDF](https://arxiv.org/pdf/2511.15274.pdf)

**作者**: Alexander Boldachev

---

## 💡 一句话要点

**比较行为树与可执行本体在机器人控制中的架构差异与适用场景**

**关键词**: `行为树` `可执行本体` `机器人控制` `事件驱动` `语义建模` `模块化架构`

## 📋 核心要点

1. 核心问题：传统机器人控制存在语义-过程鸿沟，需改进行为建模方法。
2. 方法要点：可执行本体采用事件驱动状态传播，替代行为树的轮询执行。
3. 实验或效果：在移动操作任务中，可执行本体实现高反应性和模块性。

## 📄 摘要（原文）

> This paper compares two distinct approaches to modeling robotic behavior: imperative Behavior Trees (BTs) and declarative Executable Ontologies (EO), implemented through the boldsea framework. BTs structure behavior hierarchically using control-flow, whereas EO represents the domain as a temporal, event-based semantic graph driven by dataflow rules. We demonstrate that EO achieves comparable reactivity and modularity to BTs through a fundamentally different architecture: replacing polling-based tick execution with event-driven state propagation. We propose that EO offers an alternative framework, moving from procedural programming to semantic domain modeling, to address the semantic-process gap in traditional robotic control. EO supports runtime model modification, full temporal traceability, and a unified representation of data, logic, and interface - features that are difficult or sometimes impossible to achieve with BTs, although BTs excel in established, predictable scenarios. The comparison is grounded in a practical mobile manipulation task. This comparison highlights the respective operational strengths of each approach in dynamic, evolving robotic systems.

