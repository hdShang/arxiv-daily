---
layout: default
title: Pause Tokens Strictly Increase the Expressivity of Constant-Depth Transformers
---

# Pause Tokens Strictly Increase the Expressivity of Constant-Depth Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21024" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21024v1</a>
  <a href="https://arxiv.org/pdf/2505.21024.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21024v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21024v1', 'Pause Tokens Strictly Increase the Expressivity of Constant-Depth Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Charles London, Varun Kanade

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**引入暂停符号以提升常深度变换器的表达能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `变换器` `暂停符号` `表达能力` `深度学习` `理论分析` `自然语言处理` `数学推理`

## 📋 核心要点

1. 现有的变换器在处理某些任务时表现不佳，尤其是缺乏有效的符号来增强其表达能力。
2. 本文提出通过引入暂停符号来提升常深度变换器的计算表达能力，从而解决现有方法的局限性。
3. 实验结果显示，添加暂停符号后，变换器能够学习到之前无法学习的函数，显著提升了模型的性能。

## 📝 摘要（中文）

暂停符号（如"..."）在语言和数学任务中持续提升变换器的性能，但其理论效果尚未解释。本文首次提供了形式上的分离结果，证明在常深度、对数宽度的变换器中，添加暂停符号严格增加了其计算表达能力。对于有界精度的激活函数，未添加暂停符号的变换器只能计算$	ext{AC}^0$函数的严格子集，而添加多项式数量的暂停符号则使其能够表达整个类。对于对数精度的变换器，添加暂停符号的表达能力达到$	ext{TC}^0$，与已知的上界相匹配。实证结果表明，双层因果掩蔽变换器在提供暂停符号时能够学习奇偶性，而在没有暂停符号时则无法学习。这些结果为先前的实证发现提供了严格的理论解释，并阐明了暂停符号如何与宽度、深度和数值精度相互作用。

## 🔬 方法详解

**问题定义**：本文旨在解决常深度变换器在表达能力上的不足，特别是缺乏暂停符号时其计算能力的限制。现有方法在处理复杂任务时表现不佳，无法有效表达某些函数。

**核心思路**：论文的核心思路是通过引入暂停符号来增强变换器的表达能力，证明其在理论上的有效性和实证上的可行性。通过添加多项式数量的暂停符号，变换器能够表达更广泛的函数类。

**技术框架**：整体架构包括对常深度、对数宽度变换器的理论分析和实证验证。主要模块包括暂停符号的引入、表达能力的理论证明以及实验验证。

**关键创新**：最重要的技术创新在于首次提供了暂停符号对常深度变换器表达能力的严格提升证明，明确了其与现有方法的本质区别。

**关键设计**：关键设计包括对变换器的激活函数进行有界精度设置，以及在实验中使用双层因果掩蔽结构来验证暂停符号的有效性。

## 📊 实验亮点

实验结果表明，双层因果掩蔽变换器在添加暂停符号后能够成功学习奇偶性函数，而在没有暂停符号的情况下则无法实现。这一发现验证了暂停符号在提升模型性能方面的显著作用，提供了理论与实证的双重支持。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、数学推理和其他需要复杂推理能力的任务。通过提升变换器的表达能力，研究成果能够在智能助手、自动化推理和教育技术等领域产生实际价值，并推动相关技术的发展。

## 📄 摘要（原文）

> Pause tokens, simple filler symbols such as "...", consistently improve Transformer performance on both language and mathematical tasks, yet their theoretical effect remains unexplained. We provide the first formal separation result, proving that adding pause tokens to constant-depth, logarithmic-width Transformers strictly increases their computational expressivity. With bounded-precision activations, Transformers without pause tokens compute only a strict subset of $\mathsf{AC}^0$ functions, while adding a polynomial number of pause tokens allows them to express the entire class. For logarithmic-precision Transformers, we show that adding pause tokens achieves expressivity equivalent to $\mathsf{TC}^0$, matching known upper bounds. Empirically, we demonstrate that two-layer causally masked Transformers can learn parity when supplied with pause tokens, a function that they appear unable to learn without them. Our results provide a rigorous theoretical explanation for prior empirical findings, clarify how pause tokens interact with width, depth, and numeric precision, and position them as a distinct mechanism, complementary to chain-of-thought prompting, for enhancing Transformer reasoning.

