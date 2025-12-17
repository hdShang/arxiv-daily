---
layout: default
title: Please Don't Kill My Vibe: Empowering Agents with Data Flow Control
---

# Please Don't Kill My Vibe: Empowering Agents with Data Flow Control

**arXiv**: [2512.05374v1](https://arxiv.org/abs/2512.05374) | [PDF](https://arxiv.org/pdf/2512.05374.pdf)

**作者**: Charlie Summers, Haneen Mohammed, Eugene Wu

---

## 💡 一句话要点

**提出数据流控制以解决LLM代理中的策略违规与安全风险**

**关键词**: `数据流控制` `LLM代理` `策略执行` `DBMS集成` `安全风险` `代理生态系统`

## 📋 核心要点

1. 核心问题：LLM代理缺乏管理不良数据流的可见性和机制，导致策略违规、过程腐败和安全漏洞。
2. 方法要点：主张系统原生支持数据流控制，将策略执行从应用层转移到DBMS，类似数据验证和访问控制的演变。
3. 实验或效果：描述了为DBMS开发便携式数据流控制实例的早期工作，并概述了面向代理生态系统的更广泛研究议程。

## 📄 摘要（原文）

> The promise of Large Language Model (LLM) agents is to perform complex, stateful tasks. This promise is stunted by significant risks - policy violations, process corruption, and security flaws - that stem from the lack of visibility and mechanisms to manage undesirable data flows produced by agent actions. Today, agent workflows are responsible for enforcing these policies in ad hoc ways. Just as data validation and access controls shifted from the application to the DBMS, freeing application developers from these concerns, we argue that systems should support Data Flow Controls (DFCs) and enforce DFC policies natively. This paper describes early work developing a portable instance of DFC for DBMSes and outlines a broader research agenda toward DFC for agent ecosystems.

