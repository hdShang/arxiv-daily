---
layout: default
title: "FALCON: Autonomous Cyber Threat Intelligence Mining with LLMs for IDS Rule Generation"
---

# FALCON: Autonomous Cyber Threat Intelligence Mining with LLMs for IDS Rule Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18684" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18684v1</a>
  <a href="https://arxiv.org/pdf/2508.18684.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18684v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18684v1', 'FALCON: Autonomous Cyber Threat Intelligence Mining with LLMs for IDS Rule Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaswata Mitra, Azim Bazarov, Martin Duclos, Sudip Mittal, Aritran Piplai, Md Rayhanur Rahman, Edward Zieglar, Shahram Rahimi

**分类**: cs.CR, cs.AI, cs.CL, cs.LG, eess.SY

**发布日期**: 2025-08-26

**备注**: 11 pages, 5 figures, 4 tables

---

## 💡 一句话要点

**提出FALCON以实现自主生成入侵检测系统规则**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `入侵检测系统` `网络安全` `网络威胁情报` `大型语言模型` `自动化规则生成` `实时评估` `多阶段验证`

## 📋 核心要点

1. 现有的入侵检测系统规则更新频繁且耗时，导致安全防护能力不足。
2. FALCON框架利用大型语言模型实现自主生成IDS规则，并进行实时评估。
3. 实验结果显示FALCON在规则生成的准确性上达到95%，显著提升了安全响应速度。

## 📝 摘要（中文）

基于签名的入侵检测系统（IDS）通过将网络或主机活动与预定义规则进行匹配来检测恶意活动。这些规则源自广泛的网络威胁情报（CTI），包括通过自动化工具和手动威胁分析（如沙箱）获得的攻击签名和行为模式。CTI随后被转化为可操作的规则，以便于IDS引擎实现实时检测和防御。然而，网络威胁的不断演变要求频繁更新规则，这延迟了部署时间并削弱了整体安全准备。本文提出FALCON，一个自主代理框架，能够实时生成可部署的IDS规则，并通过内置的多阶段验证器进行评估。我们的评估表明，FALCON在自动规则生成方面表现出色，平均准确率达到95%，并且在多个网络安全分析师的定性评估中，所有指标的评分一致性达到84%。这些结果强调了基于大型语言模型（LLM）进行数据挖掘在实时网络威胁缓解中的可行性和有效性。

## 🔬 方法详解

**问题定义**：当前的入侵检测系统依赖于手动更新规则，面临着网络威胁快速演变带来的挑战，导致安全防护能力不足和响应延迟。

**核心思路**：FALCON框架通过利用大型语言模型（LLM）实现自主生成IDS规则，结合内置的多阶段验证器进行实时评估，以提高规则生成的效率和准确性。

**技术框架**：FALCON的整体架构包括数据采集模块、规则生成模块和验证模块。数据采集模块负责从CTI中提取信息，规则生成模块利用LLM生成规则，验证模块则对生成的规则进行多阶段评估。

**关键创新**：FALCON的核心创新在于将LLM应用于IDS规则生成，突破了传统手动更新的局限，实现了实时、自动化的规则生成与评估。

**关键设计**：在设计中，FALCON采用了多阶段验证机制，确保生成规则的准确性和有效性，并通过构建综合数据集来支持规则生成的多样性和适用性。

## 📊 实验亮点

FALCON在自动规则生成方面表现优异，平均准确率达到95%。通过与多个网络安全分析师的定性评估，所有指标的评分一致性达到84%，显示出其在实时网络威胁缓解中的有效性。

## 🎯 应用场景

FALCON框架具有广泛的应用潜力，适用于各种网络安全环境，特别是在需要快速响应和动态更新的场景中。其自动化特性能够显著提升入侵检测系统的效率和准确性，未来可扩展至更复杂的安全防护体系中。

## 📄 摘要（原文）

> Signature-based Intrusion Detection Systems (IDS) detect malicious activities by matching network or host activity against predefined rules. These rules are derived from extensive Cyber Threat Intelligence (CTI), which includes attack signatures and behavioral patterns obtained through automated tools and manual threat analysis, such as sandboxing. The CTI is then transformed into actionable rules for the IDS engine, enabling real-time detection and prevention. However, the constant evolution of cyber threats necessitates frequent rule updates, which delay deployment time and weaken overall security readiness. Recent advancements in agentic systems powered by Large Language Models (LLMs) offer the potential for autonomous IDS rule generation with internal evaluation. We introduce FALCON, an autonomous agentic framework that generates deployable IDS rules from CTI data in real-time and evaluates them using built-in multi-phased validators. To demonstrate versatility, we target both network (Snort) and host-based (YARA) mediums and construct a comprehensive dataset of IDS rules with their corresponding CTIs. Our evaluations indicate FALCON excels in automatic rule generation, with an average of 95% accuracy validated by qualitative evaluation with 84% inter-rater agreement among multiple cybersecurity analysts across all metrics. These results underscore the feasibility and effectiveness of LLM-driven data mining for real-time cyber threat mitigation.

