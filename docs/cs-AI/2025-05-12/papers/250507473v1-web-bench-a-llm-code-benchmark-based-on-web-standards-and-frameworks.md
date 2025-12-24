---
layout: default
title: Web-Bench: A LLM Code Benchmark Based on Web Standards and Frameworks
---

# Web-Bench: A LLM Code Benchmark Based on Web Standards and Frameworks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07473" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07473v1</a>
  <a href="https://arxiv.org/pdf/2505.07473.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07473v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07473v1', 'Web-Bench: A LLM Code Benchmark Based on Web Standards and Frameworks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Xu, YiWei Mao, XinYi Guan, ZiLong Feng

**分类**: cs.AI

**发布日期**: 2025-05-12

**备注**: 28 pages, 15 figures

---

## 💡 一句话要点

**提出Web-Bench以解决LLM代码基准测试饱和问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码基准` `Web开发` `软件工程` `任务依赖`

## 📋 核心要点

1. 现有的LLM代码基准测试逐渐饱和，导致其对模型优化的指导作用减弱。
2. 本文提出Web-Bench基准，包含50个复杂项目，模拟真实开发流程，旨在提升LLM的编码能力。
3. 实验表明，Web-Agent在Web-Bench上的Pass@1仅为25.1%，显著低于其他基准的表现，显示出其挑战性。

## 📝 摘要（中文）

大型语言模型（LLMs）在编码领域的应用正在迅速发展，从代码助手到自主编码代理，再到通过自然语言生成完整项目。早期的LLM代码基准主要关注代码生成的准确性，但这些基准逐渐饱和，削弱了其对LLMs的指导作用。为此，本文提出了新的基准Web-Bench，包含50个项目，每个项目由20个具有顺序依赖的任务组成，模拟真实的开发工作流程。设计Web-Bench时，旨在涵盖Web开发的基础元素：Web标准和Web框架。实验结果显示，当前最先进的模型在该基准上的表现显著低于现有软件工程基准。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM代码基准测试饱和的问题，现有基准如HumanEval和MBPP的高通过率已无法有效指导模型优化。

**核心思路**：提出Web-Bench基准，通过设计包含顺序依赖的任务项目，模拟真实开发流程，覆盖Web开发的基础标准和框架，以提升LLM的编码能力。

**技术框架**：Web-Bench包含50个项目，每个项目由20个任务构成，任务之间存在顺序依赖，整体流程模拟了工程师的开发工作。

**关键创新**：Web-Bench的设计不仅关注代码生成的准确性，还强调了Web标准和框架的重要性，提供了更具挑战性的测试环境。

**关键设计**：每个项目由经验丰富的工程师设计，完成一个项目平均需要4到8小时，确保了任务的复杂性和现实性。

## 📊 实验亮点

在Web-Bench基准测试中，最先进的模型Claude 3.7 Sonnet的Pass@1仅为25.1%，显著低于SWE-Bench的Verified（65.4%）和Full（33.8%）分数，显示出Web-Bench的挑战性和有效性。

## 🎯 应用场景

Web-Bench的设计为大型语言模型在Web开发领域的应用提供了新的基准测试工具，能够更好地评估和优化LLM的编码能力。未来，该基准可能在教育、软件开发和自动化编程等多个领域发挥重要作用，推动LLM技术的进一步发展。

## 📄 摘要（原文）

> The application of large language models (LLMs) in the field of coding is evolving rapidly: from code assistants, to autonomous coding agents, and then to generating complete projects through natural language. Early LLM code benchmarks primarily focused on code generation accuracy, but these benchmarks have gradually become saturated. Benchmark saturation weakens their guiding role for LLMs. For example, HumanEval Pass@1 has reached 99.4% and MBPP 94.2%. Among various attempts to address benchmark saturation, approaches based on software engineering have stood out, but the saturation of existing software engineering benchmarks is rapidly increasing. To address this, we propose a new benchmark, Web-Bench, which contains 50 projects, each consisting of 20 tasks with sequential dependencies. The tasks implement project features in sequence, simulating real-world human development workflows. When designing Web-Bench, we aim to cover the foundational elements of Web development: Web Standards and Web Frameworks. Given the scale and complexity of these projects, which were designed by engineers with 5 to 10 years of experience, each presents a significant challenge. On average, a single project takes 4 to 8 hours for a senior engineer to complete. On our given benchmark agent (Web-Agent), SOTA (Claude 3.7 Sonnet) achieves only 25.1% Pass@1, significantly lower (better) than SWE-Bench's Verified (65.4%) and Full (33.8%) scores. Finally, we discuss that in any development field, Standards and Frameworks represent foundational knowledge and efficiency tools, respectively, and LLMs require optimization tailored to them.

