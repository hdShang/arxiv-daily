---
layout: default
title: SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs
---

# SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs

**arXiv**: [2512.09543v1](https://arxiv.org/abs/2512.09543) | [PDF](https://arxiv.org/pdf/2512.09543.pdf)

**作者**: Arihant Tripathy, Ch Pavan Harshit, Karthik Vaidhyanathan

---

## 💡 一句话要点

**实证研究SLM在代理问题解决框架中的能效，揭示架构设计是能耗主因且能量浪费严重**

**关键词**: `小语言模型` `能效分析` `代理框架` `软件工程自动化` `资源消耗`

## 📋 核心要点

1. 核心问题：SLM在复杂代理框架中的实际能效和性能未知，限制本地部署应用
2. 方法要点：在固定硬件上评估四个框架使用两种SLM的性能、能耗和资源消耗
3. 实验或效果：框架架构是能耗主因，但能量浪费严重，任务解决率近零

## 📄 摘要（原文）

> Context. LLM-based autonomous agents in software engineering rely on large, proprietary models, limiting local deployment. This has spurred interest in Small Language Models (SLMs), but their practical effectiveness and efficiency within complex agentic frameworks for automated issue resolution remain poorly understood.
>   Goal. We investigate the performance, energy efficiency, and resource consumption of four leading agentic issue resolution frameworks when deliberately constrained to using SLMs. We aim to assess the viability of these systems for this task in resource-limited settings and characterize the resulting trade-offs.
>   Method. We conduct a controlled evaluation of four leading agentic frameworks (SWE-Agent, OpenHands, Mini SWE Agent, AutoCodeRover) using two SLMs (Gemma-3 4B, Qwen-3 1.7B) on the SWE-bench Verified Mini benchmark. On fixed hardware, we measure energy, duration, token usage, and memory over 150 runs per configuration.
>   Results. We find that framework architecture is the primary driver of energy consumption. The most energy-intensive framework, AutoCodeRover (Gemma), consumed 9.4x more energy on average than the least energy-intensive, OpenHands (Gemma). However, this energy is largely wasted. Task resolution rates were near-zero, demonstrating that current frameworks, when paired with SLMs, consume significant energy on unproductive reasoning loops. The SLM's limited reasoning was the bottleneck for success, but the framework's design was the bottleneck for efficiency.
>   Conclusions. Current agentic frameworks, designed for powerful LLMs, fail to operate efficiently with SLMs. We find that framework architecture is the primary driver of energy consumption, but this energy is largely wasted due to the SLMs' limited reasoning. Viable low-energy solutions require shifting from passive orchestration to architectures that actively manage SLM weaknesses.

