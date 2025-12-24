---
layout: default
title: "RExBench: Can coding agents autonomously implement AI research extensions?"
---

# RExBench: Can coding agents autonomously implement AI research extensions?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22598" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22598v2</a>
  <a href="https://arxiv.org/pdf/2506.22598.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22598v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22598v2', 'RExBench: Can coding agents autonomously implement AI research extensions?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicholas Edwards, Yukyung Lee, Yujun Audrey Mao, Yulu Qin, Sebastian Schuster, Najoung Kim

**分类**: cs.CL

**发布日期**: 2025-06-27 (更新: 2025-07-17)

---

## 💡 一句话要点

**提出RExBench以评估AI代理的研究扩展能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `研究扩展` `自动化科研` `基准评估` `智能代理`

## 📋 核心要点

1. 现有的基于LLMs的代理在自主执行研究扩展任务时表现不佳，缺乏足够的能力。
2. 论文提出RExBench基准，旨在评估代理在实现研究扩展方面的能力，包含12个具体任务。
3. 实验结果显示，所有评估的代理在自主实现扩展方面的成功率低于40%，即使在提供人类提示的情况下也未能显著提升。

## 📝 摘要（中文）

基于大型语言模型（LLMs）的代理在自主执行复杂软件工程任务方面展现出潜力。此外，针对能够执行机器学习和自然科学研究流程部分的代理也取得了进展。本文认为，研究扩展及其实现是此类系统的关键能力，并引入RExBench以支持该能力的评估。RExBench是一个基准，包含12个现实的研究实验实现任务，旨在调查以前未实现的研究假设。每个任务都是对现有研究论文和代码库的扩展，并附有领域专家撰写的说明。RExBench对数据污染具有鲁棒性，并支持自动评估基础设施，以执行代理输出并确定成功标准是否满足。我们使用该基准评估了使用三种不同框架实现的九个LLM代理，发现所有评估的代理在自主实现大多数扩展时均失败。尽管在额外的人类提示下成功率有所提高，但在这种设置下的最佳表现仍低于40%。这表明当前代理在没有大量人类指导的情况下，仍无法处理现实的研究扩展任务。

## 🔬 方法详解

**问题定义**：本文旨在解决当前基于LLMs的代理在自主实现研究扩展任务时的能力不足问题。现有方法在处理复杂的研究任务时，往往需要大量的人类干预，无法独立完成。

**核心思路**：论文的核心思路是通过引入RExBench基准，系统地评估和提升代理在研究扩展任务中的表现。通过设置现实的实验任务，探索代理的自主实现能力。

**技术框架**：RExBench基准由12个研究实验实现任务组成，每个任务都基于现有研究论文和代码库，并附有专家指导。评估过程包括自动执行代理输出，判断其是否满足成功标准。

**关键创新**：RExBench的创新之处在于其专注于研究扩展的实现能力评估，填补了现有基准在这一领域的空白。与传统的任务评估方法相比，RExBench提供了更具针对性的测试环境。

**关键设计**：在设计RExBench时，考虑了数据污染的鲁棒性，并构建了自动评估基础设施，以确保评估过程的客观性和准确性。

## 📊 实验亮点

实验结果表明，所有评估的代理在自主实现研究扩展方面的成功率均低于40%。尽管在提供额外人类提示的情况下成功率有所提升，但最佳表现仍未超过40%，显示出当前技术的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括自动化科研、智能编程助手和教育工具等。通过提升代理在研究扩展任务中的能力，未来可以实现更高效的科研流程，减少人类研究者的负担，推动科学研究的进展。

## 📄 摘要（原文）

> Agents based on Large Language Models (LLMs) have shown promise for performing sophisticated software engineering tasks autonomously. In addition, there has been progress towards developing agents that can perform parts of the research pipeline in machine learning and the natural sciences. We argue that research extension and its implementation is a critical capability for such systems, and introduce RExBench to support the evaluation of this capability. RExBench is a benchmark consisting of 12 realistic research experiment implementation tasks that aim to investigate research hypotheses that have not previously been implemented. Each task is set up as an extension to an existing research paper and codebase, accompanied by domain expert-written instructions. RExBench is robust to data contamination, and supports an automatic evaluation infrastructure that executes agent outputs to determine whether the success criteria are met. We use this benchmark to evaluate nine LLM agents implemented using three different frameworks: aider, Claude Code, and OpenHands. We find that all agents evaluated fail to autonomously implement the majority of the extensions. Although the success rate improves with additional human-written hints, the best performance under this setting remains below 40%. This indicates that current agents are still short of being able to handle realistic research extension tasks without substantial human guidance.

