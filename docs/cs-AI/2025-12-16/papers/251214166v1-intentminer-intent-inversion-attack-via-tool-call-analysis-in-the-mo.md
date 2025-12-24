---
layout: default
title: "IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol"
---

# IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14166" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14166v1</a>
  <a href="https://arxiv.org/pdf/2512.14166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14166v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14166v1', 'IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunhao Yao, Zhiqiang Wang, Haoran Cheng, Yihang Cheng, Haohua Du, Xiang-Yang Li

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-16

**备注**: 12 pages, 6 figures

---

## 💡 一句话要点

**提出IntentMiner，通过分析工具调用日志实现用户意图反演攻击。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `意图反演攻击` `模型上下文协议` `大型语言模型` `隐私安全` `工具调用分析`

## 📋 核心要点

1. 现有基于MCP的LLM代理存在隐私泄露风险，第三方服务器可能通过分析工具调用日志推断用户意图。
2. IntentMiner框架通过分层信息隔离和三维语义分析，从工具调用日志中重建用户意图。
3. 实验表明IntentMiner能够以超过85%的准确率推断用户意图，远超基线方法，验证了隐私风险。

## 📝 摘要（中文）

大型语言模型（LLMs）迅速发展为自主代理，模型上下文协议（MCP）已成为发现和调用外部工具的标准。这种架构虽然将推理引擎与工具执行分离，增强了可扩展性，但也引入了重要的隐私风险：第三方MCP服务器作为半诚实的中介，可以观察到用户信任边界之外的详细工具交互日志。本文首先识别并形式化了一种新的隐私威胁，称为意图反演，即半诚实的MCP服务器仅通过分析合法的工具调用来重建用户的私有底层意图。为了系统地评估这种漏洞，我们提出了IntentMiner框架，该框架利用分层信息隔离和三维语义分析，整合工具目的、调用语句和返回结果，以在步骤级别准确推断用户意图。大量实验表明，IntentMiner与原始用户查询实现了高度的语义对齐（超过85%），显著优于基线方法。这些结果突出了解耦代理架构中固有的隐私风险，揭示了看似良性的工具执行日志可以作为暴露用户秘密的有效途径。

## 🔬 方法详解

**问题定义**：论文旨在解决在基于模型上下文协议（MCP）的LLM代理中，第三方MCP服务器可能通过分析用户与工具的交互日志，推断出用户私有底层意图的问题。现有方法缺乏对这种隐私泄露风险的系统性评估和有效防御机制。痛点在于，即使工具调用本身是合法的，其组合和上下文信息也可能暴露用户的敏感信息。

**核心思路**：论文的核心思路是通过分析工具的目的、调用语句和返回结果，构建用户意图的完整画像。IntentMiner框架利用分层信息隔离和三维语义分析，将工具调用日志转化为可理解的语义表示，并从中提取用户意图。这种方法模拟了攻击者通过观察工具调用日志来推断用户意图的过程，从而评估隐私风险。

**技术框架**：IntentMiner框架包含以下主要模块：1) **工具调用日志收集**：收集用户与工具交互的详细日志，包括工具名称、调用参数、返回结果等。2) **分层信息隔离**：对工具调用日志进行分层处理，隔离不同层级的信息，例如工具目的、调用语句和返回结果。3) **三维语义分析**：从工具目的、调用语句和返回结果三个维度对工具调用日志进行语义分析，提取关键信息。4) **意图推断**：利用提取的语义信息，推断用户的底层意图。

**关键创新**：论文的关键创新在于提出了意图反演攻击的概念，并设计了IntentMiner框架来系统性地评估这种攻击的有效性。与现有方法不同，IntentMiner不仅关注单个工具调用的安全性，更关注工具调用序列的整体语义，从而能够更准确地推断用户意图。

**关键设计**：IntentMiner的关键设计包括：1) **分层信息隔离策略**：根据工具调用日志的不同属性，将其划分为不同的层级，例如工具目的、调用语句和返回结果。2) **三维语义分析方法**：针对每个层级的信息，采用不同的语义分析技术，例如自然语言处理、知识图谱等。3) **意图推断模型**：利用机器学习模型，例如深度神经网络，从提取的语义信息中推断用户的底层意图。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14166v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14166v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14166v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，IntentMiner能够以超过85%的准确率推断用户的底层意图，显著优于基线方法。这表明基于工具调用日志的意图反演攻击具有很高的可行性，凸显了基于MCP的LLM代理中存在的严重隐私风险。实验还验证了IntentMiner框架的有效性，证明其可以作为评估和增强LLM代理隐私安全性的有力工具。

## 🎯 应用场景

该研究成果可应用于评估和增强基于LLM代理的系统的隐私安全性。通过IntentMiner框架，开发者可以识别潜在的意图反演攻击风险，并采取相应的防御措施，例如限制工具调用日志的访问权限、对工具调用日志进行脱敏处理等。此外，该研究还可以促进对LLM代理隐私保护技术的进一步研究，例如差分隐私、联邦学习等。

## 📄 摘要（原文）

> The rapid evolution of Large Language Models (LLMs) into autonomous agents has led to the adoption of the Model Context Protocol (MCP) as a standard for discovering and invoking external tools. While this architecture decouples the reasoning engine from tool execution to enhance scalability, it introduces a significant privacy surface: third-party MCP servers, acting as semi-honest intermediaries, can observe detailed tool interaction logs outside the user's trusted boundary. In this paper, we first identify and formalize a novel privacy threat termed Intent Inversion, where a semi-honest MCP server attempts to reconstruct the user's private underlying intent solely by analyzing legitimate tool calls. To systematically assess this vulnerability, we propose IntentMiner, a framework that leverages Hierarchical Information Isolation and Three-Dimensional Semantic Analysis, integrating tool purpose, call statements, and returned results, to accurately infer user intent at the step level. Extensive experiments demonstrate that IntentMiner achieves a high degree of semantic alignment (over 85%) with original user queries, significantly outperforming baseline approaches. These results highlight the inherent privacy risks in decoupled agent architectures, revealing that seemingly benign tool execution logs can serve as a potent vector for exposing user secrets.

