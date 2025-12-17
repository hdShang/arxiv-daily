---
layout: default
title: IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol
---

# IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol

**arXiv**: [2512.14166v1](https://arxiv.org/abs/2512.14166) | [PDF](https://arxiv.org/pdf/2512.14166.pdf)

**作者**: Yunhao Yao, Zhiqiang Wang, Haoran Cheng, Yihang Cheng, Haohua Du, Xiang-Yang Li

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-16

**备注**: 12 pages, 6 figures

---

## 💡 一句话要点

**提出IntentMiner框架，通过分析模型上下文协议中的工具调用，揭示半诚实服务器重构用户意图的隐私威胁。**

**关键词**: `意图反转攻击` `模型上下文协议` `隐私威胁` `工具调用分析` `语义对齐` `自主代理` `人工智能安全` `分层信息隔离`

## 📋 核心要点

1. 核心问题：模型上下文协议（MCP）架构中，半诚实服务器通过工具交互日志重构用户意图，导致隐私泄露风险。
2. 方法要点：提出IntentMiner框架，结合分层信息隔离和三维语义分析，从工具调用中准确推断用户意图。
3. 实验或效果：实验显示IntentMiner语义对齐率超过85%，显著优于基线，揭示解耦架构的隐私漏洞。

## 📝 摘要（中文）

大型语言模型（LLMs）向自主代理的快速发展促使模型上下文协议（MCP）成为发现和调用外部工具的标准。虽然这种架构将推理引擎与工具执行解耦以增强可扩展性，但也引入了显著的隐私暴露面：作为半诚实中介的第三方MCP服务器可以在用户信任边界外观察详细的工具交互日志。本文首次识别并形式化了一种名为“意图反转”的新型隐私威胁，即半诚实MCP服务器仅通过分析合法的工具调用来尝试重构用户的私有底层意图。为系统评估此漏洞，我们提出了IntentMiner框架，该框架利用分层信息隔离和三维语义分析，整合工具目的、调用语句和返回结果，以在步骤级别准确推断用户意图。大量实验表明，IntentMiner与原始用户查询实现了高度的语义对齐（超过85%），显著优于基线方法。这些结果突显了解耦代理架构中固有的隐私风险，揭示了看似良性的工具执行日志可能成为暴露用户秘密的有效载体。

## 🔬 方法详解

IntentMiner的整体框架基于分层信息隔离和三维语义分析。首先，通过分层信息隔离将工具调用日志分解为结构化组件，以隔离关键信息。然后，进行三维语义分析，整合工具目的（如工具的功能描述）、调用语句（用户的具体请求）和返回结果（工具的输出），以构建意图推断模型。关键技术创新点在于将工具交互的多维度信息融合，实现步骤级别的意图重建，而现有方法通常仅依赖单一维度或忽略返回结果。与现有方法的主要区别在于其系统性评估隐私威胁，而非仅关注攻击检测或防御，从而更全面地揭示MCP架构中的隐私风险。

## 📊 实验亮点

IntentMiner在实验中实现了超过85%的语义对齐率，显著优于基线方法，有效揭示了半诚实服务器通过工具调用重构用户意图的高风险，突显了解耦架构的隐私脆弱性。

## 🎯 应用场景

该研究可应用于人工智能安全领域，帮助评估和增强自主代理系统的隐私保护机制，特别是在基于MCP的LLM应用中，如智能助手、自动化工作流和第三方工具集成场景，以防范意图泄露风险。

## 📄 摘要（原文）

> The rapid evolution of Large Language Models (LLMs) into autonomous agents has led to the adoption of the Model Context Protocol (MCP) as a standard for discovering and invoking external tools. While this architecture decouples the reasoning engine from tool execution to enhance scalability, it introduces a significant privacy surface: third-party MCP servers, acting as semi-honest intermediaries, can observe detailed tool interaction logs outside the user's trusted boundary. In this paper, we first identify and formalize a novel privacy threat termed Intent Inversion, where a semi-honest MCP server attempts to reconstruct the user's private underlying intent solely by analyzing legitimate tool calls. To systematically assess this vulnerability, we propose IntentMiner, a framework that leverages Hierarchical Information Isolation and Three-Dimensional Semantic Analysis, integrating tool purpose, call statements, and returned results, to accurately infer user intent at the step level. Extensive experiments demonstrate that IntentMiner achieves a high degree of semantic alignment (over 85%) with original user queries, significantly outperforming baseline approaches. These results highlight the inherent privacy risks in decoupled agent architectures, revealing that seemingly benign tool execution logs can serve as a potent vector for exposing user secrets.

