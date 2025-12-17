---
layout: default
title: Towards Trustworthy Legal AI through LLM Agents and Formal Reasoning
---

# Towards Trustworthy Legal AI through LLM Agents and Formal Reasoning

**arXiv**: [2511.21033v1](https://arxiv.org/abs/2511.21033) | [PDF](https://arxiv.org/pdf/2511.21033.pdf)

**作者**: Linze Chen, Yufan Cai, Zhe Hou, Jinsong Dong

---

## 💡 一句话要点

**提出L4M框架，结合LLM代理与形式推理以提升法律AI的可信度**

**关键词**: `法律AI` `形式推理` `LLM代理` `SMT求解器` `可解释性` `对抗学习`

## 📋 核心要点

1. 现有LLM系统缺乏法律决策的形式理性保证，难以确保逻辑一致性
2. 方法整合对抗LLM代理与SMT求解器，实现法规形式化和可验证裁决
3. 实验显示在公共基准上超越先进LLM和基线，提供可解释符号证明

## 📄 摘要（原文）

> The rationality of law manifests in two forms: substantive rationality, which concerns the fairness or moral desirability of outcomes, and formal rationality, which requires legal decisions to follow explicitly stated, general, and logically coherent rules. Existing LLM-based systems excel at surface-level text analysis but lack the guarantees required for principled jurisprudence. We introduce L4M, a novel framework that combines adversarial LLM agents with SMT-solver-backed proofs to unite the interpretive flexibility of natural language with the rigor of symbolic verification. The pipeline consists of three phases: (1) Statute Formalization, where domain-specific prompts convert legal provisions into logical formulae; (2) Dual Fact and Statute Extraction, in which prosecutor- and defense-aligned LLMs independently map case narratives to fact tuples and statutes, ensuring role isolation; and (3) Solver-Centric Adjudication, where an autoformalizer compiles both parties' arguments into logic constraints, and unsat cores trigger iterative self-critique until a satisfiable formula is achieved, which is then verbalized by a Judge-LLM into a transparent verdict and optimized sentence. Experimental results on public benchmarks show that our system surpasses advanced LLMs including GPT-o4-mini, DeepSeek-V3, and Claude 4 as well as state-of-the-art Legal AI baselines, while providing rigorous and explainable symbolic justifications.

