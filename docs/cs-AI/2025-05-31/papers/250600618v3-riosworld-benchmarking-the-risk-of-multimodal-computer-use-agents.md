---
layout: default
title: "RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents"
---

# RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00618" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00618v3</a>
  <a href="https://arxiv.org/pdf/2506.00618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00618v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00618v3', 'RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao

**分类**: cs.AI

**发布日期**: 2025-05-31 (更新: 2025-06-20)

**备注**: 40 pages, 6 figures, Project Page: https://yjyddq.github.io/RiOSWorld.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://yjyddq.github.io/RiOSWorld.github.io/)

---

## 💡 一句话要点

**提出RiOSWorld基准以评估多模态计算机使用代理的风险**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `安全风险评估` `计算机使用代理` `风险任务` `真实环境评估`

## 📋 核心要点

1. 现有方法在评估多模态计算机使用代理的安全风险时缺乏真实的交互环境，且通常只关注特定风险类型，限制了全面评估的可能性。
2. 论文提出RiOSWorld基准，通过492个多样化的风险任务，全面评估MLLM代理在真实计算机操作中的潜在风险。
3. 实验结果显示，当前的计算机使用代理在真实场景中面临显著的安全风险，强调了安全对齐的重要性和紧迫性。

## 📝 摘要（中文）

随着多模态大型语言模型（MLLMs）的快速发展，它们被越来越多地部署为能够完成复杂计算任务的自主计算机使用代理。然而，现有针对MLLM的安全风险原则能否有效转移到真实计算机使用场景中仍然是一个亟待解决的问题。现有研究在评估MLLM计算机使用代理的安全风险时存在多项局限性，缺乏现实的交互环境，或仅关注一类或几类特定风险，忽视了真实环境的复杂性和多样性。为此，我们提出了RiOSWorld基准，旨在评估MLLM代理在真实计算机操作中的潜在风险。该基准包含492个涉及网页、社交媒体、多媒体、操作系统、电子邮件和办公软件的风险任务，并将风险分为用户来源风险和环境风险两大类。实验结果表明，当前计算机使用代理在真实场景中面临显著的安全风险，强调了对计算机使用代理进行安全对齐的必要性和紧迫性。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何有效评估多模态计算机使用代理在真实环境中的安全风险。现有方法的痛点在于缺乏真实的交互环境和对风险类型的狭隘关注，导致无法全面评估代理的安全性。

**核心思路**：论文的核心解决思路是构建RiOSWorld基准，通过包含多种计算机应用的风险任务，全面评估代理在真实操作中的风险。这种设计旨在反映真实世界的复杂性和多样性。

**技术框架**：RiOSWorld基准的整体架构包括492个任务，涵盖网页、社交媒体等多个领域。风险被分为用户来源风险和环境风险两类，评估从风险目标意图和风险目标完成两个角度进行。

**关键创新**：最重要的技术创新点在于RiOSWorld基准的构建，提供了一个全面的评估框架，能够反映多模态代理在真实环境中的复杂风险。这与现有方法的单一风险关注形成鲜明对比。

**关键设计**：在设计中，任务的多样性和风险分类是关键，确保了评估的全面性。此外，评估过程中的风险目标意图和完成度的双重视角也为分析提供了更深入的洞察。

## 📊 实验亮点

实验结果表明，当前的多模态计算机使用代理在RiOSWorld基准下面临显著的安全风险，尤其是在用户来源风险和环境风险方面。这一发现强调了对计算机使用代理进行安全对齐的必要性，提供了重要的实证数据支持。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化办公软件和社交媒体管理等。通过评估和降低多模态计算机使用代理的安全风险，能够提升用户信任度和系统可靠性，推动智能代理的广泛应用与发展。

## 📄 摘要（原文）

> With the rapid development of multimodal large language models (MLLMs), they are increasingly deployed as autonomous computer-use agents capable of accomplishing complex computer tasks. However, a pressing issue arises: Can the safety risk principles designed and aligned for general MLLMs in dialogue scenarios be effectively transferred to real-world computer-use scenarios? Existing research on evaluating the safety risks of MLLM-based computer-use agents suffers from several limitations: it either lacks realistic interactive environments, or narrowly focuses on one or a few specific risk types. These limitations ignore the complexity, variability, and diversity of real-world environments, thereby restricting comprehensive risk evaluation for computer-use agents. To this end, we introduce \textbf{RiOSWorld}, a benchmark designed to evaluate the potential risks of MLLM-based agents during real-world computer manipulations. Our benchmark includes 492 risky tasks spanning various computer applications, involving web, social media, multimedia, os, email, and office software. We categorize these risks into two major classes based on their risk source: (i) User-originated risks and (ii) Environmental risks. For the evaluation, we evaluate safety risks from two perspectives: (i) Risk goal intention and (ii) Risk goal completion. Extensive experiments with multimodal agents on \textbf{RiOSWorld} demonstrate that current computer-use agents confront significant safety risks in real-world scenarios. Our findings highlight the necessity and urgency of safety alignment for computer-use agents in real-world computer manipulation, providing valuable insights for developing trustworthy computer-use agents. Our benchmark is publicly available at https://yjyddq.github.io/RiOSWorld.github.io/.

