---
layout: default
title: MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers
---

# MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15163" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15163v1</a>
  <a href="https://arxiv.org/pdf/2512.15163.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15163v1" onclick="toggleFavorite(this, '2512.15163v1', 'MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuanjun Zong, Zhiqi Shen, Lei Wang, Yunshi Lan, Chao Yang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-17

**备注**: Our benchmark is available at https://github.com/xjzzzzzzzz/MCPSafety

---

## 💡 一句话要点

**提出MCP-SafetyBench，用于评估大语言模型在真实MCP服务器环境下的安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `安全性评估` `模型上下文协议` `多服务器交互` `安全基准`

## 📋 核心要点

1. 现有LLM安全基准测试未能充分覆盖真实世界场景，尤其是在模型与外部工具和服务交互时，缺乏对多服务器工作流安全风险的评估。
2. MCP-SafetyBench旨在通过构建在真实MCP服务器上的综合基准，模拟真实世界的多轮交互，从而更全面地评估LLM的安全性。
3. 该基准测试揭示了现有LLM在安全性方面的差距，并强调了随着任务复杂度和服务器交互增加，LLM面临的安全漏洞会显著增加。

## 📝 摘要（中文）

大型语言模型（LLMs）正演变为具备推理、规划和操作外部工具的智能体系统。模型上下文协议（MCP）是这一转变的关键推动因素，它为LLMs与异构工具和服务连接提供了标准化接口。然而，MCP的开放性和多服务器工作流引入了新的安全风险，而现有的基准测试无法捕捉到这些风险，因为它们侧重于孤立的攻击或缺乏真实世界的覆盖。我们提出了MCP-SafetyBench，这是一个构建在真实MCP服务器上的综合基准，支持跨五个领域的真实多轮评估：浏览器自动化、金融分析、位置导航、存储库管理和Web搜索。它包含一个统一的20种MCP攻击类型分类，涵盖服务器、主机和用户端，并包括需要在不确定性下进行多步骤推理和跨服务器协调的任务。使用MCP-SafetyBench，我们系统地评估了领先的开源和闭源LLMs，揭示了安全性能方面的巨大差异，以及随着任务范围和服务器交互的增长而加剧的漏洞。我们的结果强调了对更强大防御的迫切需求，并将MCP-SafetyBench确立为诊断和减轻真实世界MCP部署中安全风险的基础。

## 🔬 方法详解

**问题定义**：论文旨在解决现有大语言模型安全评估基准在真实世界模型上下文协议（MCP）部署场景下的不足。现有基准主要关注孤立攻击，缺乏对多服务器协同和复杂任务流程中潜在安全风险的评估，无法有效反映LLM在实际应用中的安全性能。

**核心思路**：论文的核心思路是构建一个基于真实MCP服务器的综合性安全评估基准，模拟真实世界的多轮交互场景。通过设计包含多种攻击类型和复杂任务的测试用例，全面评估LLM在MCP环境下的安全性，并揭示潜在的安全漏洞。

**技术框架**：MCP-SafetyBench包含以下主要组成部分：
1. **真实MCP服务器环境**：模拟真实世界的MCP部署，提供包括浏览器自动化、金融分析、位置导航、存储库管理和Web搜索等五个领域的服务。
2. **统一的攻击类型分类**：定义了20种MCP攻击类型，涵盖服务器、主机和用户端，为安全评估提供标准化的攻击向量。
3. **多轮交互任务**：设计需要多步骤推理和跨服务器协调的任务，模拟真实世界复杂应用场景。
4. **评估指标**：用于量化LLM在不同攻击类型和任务下的安全性能。

**关键创新**：MCP-SafetyBench的关键创新在于其真实性和全面性。与现有基准相比，它构建在真实的MCP服务器上，能够更准确地反映LLM在实际部署中的安全风险。此外，它还提供了一个统一的攻击类型分类和多轮交互任务，能够更全面地评估LLM的安全性。

**关键设计**：MCP-SafetyBench的关键设计包括：
1. **任务设计**：任务设计需要考虑任务的复杂性、多样性和真实性，以确保能够全面评估LLM的安全性能。
2. **攻击设计**：攻击设计需要覆盖各种可能的攻击向量，并模拟真实世界的攻击场景。
3. **评估指标**：评估指标需要能够准确量化LLM在不同攻击类型和任务下的安全性能，例如成功率、误报率等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15163v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15163v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15163v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有LLM在MCP-SafetyBench上的安全性能存在显著差异，并且随着任务复杂度和服务器交互的增加，LLM面临的安全漏洞会显著增加。例如，某些LLM在简单任务上表现良好，但在涉及跨服务器协调的复杂任务上则容易受到攻击。这些结果强调了加强LLM安全防御的迫切需求。

## 🎯 应用场景

MCP-SafetyBench可用于评估和改进大语言模型在真实世界MCP部署中的安全性。它可以帮助开发者识别和修复LLM中的安全漏洞，提高LLM在实际应用中的可靠性和安全性。此外，该基准还可以用于比较不同LLM的安全性能，为用户选择合适的LLM提供参考。

## 📄 摘要（原文）

> Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools. The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services. Yet MCP's openness and multi-server workflows introduce new safety risks that existing benchmarks fail to capture, as they focus on isolated attacks or lack real-world coverage. We present MCP-SafetyBench, a comprehensive benchmark built on real MCP servers that supports realistic multi-turn evaluation across five domains: browser automation, financial analysis, location navigation, repository management, and web search. It incorporates a unified taxonomy of 20 MCP attack types spanning server, host, and user sides, and includes tasks requiring multi-step reasoning and cross-server coordination under uncertainty. Using MCP-SafetyBench, we systematically evaluate leading open- and closed-source LLMs, revealing large disparities in safety performance and escalating vulnerabilities as task horizons and server interactions grow. Our results highlight the urgent need for stronger defenses and establish MCP-SafetyBench as a foundation for diagnosing and mitigating safety risks in real-world MCP deployments.

