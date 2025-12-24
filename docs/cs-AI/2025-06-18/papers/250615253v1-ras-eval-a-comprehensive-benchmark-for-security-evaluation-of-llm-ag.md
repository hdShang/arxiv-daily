---
layout: default
title: "RAS-Eval: A Comprehensive Benchmark for Security Evaluation of LLM Agents in Real-World Environments"
---

# RAS-Eval: A Comprehensive Benchmark for Security Evaluation of LLM Agents in Real-World Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15253" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15253v1</a>
  <a href="https://arxiv.org/pdf/2506.15253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15253v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15253v1', 'RAS-Eval: A Comprehensive Benchmark for Security Evaluation of LLM Agents in Real-World Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchuan Fu, Xiaohan Yuan, Dongxia Wang

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-18

**备注**: 12 pages, 8 figures

**🔗 代码/项目**: [GITHUB](https://github.com/lanzer-tree/RAS-Eval)

---

## 💡 一句话要点

**提出RAS-Eval以解决LLM代理安全评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全评估` `大型语言模型` `动态环境` `攻击任务` `任务完成率` `常见弱点枚举` `评估基准`

## 📋 核心要点

1. 现有方法缺乏针对LLM代理在动态环境中的标准化安全评估基准，导致安全漏洞难以识别和修复。
2. 本文提出RAS-Eval，通过构建全面的安全基准，支持多种环境下的评估，填补了这一空白。
3. 实验结果表明，攻击显著降低了代理的任务完成率，且较大模型在安全能力上表现优于小模型，揭示了潜在风险。

## 📝 摘要（中文）

随着大型语言模型（LLM）代理在医疗和金融等关键领域的快速部署，建立健全的安全框架显得尤为重要。为了解决动态环境中缺乏标准化评估基准的问题，本文提出了RAS-Eval，一个全面的安全基准，支持模拟和真实环境中的工具执行。RAS-Eval包含80个测试用例和3,802个攻击任务，映射到11个常见弱点枚举（CWE）类别，工具实现采用JSON、LangGraph和模型上下文协议（MCP）格式。对6种最先进的LLM进行评估，结果显示攻击平均降低了代理任务完成率（TCR）36.78%，在学术环境中成功率达到85.65%。研究揭示了现实世界代理部署中的关键风险，并为未来的安全研究提供了基础框架。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLM）代理在动态环境中的安全评估缺乏标准化基准的问题。现有方法未能有效识别和评估这些代理的安全漏洞，导致在实际应用中存在较大风险。

**核心思路**：论文提出RAS-Eval，构建了一个全面的安全评估基准，包含多种测试用例和攻击任务，旨在为LLM代理的安全性提供系统化的评估框架。通过支持模拟和真实环境的工具执行，增强了评估的实用性和有效性。

**技术框架**：RAS-Eval的整体架构包括80个测试用例和3,802个攻击任务，覆盖11个CWE类别。工具实现采用JSON、LangGraph和MCP格式，评估过程分为测试用例设计、攻击任务执行和结果分析三个主要阶段。

**关键创新**：最重要的技术创新在于构建了一个全面的安全基准，支持多种环境下的评估，且首次系统性地揭示了LLM代理在实际应用中的安全漏洞及其影响。与现有方法相比，RAS-Eval提供了更为细致和全面的评估框架。

**关键设计**：在设计中，关键参数包括攻击任务的多样性和复杂性，损失函数用于评估代理的任务完成率（TCR），并通过对比不同规模模型的表现，揭示安全能力的规模效应。

## 📊 实验亮点

实验结果显示，攻击平均降低了代理任务完成率（TCR）36.78%，在学术环境中攻击成功率达到85.65%。此外，研究发现较大模型在安全能力上显著优于小模型，验证了规模效应的存在。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融等关键行业，能够为LLM代理的安全性提供系统化的评估和改进方案。通过识别和修复安全漏洞，提升代理在实际应用中的可靠性和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The rapid deployment of Large language model (LLM) agents in critical domains like healthcare and finance necessitates robust security frameworks. To address the absence of standardized evaluation benchmarks for these agents in dynamic environments, we introduce RAS-Eval, a comprehensive security benchmark supporting both simulated and real-world tool execution. RAS-Eval comprises 80 test cases and 3,802 attack tasks mapped to 11 Common Weakness Enumeration (CWE) categories, with tools implemented in JSON, LangGraph, and Model Context Protocol (MCP) formats. We evaluate 6 state-of-the-art LLMs across diverse scenarios, revealing significant vulnerabilities: attacks reduced agent task completion rates (TCR) by 36.78% on average and achieved an 85.65% success rate in academic settings. Notably, scaling laws held for security capabilities, with larger models outperforming smaller counterparts. Our findings expose critical risks in real-world agent deployments and provide a foundational framework for future security research. Code and data are available at https://github.com/lanzer-tree/RAS-Eval.

