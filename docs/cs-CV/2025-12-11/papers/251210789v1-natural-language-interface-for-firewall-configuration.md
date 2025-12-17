---
layout: default
title: Natural Language Interface for Firewall Configuration
---

# Natural Language Interface for Firewall Configuration

**arXiv**: [2512.10789v1](https://arxiv.org/abs/2512.10789) | [PDF](https://arxiv.org/pdf/2512.10789.pdf)

**作者**: F. Taghiyev, A. Aslanbayli

---

## 💡 一句话要点

**提出自然语言接口框架以简化企业防火墙配置管理**

**关键词**: `自然语言接口` `防火墙配置` `中间表示` `确定性编译` `验证层` `企业网络管理`

## 📋 核心要点

1. 核心问题：企业防火墙配置复杂，需专业命令行知识，易出错且效率低。
2. 方法要点：设计基于紧凑模式绑定的中间表示，将自然语言意图转换为设备特定配置，使用LLM辅助解析但保持编译确定性。
3. 实验或效果：原型集成三层验证，在合成网络数据集上测试，支持Palo Alto PAN OS并具可扩展性。

## 📄 摘要（原文）

> This paper presents the design and prototype implementation of a natural language interface for configuring enterprise firewalls. The framework allows administrators to express access control policies in plain language, which are then translated into vendor specific configurations. A compact schema bound intermediate representation separates human intent from device syntax and in the current prototype compiles to Palo Alto PAN OS command line configuration while remaining extensible to other platforms. Large language models are used only as assistive parsers that generate typed intermediate representation objects, while compilation and enforcement remain deterministic. The prototype integrates three validation layers, namely a static linter that checks structural and vendor specific constraints, a safety gate that blocks overly permissive rules such as any to any allows, and a Batfish based simulator that validates configuration syntax and referential integrity against a synthetic device model. The paper describes the architecture, implementation, and test methodology on synthetic network context datasets and discusses how this approach can evolve into a scalable auditable and human centered workflow for firewall policy management.

