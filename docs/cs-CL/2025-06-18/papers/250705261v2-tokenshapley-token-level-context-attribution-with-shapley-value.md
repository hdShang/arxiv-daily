---
layout: default
title: "TokenShapley: Token Level Context Attribution with Shapley Value"
---

# TokenShapley: Token Level Context Attribution with Shapley Value

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.05261" class="toolbar-btn" target="_blank">📄 arXiv: 2507.05261v2</a>
  <a href="https://arxiv.org/pdf/2507.05261.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.05261v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.05261v2', 'TokenShapley: Token Level Context Attribution with Shapley Value')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingtai Xiao, Yuqing Zhu, Sirat Samyoun, Wanrong Zhang, Jiachen T. Wang, Jian Du

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-18 (更新: 2025-07-09)

---

## 💡 一句话要点

**提出TokenShapley以解决LLM生成响应的关键词归因问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `归因方法` `Shapley值` `KNN检索` `细粒度分析` `自然语言处理` `信息检索`

## 📋 核心要点

1. 现有的句子级归因方法无法满足用户对特定关键词的归因需求，导致在验证生成内容时存在挑战。
2. TokenShapley通过结合Shapley值和KNN检索技术，提供了一种令牌级别的细粒度归因方法，克服了现有方法的不足。
3. 在四个基准测试中，TokenShapley的准确率比最先进的基线提高了11-23%，显示出显著的性能提升。

## 📝 摘要（中文）

大型语言模型（LLMs）在上下文学习中展现出强大的能力，但验证其生成响应的正确性仍然是一项挑战。以往的研究主要集中在句子级别的归因，但在用户需要对特定关键词（如数字、年份或名称）进行归因时，这些方法显得不足。为了解决这一局限性，本文提出了TokenShapley，这是一种新颖的基于Shapley值的令牌级归因方法，结合了KNN检索技术。通过利用预计算的数据存储库进行上下文检索，并计算Shapley值来量化令牌的重要性，TokenShapley提供了一种细粒度的数据归因方法。对四个基准的广泛评估表明，TokenShapley在令牌级归因方面优于现有的最先进基线，准确率提高了11-23%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型生成响应时，用户对特定关键词（如数字、年份、名称等）的归因需求。现有的句子级归因方法无法提供足够的细粒度信息，导致在验证生成内容的正确性时面临困难。

**核心思路**：TokenShapley的核心思路是结合Shapley值的归因方法与KNN检索技术，通过量化每个令牌的重要性来实现细粒度的归因。这种设计使得模型能够更准确地识别和解释生成内容中的关键元素。

**技术框架**：TokenShapley的整体架构包括两个主要模块：首先是预计算的数据存储库，用于上下文检索；其次是基于Shapley值的计算模块，用于量化令牌的重要性。这两个模块协同工作，实现了高效的归因过程。

**关键创新**：TokenShapley的主要创新在于其结合了Shapley值和KNN检索的双重机制，使得令牌级别的归因不仅更加精确，而且能够处理复杂的上下文信息。这与传统的句子级归因方法形成了鲜明对比。

**关键设计**：在设计中，TokenShapley使用了优化的KNN检索算法，以提高上下文检索的效率。同时，Shapley值的计算采用了高效的近似算法，以确保在大规模数据集上的可行性和准确性。

## 📊 实验亮点

TokenShapley在四个基准测试中表现出色，相较于最先进的基线，其准确率提高了11-23%。这一显著的性能提升证明了其在令牌级归因任务中的有效性，为用户提供了更为可靠的内容验证工具。

## 🎯 应用场景

TokenShapley的研究成果在多个领域具有潜在应用价值，尤其是在自然语言处理、信息检索和人机交互等领域。通过提供更为细致的归因机制，用户能够更好地理解和验证模型生成的内容，从而提升信任度和使用体验。未来，该方法还可能扩展到其他类型的生成模型，推动相关技术的发展。

## 📄 摘要（原文）

> Large language models (LLMs) demonstrate strong capabilities in in-context learning, but verifying the correctness of their generated responses remains a challenge. Prior work has explored attribution at the sentence level, but these methods fall short when users seek attribution for specific keywords within the response, such as numbers, years, or names. To address this limitation, we propose TokenShapley, a novel token-level attribution method that combines Shapley value-based data attribution with KNN-based retrieval techniques inspired by recent advances in KNN-augmented LLMs. By leveraging a precomputed datastore for contextual retrieval and computing Shapley values to quantify token importance, TokenShapley provides a fine-grained data attribution approach. Extensive evaluations on four benchmarks show that TokenShapley outperforms state-of-the-art baselines in token-level attribution, achieving an 11-23% improvement in accuracy.

