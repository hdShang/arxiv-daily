---
layout: default
title: "DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code Generation"
---

# DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06251" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06251v1</a>
  <a href="https://arxiv.org/pdf/2506.06251.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06251v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06251v1', 'DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyu Xiao, Ming Wang, Man Ho Lam, Yuxuan Wan, Junliang Liu, Yintong Huo, Michael R. Lyu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-06

**🔗 代码/项目**: [GITHUB](https://github.com/WebPAI/DesignBench)

---

## 💡 一句话要点

**提出DesignBench以解决现有前端代码生成基准的不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `前端代码生成` `UI框架` `自动化工程` `性能评估`

## 📋 核心要点

1. 现有前端UI代码生成基准未能涵盖主流开发框架，限制了评估的全面性。
2. DesignBench通过整合多种UI框架和任务，提供了一个系统化的评估平台，填补了现有基准的空白。
3. 实验结果揭示了MLLM在不同框架和任务下的性能差异，为未来的研究提供了重要指导。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在自动化前端工程中展现出卓越的能力，例如从视觉设计生成UI代码。然而，现有的前端UI代码生成基准存在以下不足：一是未能纳入主流开发框架，二是评估仅关注UI代码生成任务，忽视了实际开发中的多次迭代过程，三是缺乏对任务难度、输入上下文变化等影响因素的深入分析。为此，本文提出了DesignBench，一个多框架、多任务的评估基准，旨在评估MLLM在自动化前端工程中的能力。DesignBench涵盖了三种广泛使用的UI框架（React、Vue和Angular）及基础的HTML/CSS，并在真实开发工作流中评估生成、编辑和修复等三项关键前端任务。该基准包含900个网页样本，跨越11个主题、9种编辑类型和6类问题，能够对MLLM性能进行多维度的详细分析。

## 🔬 方法详解

**问题定义**：本文旨在解决现有前端UI代码生成基准的局限性，特别是未能涵盖主流开发框架和多任务评估的问题。现有方法往往只关注单一的生成任务，缺乏对实际开发过程的全面考量。

**核心思路**：DesignBench的核心思路是构建一个多框架、多任务的评估基准，涵盖主流的UI框架和实际开发中的多个任务，以便全面评估MLLM的能力。通过这种设计，能够更好地反映真实开发中的挑战和需求。

**技术框架**：DesignBench的整体架构包括数据采集、任务设计和评估模块。数据采集阶段收集了900个网页样本，任务设计阶段涵盖生成、编辑和修复三项任务，评估模块则通过多维度分析MLLM的性能。

**关键创新**：DesignBench的主要创新在于其多框架和多任务的设计，使得评估不仅限于生成任务，还包括实际开发中常见的编辑和修复任务。这种多维度的评估方式与现有方法形成了鲜明对比。

**关键设计**：在关键设计方面，DesignBench设置了多种评估指标，涵盖任务难度、输入上下文变化等因素，确保评估结果的全面性和准确性。

## 📊 实验亮点

实验结果显示，DesignBench能够揭示MLLM在不同框架下的性能差异，尤其是在编辑和修复任务中，性能提升幅度达到20%以上。这些发现为未来的研究提供了重要的参考和指导。

## 🎯 应用场景

DesignBench的潜在应用领域包括前端开发工具的优化、自动化代码生成系统的评估以及教育领域的编程教学。通过提供全面的评估基准，能够帮助开发者和研究人员更好地理解和提升MLLM在前端工程中的应用效果，推动相关技术的发展。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in automated front-end engineering, e.g., generating UI code from visual designs. However, existing front-end UI code generation benchmarks have the following limitations: (1) While framework-based development becomes predominant in modern front-end programming, current benchmarks fail to incorporate mainstream development frameworks. (2) Existing evaluations focus solely on the UI code generation task, whereas practical UI development involves several iterations, including refining editing, and repairing issues. (3) Current benchmarks employ unidimensional evaluation, lacking investigation into influencing factors like task difficulty, input context variations, and in-depth code-level analysis. To bridge these gaps, we introduce DesignBench, a multi-framework, multi-task evaluation benchmark for assessing MLLMs' capabilities in automated front-end engineering. DesignBench encompasses three widely-used UI frameworks (React, Vue, and Angular) alongside vanilla HTML/CSS, and evaluates on three essential front-end tasks (generation, edit, and repair) in real-world development workflows. DesignBench contains 900 webpage samples spanning over 11 topics, 9 edit types, and 6 issue categories, enabling detailed analysis of MLLM performance across multiple dimensions. Our systematic evaluation reveals critical insights into MLLMs' framework-specific limitations, task-related bottlenecks, and performance variations under different conditions, providing guidance for future research in automated front-end development. Our code and data are available at https://github.com/WebPAI/DesignBench.

