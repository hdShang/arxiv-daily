---
layout: default
title: "TabArena: A Living Benchmark for Machine Learning on Tabular Data"
---

# TabArena: A Living Benchmark for Machine Learning on Tabular Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16791" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16791v4</a>
  <a href="https://arxiv.org/pdf/2506.16791.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16791v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16791v4', 'TabArena: A Living Benchmark for Machine Learning on Tabular Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nick Erickson, Lennart Purucker, Andrej Tschalzev, David Holzmüller, Prateek Mutalik Desai, David Salinas, Frank Hutter

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-20 (更新: 2025-11-03)

**备注**: Accepted (spotlight) at NeurIPS 2025 Datasets and Benchmarks Track. v4: fixed links in comments. v3: NeurIPS camera-ready version. v2: fixed author list. 51 pages. Code available at https://tabarena.ai/code and examples at https://tabarena.ai/code-examples and dataset curation at https://tabarena.ai/data-tabular-ml-iid-study and https://tabarena.ai/dataset-curation

---

## 💡 一句话要点

**提出TabArena以解决静态基准测试问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格数据` `基准测试` `动态维护` `深度学习` `模型集成` `机器学习` `超参数优化`

## 📋 核心要点

1. 现有的基准测试方法静态且无法及时更新，导致无法反映最新的模型性能和技术进展。
2. TabArena通过手动策划数据集和模型，建立了一个动态维护的基准测试系统，提供实时更新和评估。
3. 实验结果显示，集成方法显著提升了模型性能，深度学习在较大时间预算下表现优异，基础模型在小数据集上表现突出。

## 📝 摘要（中文）

随着深度学习和基础模型在表格数据上的日益普及，标准化和可靠基准的需求愈发迫切。然而，现有基准测试往往是静态的，无法及时更新。为此，本文提出了TabArena，这是首个持续维护的动态表格基准测试系统。通过手动策划代表性数据集和模型，进行大规模基准测试，建立公共排行榜，并组建经验丰富的维护团队，TabArena为研究者提供了一个可持续的评估平台。研究表明，验证方法和超参数配置的集成对模型性能有显著影响，深度学习方法在较大时间预算下表现出色，而基础模型在小数据集上表现优异。最终，模型间的集成推动了表格机器学习的最新进展。

## 🔬 方法详解

**问题定义**：现有的表格数据基准测试方法往往是静态的，无法及时反映模型的最新性能和技术进展，导致研究者无法获得准确的评估结果。

**核心思路**：TabArena的核心思路是创建一个持续维护的动态基准测试系统，通过手动策划数据集和模型，确保基准测试的实时性和可靠性。

**技术框架**：TabArena的整体架构包括数据集策划、模型选择、大规模基准测试和公共排行榜的建立。系统由经验丰富的维护团队负责，确保数据和模型的质量。

**关键创新**：TabArena的最大创新在于其动态维护的特性，能够根据最新的研究进展和模型更新及时调整基准测试内容，这与传统静态基准测试形成鲜明对比。

**关键设计**：在设计中，研究者关注验证方法和超参数配置的集成，确保模型在评估时能够发挥最佳性能，同时也指出了深度学习模型在集成时可能出现的过拟合问题。

## 📊 实验亮点

实验结果表明，集成方法显著提升了模型性能，深度学习方法在较大时间预算下与梯度提升树竞争，而基础模型在小数据集上表现优异。通过模型间的集成，TabArena推动了表格机器学习的最新进展，显示出更高的性能提升幅度。

## 🎯 应用场景

TabArena的研究成果可广泛应用于机器学习领域，尤其是在表格数据的处理和分析中。其动态基准测试系统能够为研究者提供实时的模型评估，促进新技术的快速迭代和应用，推动整个行业的发展。

## 📄 摘要（原文）

> With the growing popularity of deep learning and foundation models for tabular data, the need for standardized and reliable benchmarks is higher than ever. However, current benchmarks are static. Their design is not updated even if flaws are discovered, model versions are updated, or new models are released. To address this, we introduce TabArena, the first continuously maintained living tabular benchmarking system. To launch TabArena, we manually curate a representative collection of datasets and well-implemented models, conduct a large-scale benchmarking study to initialize a public leaderboard, and assemble a team of experienced maintainers. Our results highlight the influence of validation method and ensembling of hyperparameter configurations to benchmark models at their full potential. While gradient-boosted trees are still strong contenders on practical tabular datasets, we observe that deep learning methods have caught up under larger time budgets with ensembling. At the same time, foundation models excel on smaller datasets. Finally, we show that ensembles across models advance the state-of-the-art in tabular machine learning. We observe that some deep learning models are overrepresented in cross-model ensembles due to validation set overfitting, and we encourage model developers to address this issue. We launch TabArena with a public leaderboard, reproducible code, and maintenance protocols to create a living benchmark available at https://tabarena.ai.

