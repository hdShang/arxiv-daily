---
layout: default
title: Efficient Unstructured Pruning of Mamba State-Space Models for Resource-Constrained Environments
---

# Efficient Unstructured Pruning of Mamba State-Space Models for Resource-Constrained Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08299" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08299v2</a>
  <a href="https://arxiv.org/pdf/2505.08299.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08299v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08299v2', 'Efficient Unstructured Pruning of Mamba State-Space Models for Resource-Constrained Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma

**分类**: cs.LG, cs.CV

**发布日期**: 2025-05-13 (更新: 2025-09-05)

**期刊**: Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing

---

## 💡 一句话要点

**提出高效无结构剪枝框架以解决Mamba模型在资源受限环境中的部署问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

## 📋 核心要点

1. 现有的Mamba模型在资源受限环境中部署时，由于参数量庞大，面临显著的挑战。
2. 本文提出了一种无结构剪枝框架，通过结合梯度信息和权重幅度来优化模型参数，提升部署效率。
3. 实验结果表明，该方法在多个基准测试中实现了高达70%的参数减少，同时保持了超过95%的性能。
4. method_zh

## 📝 摘要（中文）

状态空间模型（SSMs），尤其是Mamba架构，已成为序列建模的强大替代方案，具有线性时间复杂度和在多种任务中具有竞争力的性能。然而，其庞大的参数量在资源受限环境中部署时面临重大挑战。本文提出了一种新颖的无结构剪枝框架，针对Mamba模型实现了高达70%的参数减少，同时保持超过95%的原始性能。我们的方法结合了三项关键创新：1）一种基于梯度的幅度剪枝技术，结合权重幅度和梯度信息识别不太重要的参数；2）逐步增加稀疏性的迭代剪枝计划，以保持模型稳定性；3）一种全局剪枝策略，优化整个模型的参数分配。通过在WikiText-103、Long Range Arena和ETT时间序列基准上的广泛实验，我们展示了显著的效率提升和最小的性能下降。

## 📄 摘要（原文）

> State-space models (SSMs), particularly the Mamba architecture, have emerged as powerful alternatives to Transformers for sequence modeling, offering linear-time complexity and competitive performance across diverse tasks. However, their large parameter counts pose significant challenges for deployment in resource-constrained environments. We propose a novel unstructured pruning framework tailored for Mamba models that achieves up to 70\% parameter reduction while retaining over 95\% of the original performance. Our approach integrates three key innovations: (1) a gradient-aware magnitude pruning technique that combines weight magnitude and gradient information to identify less critical parameters, (2) an iterative pruning schedule that gradually increases sparsity to maintain model stability, and (3) a global pruning strategy that optimizes parameter allocation across the entire model. Through extensive experiments on WikiText-103, Long Range Arena, and ETT time-series benchmarks, we demonstrate significant efficiency gains with minimal performance degradation. Our analysis of pruning effects on Mamba's components reveals critical insights into the architecture's redundancy and robustness, enabling practical deployment in resource-constrained settings while broadening Mamba's applicability.

