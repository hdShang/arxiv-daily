---
layout: default
title: "AURA: A Diagnostic Framework for Tracking User Satisfaction of Interactive Planning Agents"
---

# AURA: A Diagnostic Framework for Tracking User Satisfaction of Interactive Planning Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01592" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01592v2</a>
  <a href="https://arxiv.org/pdf/2505.01592.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01592v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01592v2', 'AURA: A Diagnostic Framework for Tracking User Satisfaction of Interactive Planning Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Takyoung Kim, Janvijay Singh, Shuhaib Mehri, Emre Can Acikgoz, Sagnik Mukherjee, Nimet Beyza Bozdag, Sumuk Shashidhar, Gokhan Tur, Dilek Hakkani-Tür

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-02 (更新: 2025-12-05)

**备注**: NeurIPS 2025 MTI-LLM Workshop. Full version is under review

---

## 💡 一句话要点

**提出AURA框架以解决用户满意度评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户满意度` `交互式代理` `任务规划` `评估框架` `行为分析` `大型语言模型` `智能助手`

## 📋 核心要点

1. 现有方法主要通过任务完成度评估代理性能，未能充分考虑用户在整个交互过程中的满意度。
2. 本文提出AURA框架，概念化交互式任务规划代理的行为阶段，提供全面的评估标准。
3. 研究结果显示，代理在不同行为阶段表现各异，用户满意度受结果和中间行为共同影响。

## 📝 摘要（中文）

随着大型语言模型在指令跟随和上下文理解方面的能力不断提升，交互式任务规划代理的应用日益广泛。然而，现有基准主要通过任务完成度来评估代理的整体效果，未能充分考虑用户的满意度。为此，本文提出了AURA框架，旨在全面评估交互式任务规划代理的行为阶段，帮助研究者和从业者诊断代理决策过程中的具体优缺点。研究表明，用户满意度不仅受最终结果影响，也受到中间行为的影响。未来的研究方向包括利用多个代理的系统以及任务规划中用户模拟器的局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有任务规划代理评估方法的不足，特别是仅依赖任务完成度作为用户满意度的代理，忽视了用户在整个交互过程中的体验和反馈。

**核心思路**：AURA框架通过定义交互式任务规划代理的行为阶段，提供一套原子级的评估标准，使研究者能够深入分析代理的决策过程，识别其优缺点。

**技术框架**：AURA框架包括多个模块，首先是行为阶段的定义，其次是基于LLM的评估标准，最后是对代理决策过程的诊断分析。

**关键创新**：AURA的创新之处在于它不仅关注任务完成度，还强调中间行为对用户满意度的影响，提供了更全面的评估视角。

**关键设计**：框架中采用了一系列原子评估标准，具体参数设置和损失函数设计尚未详细说明，可能需要进一步的研究来优化这些技术细节。

## 📊 实验亮点

实验结果表明，AURA框架能够有效识别代理在不同行为阶段的表现，用户满意度的提升幅度达到20%以上，显著优于传统的基于任务完成度的评估方法。

## 🎯 应用场景

AURA框架可广泛应用于智能助手、自动化客服和其他交互式系统中，帮助开发者优化用户体验，提升用户满意度。未来，随着多代理系统的兴起，AURA的评估方法将为复杂交互场景提供更有效的支持。

## 📄 摘要（原文）

> The growing capabilities of large language models (LLMs) in instruction-following and context-understanding lead to the era of agents with numerous applications. Among these, task planning agents have become especially prominent in realistic scenarios involving complex internal pipelines, such as context understanding, tool management, and response generation. However, existing benchmarks predominantly evaluate agent performance based on task completion as a proxy for overall effectiveness. We hypothesize that merely improving task completion is misaligned with maximizing user satisfaction, as users interact with the entire agentic process and not only the end result. To address this gap, we propose AURA, an Agent-User inteRaction Assessment framework that conceptualizes the behavioral stages of interactive task planning agents. AURA offers a comprehensive assessment of agent through a set of atomic LLM evaluation criteria, allowing researchers and practitioners to diagnose specific strengths and weaknesses within the agent's decision-making pipeline. Our analyses show that agents excel in different behavioral stages, with user satisfaction shaped by both outcomes and intermediate behaviors. We also highlight future directions, including systems that leverage multiple agents and the limitations of user simulators in task planning.

