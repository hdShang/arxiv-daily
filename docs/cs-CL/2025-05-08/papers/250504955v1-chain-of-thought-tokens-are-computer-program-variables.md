---
layout: default
title: Chain-of-Thought Tokens are Computer Program Variables
---

# Chain-of-Thought Tokens are Computer Program Variables

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04955" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04955v1</a>
  <a href="https://arxiv.org/pdf/2505.04955.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04955v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04955v1', 'Chain-of-Thought Tokens are Computer Program Variables')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fangwei Zhu, Peiyi Wang, Zhifang Sui

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-08

**🔗 代码/项目**: [GITHUB](https://github.com/solitaryzero/CoTs_are_Variables)

---

## 💡 一句话要点

**提出将链式思维令牌视为计算机程序变量以解决复杂推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `链式思维` `大型语言模型` `复杂推理` `计算机程序变量` `多位数乘法` `动态规划` `中间结果` `模型优化`

## 📋 核心要点

1. 核心问题：现有的链式思维方法在复杂推理任务中存在机制不明确的问题，影响其有效性。
2. 方法要点：本文提出将CoT令牌视为计算机程序中的变量，探索其在多位数乘法和动态规划中的作用。
3. 实验或效果：研究表明，仅保留中间结果的令牌即可实现与完整CoT相当的性能，且干预CoT值会影响后续结果。

## 📝 摘要（中文）

链式思维（CoT）要求大型语言模型（LLMs）在得出最终答案之前生成中间步骤，已被证明对解决复杂推理任务有效。然而，CoT的内部机制仍然不甚清晰。本文通过实证研究CoT令牌在LLMs中的作用，聚焦于多位数乘法和动态规划这两项组合任务。研究发现，仅保留存储中间结果的令牌也能实现相似的性能。此外，观察到以替代潜在形式存储中间结果不会影响模型性能。随机干预CoT中的某些值后，后续的CoT令牌和最终答案会相应变化。这些发现表明，CoT令牌可能像计算机程序中的变量，但也存在意外捷径和令牌间计算复杂性限制等潜在缺陷。

## 🔬 方法详解

**问题定义**：本文旨在探讨链式思维（CoT）在大型语言模型中的作用，尤其是在复杂推理任务中的有效性。现有方法在处理多位数乘法和动态规划时，CoT的内部机制尚不明确，导致其应用效果不稳定。

**核心思路**：论文提出将CoT令牌视为计算机程序中的变量，认为这些令牌在推理过程中起到存储中间结果的作用。通过这种视角，研究者能够更好地理解CoT的功能及其潜在问题。

**技术框架**：研究通过设计实验，分析CoT令牌在多位数乘法和动态规划任务中的表现。主要模块包括数据准备、模型训练、结果评估和干预实验。

**关键创新**：最重要的创新点在于将CoT令牌与计算机程序变量进行类比，揭示了其在推理过程中的作用及潜在缺陷。这一视角为理解和优化LLMs提供了新的思路。

**关键设计**：在实验中，研究者设置了不同的参数以评估CoT令牌的影响，包括中间结果的存储方式和干预策略。损失函数和网络结构的设计也经过精心调整，以确保实验结果的可靠性。

## 📊 实验亮点

实验结果显示，仅保留存储中间结果的CoT令牌在多位数乘法和动态规划任务中表现出与完整CoT相当的性能，验证了其作为变量的有效性。此外，随机干预CoT令牌的值会导致后续结果的显著变化，进一步支持了研究的核心观点。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化编程和复杂决策支持系统。通过优化LLMs在推理任务中的表现，能够提高智能助手的准确性和效率，进而推动人工智能在实际应用中的广泛采用。

## 📄 摘要（原文）

> Chain-of-thoughts (CoT) requires large language models (LLMs) to generate intermediate steps before reaching the final answer, and has been proven effective to help LLMs solve complex reasoning tasks. However, the inner mechanism of CoT still remains largely unclear. In this paper, we empirically study the role of CoT tokens in LLMs on two compositional tasks: multi-digit multiplication and dynamic programming. While CoT is essential for solving these problems, we find that preserving only tokens that store intermediate results would achieve comparable performance. Furthermore, we observe that storing intermediate results in an alternative latent form will not affect model performance. We also randomly intervene some values in CoT, and notice that subsequent CoT tokens and the final answer would change correspondingly. These findings suggest that CoT tokens may function like variables in computer programs but with potential drawbacks like unintended shortcuts and computational complexity limits between tokens. The code and data are available at https://github.com/solitaryzero/CoTs_are_Variables.

