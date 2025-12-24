---
layout: default
title: Equivalent Linear Mappings of Large Language Models
---

# Equivalent Linear Mappings of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24293" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24293v3</a>
  <a href="https://arxiv.org/pdf/2505.24293.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24293v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24293v3', 'Equivalent Linear Mappings of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: James R. Golden

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-30 (更新: 2025-10-11)

**备注**: title changed; major revisions; code available at https://github.com/jamesgolden1/equivalent-linear-LLMs/; published at https://openreview.net/forum?id=oDWbJsIuEp

**期刊**: Transactions on Machine Learning Research (TMLR) (10/2025)

---

## 💡 一句话要点

**提出等效线性映射以解析大型语言模型的推理机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可解释性` `线性映射` `变换器` `推理机制` `语义结构` `雅可比矩阵`

## 📋 核心要点

1. 现有方法在解释大型语言模型的计算机制时存在局限，无法揭示隐藏表示的生成过程。
2. 本文提出将LLM推理映射为等效线性系统，通过固定输入依赖的线性变换来实现可解释性。
3. 实验结果显示，该方法在多个模型上重构输出嵌入的相对误差低于$10^{-13}$，展示了LLMs在低维语义结构中的操作特性。

## 📝 摘要（中文）

尽管在变换器可解释性方面取得了显著进展，但理解大型语言模型（LLMs）的计算机制仍然是一个基本挑战。许多方法解释了网络的隐藏表示，但对这些表示的生成方式却无能为力。本文通过将LLM推理映射到一个等效且可解释的线性系统，成功重构预测输出嵌入，且相对误差低于$10^{-13}$，无需额外的模型训练。我们利用变换器的特性，将每个操作（门控激活、注意力和归一化）表示为$A(x) 	imes x$，其中$A(x)$是输入依赖的线性变换。通过战略性地分离梯度计算的组件，固定$A(x)$的值，得到等效的线性映射。该方法展示了LLMs在极低维子空间中的操作特性，并揭示了语义概念的可解释性。

## 🔬 方法详解

**问题定义**：本文旨在解决对大型语言模型推理机制的理解不足，现有方法无法有效解释隐藏表示的生成过程。

**核心思路**：通过将LLM推理映射为等效线性系统，利用变换器的特性将每个操作表示为输入依赖的线性变换，从而实现可解释性。

**技术框架**：整体架构包括固定$A(x)$的值以计算雅可比矩阵，进而得到等效线性映射。每个输入标记对应一个线性算子，逐层分析其注意力和多层感知机模块的作用。

**关键创新**：最重要的创新在于通过雅可比矩阵的分离计算，揭示了LLMs在低维子空间中的操作特性，与现有方法相比，提供了更深层次的可解释性。

**关键设计**：在实验中，采用了双浮点精度计算，确保重构输出嵌入的相对误差低于$10^{-13}$，并展示了不同模型（如Qwen 3、Gemma 3和Llama 3）的线性表示。

## 📊 实验亮点

实验结果表明，本文提出的等效线性映射方法在多个大型语言模型上实现了重构输出嵌入的相对误差低于$10^{-13}$，展示了LLMs在低维语义结构中的操作特性，显著提升了对模型推理过程的可解释性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、文本生成和机器翻译等。通过提供可解释的推理机制，研究者和开发者可以更好地理解和优化大型语言模型的行为，提升其在实际应用中的可靠性和透明度。

## 📄 摘要（原文）

> Despite significant progress in transformer interpretability, an understanding of the computational mechanisms of large language models (LLMs) remains a fundamental challenge. Many approaches interpret a network's hidden representations but remain agnostic about how those representations are generated. We address this by mapping LLM inference for a given input sequence to an equivalent and interpretable linear system which reconstructs the predicted output embedding with relative error below $10^{-13}$ at double floating-point precision, requiring no additional model training. We exploit a property of transformers wherein every operation (gated activations, attention, and normalization) can be expressed as $A(x) \cdot x$, where $A(x)$ represents an input-dependent linear transform and $x$ preserves the linear pathway. To expose this linear structure, we strategically detach components of the gradient computation with respect to an input sequence, freezing the $A(x)$ terms at their values computed during inference, such that the Jacobian yields an equivalent linear mapping. This detached Jacobian of the model reconstructs the output with one linear operator per input token, which is shown for Qwen 3, Gemma 3 and Llama 3, up to Qwen 3 14B. These linear representations demonstrate that LLMs operate in extremely low-dimensional subspaces where the singular vectors can be decoded to interpretable semantic concepts. The computation for each intermediate output also has a linear equivalent, and we examine how the linear representations of individual layers and their attention and multilayer perceptron modules build predictions, and use these as steering operators to insert semantic concepts into unrelated text. Despite their global nonlinearity, LLMs can be interpreted through equivalent linear representations that reveal low-dimensional semantic structures in the next-token prediction process.

