---
layout: default
title: "CE-Bench: Towards a Reliable Contrastive Evaluation Benchmark of Interpretability of Sparse Autoencoders"
---

# CE-Bench: Towards a Reliable Contrastive Evaluation Benchmark of Interpretability of Sparse Autoencoders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00691" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00691v2</a>
  <a href="https://arxiv.org/pdf/2509.00691.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00691v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00691v2', 'CE-Bench: Towards a Reliable Contrastive Evaluation Benchmark of Interpretability of Sparse Autoencoders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alex Gulko, Yusen Peng, Sachin Kumar

**分类**: cs.CL

**发布日期**: 2025-08-31 (更新: 2025-09-27)

---

## 💡 一句话要点

**提出CE-Bench以解决稀疏自编码器可解释性评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏自编码器` `可解释性评估` `对比学习` `机器学习` `自然语言处理`

## 📋 核心要点

1. 现有的稀疏自编码器评估方法大多依赖外部大型语言模型，限制了其独立性和可靠性。
2. 本文提出CE-Bench，一个基于对比故事对的数据集，旨在提供轻量且可靠的稀疏自编码器可解释性评估。
3. 实验结果显示，CE-Bench在可解释性评估上与现有基准高度一致，且无需外部评判，提升了评估的独立性。

## 📝 摘要（中文）

稀疏自编码器（SAEs）是一种有前景的方法，用于揭示大型语言模型（LLMs）中的可解释特征。尽管现有多种自动评估方法，但大多数依赖于外部LLM。本文提出了CE-Bench，一个新颖且轻量的稀疏自编码器对比评估基准，基于精心策划的对比故事对数据集。我们进行了全面的评估研究，以验证我们方法的有效性。结果表明，CE-Bench可靠地测量稀疏自编码器的可解释性，并与现有基准良好对齐，无需外部LLM评判，且与SAEBench的结果达到超过70%的斯皮尔曼相关性。官方实现和评估数据集已开源并公开可用。

## 🔬 方法详解

**问题定义**：本文旨在解决稀疏自编码器可解释性评估中对外部大型语言模型的依赖问题。现有方法的痛点在于评估的可靠性和独立性不足。

**核心思路**：CE-Bench通过构建一个基于对比故事对的数据集，提供了一种轻量级的评估框架，旨在独立于外部模型进行可解释性评估。

**技术框架**：CE-Bench的整体架构包括数据集构建、对比评估方法和结果分析三个主要模块。首先，构建对比故事对以形成评估基础；其次，设计评估方法以量化可解释性；最后，进行结果分析以验证评估的有效性。

**关键创新**：CE-Bench的核心创新在于其不依赖外部大型语言模型进行评估，提供了一种新的评估标准，且与现有基准（如SAEBench）结果高度一致。

**关键设计**：在设计中，CE-Bench采用了精心策划的对比故事对，并通过斯皮尔曼相关性来量化评估结果，确保了评估的可靠性和有效性。

## 📊 实验亮点

实验结果表明，CE-Bench在可解释性评估上与SAEBench的结果达到了超过70%的斯皮尔曼相关性，显示出其评估方法的有效性和可靠性。该方法的提出为稀疏自编码器的评估提供了新的思路，具有重要的学术价值。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器学习模型的可解释性研究以及相关领域的模型评估。CE-Bench的设计可以为研究人员提供一种新的评估工具，帮助他们更好地理解和优化稀疏自编码器的可解释性，进而推动相关技术的发展。

## 📄 摘要（原文）

> Sparse autoencoders (SAEs) are a promising approach for uncovering interpretable features in large language models (LLMs). While several automated evaluation methods exist for SAEs, most rely on external LLMs. In this work, we introduce CE-Bench, a novel and lightweight contrastive evaluation benchmark for sparse autoencoders, built on a curated dataset of contrastive story pairs. We conduct comprehensive evaluation studies to validate the effectiveness of our approach. Our results show that CE-Bench reliably measures the interpretability of sparse autoencoders and aligns well with existing benchmarks without requiring an external LLM judge, achieving over 70% Spearman correlation with results in SAEBench. The official implementation and evaluation dataset are open-sourced and publicly available.

