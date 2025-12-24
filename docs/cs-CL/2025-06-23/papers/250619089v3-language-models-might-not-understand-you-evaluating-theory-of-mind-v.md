---
layout: default
title: "Language Models Might Not Understand You: Evaluating Theory of Mind via Story Prompting"
---

# Language Models Might Not Understand You: Evaluating Theory of Mind via Story Prompting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19089" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19089v3</a>
  <a href="https://arxiv.org/pdf/2506.19089.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19089v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19089v3', 'Language Models Might Not Understand You: Evaluating Theory of Mind via Story Prompting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nathaniel Getachew, Abulhair Saparov

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-23 (更新: 2025-09-09)

**备注**: 12 pages, 11 figures

---

## 💡 一句话要点

**提出StorySim框架以评估语言模型的心智理论能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心智理论` `语言模型` `世界建模` `故事生成` `可编程框架` `启发式行为` `人机交互`

## 📋 核心要点

1. 现有方法在评估语言模型的心智理论能力时，可能受到预训练数据污染的影响，缺乏有效的控制和创新性。
2. 本文提出的StorySim框架通过可编程的Storyboard生成新颖的故事提示，能够精确操控角色视角和事件，从而设计ToM和WM任务。
3. 实验结果表明，大多数语言模型在WM任务上的表现优于ToM任务，且在与人类推理时表现更佳，揭示了模型的启发式行为特征。

## 📝 摘要（中文）

本文介绍了可编程框架StorySim，用于合成生成故事，以评估大型语言模型（LLMs）的心智理论（ToM）和世界建模（WM）能力。与以往基准测试不同，StorySim通过高度可控的Storyboard生成新颖的、组合的故事提示，从而实现对角色视角和事件的精确操控。我们设计了一系列一阶和二阶ToM任务，以及控制心理状态跟踪和建模能力的WM任务。实验结果显示，大多数模型在WM任务上的表现优于ToM任务，并且模型在与人类进行推理时表现更佳。此外，我们的框架还揭示了启发式行为的证据，如近期偏见和对故事早期事件的过度依赖。所有生成数据和评估的代码均可免费获取。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在评估语言模型心智理论能力时的不足，尤其是预训练数据的污染和缺乏创新的故事提示生成。

**核心思路**：通过引入可编程的StorySim框架，利用Storyboard生成新颖的故事提示，从而实现对角色视角和事件的精确控制，设计出有效的ToM和WM任务。

**技术框架**：StorySim框架包括多个模块，首先通过Storyboard生成基础故事结构，然后根据控制参数生成具体的故事提示，最后设计ToM和WM任务进行评估。

**关键创新**：最重要的创新在于StorySim框架的可编程性和高度控制性，使得生成的故事提示具有新颖性和组合性，避免了传统方法的局限性。

**关键设计**：在设计过程中，关键参数包括角色视角的选择、事件的组合方式，以及损失函数的设置，以确保生成故事的多样性和有效性。

## 📊 实验亮点

实验结果显示，大多数大型语言模型在WM任务上的表现优于ToM任务，且在与人类进行推理时表现更佳。此外，发现模型存在近期偏见和对早期事件的过度依赖，揭示了其推理过程中的启发式行为特征。

## 🎯 应用场景

该研究的潜在应用领域包括教育、心理学和人机交互等。通过评估语言模型的心智理论能力，可以帮助开发更智能的对话系统和教育工具，提升人机交互的自然性和有效性。未来，该框架还可能推动对语言模型理解能力的深入研究。

## 📄 摘要（原文）

> We introduce $\texttt{StorySim}$, a programmable framework for synthetically generating stories to evaluate the theory of mind (ToM) and world modeling (WM) capabilities of large language models (LLMs). Unlike prior benchmarks that may suffer from contamination in pretraining data, $\texttt{StorySim}$ produces novel, compositional story prompts anchored by a highly controllable $\texttt{Storyboard}$, enabling precise manipulation of character perspectives and events. We use this framework to design first- and second-order ToM tasks alongside WM tasks that control for the ability to track and model mental states. Our experiments across a suite of state-of-the-art LLMs reveal that most models perform better on WM tasks than ToM tasks, and that models tend to perform better reasoning with humans compared to inanimate objects. Additionally, our framework enabled us to find evidence of heuristic behavior such as recency bias and an over-reliance on earlier events in the story. All code for generating data and evaluations is freely available.

