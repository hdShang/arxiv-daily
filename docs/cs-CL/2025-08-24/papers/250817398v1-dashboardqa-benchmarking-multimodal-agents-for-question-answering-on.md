---
layout: default
title: "DashboardQA: Benchmarking Multimodal Agents for Question Answering on Interactive Dashboards"
---

# DashboardQA: Benchmarking Multimodal Agents for Question Answering on Interactive Dashboards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17398" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17398v1</a>
  <a href="https://arxiv.org/pdf/2508.17398.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17398v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17398v1', 'DashboardQA: Benchmarking Multimodal Agents for Question Answering on Interactive Dashboards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aaryaman Kartha, Ahmed Masry, Mohammed Saidul Islam, Thinh Lang, Shadikur Rahman, Ridwan Mahbub, Mizanur Rahman, Mahir Ahmed, Md Rizwan Parvez, Enamul Hoque, Shafiq Joty

**分类**: cs.CL

**发布日期**: 2025-08-24

**🔗 代码/项目**: [GITHUB](https://github.com/vis-nlp/DashboardQA)

---

## 💡 一句话要点

**提出DashboardQA以解决交互式仪表板问答评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `交互式仪表板` `问答系统` `多模态代理` `数据可视化` `视觉-语言模型`

## 📋 核心要点

1. 现有的数据可视化问答基准主要集中于静态图表，忽视了仪表板的交互性，限制了对多模态代理的评估。
2. 本文提出DashboardQA基准，专门用于评估视觉-语言GUI代理在真实仪表板上的理解和交互能力。
3. 实验结果显示，即使是表现最好的代理在交互式仪表板推理任务上也面临重大挑战，准确率仅为38.69%。

## 📝 摘要（中文）

仪表板是强大的数据可视化工具，支持用户探索和分析数据。然而，现有的数据可视化问答基准大多忽视了仪表板的交互性，限制了对现代多模态代理的评估能力。为此，本文提出了DashboardQA，这是第一个专门设计用于评估视觉-语言GUI代理如何理解和与真实仪表板交互的基准。该基准包含112个来自Tableau Public的交互式仪表板和405个问题-答案对，涵盖多种类型。通过评估多种领先的GUI代理，研究揭示了它们在理解仪表板元素、规划交互轨迹和推理方面的关键局限性，表明交互式仪表板推理是一项具有挑战性的任务。

## 🔬 方法详解

**问题定义**：本文旨在解决现有问答基准对交互式仪表板的评估不足的问题。现有方法主要关注静态图表，无法有效评估多模态代理在真实场景中的表现。

**核心思路**：提出DashboardQA基准，通过引入真实的交互式仪表板和多种类型的问题，评估视觉-语言代理的理解和交互能力。这样的设计能够更好地反映实际应用中的挑战。

**技术框架**：DashboardQA基准包括112个交互式仪表板和405个问题-答案对，涵盖多种问题类型，如多选、事实、假设等。评估过程中，使用多种闭源和开源的GUI代理进行对比分析。

**关键创新**：DashboardQA是首个专门针对交互式仪表板的问答基准，填补了现有研究的空白，推动了多模态代理在复杂场景下的评估。

**关键设计**：在实验中，采用了多种评估指标，重点关注代理在理解仪表板元素、规划交互路径和推理能力上的表现。

## 📊 实验亮点

实验结果显示，表现最好的代理在DashboardQA基准上的准确率仅为38.69%，而OpenAI CUA代理的准确率为22.69%。这些结果表明，交互式仪表板推理任务的难度极高，现有代理在该领域仍有很大的提升空间。

## 🎯 应用场景

该研究的潜在应用领域包括商业智能、数据分析和决策支持系统。通过提升多模态代理在交互式仪表板上的问答能力，能够更好地辅助用户进行数据驱动的决策，提升工作效率。未来，该基准可能推动更多针对交互式数据可视化的研究与应用。

## 📄 摘要（原文）

> Dashboards are powerful visualization tools for data-driven decision-making, integrating multiple interactive views that allow users to explore, filter, and navigate data. Unlike static charts, dashboards support rich interactivity, which is essential for uncovering insights in real-world analytical workflows. However, existing question-answering benchmarks for data visualizations largely overlook this interactivity, focusing instead on static charts. This limitation severely constrains their ability to evaluate the capabilities of modern multimodal agents designed for GUI-based reasoning. To address this gap, we introduce DashboardQA, the first benchmark explicitly designed to assess how vision-language GUI agents comprehend and interact with real-world dashboards. The benchmark includes 112 interactive dashboards from Tableau Public and 405 question-answer pairs with interactive dashboards spanning five categories: multiple-choice, factoid, hypothetical, multi-dashboard, and conversational. By assessing a variety of leading closed- and open-source GUI agents, our analysis reveals their key limitations, particularly in grounding dashboard elements, planning interaction trajectories, and performing reasoning. Our findings indicate that interactive dashboard reasoning is a challenging task overall for all the VLMs evaluated. Even the top-performing agents struggle; for instance, the best agent based on Gemini-Pro-2.5 achieves only 38.69% accuracy, while the OpenAI CUA agent reaches just 22.69%, demonstrating the benchmark's significant difficulty. We release DashboardQA at https://github.com/vis-nlp/DashboardQA

