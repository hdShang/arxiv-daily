---
layout: default
title: "MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers"
---

# MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14925" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14925v1</a>
  <a href="https://arxiv.org/pdf/2508.14925.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14925v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14925v1', 'MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiqiang Wang, Yichao Gao, Yanting Wang, Suyuan Liu, Haifeng Sun, Haoran Cheng, Guanquan Shi, Haohua Du, Xiangyang Li

**分类**: cs.CR, cs.LG

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出MCPTox基准以评估工具中毒攻击对MCP服务器的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工具中毒` `模型上下文协议` `安全性评估` `恶意测试案例` `大型语言模型` `自主代理` `攻击模板`

## 📋 核心要点

1. 现有研究主要集中在通过外部工具输出注入攻击，而工具中毒作为一种更根本的脆弱性尚未得到系统评估。
2. 论文提出MCPTox基准，通过构建真实MCP环境，系统性评估代理对工具中毒的鲁棒性。
3. 实验结果显示，许多能力较强的模型对工具中毒攻击更为敏感，攻击成功率高达72.8%。

## 📝 摘要（中文）

通过为大型语言模型（LLM）代理提供与外部工具交互的标准化接口，模型上下文协议（MCP）迅速成为现代自主代理生态系统的基石。然而，这也带来了新的攻击面，尤其是工具中毒攻击。本文首次提出MCPTox基准，系统评估代理在现实MCP环境下对工具中毒的鲁棒性。MCPTox基于45个真实的MCP服务器和353个真实工具构建，设计了三种攻击模板生成1312个恶意测试案例。评估结果显示，20个主流LLM代理普遍存在工具中毒的脆弱性，o1-mini模型的攻击成功率高达72.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决工具中毒攻击对MCP服务器的影响，现有方法未能系统评估这一脆弱性，导致对潜在威胁的认识不足。

**核心思路**：通过构建MCPTox基准，系统性地评估代理在真实MCP环境下的鲁棒性，设计攻击模板生成恶意测试案例，以揭示工具中毒的风险。

**技术框架**：MCPTox基于45个真实MCP服务器和353个工具，设计三种攻击模板，生成1312个恶意测试案例，涵盖10类潜在风险。评估20个主流LLM代理的表现。

**关键创新**：MCPTox是首个针对工具中毒攻击的系统性基准，填补了现有研究的空白，揭示了代理在面对恶意工具时的脆弱性。

**关键设计**：通过少量学习生成恶意测试案例，采用多种攻击模板，评估不同模型的攻击成功率，发现更强大的模型在指令执行上更易受到攻击。

## 📊 实验亮点

实验结果显示，20个主流LLM代理普遍存在工具中毒的脆弱性，其中o1-mini模型的攻击成功率高达72.8%。此外，分析表明，现有的安全对齐措施在面对利用合法工具进行未授权操作的恶意行为时效果不佳，最高拒绝率不足3%。

## 🎯 应用场景

该研究的潜在应用领域包括安全敏感的AI代理系统，如金融服务、医疗健康和自动化控制等。通过理解和减轻工具中毒攻击的影响，可以提升这些系统的安全性和可靠性，确保在使用外部工具时的安全操作。未来，该基准可为开发更安全的AI代理提供重要参考。

## 📄 摘要（原文）

> By providing a standardized interface for LLM agents to interact with external tools, the Model Context Protocol (MCP) is quickly becoming a cornerstone of the modern autonomous agent ecosystem. However, it creates novel attack surfaces due to untrusted external tools. While prior work has focused on attacks injected through external tool outputs, we investigate a more fundamental vulnerability: Tool Poisoning, where malicious instructions are embedded within a tool's metadata without execution. To date, this threat has been primarily demonstrated through isolated cases, lacking a systematic, large-scale evaluation.
>   We introduce MCPTox, the first benchmark to systematically evaluate agent robustness against Tool Poisoning in realistic MCP settings. MCPTox is constructed upon 45 live, real-world MCP servers and 353 authentic tools. To achieve this, we design three distinct attack templates to generate a comprehensive suite of 1312 malicious test cases by few-shot learning, covering 10 categories of potential risks. Our evaluation on 20 prominent LLM agents setting reveals a widespread vulnerability to Tool Poisoning, with o1-mini, achieving an attack success rate of 72.8\%. We find that more capable models are often more susceptible, as the attack exploits their superior instruction-following abilities. Finally, the failure case analysis reveals that agents rarely refuse these attacks, with the highest refused rate (Claude-3.7-Sonnet) less than 3\%, demonstrating that existing safety alignment is ineffective against malicious actions that use legitimate tools for unauthorized operation. Our findings create a crucial empirical baseline for understanding and mitigating this widespread threat, and we release MCPTox for the development of verifiably safer AI agents. Our dataset is available at an anonymized repository: \textit{https://anonymous.4open.science/r/AAAI26-7C02}.

