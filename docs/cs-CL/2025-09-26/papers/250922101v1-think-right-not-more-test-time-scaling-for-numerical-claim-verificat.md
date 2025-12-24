---
layout: default
title: "Think Right, Not More: Test-Time Scaling for Numerical Claim Verification"
---

# Think Right, Not More: Test-Time Scaling for Numerical Claim Verification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22101" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22101v1</a>
  <a href="https://arxiv.org/pdf/2509.22101.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22101v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22101v1', 'Think Right, Not More: Test-Time Scaling for Numerical Claim Verification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Primakov Chungkham, V Venktesh, Vinay Setty, Avishek Anand

**分类**: cs.CL

**发布日期**: 2025-09-26

**备注**: Accepted to EMNLP 2025, 19 pages

**🔗 代码/项目**: [GITHUB](https://github.com/VenkteshV/VerifierFC)

---

## 💡 一句话要点

**提出VERIFIERFC模型，通过测试时缩放提升LLM在数值声明验证中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `事实核查` `数值推理` `大型语言模型` `测试时缩放` `推理漂移`

## 📋 核心要点

1. 现有LLM在处理需要组合和数值推理的复杂数值声明验证任务时，存在无法理解数值细微差别和推理漂移的问题。
2. 论文提出VERIFIERFC模型，通过测试时缩放（TTS）策略，从LLM中提取多个推理路径，并利用验证器模型选择最佳路径。
3. 实验结果表明，TTS能有效缓解推理漂移问题，显著提升数值声明验证性能，自适应TTS机制在效率上提升1.8倍，性能提升18.8%。

## 📝 摘要（中文）

本文针对现实世界中数值声明的事实核查问题，该问题需要多步骤推理和数值推理来验证声明的各个方面。尽管包括推理模型在内的大型语言模型（LLM）取得了巨大进展，但在需要组合和数值推理的事实核查方面仍然存在不足。它们无法理解数值方面的细微差别，并且容易出现推理漂移问题，即模型无法将各种信息置于上下文中，导致误解和推理过程的回溯。本文系统地探索了在测试时缩放计算（TTS）对LLM在复杂数值声明的事实核查任务上的影响，这需要从LLM中引出多个推理路径。我们训练了一个验证器模型（VERIFIERFC）来导航可能的推理路径空间，并选择一个可能导致正确结果的路径。我们观察到TTS有助于缓解推理漂移问题，从而显著提高数值声明的事实核查性能。为了提高TTS的计算效率，我们引入了一种自适应机制，该机制根据声明的感知复杂性选择性地执行TTS。这种方法比标准TTS的效率高1.8倍，同时比单次声明验证方法实现了18.8%的显著性能提升。我们的代码和数据可在https://github.com/VenkteshV/VerifierFC找到。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在事实核查，特别是复杂数值声明验证任务中的不足。现有方法的痛点在于LLM难以进行多步骤推理和数值推理，容易出现推理漂移，导致验证结果不准确。

**核心思路**：论文的核心思路是利用测试时缩放（Test-Time Scaling, TTS）策略，通过多次调用LLM生成多个可能的推理路径，然后训练一个验证器模型（VERIFIERFC）来评估这些路径，并选择最有可能得出正确结论的路径。这种方法旨在缓解推理漂移问题，提高验证的准确性。

**技术框架**：整体框架包含以下几个主要阶段：1) 使用LLM生成多个推理路径；2) 使用训练好的验证器模型（VERIFIERFC）对每个推理路径进行评估打分；3) 选择得分最高的推理路径作为最终的验证结果。为了提高效率，还引入了自适应TTS机制，根据声明的复杂性动态调整推理路径的数量。

**关键创新**：最重要的技术创新点在于结合了测试时缩放和可学习的验证器模型。传统的TTS方法通常只是简单地平均或投票多个结果，而VERIFIERFC能够学习不同推理路径的质量，并选择最佳路径，从而更有效地利用了TTS的优势。自适应TTS机制也是一个创新点，它能够根据输入数据的复杂性动态调整计算量，提高了计算效率。

**关键设计**：VERIFIERFC模型的具体结构未知，但可以推测其输入是LLM生成的推理路径，输出是该路径的质量评分。自适应TTS机制的关键在于如何衡量声明的复杂性，论文中使用的具体方法未知。损失函数的设计目标是使VERIFIERFC能够准确区分正确和错误的推理路径。

## 📊 实验亮点

实验结果表明，提出的VERIFIERFC模型在数值声明验证任务上取得了显著的性能提升。自适应TTS机制在计算效率上比标准TTS提高了1.8倍，同时比单次声明验证方法实现了18.8%的性能提升。这些数据表明，该方法在提高准确性和效率方面都具有优势。

## 🎯 应用场景

该研究成果可应用于各种需要事实核查的场景，例如新闻验证、科学研究、金融分析等。通过提高数值声明验证的准确性，可以减少虚假信息的传播，提高决策的可靠性，并为自动化知识发现提供更可靠的基础。

## 📄 摘要（原文）

> Fact-checking real-world claims, particularly numerical claims, is inherently complex that require multistep reasoning and numerical reasoning for verifying diverse aspects of the claim. Although large language models (LLMs) including reasoning models have made tremendous advances, they still fall short on fact-checking real-world claims that require a combination of compositional and numerical reasoning. They are unable to understand nuance of numerical aspects, and are also susceptible to the reasoning drift issue, where the model is unable to contextualize diverse information resulting in misinterpretation and backtracking of reasoning process. In this work, we systematically explore scaling test-time compute (TTS) for LLMs on the task of fact-checking complex numerical claims, which entails eliciting multiple reasoning paths from an LLM. We train a verifier model (VERIFIERFC) to navigate this space of possible reasoning paths and select one that could lead to the correct verdict. We observe that TTS helps mitigate the reasoning drift issue, leading to significant performance gains for fact-checking numerical claims. To improve compute efficiency in TTS, we introduce an adaptive mechanism that performs TTS selectively based on the perceived complexity of the claim. This approach achieves 1.8x higher efficiency than standard TTS, while delivering a notable 18.8% performance improvement over single-shot claim verification methods. Our code and data can be found at https://github.com/VenkteshV/VerifierFC

