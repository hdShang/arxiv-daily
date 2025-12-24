---
layout: default
title: "X-SQL: Expert Schema Linking and Understanding of Text-to-SQL with Multi-LLMs"
---

# X-SQL: Expert Schema Linking and Understanding of Text-to-SQL with Multi-LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05899" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05899v1</a>
  <a href="https://arxiv.org/pdf/2509.05899.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05899v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05899v1', 'X-SQL: Expert Schema Linking and Understanding of Text-to-SQL with Multi-LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dazhi Peng

**分类**: cs.LG, cs.DB

**发布日期**: 2025-09-07

---

## 💡 一句话要点

**X-SQL通过多LLM协同，增强模式链接与理解，显著提升Text-to-SQL性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Text-to-SQL` `大型语言模型` `模式链接` `模式理解` `监督微调` `数据库` `代码生成`

## 📋 核心要点

1. 现有Text-to-SQL框架常忽略数据库模式信息的重要性，导致生成的SQL查询质量受限。
2. X-SQL通过X-Linking和X-Admin两个组件，分别增强模式链接和模式理解，从而提升SQL生成质量。
3. 实验结果表明，X-SQL在Spider数据集上取得了领先的执行准确率，证明了其有效性。

## 📝 摘要（中文）

本文提出了一种名为X-SQL的Text-to-SQL框架，该框架利用大型语言模型（LLMs）在代码生成方面的强大能力。研究强调了数据库模式信息在生成高质量SQL查询中的重要性，并提出了一个包含两个组件的数据库模式专家。首先，引入了X-Linking，一种基于LLM监督微调（SFT）的方法，相比现有的开源Text-to-SQL方法，实现了卓越的模式链接效果。其次，创新性地提出了X-Admin组件，专注于模式理解，弥合了抽象模式信息与用户自然语言问题之间的差距。除了更好地学习模式信息外，还实验了在系统中使用多个LLM来进一步提升性能。通过将这些技术融入到端到端框架X-SQL中，在Spider-Dev数据集上实现了84.9%的执行准确率，在Spider-Test数据集上实现了82.5%的执行准确率。这一卓越的性能使X-SQL成为基于开源模型的领先Text-to-SQL框架。

## 🔬 方法详解

**问题定义**：Text-to-SQL任务旨在将自然语言问题转换为可执行的SQL查询。现有方法在利用数据库模式信息方面存在不足，导致生成的SQL查询准确率不高。尤其是在模式链接和模式理解方面，现有方法难以充分利用模式信息来指导SQL生成。

**核心思路**：X-SQL的核心思路是构建一个数据库模式专家，通过两个关键组件X-Linking和X-Admin，分别解决模式链接和模式理解的问题。X-Linking负责将自然语言中的实体与数据库模式中的元素进行精确匹配，X-Admin则负责理解模式的语义信息，并将这些信息融入到SQL生成过程中。

**技术框架**：X-SQL是一个端到端的Text-to-SQL框架，主要包含以下几个阶段：1) 输入自然语言问题和数据库模式信息；2) 使用X-Linking进行模式链接，将问题中的实体与模式元素对应；3) 使用X-Admin进行模式理解，提取模式的语义信息；4) 利用大型语言模型（LLM）生成SQL查询；5) 执行SQL查询并返回结果。框架中可以灵活地使用多个LLM来增强不同组件的性能。

**关键创新**：X-SQL的关键创新在于提出了X-Linking和X-Admin两个组件，专门用于增强模式链接和模式理解。X-Linking通过LLM监督微调（SFT）方法，实现了比现有方法更精确的模式链接。X-Admin则通过弥合抽象模式信息与用户自然语言问题之间的差距，实现了更有效的模式理解。此外，多LLM协同也是一个创新点，允许框架根据不同组件的需求选择合适的LLM。

**关键设计**：X-Linking使用LLM进行监督微调，训练目标是最大化正确模式链接的概率。X-Admin的设计细节未知，但其目标是提取模式的语义信息，可能涉及到知识图谱、语义分析等技术。框架中使用的LLM可以是不同的模型，具体选择取决于组件的需求和性能。

## 📊 实验亮点

X-SQL在Spider-Dev数据集上取得了84.9%的执行准确率，在Spider-Test数据集上取得了82.5%的执行准确率。这些结果显著优于现有的开源Text-to-SQL框架，证明了X-SQL在模式链接和模式理解方面的优势。该框架的性能提升主要归功于X-Linking和X-Admin两个组件的有效设计。

## 🎯 应用场景

X-SQL可应用于智能客服、数据分析、商业智能等领域。它可以帮助用户通过自然语言查询数据库，无需编写复杂的SQL语句，从而提高数据访问效率和用户体验。未来，X-SQL可以进一步扩展到更复杂的数据库和查询场景，并与其他自然语言处理技术相结合，实现更智能化的数据分析。

## 📄 摘要（原文）

> With Large Language Models' (LLMs) emergent abilities on code generation tasks, Text-to-SQL has become one of the most popular downstream applications. Despite the strong results of multiple recent LLM-based Text-to-SQL frameworks, the research community often overlooks the importance of database schema information for generating high-quality SQL queries. We find that such schema information plays a significant or even dominant role in the Text-to-SQL task. To tackle this challenge, we propose a novel database schema expert with two components. We first introduce X-Linking, an LLM Supervised Finetuning (SFT)-based method that achieves superior Schema Linking results compared to existing open-source Text-to-SQL methods. In addition, we innovatively propose an X-Admin component that focuses on Schema Understanding by bridging the gap between abstract schema information and the user's natural language question. Aside from better learning with schema information, we experiment with Multi-LLMs for different components within the system to further boost its performance. By incorporating these techniques into our end-to-end framework, X-SQL, we have achieved Execution Accuracies of 84.9% on the Spider-Dev dataset and 82.5% on the Spider-Test dataset. This outstanding performance establishes X-SQL as the leading Text-to-SQL framework based on open-source models.

