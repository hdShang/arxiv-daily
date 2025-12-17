---
layout: default
title: Satisfiability Modulo Theory Meets Inductive Logic Programming
---

# Satisfiability Modulo Theory Meets Inductive Logic Programming

**arXiv**: [2512.12918v1](https://arxiv.org/abs/2512.12918) | [PDF](https://arxiv.org/pdf/2512.12918.pdf)

**作者**: Nijesh Upreti, Vaishak Belle

---

## 💡 一句话要点

**提出SMT-ILP模块化架构以增强归纳逻辑编程在数值约束学习中的表达能力**

**关键词**: `归纳逻辑编程` `可满足性模理论` `数值约束学习` `混合规则学习` `模块化架构` `符号推理`

## 📋 核心要点

1. 归纳逻辑编程在关系域中学习可解释规则，但难以处理数值约束和算术关系。
2. 通过耦合PyGol与Z3，将候选子句解释为无量化公式，支持符号谓词与数值约束的混合规则学习。
3. 在合成数据集上评估，展示该架构在线性、非线性及多跳推理中的扩展表达能力。

## 📄 摘要（原文）

> Inductive Logic Programming (ILP) provides interpretable rule learning in relational domains, yet remains limited in its ability to induce and reason with numerical constraints. Classical ILP systems operate over discrete predicates and typically rely on discretisation or hand-crafted numerical predicates, making it difficult to infer thresholds or arithmetic relations that must hold jointly across examples. Recent work has begun to address these limitations through tighter integrations of ILP with Satisfiability Modulo Theories (SMT) or specialised numerical inference mechanisms. In this paper we investigate a modular alternative that couples the ILP system PyGol with the SMT solver Z3. Candidate clauses proposed by PyGol are interpreted as quantifier-free formulas over background theories such as linear or nonlinear real arithmetic, allowing numerical parameters to be instantiated and verified by the SMT solver while preserving ILP's declarative relational bias. This supports the induction of hybrid rules that combine symbolic predicates with learned numerical constraints, including thresholds, intervals, and multi-literal arithmetic relations. We formalise this SMT-ILP setting and evaluate it on a suite of synthetic datasets designed to probe linear, relational, nonlinear, and multi-hop reasoning. The results illustrate how a modular SMT-ILP architecture can extend the expressivity of symbolic rule learning, complementing prior numerical ILP approaches while providing a flexible basis for future extensions toward richer theory-aware induction.

