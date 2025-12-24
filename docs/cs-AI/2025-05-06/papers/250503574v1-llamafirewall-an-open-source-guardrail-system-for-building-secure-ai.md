---
layout: default
title: "LlamaFirewall: An open source guardrail system for building secure AI agents"
---

# LlamaFirewall: An open source guardrail system for building secure AI agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03574" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03574v1</a>
  <a href="https://arxiv.org/pdf/2505.03574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03574v1', 'LlamaFirewall: An open source guardrail system for building secure AI agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sahana Chennabasappa, Cyrus Nikolaidis, Daniel Song, David Molnar, Stephanie Ding, Shengye Wan, Spencer Whitman, Lauren Deason, Nicholas Doucette, Abraham Montilla, Alekhya Gampa, Beto de Paola, Dominik Gabi, James Crnkovich, Jean-Christophe Testud, Kat He, Rashnil Chaturvedi, Wu Zhou, Joshua Saxe

**分类**: cs.CR, cs.AI

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出LlamaFirewall以解决AI代理安全风险问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全防护` `大型语言模型` `实时监控` `代码安全` `AI代理` `开源框架` `提示注入` `链式思维`

## 📋 核心要点

1. 现有的安全措施无法有效应对大型语言模型带来的新型安全风险，尤其是在高风险应用场景中。
2. LlamaFirewall框架通过三种防护机制，提供实时监控和安全策略执行，旨在降低AI代理的安全风险。
3. 实验结果表明，LlamaFirewall在防止提示注入和代码生成安全性方面表现优异，超越了现有方法。

## 📝 摘要（中文）

大型语言模型（LLMs）已从简单的聊天机器人演变为能够执行复杂任务的自主代理，这些任务包括编辑生产代码、协调工作流程以及根据不可信输入（如网页和电子邮件）采取高风险行动。这些能力引入了新的安全风险，而现有的安全措施（如模型微调或专注于聊天机器人的防护措施）并未完全解决这些问题。为此，LlamaFirewall作为一个开源的安全防护框架被提出，旨在作为AI代理安全风险的最后防线。该框架通过三种强大的防护机制来减轻风险，包括PromptGuard 2、Agent Alignment Checks和CodeShield，提供了实时监控和安全策略执行的能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在执行复杂任务时所引发的安全风险，现有方法如模型微调和聊天机器人防护措施无法有效应对这些风险，尤其是在高风险应用场景中。

**核心思路**：LlamaFirewall框架的核心思想是通过实时监控和执行安全策略，提供一个多层次的防护机制，以应对AI代理的安全威胁。该框架设计了三种主要的防护机制，以确保安全性和灵活性。

**技术框架**：LlamaFirewall的整体架构包括三个主要模块：PromptGuard 2（通用的越狱检测器）、Agent Alignment Checks（链式思维审计器）和CodeShield（在线静态分析引擎）。这些模块协同工作，形成一个完整的安全防护体系。

**关键创新**：LlamaFirewall的关键创新在于其三种防护机制的设计，特别是PromptGuard 2在越狱检测中的卓越表现，以及Agent Alignment Checks在防止间接注入方面的有效性，这些都显著提升了安全防护能力。

**关键设计**：在设计中，PromptGuard 2采用了先进的检测算法，Agent Alignment Checks通过链式思维分析代理的推理过程，而CodeShield则实现了快速且可扩展的在线静态分析，确保生成代码的安全性。

## 📊 实验亮点

实验结果显示，LlamaFirewall在防止提示注入和代码生成安全性方面表现优异，PromptGuard 2的检测准确率达到了当前最先进水平，Agent Alignment Checks在防止间接注入方面的有效性明显优于现有方法，整体提升了AI代理的安全防护能力。

## 🎯 应用场景

LlamaFirewall的潜在应用场景包括金融、医疗和自动化等高风险领域，能够为AI代理提供实时的安全防护，确保其在处理敏感信息和执行关键任务时的安全性。这一框架的实施将显著提高AI系统的信任度和可靠性。

## 📄 摘要（原文）

> Large language models (LLMs) have evolved from simple chatbots into autonomous agents capable of performing complex tasks such as editing production code, orchestrating workflows, and taking higher-stakes actions based on untrusted inputs like webpages and emails. These capabilities introduce new security risks that existing security measures, such as model fine-tuning or chatbot-focused guardrails, do not fully address. Given the higher stakes and the absence of deterministic solutions to mitigate these risks, there is a critical need for a real-time guardrail monitor to serve as a final layer of defense, and support system level, use case specific safety policy definition and enforcement. We introduce LlamaFirewall, an open-source security focused guardrail framework designed to serve as a final layer of defense against security risks associated with AI Agents. Our framework mitigates risks such as prompt injection, agent misalignment, and insecure code risks through three powerful guardrails: PromptGuard 2, a universal jailbreak detector that demonstrates clear state of the art performance; Agent Alignment Checks, a chain-of-thought auditor that inspects agent reasoning for prompt injection and goal misalignment, which, while still experimental, shows stronger efficacy at preventing indirect injections in general scenarios than previously proposed approaches; and CodeShield, an online static analysis engine that is both fast and extensible, aimed at preventing the generation of insecure or dangerous code by coding agents. Additionally, we include easy-to-use customizable scanners that make it possible for any developer who can write a regular expression or an LLM prompt to quickly update an agent's security guardrails.

