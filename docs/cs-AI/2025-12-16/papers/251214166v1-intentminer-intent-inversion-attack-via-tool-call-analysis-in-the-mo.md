---
layout: default
title: IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol
---

# IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14166" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14166v1</a>
  <a href="https://arxiv.org/pdf/2512.14166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14166v1" onclick="toggleFavorite(this, '2512.14166v1', 'IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunhao Yao, Zhiqiang Wang, Haoran Cheng, Yihang Cheng, Haohua Du, Xiang-Yang Li

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-16

**备注**: 12 pages, 6 figures

---

## 💡 一句话要点

**提出IntentMiner框架，通过分析工具调用日志实现用户意图反演攻击。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `意图反演攻击` `模型上下文协议` `大型语言模型代理` `隐私泄露` `工具调用分析`

## 📋 核心要点

1. 现有基于MCP的LLM代理架构存在隐私漏洞，第三方服务器可能通过工具调用日志推断用户意图。
2. IntentMiner框架通过分层信息隔离和三维语义分析，从工具调用中提取用户意图。
3. 实验表明，IntentMiner能够以超过85%的准确率重构用户意图，远超基线方法。

## 📝 摘要（中文）

大型语言模型（LLMs）迅速发展为自主代理，模型上下文协议（MCP）已成为发现和调用外部工具的标准。虽然这种架构将推理引擎与工具执行分离，以提高可扩展性，但也引入了一个重要的隐私风险：第三方MCP服务器作为半诚实的中介，可以观察到用户信任边界之外的详细工具交互日志。本文首次识别并形式化了一种新的隐私威胁，称为意图反演，即半诚实的MCP服务器仅通过分析合法的工具调用来重建用户的私有底层意图。为了系统地评估这种漏洞，我们提出了IntentMiner，该框架利用分层信息隔离和三维语义分析，整合工具目的、调用语句和返回结果，以在步骤级别准确推断用户意图。大量实验表明，IntentMiner与原始用户查询实现了高度的语义对齐（超过85%），显著优于基线方法。这些结果突出了解耦代理架构中固有的隐私风险，揭示了看似良性的工具执行日志可以作为暴露用户秘密的有效途径。

## 🔬 方法详解

**问题定义**：论文旨在解决在基于模型上下文协议（MCP）的LLM代理架构中，半诚实的第三方MCP服务器通过分析用户与工具的交互日志，反推出用户真实意图的隐私泄露问题。现有方法缺乏对这种新型攻击的有效防御，用户在使用LLM代理时面临潜在的隐私风险。

**核心思路**：论文的核心思路是利用工具调用日志中蕴含的丰富信息，包括工具的目的、调用语句和返回结果，通过语义分析来重建用户的意图。IntentMiner框架假设攻击者（MCP服务器）是半诚实的，即它会按照协议执行操作，但会尝试从观察到的数据中推断出额外的用户信息。

**技术框架**：IntentMiner框架主要包含以下几个模块：1) **工具调用日志收集**：收集用户与工具交互的详细日志，包括工具名称、调用参数、返回结果等。2) **分层信息隔离**：对收集到的日志进行分层处理，隔离敏感信息，防止直接泄露用户隐私。3) **三维语义分析**：从工具目的、调用语句和返回结果三个维度对日志进行语义分析，提取用户意图的关键信息。4) **意图重构**：利用提取的信息，重构用户的原始意图。

**关键创新**：论文的关键创新在于提出了意图反演攻击的概念，并设计了IntentMiner框架来系统地评估这种攻击的有效性。与传统的隐私攻击不同，意图反演攻击不需要直接访问用户的敏感数据，而是通过分析看似无害的工具调用日志来推断用户的意图。

**关键设计**：IntentMiner框架的关键设计包括：1) **分层信息隔离策略**：设计了有效的信息隔离策略，防止直接泄露用户隐私，同时保留足够的信息用于意图推断。2) **三维语义分析方法**：开发了针对工具目的、调用语句和返回结果的语义分析方法，提取用户意图的关键信息。3) **意图重构算法**：设计了意图重构算法，利用提取的信息，尽可能准确地重构用户的原始意图。

## 📊 实验亮点

实验结果表明，IntentMiner框架能够以超过85%的语义对齐率重构用户的原始意图，显著优于基线方法。这表明，即使在看似安全的MCP架构下，用户的隐私仍然面临严重的威胁。实验还评估了不同信息隔离策略对攻击效果的影响，为设计更有效的隐私保护措施提供了参考。

## 🎯 应用场景

该研究成果可应用于评估和增强基于LLM代理的系统的隐私性。通过IntentMiner框架，开发者可以识别潜在的隐私漏洞，并采取相应的防御措施，例如对工具调用日志进行脱敏处理、限制第三方服务器的访问权限等。此外，该研究还可以促进隐私保护技术的进一步发展，例如差分隐私、联邦学习等。

## 📄 摘要（原文）

> The rapid evolution of Large Language Models (LLMs) into autonomous agents has led to the adoption of the Model Context Protocol (MCP) as a standard for discovering and invoking external tools. While this architecture decouples the reasoning engine from tool execution to enhance scalability, it introduces a significant privacy surface: third-party MCP servers, acting as semi-honest intermediaries, can observe detailed tool interaction logs outside the user's trusted boundary. In this paper, we first identify and formalize a novel privacy threat termed Intent Inversion, where a semi-honest MCP server attempts to reconstruct the user's private underlying intent solely by analyzing legitimate tool calls. To systematically assess this vulnerability, we propose IntentMiner, a framework that leverages Hierarchical Information Isolation and Three-Dimensional Semantic Analysis, integrating tool purpose, call statements, and returned results, to accurately infer user intent at the step level. Extensive experiments demonstrate that IntentMiner achieves a high degree of semantic alignment (over 85%) with original user queries, significantly outperforming baseline approaches. These results highlight the inherent privacy risks in decoupled agent architectures, revealing that seemingly benign tool execution logs can serve as a potent vector for exposing user secrets.

