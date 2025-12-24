---
layout: default
title: "CoP: Agentic Red-teaming for Large Language Models using Composition of Principles"
---

# CoP: Agentic Red-teaming for Large Language Models using Composition of Principles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00781" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00781v3</a>
  <a href="https://arxiv.org/pdf/2506.00781.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00781v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00781v3', 'CoP: Agentic Red-teaming for Large Language Models using Composition of Principles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Xiong, Pin-Yu Chen, Tsung-Yi Ho

**分类**: cs.AI

**发布日期**: 2025-06-01 (更新: 2025-12-06)

---

## 💡 一句话要点

**提出CoP框架以自动化大语言模型的红队测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `红队测试` `安全性评估` `自动化测试` `越狱攻击` `AI代理` `原则组合`

## 📋 核心要点

1. 现有的红队测试方法难以系统化和自动化，导致潜在风险难以被及时发现。
2. 本文提出的CoP框架通过人类提供的红队原则，自动生成有效的红队策略，提升测试效率。
3. 实验结果表明，CoP框架在对抗领先LLMs时，成功率提升显著，最高可达19.0倍。

## 📝 摘要（中文）

近年来，大语言模型（LLMs）的快速发展推动了多个领域的变革应用。然而，针对这些模型的越狱攻击日益成为一个紧迫的问题，旨在通过欺骗目标LLMs来获取有害和风险的响应。本文提出了一种代理工作流程，通过原则组合（CoP）框架来自动化和扩展LLMs的红队测试过程。人类用户提供一组红队原则作为指令，AI代理则自动协调有效的红队策略并生成越狱提示。与现有红队方法不同，CoP框架提供了一个统一且可扩展的框架，以涵盖和协调人类提供的红队原则，从而实现新红队策略的自动发现。在对领先的LLMs进行测试时，CoP揭示了前所未有的安全风险，发现了新颖的越狱提示，并将已知的单轮攻击成功率提高了多达19.0倍。

## 🔬 方法详解

**问题定义**：本文旨在解决当前红队测试方法在系统化和自动化方面的不足，特别是在发现潜在安全风险和生成有效攻击提示方面的挑战。现有方法往往依赖于人工操作，效率低下且难以扩展。

**核心思路**：论文提出的CoP框架通过组合人类提供的红队原则，利用AI代理自动化生成红队策略。这种设计旨在提高红队测试的效率和有效性，使其能够更好地应对复杂的安全挑战。

**技术框架**：CoP框架的整体架构包括三个主要模块：人类输入模块、AI代理模块和红队策略生成模块。人类用户提供红队原则，AI代理根据这些原则自动生成攻击提示，并进行测试和评估。

**关键创新**：CoP框架的核心创新在于其统一且可扩展的设计，能够有效整合多种红队原则，并自动发现新的红队策略。这与传统方法的人工依赖形成鲜明对比，显著提升了测试的全面性和深度。

**关键设计**：在技术细节上，CoP框架的参数设置和策略生成算法经过优化，以确保生成的攻击提示具有高效性和针对性。此外，框架还采用了特定的损失函数来评估生成策略的有效性。

## 📊 实验亮点

实验结果显示，CoP框架在对抗领先的大语言模型时，成功发现了多种新颖的越狱提示，并将已知的单轮攻击成功率提高了多达19.0倍。这一显著提升表明了CoP框架在红队测试中的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括安全审计、AI模型的安全性评估以及自动化测试工具的开发。通过自动化红队测试，能够更有效地识别和修复大语言模型中的安全漏洞，从而提高其在实际应用中的安全性和可靠性。未来，CoP框架可能会在更广泛的AI安全领域产生深远影响。

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) have spurred transformative applications in various domains, ranging from open-source to proprietary LLMs. However, jailbreak attacks, which aim to break safety alignment and user compliance by tricking the target LLMs into answering harmful and risky responses, are becoming an urgent concern. The practice of red-teaming for LLMs is to proactively explore potential risks and error-prone instances before the release of frontier AI technology. This paper proposes an agentic workflow to automate and scale the red-teaming process of LLMs through the Composition-of-Principles (CoP) framework, where human users provide a set of red-teaming principles as instructions to an AI agent to automatically orchestrate effective red-teaming strategies and generate jailbreak prompts. Distinct from existing red-teaming methods, our CoP framework provides a unified and extensible framework to encompass and orchestrate human-provided red-teaming principles to enable the automated discovery of new red-teaming strategies. When tested against leading LLMs, CoP reveals unprecedented safety risks by finding novel jailbreak prompts and improving the best-known single-turn attack success rate by up to 19.0 times.

