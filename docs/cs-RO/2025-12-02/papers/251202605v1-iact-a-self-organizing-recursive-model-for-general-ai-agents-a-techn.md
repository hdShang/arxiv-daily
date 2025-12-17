---
layout: default
title: IACT: A Self-Organizing Recursive Model for General AI Agents: A Technical White Paper on the Architecture Behind kragent.ai
---

# IACT: A Self-Organizing Recursive Model for General AI Agents: A Technical White Paper on the Architecture Behind kragent.ai

**arXiv**: [2512.02605v1](https://arxiv.org/abs/2512.02605) | [PDF](https://arxiv.org/pdf/2512.02605.pdf)

**作者**: Pengju Lu

---

## 💡 一句话要点

**提出交互式代理调用树模型以解决静态工作流在开放任务中的局限**

**关键词**: `交互式代理` `递归模型` `自主系统` `错误纠正` `开放任务` `对话驱动`

## 📋 核心要点

1. 核心问题：传统代理系统依赖预定义图或编程，难以适应开放任务和错误传播。
2. 方法要点：基于用户对话自主构建动态递归代理拓扑，通过双向状态对话实现交互冗余。
3. 实验或效果：在kragent.ai系统中部署，提供真实工作流的定性证据而非基准测试。

## 📄 摘要（原文）

> This technical white paper introduces the Interactive Agents Call Tree (IACT), a computational model designed to address the limitations of static, hard-coded agent workflows. Unlike traditional systems that require pre-defined graphs or specialized programming, IACT operates as a general-purpose autonomous system driven purely by user dialogue. Given a high-level objective, the system autonomously grows a dynamic, recursive agent topology incrementally tailored to the problem's structure. This allows it to scale its organizational complexity to match open-ended tasks. To mitigate the error propagation inherent in unidirectional function calls, IACT introduces interactional redundancy by replacing rigid invocations with bidirectional, stateful dialogues. This mechanism enables runtime error correction and ambiguity resolution. We describe the architecture, design principles, and practical lessons behind the production deployment of this model in the kragent.ai system, presenting qualitative evidence from real-world workflows rather than exhaustive benchmark results.

