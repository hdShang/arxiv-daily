---
layout: default
title: "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems"
---

# Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17208" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17208v2</a>
  <a href="https://arxiv.org/pdf/2506.17208.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17208v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17208v2', 'Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matias Martinez, Xavier Franch

**分类**: cs.SE, cs.AI, cs.CL

**发布日期**: 2025-06-20 (更新: 2025-08-18)

---

## 💡 一句话要点

**分析SWE-Bench排行榜，揭示LLM与代理修复系统的提交者与架构特征**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化程序修复` `大型语言模型` `代理系统` `SWE-Bench` `开源软件` `技术分析` `系统架构`

## 📋 核心要点

1. 现有的自动化程序修复方法缺乏对提交者和架构的详细文档，导致许多解决方案的设计和来源不明确。
2. 本文通过分析SWE-Bench排行榜的79个Lite和99个Verified提交，揭示了LLM和代理系统的使用情况及其设计特征。
3. 研究结果显示，专有LLM的使用占主导地位，且贡献者的背景多样，从个人开发者到大型科技公司均有涉及。

## 📝 摘要（中文）

随着自动化程序修复（APR）的快速发展，特别是大型语言模型（LLMs）和基于代理的系统的进步，SWE-Bench成为评估LLM修复系统的重要基准。本文首次全面研究了SWE-Bench Lite和Verified排行榜的所有提交，分析了80种独特的方法，涵盖提交者类型、产品可用性、LLM使用情况和系统架构等维度。研究发现，专有LLM（尤其是Claude 3.5）占主导地位，且存在代理和非代理设计，贡献者包括个人开发者和大型科技公司。

## 🔬 方法详解

**问题定义**：本文旨在解决SWE-Bench排行榜提交者和架构缺乏透明度的问题，现有方法未能详细记录解决方案的设计和来源。

**核心思路**：通过对SWE-Bench Lite和Verified排行榜的提交进行全面分析，揭示不同提交者的类型、使用的LLM及其系统架构的特征。

**技术框架**：研究采用定量和定性分析相结合的方法，首先收集所有提交数据，然后从多个维度进行分类和比较，最终总结出主要发现。

**关键创新**：本研究首次系统性地分析了SWE-Bench排行榜的提交，填补了现有文献中对LLM和代理修复系统架构理解的空白。

**关键设计**：在分析过程中，重点关注了提交者的背景、产品的可用性、LLM的具体使用情况以及系统的设计架构，确保了分析的全面性和准确性。

## 📊 实验亮点

研究结果表明，专有LLM（如Claude 3.5）在提交中占据主导地位，且代理和非代理设计的存在显示出多样化的解决方案。通过对79个Lite和99个Verified提交的分析，揭示了贡献者的广泛背景，促进了对当前APR技术的深入理解。

## 🎯 应用场景

该研究为自动化程序修复领域提供了重要的基准和参考，帮助研究人员和开发者理解当前技术的趋势与局限性。未来，基于此研究的发现，可以推动更高效的修复系统的设计与开发，促进开源社区的技术进步。

## 📄 摘要（原文）

> The rapid progress in Automated Program Repair (APR) has been driven by advances in AI, particularly large language models (LLMs) and agent-based systems. SWE-Bench is a recent benchmark designed to evaluate LLM-based repair systems using real issues and pull requests mined from 12 popular open-source Python repositories. Its public leaderboards -- SWE-Bench Lite and SWE-Bench Verified -- have become central platforms for tracking progress and comparing solutions. However, because the submission process does not require detailed documentation, the architectural design and origin of many solutions remain unclear. In this paper, we present the first comprehensive study of all submissions to the SWE-Bench Lite (79 entries) and Verified (99 entries) leaderboards, analyzing 80 unique approaches across dimensions such as submitter type, product availability, LLM usage, and system architecture. Our findings reveal the dominance of proprietary LLMs (especially Claude 3.5), the presence of both agentic and non-agentic designs, and a contributor base spanning from individual developers to large tech companies.

