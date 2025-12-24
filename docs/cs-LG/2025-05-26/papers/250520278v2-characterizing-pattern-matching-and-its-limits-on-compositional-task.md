---
layout: default
title: Characterizing Pattern Matching and Its Limits on Compositional Task Structures
---

# Characterizing Pattern Matching and Its Limits on Compositional Task Structures

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20278" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20278v2</a>
  <a href="https://arxiv.org/pdf/2505.20278.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20278v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20278v2', 'Characterizing Pattern Matching and Its Limits on Compositional Task Structures')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hoyeon Chang, Jinho Park, Hanseul Cho, Sohee Yang, Miyoung Ko, Hyeonbin Hwang, Seungpil Won, Dohaeng Lee, Youbin Ahn, Minjoon Seo

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-26 (更新: 2025-11-26)

---

## 💡 一句话要点

**提出模式匹配的形式化框架以解决组合任务中的泛化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模式匹配` `功能等价` `组合任务` `超出分布泛化` `路径模糊性` `大型语言模型` `样本复杂度` `Transformer`

## 📋 核心要点

1. 现有方法在组合任务中存在多种泛化来源，导致对LLMs模式匹配能力的评估不够精确。
2. 本文通过将模式匹配形式化为功能等价，系统研究了模型在控制任务中的表现，提供了清晰的理论框架。
3. 实验证明，模式匹配的实例成功率与见证相关功能等价的上下文数量密切相关，且路径模糊性影响模型的准确性和可解释性。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）展现出令人印象深刻的能力，但其成功往往依赖于模式匹配行为，这与组合任务中的超出分布（OOD）泛化失败相关。现有的行为研究常常使用多种泛化来源的任务设置，模糊了LLMs在模式匹配中的表现及其局限性。为了解决这一模糊性，本文首先将模式匹配形式化为功能等价，即识别输入子序列对在其他输入保持不变时始终导致相同结果的情况。然后，我们系统研究了仅解码器Transformer和Mamba在控制任务中的表现，这些任务的组合结构隔离了这一机制。我们的形式化方法提供了预测性和定量的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决LLMs在组合任务中模式匹配能力的评估不准确的问题，现有方法未能清晰区分多种泛化来源对模型表现的影响。

**核心思路**：通过将模式匹配形式化为功能等价，识别输入子序列对，从而提供一个可预测和可验证的框架来分析模型的泛化能力。

**技术框架**：研究采用控制任务的组合结构，主要模块包括功能等价的识别、样本复杂度的界定以及路径模糊性的分析。

**关键创新**：提出了功能等价的形式化定义，揭示了模式匹配的实例成功率与上下文数量之间的关系，提供了对路径模糊性的深入分析。

**关键设计**：在实验中，采用了20倍参数扩展的设置，验证了理论预测，并通过不同架构的比较，分析了样本复杂度和路径模糊性对模型表现的影响。

## 📊 实验亮点

实验结果表明，模式匹配的实例成功率与见证功能等价的上下文数量呈正相关，且在20倍参数扩展下，模型的表现与理论预测高度一致。此外，路径模糊性被证明是影响模型准确性和可解释性的关键因素。

## 🎯 应用场景

该研究为理解和改进大型语言模型在组合任务中的表现提供了理论基础，潜在应用包括自然语言处理、机器人控制和复杂系统建模等领域。通过明确模式匹配的局限性，未来可以设计出更具泛化能力的模型，提升其在实际应用中的表现。

## 📄 摘要（原文）

> Despite impressive capabilities, LLMs' successes often rely on pattern-matching behaviors, yet these are also linked to OOD generalization failures in compositional tasks. However, behavioral studies commonly employ task setups that allow multiple generalization sources (e.g., algebraic invariances, structural repetition), obscuring a precise and testable account of how well LLMs perform generalization through pattern matching and their limitations. To address this ambiguity, we first formalize pattern matching as functional equivalence, i.e., identifying pairs of subsequences of inputs that consistently lead to identical results when the rest of the input is held constant. Then, we systematically study how decoder-only Transformer and Mamba behave in controlled tasks with compositional structures that isolate this mechanism. Our formalism yields predictive and quantitative insights: (1) Instance-wise success of pattern matching is well predicted by the number of contexts witnessing the relevant functional equivalence. (2) We prove a tight sample complexity bound of learning a two-hop structure by identifying the exponent of the data scaling law for perfect in-domain generalization. Our empirical results align with the theoretical prediction, under 20x parameter scaling and across architectures. (3) Path ambiguity is a structural barrier: when a variable influences the output via multiple paths, models fail to form unified intermediate state representations, impairing accuracy and interpretability. (4) Chain-of-Thought reduces data requirements yet does not resolve path ambiguity. Hence, we provide a predictive, falsifiable boundary for pattern matching and a foundational diagnostic for disentangling mixed generalization mechanisms.

