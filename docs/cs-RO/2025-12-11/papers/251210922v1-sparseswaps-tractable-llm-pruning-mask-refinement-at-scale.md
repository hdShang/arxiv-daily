---
layout: default
title: SparseSwaps: Tractable LLM Pruning Mask Refinement at Scale
---

# SparseSwaps: Tractable LLM Pruning Mask Refinement at Scale

**arXiv**: [2512.10922v1](https://arxiv.org/abs/2512.10922) | [PDF](https://arxiv.org/pdf/2512.10922.pdf)

**作者**: Max Zimmer, Christophe Roux, Moritz Wagner, Deborah Hendrych, Sebastian Pokutta

---

## 💡 一句话要点

**提出SparseSwaps方法，通过高效1-swap算法在大规模LLM上优化剪枝掩码选择。**

**关键词**: `大语言模型剪枝` `掩码优化` `1-swap算法` `Gram矩阵` `GPU加速` `零样本性能`

## 📋 核心要点

1. 核心问题：LLM剪枝中掩码选择问题组合复杂，传统方法计算不可行或近似效果差。
2. 方法要点：强制每行等稀疏度，基于Gram矩阵高效计算最优1-swap，实现GPU加速和超参数自由。
3. 实验或效果：相比Wanda减少60%每层剪枝误差，提升GPT架构的困惑度和零样本准确率。

## 📄 摘要（原文）

> The resource requirements of Neural Networks can be significantly reduced through pruning -- the removal of seemingly less important parameters. However, with the rise of Large Language Models (LLMs), full retraining to recover pruning-induced performance degradation is often prohibitive and classical approaches such as global magnitude pruning are suboptimal on Transformer architectures. State-of-the-art methods hence solve a layer-wise mask selection problem, the problem of finding a pruning mask which minimizes the per-layer pruning error on a small set of calibration data. Exactly solving this problem to optimality using Integer Programming (IP) solvers is computationally infeasible due to its combinatorial nature and the size of the search space, and existing approaches therefore rely on approximations or heuristics. In this work, we demonstrate that the mask selection problem can be made drastically more tractable at LLM scale. To that end, we decouple the rows by enforcing equal sparsity levels per row. This allows us to derive optimal 1-swaps (exchanging one kept and one pruned weight) that can be computed efficiently using the Gram matrix of the calibration data. Using these observations, we propose a tractable and simple 1-swap algorithm that warm starts from any pruning mask, runs efficiently on GPUs at LLM scale, and is essentially hyperparameter-free. We demonstrate that our approach reduces per-layer pruning error by up to 60% over Wanda (Sun et al., 2023) and consistently improves perplexity and zero-shot accuracy across state-of-the-art GPT architectures.

