---
layout: default
title: Ψ-Arena: Interactive Assessment and Optimization of LLM-based Psychological Counselors with Tripartite Feedback
---

# Ψ-Arena: Interactive Assessment and Optimization of LLM-based Psychological Counselors with Tripartite Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03293" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03293v1</a>
  <a href="https://arxiv.org/pdf/2505.03293.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03293v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03293v1', 'Ψ-Arena: Interactive Assessment and Optimization of LLM-based Psychological Counselors with Tripartite Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shijing Zhu, Zhuang Chen, Guanqun Bi, Binghang Li, Yaxi Deng, Dazhen Wan, Libiao Peng, Xiyao Xiao, Rongsheng Zhang, Tangjie Lv, Zhipeng Hu, FangFang Li, Minlie Huang

**分类**: cs.CL

**发布日期**: 2025-05-06

**备注**: in progress

---

## 💡 一句话要点

**提出Ψ-Arena以解决LLM心理咨询师评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心理健康` `大型语言模型` `咨询师评估` `互动框架` `闭环优化` `多方反馈` `真实场景模拟`

## 📋 核心要点

1. 现有的LLM心理咨询师评估方法主要集中于静态知识测试，缺乏动态和多角度的反馈，影响评估的全面性和有效性。
2. 本文提出Ψ-Arena框架，通过模拟真实咨询场景和整合多方反馈，提供了一种互动式的评估和优化方法。
3. 实验表明，Ψ-Arena在八种LLM上实现了显著的性能提升，反思优化使咨询表现提高了141%。

## 📝 摘要（中文）

大型语言模型（LLMs）在提供可扩展的心理健康支持方面展现出潜力，但评估其咨询能力至关重要，以确保有效性和安全性。现有评估方法受限于静态评估，主要关注知识测试，且缺乏多角度的反馈机制。为此，本文提出Ψ-Arena，一个互动框架，用于全面评估和优化基于LLM的咨询师，具有三大特点：1）通过与心理特征化的非玩家角色（NPC）客户进行多阶段对话，模拟真实的咨询互动；2）整合客户、咨询师和监督者的三方评估；3）通过诊断反馈进行闭环优化。实验结果显示，在不同的真实场景和评估视角下，八种最先进的LLM表现出显著的性能差异，反思基础的优化使咨询表现提升高达141%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM心理咨询师评估方法的不足，尤其是静态评估和缺乏多角度反馈的问题。现有方法主要依赖知识测试，无法全面反映咨询师的实际能力。

**核心思路**：Ψ-Arena框架通过模拟真实的咨询互动，整合客户、咨询师和监督者的反馈，实现动态评估和闭环优化，从而提高咨询效果。

**技术框架**：Ψ-Arena的整体架构包括三个主要模块：1）真实场景模拟，通过与心理特征化的NPC客户进行多阶段对话；2）三方评估机制，综合客户、咨询师和监督者的反馈；3）闭环优化，通过诊断反馈迭代改进LLM咨询师的表现。

**关键创新**：Ψ-Arena的创新在于其互动性和多维度评估机制，突破了传统静态评估的局限，能够实时反馈和优化咨询师的表现。

**关键设计**：在设计中，采用了多阶段对话流程，设置了不同的评估指标，并通过反思机制进行优化，确保了评估的全面性和有效性。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，Ψ-Arena在八种最先进的LLM上实现了显著的性能差异，反思优化使咨询表现提升高达141%。这一结果表明，Ψ-Arena能够有效提升LLM在真实场景中的咨询能力，具有重要的实用价值。

## 🎯 应用场景

Ψ-Arena框架在心理健康领域具有广泛的应用潜力，可以用于训练和评估基于LLM的心理咨询师，提升其咨询效果。未来，该框架有望推动心理健康服务的智能化和个性化，为用户提供更安全、有效的心理支持。

## 📄 摘要（原文）

> Large language models (LLMs) have shown promise in providing scalable mental health support, while evaluating their counseling capability remains crucial to ensure both efficacy and safety. Existing evaluations are limited by the static assessment that focuses on knowledge tests, the single perspective that centers on user experience, and the open-loop framework that lacks actionable feedback. To address these issues, we propose Ψ-Arena, an interactive framework for comprehensive assessment and optimization of LLM-based counselors, featuring three key characteristics: (1) Realistic arena interactions that simulate real-world counseling through multi-stage dialogues with psychologically profiled NPC clients, (2) Tripartite evaluation that integrates assessments from the client, counselor, and supervisor perspectives, and (3) Closed-loop optimization that iteratively improves LLM counselors using diagnostic feedback. Experiments across eight state-of-the-art LLMs show significant performance variations in different real-world scenarios and evaluation perspectives. Moreover, reflection-based optimization results in up to a 141% improvement in counseling performance. We hope PsychoArena provides a foundational resource for advancing reliable and human-aligned LLM applications in mental healthcare.

