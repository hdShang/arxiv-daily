---
layout: default
title: IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol
---

# IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14166" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14166</a>
  <a href="https://arxiv.org/pdf/2512.14166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14166" onclick="toggleFavorite(this, '2512.14166', 'IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunhao Yao, Zhiqiang Wang, Haoran Cheng, Yihang Cheng, Haohua Du, Xiang-Yang Li

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出IntentMiner框架，通过分析工具调用日志实现用户意图反演攻击。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `意图反演` `模型上下文协议` `大型语言模型` `隐私攻击` `工具调用分析`

## 📋 核心要点

1. 现有基于MCP的LLM代理架构存在隐私漏洞，第三方服务器可能通过分析工具调用推断用户意图。
2. IntentMiner框架通过分层信息隔离和三维语义分析，从工具调用日志中重建用户意图。
3. 实验表明IntentMiner能够以超过85%的准确率推断用户意图，远超基线方法，验证了攻击的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）向自主代理的快速演进促使模型上下文协议（MCP）被广泛采用，作为发现和调用外部工具的标准。虽然这种架构将推理引擎与工具执行分离，以提高可扩展性，但也引入了一个重要的隐私风险：第三方MCP服务器作为半诚实的中介，可以观察到用户信任边界之外的详细工具交互日志。本文首次识别并形式化了一种新的隐私威胁，称为意图反演，即半诚实MCP服务器仅通过分析合法的工具调用来重建用户的私有底层意图。为了系统地评估这种漏洞，我们提出了IntentMiner，一个利用分层信息隔离和三维语义分析的框架，整合工具目的、调用语句和返回结果，以在步骤级别准确推断用户意图。大量实验表明，IntentMiner与原始用户查询实现了高度的语义对齐（超过85%），显著优于基线方法。这些结果突出了解耦代理架构中固有的隐私风险，揭示了看似良性的工具执行日志可以作为暴露用户秘密的有效途径。

## 🔬 方法详解

**问题定义**：论文旨在解决在基于模型上下文协议（MCP）的LLM代理架构中，第三方MCP服务器可能通过分析用户与工具的交互日志来推断用户真实意图的隐私问题。现有方法缺乏对这种新型隐私威胁的系统性分析和有效防御机制。攻击者（半诚实MCP服务器）的目标是从合法的工具调用序列中反推出用户的原始查询意图。

**核心思路**：论文的核心思路是利用工具调用日志中蕴含的丰富语义信息，包括工具的目的、调用语句和返回结果，通过综合分析这些信息来重建用户的意图。这种方法基于一个假设：即使工具调用本身是合法的，其序列和内容也可能泄露用户的敏感信息。通过模拟攻击者的视角，评估现有架构的隐私风险。

**技术框架**：IntentMiner框架包含以下主要模块：1) **数据收集模块**：收集用户与工具交互的日志，包括工具名称、调用参数和返回结果。2) **分层信息隔离模块**：对收集到的数据进行预处理，隔离不同层次的信息，例如工具目的、调用语句和返回结果。3) **三维语义分析模块**：从工具目的、调用语句和返回结果三个维度对数据进行语义分析，提取关键信息。4) **意图推断模块**：利用提取的语义信息，结合机器学习模型（例如，基于Transformer的模型），推断用户的原始意图。

**关键创新**：论文的关键创新在于：1) 首次识别并形式化了“意图反演”这种新型隐私威胁。2) 提出了IntentMiner框架，该框架能够有效地从工具调用日志中推断用户意图。3) 采用了分层信息隔离和三维语义分析技术，提高了意图推断的准确性。与现有方法相比，IntentMiner更关注工具调用日志中蕴含的语义信息，能够更准确地重建用户意图。

**关键设计**：在三维语义分析模块中，论文可能使用了预训练的语言模型（例如BERT或RoBERTa）来提取工具目的、调用语句和返回结果的语义特征。意图推断模块可能采用了序列到序列的模型结构，将工具调用序列作为输入，用户的原始意图作为输出。损失函数可能采用了交叉熵损失或类似的损失函数，用于衡量推断意图与原始意图之间的差异。具体的参数设置和网络结构细节未知，需要在论文中进一步查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14166/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14166/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14166/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，IntentMiner能够以超过85%的语义对齐度（与原始用户查询相比）推断用户意图，显著优于基线方法。这一结果表明，即使工具调用本身是合法的，其序列和内容也可能泄露用户的敏感信息。该研究揭示了基于MCP的LLM代理架构中存在的严重隐私风险，并为开发更安全的LLM代理系统提供了重要的参考。

## 🎯 应用场景

该研究成果可应用于评估和增强基于LLM代理的系统的隐私性。通过IntentMiner，开发者可以识别潜在的隐私漏洞，并采取相应的安全措施，例如对工具调用日志进行脱敏处理、限制第三方服务器的访问权限等。此外，该研究还可以促进隐私保护技术的研发，例如差分隐私、联邦学习等，以保护用户在使用LLM代理时的隐私。

## 📄 摘要（原文）

> The rapid evolution of Large Language Models (LLMs) into autonomous agents has led to the adoption of the Model Context Protocol (MCP) as a standard for discovering and invoking external tools. While this architecture decouples the reasoning engine from tool execution to enhance scalability, it introduces a significant privacy surface: third-party MCP servers, acting as semi-honest intermediaries, can observe detailed tool interaction logs outside the user's trusted boundary. In this paper, we first identify and formalize a novel privacy threat termed Intent Inversion, where a semi-honest MCP server attempts to reconstruct the user's private underlying intent solely by analyzing legitimate tool calls. To systematically assess this vulnerability, we propose IntentMiner, a framework that leverages Hierarchical Information Isolation and Three-Dimensional Semantic Analysis, integrating tool purpose, call statements, and returned results, to accurately infer user intent at the step level. Extensive experiments demonstrate that IntentMiner achieves a high degree of semantic alignment (over 85%) with original user queries, significantly outperforming baseline approaches. These results highlight the inherent privacy risks in decoupled agent architectures, revealing that seemingly benign tool execution logs can serve as a potent vector for exposing user secrets.

