---
layout: default
title: Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs
---

# Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs

**arXiv**: [2512.04668v1](https://arxiv.org/abs/2512.04668) | [PDF](https://arxiv.org/pdf/2512.04668.pdf)

**作者**: Jinbo Liu, Defu Cao, Yifei Wei, Tianyao Su, Yuan Liang, Yushun Dong, Yue Zhao, Xiyang Hu

---

## 💡 一句话要点

**提出MAMA框架以量化多智能体LLM系统中图拓扑对内存泄漏的影响**

**关键词**: `多智能体系统` `内存泄漏` `图拓扑` `隐私风险` `LLM安全` `PII保护`

## 📋 核心要点

1. 核心问题：图拓扑如何影响多智能体LLM系统的内存泄漏，缺乏量化研究
2. 方法要点：基于合成文档和两阶段协议（Engram和Resonance），测量不同拓扑下的PII恢复率
3. 实验或效果：发现全连接图泄漏最大，链状图保护最强，拓扑排名与模型选择无关

## 📄 摘要（原文）

> Graph topology is a fundamental determinant of memory leakage in multi-agent LLM systems, yet its effects remain poorly quantified. We introduce MAMA (Multi-Agent Memory Attack), a framework that measures how network structure shapes leakage. MAMA operates on synthetic documents containing labeled Personally Identifiable Information (PII) entities, from which we generate sanitized task instructions. We execute a two-phase protocol: Engram (seeding private information into a target agent's memory) and Resonance (multi-round interaction where an attacker attempts extraction). Over up to 10 interaction rounds, we quantify leakage as the fraction of ground-truth PII recovered from attacking agent outputs via exact matching. We systematically evaluate six common network topologies (fully connected, ring, chain, binary tree, star, and star-ring), varying agent counts $n\in\{4,5,6\}$, attacker-target placements, and base models. Our findings reveal consistent patterns: fully connected graphs exhibit maximum leakage while chains provide strongest protection; shorter attacker-target graph distance and higher target centrality significantly increase vulnerability; leakage rises sharply in early rounds before plateauing; model choice shifts absolute leakage rates but preserves topology rankings; temporal/locational PII attributes leak more readily than identity credentials or regulated identifiers. These results provide the first systematic mapping from architectural choices to measurable privacy risk, yielding actionable guidance: prefer sparse or hierarchical connectivity, maximize attacker-target separation, limit node degree and network radius, avoid shortcuts bypassing hubs, and implement topology-aware access controls.

