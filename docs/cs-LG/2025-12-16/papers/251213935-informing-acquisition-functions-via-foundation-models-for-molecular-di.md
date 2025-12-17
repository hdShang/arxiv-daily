---
layout: default
title: Informing Acquisition Functions via Foundation Models for Molecular Discovery
---

# Informing Acquisition Functions via Foundation Models for Molecular Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13935" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13935</a>
  <a href="https://arxiv.org/pdf/2512.13935.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13935" onclick="toggleFavorite(this, '2512.13935', 'Informing Acquisition Functions via Foundation Models for Molecular Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Chen, Fabio Ramos, Alán Aspuru-Guzik, Florian Shkurti

**分类**: cs.LG, cs.AI, bio.QM

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于大模型的无似然贝叶斯优化方法，加速分子发现。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `贝叶斯优化` `分子发现` `大型语言模型` `化学基础模型` `无似然优化`

## 📋 核心要点

1. 传统贝叶斯优化在分子发现中面临低数据、高维度和计算成本高的挑战，限制了其性能。
2. 该论文提出一种无似然贝叶斯优化方法，直接利用大型语言模型和化学基础模型的先验知识来指导采集函数。
3. 实验结果表明，该方法在可扩展性、鲁棒性和样本效率方面均有显著提升，尤其是在LLM引导的分子发现中。

## 📝 摘要（中文）

贝叶斯优化(BO)是一种通过估计分子到其属性的映射并寻找最佳候选分子来加速分子发现的关键方法。通常，BO迭代地更新该映射的概率代理模型，并优化从模型导出的采集函数来指导分子选择。然而，其性能在数据量不足、先验知识匮乏和候选空间巨大的低数据状态下受到限制。大型语言模型(LLM)和化学基础模型提供了丰富的先验知识来增强BO，但高维特征、昂贵的上下文学习以及深度贝叶斯代理模型的计算负担阻碍了它们的充分利用。为了解决这些挑战，我们提出了一种无似然BO方法，该方法绕过显式代理建模，直接利用来自通用LLM和化学特定基础模型的先验知识来告知采集函数。我们的方法还学习分子搜索空间的树状结构划分，并使用局部采集函数，从而可以通过蒙特卡洛树搜索有效地选择候选分子。通过进一步结合基于LLM的粗粒度聚类，它通过将采集函数评估限制在具有统计学上更高属性值的聚类中，从而大大提高了对大型候选集的可扩展性。通过广泛的实验和消融研究，我们表明所提出的方法大大提高了LLM引导的分子发现中BO的可扩展性、鲁棒性和样本效率。

## 🔬 方法详解

**问题定义**：论文旨在解决分子发现中，传统贝叶斯优化方法在低数据量、高维空间和计算资源有限的情况下表现不佳的问题。现有方法依赖于构建分子属性的代理模型，但当数据不足时，代理模型的准确性会受到严重影响，导致优化效果不佳。此外，直接使用大型语言模型（LLM）的特征进行贝叶斯优化面临高维特征处理和计算负担过重的问题。

**核心思路**：论文的核心思路是绕过显式的代理模型构建，直接利用大型语言模型和化学领域基础模型提供的先验知识来指导贝叶斯优化的采集函数。通过这种方式，可以避免代理模型带来的误差累积，并充分利用预训练模型中蕴含的丰富信息。同时，论文还引入了树状结构的搜索空间划分和基于LLM的粗粒度聚类，以提高算法的可扩展性和效率。

**技术框架**：该方法主要包含以下几个阶段：1) 利用大型语言模型或化学领域基础模型提取分子特征；2) 构建分子搜索空间的树状结构划分，每个节点对应一个分子子集；3) 在每个节点上定义局部采集函数，该函数直接利用预训练模型的先验知识；4) 使用蒙特卡洛树搜索（MCTS）在树状结构上进行搜索，选择具有最高采集函数值的分子；5) 利用基于LLM的粗粒度聚类，将候选分子集划分为若干个簇，并仅在具有较高属性值的簇中进行采集函数评估。

**关键创新**：该方法最重要的创新点在于提出了无似然贝叶斯优化框架，避免了显式代理模型的构建，直接利用预训练模型的先验知识指导采集函数。此外，树状结构搜索空间划分和基于LLM的粗粒度聚类也显著提高了算法的可扩展性和效率。

**关键设计**：论文的关键设计包括：1) 采集函数的具体形式，如何将预训练模型的输出转化为采集函数值；2) 树状结构划分的具体方法，例如如何选择划分标准和划分深度；3) 基于LLM的粗粒度聚类的实现细节，例如如何选择聚类算法和簇的数量；4) 蒙特卡洛树搜索的参数设置，例如探索-利用平衡系数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13935/figures/molecules/mole1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13935/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13935/figures/toy_data/root_leaf_acqf_iter_1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在分子发现任务中显著优于传统的贝叶斯优化方法。具体而言，该方法在可扩展性、鲁棒性和样本效率方面均有显著提升。例如，在处理大规模候选分子集时，该方法能够有效地缩小搜索范围，并快速找到具有较高属性值的分子。消融实验进一步验证了各个模块的有效性。

## 🎯 应用场景

该研究成果可广泛应用于药物发现、材料设计等领域。通过利用大型语言模型和化学基础模型的先验知识，可以加速新分子或新材料的发现过程，降低研发成本，并提高研发效率。该方法尤其适用于数据稀缺或计算资源有限的场景，具有重要的实际应用价值。

## 📄 摘要（原文）

> Bayesian Optimization (BO) is a key methodology for accelerating molecular discovery by estimating the mapping from molecules to their properties while seeking the optimal candidate. Typically, BO iteratively updates a probabilistic surrogate model of this mapping and optimizes acquisition functions derived from the model to guide molecule selection. However, its performance is limited in low-data regimes with insufficient prior knowledge and vast candidate spaces. Large language models (LLMs) and chemistry foundation models offer rich priors to enhance BO, but high-dimensional features, costly in-context learning, and the computational burden of deep Bayesian surrogates hinder their full utilization. To address these challenges, we propose a likelihood-free BO method that bypasses explicit surrogate modeling and directly leverages priors from general LLMs and chemistry-specific foundation models to inform acquisition functions. Our method also learns a tree-structured partition of the molecular search space with local acquisition functions, enabling efficient candidate selection via Monte Carlo Tree Search. By further incorporating coarse-grained LLM-based clustering, it substantially improves scalability to large candidate sets by restricting acquisition function evaluations to clusters with statistically higher property values. We show through extensive experiments and ablations that the proposed method substantially improves scalability, robustness, and sample efficiency in LLM-guided BO for molecular discovery.

