---
layout: default
title: "Datarus-R1: An Adaptive Multi-Step Reasoning LLM for Automated Data Analysis"
---

# Datarus-R1: An Adaptive Multi-Step Reasoning LLM for Automated Data Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13382" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13382v1</a>
  <a href="https://arxiv.org/pdf/2508.13382.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13382v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13382v1', 'Datarus-R1: An Adaptive Multi-Step Reasoning LLM for Automated Data Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ayoub Ben Chaliah, Hela Dellagi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出Datarus-R1以解决自动化数据分析中的推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化数据分析` `推理能力` `语言模型` `深度学习` `合成数据生成`

## 📋 核心要点

1. 现有方法在处理复杂数据分析任务时，往往缺乏有效的推理能力和结构化思维，导致结果不够准确。
2. Datarus-R1通过训练完整的分析轨迹，结合双重奖励机制和优化的生成策略，提升了模型的推理能力和输出质量。
3. 实验结果显示，Datarus在标准基准测试中超越同类模型，准确率提高了30%，且每个解决方案的token数量减少了18-49%。

## 📝 摘要（中文）

我们提出了Datarus-R1-14B，一个拥有140亿参数的开放权重语言模型，经过微调以充当虚拟数据分析师和研究生级问题解决者。Datarus的训练不仅基于孤立的问题-答案对，而是涵盖了完整的分析轨迹，包括推理步骤、代码执行、错误追踪、自我修正和最终结论，所有内容以ReAct风格的笔记本格式呈现，涉及金融、医学、数值分析等多个定量领域。我们的训练管道结合了轨迹中心的合成数据生成器、双重奖励框架和内存优化的Group Relative Policy Optimization实现。

## 🔬 方法详解

**问题定义**：论文旨在解决现有自动化数据分析模型在推理和结构化思维方面的不足，尤其是在复杂问题上的表现不佳。

**核心思路**：Datarus-R1通过训练完整的分析轨迹而非孤立的问答对，结合双重奖励机制，提升了模型的推理能力和输出质量。

**技术框架**：整体架构包括轨迹中心的合成数据生成器、双重奖励框架和内存优化的GRPO实现，确保模型在推理和执行代码时的高效性。

**关键创新**：Datarus的双重推理接口设计是其核心创新，支持在代理模式下生成ReAct标记步骤并执行真实代码，在反思模式下输出紧凑的思维链条。

**关键设计**：模型采用了轻量级标记结构信号与层次奖励模型的结合，使用余弦课程平滑地调整结构保真度与语义深度的重点，减少了常见的格式崩溃和冗长问题。

## 📊 实验亮点

Datarus在标准公共基准测试中表现优异，超越了同类模型，尤其在AIME 2024/2025和LiveCodeBench上，准确率提高了30%，同时每个解决方案的token数量减少了18-49%。这些结果表明，Datarus在推理效率和输出质量上均有显著提升。

## 🎯 应用场景

Datarus-R1在金融、医学和数值分析等多个领域具有广泛的应用潜力。作为虚拟数据分析师，它能够自动化处理复杂的数据分析任务，帮助研究人员和行业专家提高工作效率，减少人为错误。此外，该模型的设计理念也为未来的智能助手和决策支持系统提供了重要的参考。

## 📄 摘要（原文）

> We present Datarus-R1-14B, a 14 B-parameter open-weights language model fine-tuned from Qwen 2.5-14B-Instruct to act as a virtual data analyst and graduate-level problem solver. Datarus is trained not on isolated question-answer pairs but on full analytical trajectories including reasoning steps, code execution, error traces, self-corrections, and final conclusions, all captured in a ReAct-style notebook format spanning finance, medicine, numerical analysis, and other quantitative domains. Our training pipeline combines (i) a trajectory-centric synthetic data generator that yielded 144 000 tagged notebook episodes, (ii) a dual-reward framework blending a lightweight tag-based structural signal with a Hierarchical Reward Model (HRM) that scores both single-step soundness and end-to-end coherence, and (iii) a memory-optimized implementation of Group Relative Policy Optimization (GRPO) featuring KV-cache reuse, sequential generation, and reference-model sharding. A cosine curriculum smoothly shifts emphasis from structural fidelity to semantic depth, reducing the format collapse and verbosity that often plague RL-aligned LLMs. A central design choice in Datarus is it dual reasoning interface. In agentic mode the model produces ReAct-tagged steps that invoke Python tools to execute real code; in reflection mode it outputs compact Chain-of-Thought (CoT) traces delimited by <think> and <answer> tags. On demanding postgraduate-level problems, Datarus exhibits an "AHA-moment" pattern: it sketches hypotheses, revises them once or twice, and converges avoiding the circular, token-inflating loops common to contemporary systems. Across standard public benchmarks Datarus surpasses similar size models and even reaches the level of larger reasoning models such as QwQ-32B achieving up to 30% higher accuracy on AIME 2024/2025 and LiveCodeBench while emitting 18-49% fewer tokens per solution.

