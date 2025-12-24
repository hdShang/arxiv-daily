---
layout: default
title: Not All Correct Answers Are Equal: Why Your Distillation Source Matters
---

# Not All Correct Answers Are Equal: Why Your Distillation Source Matters

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14464" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14464v2</a>
  <a href="https://arxiv.org/pdf/2505.14464.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14464v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14464v2', 'Not All Correct Answers Are Equal: Why Your Distillation Source Matters')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyu Tian, Yunjie Ji, Haotian Wang, Shuaiting Chen, Sitong Zhao, Yiping Peng, Han Zhao, Xiangang Li

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-05-22)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/a-m-team)

---

## 💡 一句话要点

**通过高质量蒸馏数据提升语言模型推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `蒸馏训练` `语言模型` `推理能力` `数据集构建` `模型评估`

## 📋 核心要点

1. 现有的语言模型在推理能力上存在不足，尤其是在处理复杂任务时表现不佳。
2. 本文提出通过高质量的蒸馏数据来提升语言模型的推理能力，重点分析不同教师模型的输出质量。
3. 实验结果显示，基于AM-Thinking-v1蒸馏的数据在多个推理基准上表现最佳，且模型输出具有适应性。

## 📝 摘要（中文）

蒸馏已成为增强开源语言模型推理能力的有效方法。本文通过对三种先进教师模型（AM-Thinking-v1、Qwen3-235B-A22B和DeepSeek-R1）进行大规模实证研究，收集了189万条查询的验证输出，构建了三个平行数据集并分析其分布。结果表明，AM-Thinking-v1蒸馏数据在标记长度多样性和困惑度上表现优异。基于该数据集训练的学生模型在多个推理基准上表现最佳，展示了适应性输出行为。研究结果强调了高质量推理轨迹的重要性，并公开了相关数据集以支持未来研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语言模型推理能力不足的问题，尤其是在复杂任务中的表现不佳，现有方法往往依赖于低质量的训练数据。

**核心思路**：通过收集和分析来自不同教师模型的高质量蒸馏数据，探索其对学生模型推理能力的影响，强调蒸馏源的重要性。

**技术框架**：整体流程包括数据收集、数据集构建、模型训练和性能评估。首先从三个教师模型中提取输出，然后构建三个平行数据集，最后在多个推理基准上评估学生模型的表现。

**关键创新**：最重要的创新在于通过大规模实证研究揭示了不同教师模型输出质量对学生模型性能的显著影响，尤其是AM-Thinking-v1蒸馏数据的优越性。

**关键设计**：在数据集构建中，关注标记长度的多样性和困惑度，确保训练数据的高质量；在模型训练中，采用适应性输出策略，使模型能够根据任务难度调整响应长度。

## 📊 实验亮点

实验结果显示，基于AM-Thinking-v1蒸馏的数据在AIME2024、AIME2025、MATH500和LiveCodeBench等推理基准上分别取得了84.3、72.2、98.4和65.9的优异成绩，明显优于其他数据集训练的模型，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动问答系统和复杂问题求解等。通过提升语言模型的推理能力，可以在更广泛的场景中实现更高效的智能交互，推动自然语言处理技术的发展。

## 📄 摘要（原文）

> Distillation has emerged as a practical and effective approach to enhance the reasoning capabilities of open-source language models. In this work, we conduct a large-scale empirical study on reasoning data distillation by collecting verified outputs from three state-of-the-art teacher models-AM-Thinking-v1, Qwen3-235B-A22B, and DeepSeek-R1-on a shared corpus of 1.89 million queries. We construct three parallel datasets and analyze their distributions, revealing that AM-Thinking-v1-distilled data exhibits greater token length diversity and lower perplexity. Student models trained on each dataset are evaluated on reasoning benchmarks including AIME2024, AIME2025, MATH500, and LiveCodeBench. The model distilled from AM-Thinking-v1 consistently achieves the best performance (e.g., 84.3 on AIME2024, 72.2 on AIME2025, 98.4 on MATH500, and 65.9 on LiveCodeBench) and demonstrates adaptive output behavior-producing longer responses for harder tasks and shorter ones for simpler tasks. These findings highlight the value of high-quality, verified reasoning traces. We release the AM-Thinking-v1 and Qwen3-235B-A22B distilled datasets to support future research on open and high-performing reasoning-oriented language models. The datasets are publicly available on Hugging Face\footnote{Datasets are available on Hugging Face: \href{https://huggingface.co/datasets/a-m-team/AM-Thinking-v1-Distilled}{AM-Thinking-v1-Distilled}, \href{https://huggingface.co/datasets/a-m-team/AM-Qwen3-Distilled}{AM-Qwen3-Distilled}.}.

