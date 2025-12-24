---
layout: default
title: "Agent RL Scaling Law: Agent RL with Spontaneous Code Execution for Mathematical Problem Solving"
---

# Agent RL Scaling Law: Agent RL with Spontaneous Code Execution for Mathematical Problem Solving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07773" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07773v4</a>
  <a href="https://arxiv.org/pdf/2505.07773.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07773v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07773v4', 'Agent RL Scaling Law: Agent RL with Spontaneous Code Execution for Mathematical Problem Solving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinji Mai, Haotian Xu, Zhong-Zhi Li, Xing W, Weinong Wang, Jian Hu, Yingying Zhang, Wenqiang Zhang

**分类**: cs.AI

**发布日期**: 2025-05-12 (更新: 2025-08-20)

**🔗 代码/项目**: [GITHUB](https://github.com/yyht/openrlhf_async_pipline) | [GITHUB](https://github.com/yyht/openrlhf)

---

## 💡 一句话要点

**提出ZeroTIR以解决数学问题求解中的工具使用挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `工具集成推理` `数学问题求解` `自发代码执行` `大型语言模型` `ZeroTIR` `自动化推理`

## 📋 核心要点

1. 现有的大型语言模型在数学推理任务中缺乏精确性，尤其是在需要代码执行的场景中表现不佳。
2. 论文提出了ZeroTIR方法，通过强化学习训练模型自发生成和执行Python代码，解决数学问题。
3. 实验结果表明，ZeroTIR在多个数学基准测试中显著优于传统的非工具强化学习方法，展示了工具使用的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在需要精确、可验证计算的数学推理任务中常常表现不佳。尽管基于结果的强化学习（RL）能够增强文本推理能力，但理解代理如何自主学习利用外部工具（如代码执行）仍然至关重要。本文研究了基于结果奖励的RL在工具集成推理中的应用，提出了ZeroTIR方法，训练基础LLMs自发生成和执行Python代码以解决数学问题，而无需监督工具使用示例。我们发现，随着RL训练的进行，关键指标呈现出可预测的扩展关系，训练步骤的增加与自发代码执行频率、平均响应长度和最终任务准确性之间存在强正相关。这表明训练投入的计算努力与有效的工具增强推理策略的出现之间存在可量化的关系。实验结果显示，ZeroTIR在挑战性数学基准测试中显著超越了非工具的ZeroRL基线。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在数学问题求解中对工具使用的依赖不足，现有方法往往需要监督示例，限制了模型的自主学习能力。

**核心思路**：通过强化学习从结果奖励出发，训练模型自发生成和执行代码，提升其在数学推理中的表现，避免对人工标注的依赖。

**技术框架**：整体架构包括一个解耦的代码执行环境，模型在此环境中进行训练，主要模块包括代码生成、执行和结果反馈。

**关键创新**：最重要的创新在于提出了ZeroTIR方法，使得模型能够在没有监督示例的情况下，自主学习如何有效利用外部工具进行推理，显著提升了模型的数学推理能力。

**关键设计**：在训练过程中，设置了适当的奖励机制以鼓励自发代码执行，采用了标准的强化学习算法，并在多个基准测试上进行了验证，确保了方法的有效性和可重复性。

## 📊 实验亮点

实验结果显示，ZeroTIR在多个挑战性数学基准测试中显著超越了传统的非工具强化学习方法ZeroRL，具体表现为自发代码执行频率和任务准确性均有显著提升，验证了工具使用的有效性和必要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化数学求解和智能助手等。通过提升模型的自主工具使用能力，可以在更广泛的数学和科学计算任务中实现高效的自动化解决方案，未来可能对教育和科研领域产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) often struggle with mathematical reasoning tasks requiring precise, verifiable computation. While Reinforcement Learning (RL) from outcome-based rewards enhances text-based reasoning, understanding how agents autonomously learn to leverage external tools like code execution remains crucial. We investigate RL from outcome-based rewards for Tool-Integrated Reasoning, ZeroTIR, training base LLMs to spontaneously generate and execute Python code for mathematical problems without supervised tool-use examples. Our central contribution is we demonstrate that as RL training progresses, key metrics scale predictably. Specifically, we observe strong positive correlations where increased training steps lead to increases in the spontaneous code execution frequency, the average response length, and, critically, the final task accuracy. This suggests a quantifiable relationship between computational effort invested in training and the emergence of effective, tool-augmented reasoning strategies. We implement a robust framework featuring a decoupled code execution environment and validate our findings across standard RL algorithms and frameworks. Experiments show ZeroTIR significantly surpasses non-tool ZeroRL baselines on challenging math benchmarks. Our findings provide a foundational understanding of how autonomous tool use is acquired and scales within Agent RL, offering a reproducible benchmark for future studies. Code is released at \href{https://github.com/yyht/openrlhf_async_pipline}{https://github.com/yyht/openrlhf\_async\_pipline}.

