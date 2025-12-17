---
layout: default
title: TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation
---

# TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14358" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14358</a>
  <a href="https://arxiv.org/pdf/2512.14358.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14358" onclick="toggleFavorite(this, '2512.14358', 'TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qizhi Wang

**分类**: cs.AI, cs.DB

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**TiCard：一种可部署的、仅使用EXPLAIN信息的基数估计残差学习框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基数估计` `查询优化` `残差学习` `数据库系统` `AI4DB`

## 📋 核心要点

1. 现有基数估计器在捕获复杂相关性方面存在不足，而学习型估计器部署成本高，需要侵入式集成。
2. TiCard通过学习残差校正来增强原生估计器，仅使用EXPLAIN信息，降低了部署难度和侵入性。
3. 实验表明，TiCard在TPCH和Join Order Benchmark上显著提高了尾部精度，P90和P99 Q-error均大幅降低。

## 📝 摘要（中文）

基数估计是基于代价的查询优化的关键瓶颈，但可部署的改进仍然困难：传统估计器会遗漏相关性，而学习型估计器通常需要特定于工作负载的训练流程和对优化器的侵入式集成。本文提出了TiCard，一个低侵入性的、基于校正的框架，它增强（而不是替换）数据库的原生估计器。TiCard使用仅EXPLAIN的特征学习乘法残差校正，并且仅使用EXPLAIN ANALYZE进行离线标签生成。我们研究了两种实际的实例化：（i）用于亚毫秒级推理的梯度提升回归器，以及（ii）TabPFN，一种通过刷新小型参考集而无需梯度重新训练的上下文表格基础模型。在使用TPCH和Join Order Benchmark的TiDB上，在低跟踪设置（总共263次执行；157次用于学习）中，TiCard显着提高了算子级别的尾部精度：P90 Q-error从312.85（原生）降至13.69（TiCard-GBR），P99从37,974.37降至3,416.50（TiCard-TabPFN），而仅连接策略保持了近乎完美的中间值行为。我们将TiCard定位为专注于可部署性的AI4DB构建块：明确的范围、保守的集成策略以及从离线校正到优化器内使用的集成路线图。

## 🔬 方法详解

**问题定义**：基数估计是查询优化的关键，准确的基数估计能够帮助优化器选择最佳的查询执行计划。然而，传统的基数估计方法难以捕捉复杂的数据相关性，导致估计误差较大。而现有的学习型基数估计器通常需要大量的训练数据和复杂的训练流程，并且需要深入集成到数据库优化器中，部署成本较高。

**核心思路**：TiCard的核心思路是利用残差学习的思想，通过学习原生估计器预测结果的残差（即误差）来进行校正。它不直接替换原生估计器，而是作为其补充，通过学习一个校正模型来修正原生估计器的偏差。这种方法降低了对原生估计器的依赖，并且更容易部署。

**技术框架**：TiCard的整体框架包括以下几个主要步骤：1) 使用数据库的EXPLAIN功能提取查询计划的特征；2) 使用EXPLAIN ANALYZE功能获取查询计划的真实基数（作为标签）；3) 训练一个残差校正模型，该模型以EXPLAIN特征作为输入，以原生估计器的预测误差作为标签；4) 在线查询时，首先使用原生估计器进行基数估计，然后使用训练好的残差校正模型对估计结果进行校正。

**关键创新**：TiCard的关键创新在于其低侵入性和可部署性。它仅使用EXPLAIN信息进行特征提取和训练，无需修改数据库内核。此外，TiCard采用了残差学习的方法，使得校正模型可以专注于学习原生估计器的误差，从而提高了校正的精度。同时，论文探索了两种不同的校正模型：梯度提升回归器（GBR）和TabPFN，以适应不同的性能需求。

**关键设计**：TiCard的关键设计包括：1) 使用EXPLAIN信息作为特征，避免了对数据库内部结构的依赖；2) 使用乘法残差校正，即校正模型预测的是一个比例因子，用于乘以原生估计器的预测结果；3) 探索了两种不同的校正模型：GBR用于亚毫秒级推理，TabPFN用于在少量数据下快速适应；4) 设计了一个Join-Only策略，只对连接操作的基数进行校正，以避免对其他操作的基数估计产生负面影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14358/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14358/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14358/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，TiCard在TiDB数据库上，使用TPCH和Join Order Benchmark数据集，在低跟踪设置下（仅使用263次执行，其中157次用于学习），显著提高了算子级别的尾部精度。具体来说，使用梯度提升回归器（TiCard-GBR）时，P90 Q-error从原生估计器的312.85降至13.69；使用TabPFN（TiCard-TabPFN）时，P99 Q-error从37,974.37降至3,416.50。Join-Only策略还保证了近乎完美的中间值行为。

## 🎯 应用场景

TiCard可以应用于各种需要进行查询优化的数据库系统中，尤其适用于那些难以进行深度定制和修改的数据库。通过低侵入性的方式提高基数估计的准确性，从而改善查询性能，降低数据库运维成本。未来，TiCard可以进一步扩展到支持更复杂的查询类型和数据分布，并与其他AI4DB技术相结合，构建更智能的数据库系统。

## 📄 摘要（原文）

> Cardinality estimation is a key bottleneck for cost-based query optimization, yet deployable improvements remain difficult: classical estimators miss correlations, while learned estimators often require workload-specific training pipelines and invasive integration into the optimizer. This paper presents TiCard, a low intrusion, correction-based framework that augments (rather than replaces) a database's native estimator. TiCard learns multiplicative residual corrections using EXPLAIN-only features, and uses EXPLAIN ANALYZE only for offline labels. We study two practical instantiations: (i) a Gradient Boosting Regressor for sub-millisecond inference, and (ii) TabPFN, an in-context tabular foundation model that adapts by refreshing a small reference set without gradient retraining. On TiDB with TPCH and the Join Order Benchmark, in a low-trace setting (263 executions total; 157 used for learning), TiCard improves operator-level tail accuracy substantially: P90 Q-error drops from 312.85 (native) to 13.69 (TiCard-GBR), and P99 drops from 37,974.37 to 3,416.50 (TiCard-TabPFN), while a join-only policy preserves near-perfect median behavior. We position TiCard as an AI4DB building block focused on deployability: explicit scope, conservative integration policies, and an integration roadmap from offline correction to in-optimizer use.

