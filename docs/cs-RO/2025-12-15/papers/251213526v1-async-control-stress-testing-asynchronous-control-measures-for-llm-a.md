---
layout: default
title: Async Control: Stress-testing Asynchronous Control Measures for LLM Agents
---

# Async Control: Stress-testing Asynchronous Control Measures for LLM Agents

**arXiv**: [2512.13526v1](https://arxiv.org/abs/2512.13526) | [PDF](https://arxiv.org/pdf/2512.13526.pdf)

**作者**: Asa Cooper Stickland, Jan Michelfeit, Arathi Mani, Charlie Griffin, Ollie Matthews, Tomek Korbak, Rogan Inglis, Oliver Makins, Alan Cooney

---

## 💡 一句话要点

**提出异步监控方法以评估LLM代理在软件工程中的破坏风险**

**关键词**: `LLM代理安全` `异步监控` `对抗游戏` `软件工程环境` `风险评估`

## 📋 核心要点

1. 核心问题：LLM代理在敏感代码库中可能故意破坏，需监控其行为以防止不可逆损害。
2. 方法要点：采用异步监控，通过红蓝队对抗游戏开发监控系统，不增加运行时延迟。
3. 实验或效果：在5个软件工程环境中，集成监控器在1%误报率下达到6%漏报率，并基于此估计部署风险。

## 📄 摘要（原文）

> LLM-based software engineering agents are increasingly used in real-world development tasks, often with access to sensitive data or security-critical codebases. Such agents could intentionally sabotage these codebases if they were misaligned. We investigate asynchronous monitoring, in which a monitoring system reviews agent actions after the fact. Unlike synchronous monitoring, this approach does not impose runtime latency, while still attempting to disrupt attacks before irreversible harm occurs. We treat monitor development as an adversarial game between a blue team (who design monitors) and a red team (who create sabotaging agents). We attempt to set the game rules such that they upper bound the sabotage potential of an agent based on Claude 4.1 Opus. To ground this game in a realistic, high-stakes deployment scenario, we develop a suite of 5 diverse software engineering environments that simulate tasks that an agent might perform within an AI developer's internal infrastructure. Over the course of the game, we develop an ensemble monitor that achieves a 6% false negative rate at 1% false positive rate on a held out test environment. Then, we estimate risk of sabotage at deployment time by extrapolating from our monitor's false negative rate. We describe one simple model for this extrapolation, present a sensitivity analysis, and describe situations in which the model would be invalid. Code is available at: https://github.com/UKGovernmentBEIS/async-control.

