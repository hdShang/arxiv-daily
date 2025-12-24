---
layout: default
title: "LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research"
---

# LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17335" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17335v1</a>
  <a href="https://arxiv.org/pdf/2506.17335.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17335v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17335v1', 'LMR-BENCH: Evaluating LLM Agent\'s Ability on Reproducing Language Modeling Research')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuo Yan, Ruochen Li, Ziming Luo, Zimu Wang, Daoyang Li, Liqiang Jing, Kaiyu He, Peilin Wu, George Michalopoulos, Yue Zhang, Ziyang Zhang, Mian Zhang, Zhiyu Chen, Xinya Du

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出LMR-BENCH以评估LLM代理在语言建模研究中的代码重现能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码重现` `自然语言处理` `科学推理` `基准评估` `机器学习` `自动化研究`

## 📋 核心要点

1. 现有方法在重现研究论文中的代码能力不足，特别是在复杂的推理和代码理解方面存在挑战。
2. 论文提出LMR-BENCH基准，通过28个任务系统评估LLM代理在代码重现中的表现，填补了这一研究空白。
3. 实验结果显示，当前最先进的LLM模型在科学推理和代码综合方面仍有显著局限，亟需改进。

## 📝 摘要（中文）

大型语言模型（LLM）代理在推动科学发现方面展现出显著潜力。然而，它们在重现研究论文中的代码，尤其是在自然语言处理（NLP）领域的能力仍未得到充分探索。此任务涉及复杂的推理挑战，包括抽象概念的智力综合和对相互依赖文件的代码库的理解。为填补这一空白，本文提出了LMR-BENCH，一个旨在系统评估LLM代理在语言建模研究中代码重现能力的基准。该基准包含28个代码重现任务，来源于过去五年内23篇发表在顶级NLP会议上的研究论文，涵盖九个基本类别。模型接收研究论文、包含一个或多个被遮蔽函数的代码库以及实现这些函数的指令。实验结果表明，即使是最先进的模型在科学推理和代码综合方面仍存在持续的局限性，突显了LLM代理在自主重现科学研究中的关键缺口。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM代理在重现语言建模研究中代码的能力不足，现有方法在处理复杂推理和代码库理解方面存在显著痛点。

**核心思路**：LMR-BENCH基准通过设计一系列代码重现任务，系统性地评估LLM代理的能力，旨在揭示其在科学研究重现中的局限性。

**技术框架**：整体架构包括任务设计、模型输入（研究论文和代码库）、以及评估标准（单元测试准确性和代码正确性评估）。主要模块包括任务生成、模型推理和结果评估。

**关键创新**：LMR-BENCH的设计是其核心创新点，通过系统化的任务评估填补了LLM在科学研究重现能力评估的空白，与现有方法相比，更加注重复杂推理和代码综合能力的评估。

**关键设计**：在任务设计中，采用了多样化的代码重现任务，确保涵盖不同的研究领域和复杂度，同时在评估中引入了标准化的单元测试，以量化模型的表现。实验中使用了最新的LLM模型进行对比，确保结果的可靠性和有效性。

## 📊 实验亮点

实验结果显示，当前最先进的LLM模型在28个代码重现任务中的表现仍然有限，尤其在科学推理和代码综合方面存在显著不足。具体而言，模型在单元测试中的准确率未达到预期，反映出在自主重现科学研究方面的关键缺口。

## 🎯 应用场景

该研究的潜在应用领域包括科学研究自动化、代码生成工具以及教育领域的编程教学。通过提高LLM在代码重现方面的能力，可以促进科学发现的效率，并为开发更智能的编程助手奠定基础。未来，LMR-BENCH可能成为评估LLM能力的重要标准，推动相关技术的进步。

## 📄 摘要（原文）

> Large language model (LLM) agents have demonstrated remarkable potential in advancing scientific discovery. However, their capability in the fundamental yet crucial task of reproducing code from research papers, especially in the NLP domain, remains underexplored. This task includes unique complex reasoning challenges in the intellectual synthesis of abstract concepts and the comprehension of code repositories with interdependent files. Motivated by this gap, we present LMR-BENCH, a benchmark designed to systematically evaluate the capability of LLM agents on code reproduction from Language Modeling Research. It consists of 28 code reproduction tasks derived from 23 research papers published in top-tier NLP venues over the past five years, spanning nine fundamental categories. Models are provided with a research paper, a code repository containing one or more masked functions, and instructions for implementing these functions. We conduct extensive experiments in standard prompting and LLM agent settings with state-of-the-art LLMs, evaluating the accuracy of unit tests and performing LLM-based evaluation of code correctness. Experimental results reveal that even the most advanced models still exhibit persistent limitations in scientific reasoning and code synthesis, highlighting critical gaps in LLM agents' ability to autonomously reproduce scientific research

