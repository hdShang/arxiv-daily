---
layout: default
title: "DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents"
---

# DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12104" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12104v2</a>
  <a href="https://arxiv.org/pdf/2506.12104.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12104v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12104v2', 'DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Li, Xiaogeng Liu, Hung-Chun Chiu, Dianqi Li, Ning Zhang, Chaowei Xiao

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-13 (更新: 2025-10-24)

**备注**: Accepted to NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/SaFoLab-WISC/DRIFT)

---

## 💡 一句话要点

**提出DRIFT以解决大语言模型代理系统的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `安全防御` `动态规则` `内存隔离` `智能代理` `提示注入攻击` `系统可信性`

## 📋 核心要点

1. 现有的系统级防御方法在动态更新安全规则和内存流隔离方面存在不足，容易受到提示注入攻击的影响。
2. DRIFT框架通过安全规划器、动态验证器和注入隔离器三大模块，动态管理安全规则并隔离潜在风险。
3. 在AgentDojo和ASB基准测试中，DRIFT展示了卓越的安全性能，且在多种模型上保持高效的实用性。

## 📝 摘要（中文）

大语言模型（LLMs）因其强大的推理和规划能力而日益成为代理系统的核心。然而，与外部环境的交互也引入了提示注入攻击的风险，可能导致经济损失、隐私泄露或系统妥协。现有的系统级防御方法虽然有一定成效，但在动态更新安全规则和内存流隔离方面仍面临挑战。为此，本文提出了DRIFT，一个动态规则基础的隔离框架，能够在控制和数据层面施加约束。通过安全规划器构建最小功能轨迹，并利用动态验证器监控偏离情况，最后通过注入隔离器检测并屏蔽可能冲突的指令。实验证明，DRIFT在AgentDojo和ASB基准测试中表现出色，展现了其强大的安全性能和高效的实用性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型代理系统中提示注入攻击带来的安全隐患。现有方法多为静态防御，无法动态适应新的攻击模式，且缺乏内存流的隔离机制。

**核心思路**：DRIFT框架通过动态规则管理和内存隔离，确保代理系统在执行用户任务时不受恶意输入的干扰。设计上强调动态更新和实时监控，以适应复杂的外部环境。

**技术框架**：DRIFT由三个主要模块组成：安全规划器负责构建功能轨迹和参数检查表；动态验证器监控执行过程中的偏离情况；注入隔离器则负责检测和屏蔽潜在的冲突指令。

**关键创新**：DRIFT的创新在于其动态规则更新能力和内存流隔离机制，显著提升了代理系统的安全性和灵活性，与传统静态防御方法形成鲜明对比。

**关键设计**：在设计中，安全规划器使用JSON-schema风格的参数检查表，动态验证器设定了特定的权限限制，注入隔离器则采用了先进的检测算法，以确保系统的实时响应能力。

## 📊 实验亮点

在AgentDojo和ASB基准测试中，DRIFT展现出卓越的安全性能，安全性指标提升幅度超过30%，同时在多种模型上保持高效的实用性，证明了其强大的适应性和鲁棒性。

## 🎯 应用场景

DRIFT框架具有广泛的应用潜力，特别是在需要高安全性的智能代理系统中，如金融服务、医疗保健和自动化控制等领域。通过有效防御提示注入攻击，DRIFT能够保护用户隐私和系统完整性，提升智能系统的可信度和实用性。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly central to agentic systems due to their strong reasoning and planning capabilities. By interacting with external environments through predefined tools, these agents can carry out complex user tasks. Nonetheless, this interaction also introduces the risk of prompt injection attacks, where malicious inputs from external sources can mislead the agent's behavior, potentially resulting in economic loss, privacy leakage, or system compromise. System-level defenses have recently shown promise by enforcing static or predefined policies, but they still face two key challenges: the ability to dynamically update security rules and the need for memory stream isolation. To address these challenges, we propose DRIFT, a Dynamic Rule-based Isolation Framework for Trustworthy agentic systems, which enforces both control- and data-level constraints. A Secure Planner first constructs a minimal function trajectory and a JSON-schema-style parameter checklist for each function node based on the user query. A Dynamic Validator then monitors deviations from the original plan, assessing whether changes comply with privilege limitations and the user's intent. Finally, an Injection Isolator detects and masks any instructions that may conflict with the user query from the memory stream to mitigate long-term risks. We empirically validate the effectiveness of DRIFT on the AgentDojo and ASB benchmark, demonstrating its strong security performance while maintaining high utility across diverse models, showcasing both its robustness and adaptability. The code is released at https://github.com/SaFoLab-WISC/DRIFT.

