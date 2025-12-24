---
layout: default
title: "Context manipulation attacks : Web agents are susceptible to corrupted memory"
---

# Context manipulation attacks : Web agents are susceptible to corrupted memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17318" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17318v1</a>
  <a href="https://arxiv.org/pdf/2506.17318.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17318v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17318v1', 'Context manipulation attacks : Web agents are susceptible to corrupted memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Atharv Singh Patlan, Ashwin Hebbar, Pramod Viswanath, Prateek Mittal

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-18

**备注**: 10 pages, 6 figures

---

## 💡 一句话要点

**提出计划注入攻击以解决网络代理的内存安全问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文操控` `计划注入` `网络安全` `自主代理` `隐私泄露` `攻击防御` `大型语言模型`

## 📋 核心要点

1. 现有的自主网络代理在上下文管理上存在严重的安全漏洞，容易受到攻击。
2. 论文提出了一种名为“计划注入”的新型攻击方法，专注于操控代理的内部任务表示。
3. 实验结果显示，计划注入的攻击成功率比传统方法高出3倍，且隐私泄露任务成功率提升17.7%。

## 📝 摘要（中文）

自主网络导航代理将自然语言指令转换为浏览器操作序列，广泛应用于电子商务、信息检索和内容发现等复杂任务。由于大型语言模型的无状态特性，这些代理严重依赖外部内存系统来维持交互中的上下文。然而，代理内存通常由客户端或第三方应用管理，导致显著的安全漏洞。本文引入并形式化了“计划注入”这一新型上下文操控攻击，针对这些脆弱的上下文，破坏代理的内部任务表示。通过对两个流行的网络代理进行系统评估，发现计划注入能够绕过强健的提示注入防御，攻击成功率比可比的基于提示的攻击高出3倍。此外，“上下文链式注入”在合法用户目标与攻击者目标之间构建逻辑桥梁，使隐私泄露任务的成功率提高了17.7%。我们的研究强调，安全的内存处理必须成为代理系统的首要关注点。

## 🔬 方法详解

**问题定义**：本文解决的是自主网络代理在上下文管理中存在的安全问题，现有方法未能有效保护代理的内存，导致易受攻击。

**核心思路**：论文提出的“计划注入”攻击通过操控代理的上下文，破坏其内部任务表示，从而实现对代理的控制。此设计旨在利用代理内存的脆弱性，提升攻击成功率。

**技术框架**：整体架构包括攻击模型和防御模型。攻击模型通过构造特定的输入，诱导代理执行不当操作；防御模型则评估现有的提示注入防御机制的有效性。

**关键创新**：最重要的技术创新在于“计划注入”攻击的提出，它能够绕过现有的防御措施，显著提高攻击成功率，与传统方法相比具有本质区别。

**关键设计**：在实验中，设计了多种输入格式和逻辑桥接策略，以优化攻击效果。具体参数设置和损失函数的选择经过多次实验验证，以确保攻击的有效性和隐蔽性。

## 📊 实验亮点

实验结果表明，计划注入攻击的成功率比传统的提示注入攻击高出3倍，且在隐私泄露任务中，通过上下文链式注入，成功率提升了17.7%。这些结果强调了安全内存处理在代理系统中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、自动化代理系统和人机交互界面。通过提升对上下文操控攻击的理解，能够为开发更安全的自主代理提供理论基础，进而保护用户隐私和数据安全。未来，随着代理技术的广泛应用，相关的安全防护措施将变得愈发重要。

## 📄 摘要（原文）

> Autonomous web navigation agents, which translate natural language instructions into sequences of browser actions, are increasingly deployed for complex tasks across e-commerce, information retrieval, and content discovery. Due to the stateless nature of large language models (LLMs), these agents rely heavily on external memory systems to maintain context across interactions. Unlike centralized systems where context is securely stored server-side, agent memory is often managed client-side or by third-party applications, creating significant security vulnerabilities. This was recently exploited to attack production systems.
>   We introduce and formalize "plan injection," a novel context manipulation attack that corrupts these agents' internal task representations by targeting this vulnerable context. Through systematic evaluation of two popular web agents, Browser-use and Agent-E, we show that plan injections bypass robust prompt injection defenses, achieving up to 3x higher attack success rates than comparable prompt-based attacks. Furthermore, "context-chained injections," which craft logical bridges between legitimate user goals and attacker objectives, lead to a 17.7% increase in success rate for privacy exfiltration tasks. Our findings highlight that secure memory handling must be a first-class concern in agentic systems.

