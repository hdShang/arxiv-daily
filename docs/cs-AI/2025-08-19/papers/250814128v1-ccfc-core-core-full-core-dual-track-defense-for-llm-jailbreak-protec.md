---
layout: default
title: "CCFC: Core & Core-Full-Core Dual-Track Defense for LLM Jailbreak Protection"
---

# CCFC: Core & Core-Full-Core Dual-Track Defense for LLM Jailbreak Protection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14128" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14128v1</a>
  <a href="https://arxiv.org/pdf/2508.14128.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14128v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14128v1', 'CCFC: Core & Core-Full-Core Dual-Track Defense for LLM Jailbreak Protection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaming Hu, Haoyu Wang, Debarghya Mukherjee, Ioannis Ch. Paschalidis

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-19

**备注**: 11 pages, 1 figure

---

## 💡 一句话要点

**提出CCFC框架以解决大型语言模型的越狱攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `越狱攻击` `大型语言模型` `双轨防御` `安全性` `对抗性干扰`

## 📋 核心要点

1. 越狱攻击对大型语言模型的安全性构成了严重威胁，现有防御方法在应对这些攻击时效果有限。
2. CCFC框架通过核心与全核心双轨的设计，分别处理对抗性干扰和结构模式，增强了模型的安全性。
3. 实验结果显示，CCFC在对抗性攻击下成功率降低50-75%，同时保持了良性查询的响应质量。

## 📝 摘要（中文）

越狱攻击对大型语言模型（LLMs）的安全部署构成了严重挑战。本文提出了CCFC（核心与全核心双轨）防御框架，旨在缓解LLMs在提示注入和结构感知越狱攻击中的脆弱性。CCFC首先通过少量示例提示隔离用户查询的语义核心，然后利用两个互补的轨道进行评估：核心轨道忽略对抗性干扰（如有毒后缀或前缀注入），而核心全核心轨道则破坏梯度或编辑攻击利用的结构模式。最终响应基于两个轨道的安全一致性检查进行选择，确保在不妥协响应质量的情况下实现鲁棒性。实验表明，CCFC在对抗强敌（如DeepInception、GCG）时，攻击成功率降低了50-75%，且对良性查询的保真度没有牺牲。该方法在提示级防御中始终优于现有最先进的技术，为更安全的LLM部署提供了切实有效的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在面对越狱攻击时的脆弱性，现有方法在处理提示注入和结构感知攻击时效果不佳，容易受到对抗性干扰的影响。

**核心思路**：CCFC框架的核心思想是通过双轨防御机制，首先提取用户查询的语义核心，然后分别通过核心轨道和核心全核心轨道进行评估，以增强模型的鲁棒性。

**技术框架**：CCFC的整体架构包括两个主要模块：核心轨道负责过滤对抗性干扰，核心全核心轨道则针对结构模式进行干扰。最终响应通过安全一致性检查进行选择，确保高质量输出。

**关键创新**：CCFC的主要创新在于其双轨防御机制，能够有效分离和处理不同类型的攻击，与现有单一防御方法相比，提供了更全面的保护。

**关键设计**：在设计中，CCFC采用了少量示例提示来提取语义核心，并通过特定的损失函数来优化两个轨道的输出，确保在对抗性环境下的稳定性和响应质量。

## 📊 实验亮点

CCFC框架在实验中表现出色，相较于最先进的防御技术（如DeepInception和GCG），攻击成功率降低了50-75%。这一显著提升表明CCFC在面对强敌时的有效性，同时保持了良性查询的响应质量。

## 🎯 应用场景

该研究的潜在应用领域包括安全聊天机器人、智能助手和其他依赖大型语言模型的系统。通过增强模型的安全性，CCFC框架能够有效防止恶意攻击，提升用户信任度，并为未来的AI应用提供更安全的基础。

## 📄 摘要（原文）

> Jailbreak attacks pose a serious challenge to the safe deployment of large language models (LLMs). We introduce CCFC (Core & Core-Full-Core), a dual-track, prompt-level defense framework designed to mitigate LLMs' vulnerabilities from prompt injection and structure-aware jailbreak attacks. CCFC operates by first isolating the semantic core of a user query via few-shot prompting, and then evaluating the query using two complementary tracks: a core-only track to ignore adversarial distractions (e.g., toxic suffixes or prefix injections), and a core-full-core (CFC) track to disrupt the structural patterns exploited by gradient-based or edit-based attacks. The final response is selected based on a safety consistency check across both tracks, ensuring robustness without compromising on response quality. We demonstrate that CCFC cuts attack success rates by 50-75% versus state-of-the-art defenses against strong adversaries (e.g., DeepInception, GCG), without sacrificing fidelity on benign queries. Our method consistently outperforms state-of-the-art prompt-level defenses, offering a practical and effective solution for safer LLM deployment.

