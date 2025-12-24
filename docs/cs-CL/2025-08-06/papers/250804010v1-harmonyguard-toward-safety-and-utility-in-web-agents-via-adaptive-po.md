---
layout: default
title: "HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization"
---

# HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04010" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04010v1</a>
  <a href="https://arxiv.org/pdf/2508.04010.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04010v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04010v1', 'HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yurun Chen, Xavier Hu, Yuhan Liu, Keting Yin, Juncheng Li, Zhuosheng Zhang, Shengyu Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-06

**🔗 代码/项目**: [GITHUB](https://github.com/YurunChen/HarmonyGuard)

---

## 💡 一句话要点

**提出HarmonyGuard以解决网络代理的安全与效用平衡问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络代理` `安全性` `效用优化` `多代理协作` `策略增强` `双目标优化` `动态更新` `元认知能力`

## 📋 核心要点

1. 现有方法主要集中于单一目标优化，无法有效应对网络环境中的安全与效用平衡问题。
2. HarmonyGuard通过引入自适应策略增强和双目标优化，实现了安全性与效用的协同提升。
3. 实验结果显示，HarmonyGuard在政策合规性上提高了38%，任务完成率提升了20%，并在所有任务中实现了90%以上的政策合规性。

## 📝 摘要（中文）

大型语言模型使得代理能够在开放的网络环境中自主执行任务。然而，随着网络中隐藏威胁的演变，网络代理在长序列操作中面临着在任务性能与新兴风险之间平衡的挑战。现有研究主要集中于单一目标优化或单轮场景，缺乏在网络环境中对安全性和效用的协同优化能力。为此，我们提出了HarmonyGuard，一个多代理协作框架，通过策略增强和目标优化共同提升效用和安全性。HarmonyGuard的多代理架构具有两个基本能力：自适应策略增强和双目标优化。广泛的评估表明，HarmonyGuard在政策合规性和任务完成率上均显著优于现有基线。

## 🔬 方法详解

**问题定义**：本论文旨在解决网络代理在长序列操作中面临的安全性与效用之间的平衡问题。现有方法多为单一目标优化，无法适应不断变化的网络威胁。

**核心思路**：HarmonyGuard的核心思路是通过多代理协作框架，结合自适应策略增强和双目标优化，来同时提升代理的安全性和效用。这种设计能够应对复杂的网络环境和动态威胁。

**技术框架**：HarmonyGuard的整体架构包括两个主要模块：策略代理（Policy Agent）和效用代理（Utility Agent）。策略代理负责从非结构化文档中提取和维护安全策略，并根据新威胁进行更新；效用代理则基于安全性和效用的双重目标进行实时推理和优化。

**关键创新**：本研究的关键创新在于引入了多代理协作机制，使得安全性和效用的优化可以同时进行。这与现有方法的单一目标优化形成了本质区别。

**关键设计**：在设计上，策略代理采用了动态更新机制，以适应不断变化的网络威胁；效用代理则利用元认知能力进行目标评估和优化，确保在复杂环境中实现最佳性能。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，HarmonyGuard在政策合规性上提高了38%，任务完成率提升了20%。在所有任务中，HarmonyGuard实现了超过90%的政策合规性，显著优于现有基线，展示了其在安全性与效用优化方面的有效性。

## 🎯 应用场景

HarmonyGuard的研究成果具有广泛的应用潜力，尤其是在需要高安全性和高效能的网络代理系统中，如在线客服、自动化信息检索和智能决策支持等领域。未来，该框架可为更复杂的多代理系统提供安全保障和效用优化的解决方案，推动智能代理技术的发展。

## 📄 摘要（原文）

> Large language models enable agents to autonomously perform tasks in open web environments. However, as hidden threats within the web evolve, web agents face the challenge of balancing task performance with emerging risks during long-sequence operations. Although this challenge is critical, current research remains limited to single-objective optimization or single-turn scenarios, lacking the capability for collaborative optimization of both safety and utility in web environments. To address this gap, we propose HarmonyGuard, a multi-agent collaborative framework that leverages policy enhancement and objective optimization to jointly improve both utility and safety. HarmonyGuard features a multi-agent architecture characterized by two fundamental capabilities: (1) Adaptive Policy Enhancement: We introduce the Policy Agent within HarmonyGuard, which automatically extracts and maintains structured security policies from unstructured external documents, while continuously updating policies in response to evolving threats. (2) Dual-Objective Optimization: Based on the dual objectives of safety and utility, the Utility Agent integrated within HarmonyGuard performs the Markovian real-time reasoning to evaluate the objectives and utilizes metacognitive capabilities for their optimization. Extensive evaluations on multiple benchmarks show that HarmonyGuard improves policy compliance by up to 38% and task completion by up to 20% over existing baselines, while achieving over 90% policy compliance across all tasks. Our project is available here: https://github.com/YurunChen/HarmonyGuard.

