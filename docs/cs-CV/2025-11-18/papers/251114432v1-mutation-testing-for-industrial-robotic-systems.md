---
layout: default
title: Mutation Testing for Industrial Robotic Systems
---

# Mutation Testing for Industrial Robotic Systems

**arXiv**: [2511.14432v1](https://arxiv.org/abs/2511.14432) | [PDF](https://arxiv.org/pdf/2511.14432.pdf)

**作者**: Marcela Gonçalves dos Santos, Sylvain Hallé, Fábio Petrillo

---

## 💡 一句话要点

**提出工业机器人系统专用变异测试方法以提升测试套件质量**

**关键词**: `工业机器人系统` `变异测试` `领域特定算子` `测试套件评估` `软件可靠性`

## 📋 核心要点

1. 工业机器人系统软件故障可致严重事故，需高可靠性保障
2. 定义领域特定变异算子，模拟机器人动作和传感器噪声
3. 实证研究显示方法生成更有效变异体，减少无效或等价案例

## 📄 摘要（原文）

> Industrial robotic systems (IRS) are increasingly deployed in diverse environments, where failures can result in severe accidents and costly downtime. Ensuring the reliability of the software controlling these systems is therefore critical. Mutation testing, a technique widely used in software engineering, evaluates the effectiveness of test suites by introducing small faults, or mutants, into the code. However, traditional mutation operators are poorly suited to robotic programs, which involve message-based commands and interactions with the physical world. This paper explores the adaptation of mutation testing to IRS by defining domain-specific mutation operators that capture the semantics of robot actions and sensor readings. We propose a methodology for generating meaningful mutants at the level of high-level read and write operations, including movement, gripper actions, and sensor noise injection. An empirical study on a pick-and-place scenario demonstrates that our approach produces more informative mutants and reduces the number of invalid or equivalent cases compared to conventional operators. Results highlight the potential of mutation testing to enhance test suite quality and contribute to safer, more reliable industrial robotic systems.

