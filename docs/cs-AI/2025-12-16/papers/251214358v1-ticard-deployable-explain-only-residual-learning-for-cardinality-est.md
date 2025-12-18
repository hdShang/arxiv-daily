---
layout: default
title: TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation
---

# TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14358" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14358v1</a>
  <a href="https://arxiv.org/pdf/2512.14358.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14358v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14358v1', 'TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qizhi Wang

**分类**: cs.AI, cs.DB

**发布日期**: 2025-12-16

**备注**: 16 pages(/wo references), 4 figures, 10 tables

---

## 💡 一句话要点

**TiCard：一种可部署的、仅使用EXPLAIN信息的基数估计残差学习框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基数估计` `查询优化` `残差学习` `EXPLAIN信息` `可部署性`

## 📋 核心要点

1. 传统基数估计器缺乏对数据相关性的建模能力，而学习型估计器部署复杂，需要大量特定工作负载的训练。
2. TiCard通过学习原生估计器的残差校正，而非完全替代，降低了侵入性，并利用EXPLAIN信息进行特征提取。
3. 实验表明，TiCard在低跟踪设置下显著提升了尾部查询的基数估计精度，P90和P99 Q-error均大幅降低。

## 📝 摘要（中文）

基数估计是基于代价的查询优化的关键瓶颈，但可部署的改进仍然困难：传统估计器会遗漏相关性，而学习型估计器通常需要特定于工作负载的训练流程以及对优化器的侵入式集成。本文提出了TiCard，一个低侵入性的、基于校正的框架，它增强（而不是替换）数据库的原生估计器。TiCard使用仅EXPLAIN的特征学习乘法残差校正，并且仅使用EXPLAIN ANALYZE进行离线标签生成。我们研究了两个实际的实例化：（i）用于亚毫秒级推理的梯度提升回归器，以及（ii）TabPFN，一种通过刷新小型参考集而无需梯度重新训练的上下文表格基础模型。在使用TPCH和Join Order Benchmark的TiDB上，在低跟踪设置（总共263次执行；157次用于学习）中，TiCard显着提高了算子级别的尾部精度：P90 Q-error从312.85（原生）降至13.69（TiCard-GBR），P99从37,974.37降至3,416.50（TiCard-TabPFN），而仅连接策略保留了近乎完美的中间值行为。我们将TiCard定位为专注于可部署性的AI4DB构建块：明确的范围、保守的集成策略以及从离线校正到优化器内使用的集成路线图。

## 🔬 方法详解

**问题定义**：基数估计是数据库查询优化的核心环节，其准确性直接影响查询计划的优劣。现有的基数估计方法，如传统统计方法，难以捕捉复杂的数据相关性，导致估计偏差较大。而学习型基数估计器虽然精度较高，但通常需要针对特定工作负载进行训练，部署成本高昂，且与现有数据库系统的集成存在挑战。

**核心思路**：TiCard的核心思路是“校正”而非“替代”。它不直接预测基数，而是学习原生估计器的残差，即预测原生估计器与真实基数之间的差异。这种方法降低了学习难度，并允许TiCard在不完全取代原生估计器的情况下提升性能。同时，TiCard专注于可部署性，采用低侵入性的集成方式。

**技术框架**：TiCard的整体框架包括以下几个主要阶段：1) 使用EXPLAIN语句提取查询计划的特征；2) 使用EXPLAIN ANALYZE语句获取真实基数作为标签；3) 训练残差校正模型，学习EXPLAIN特征与基数残差之间的映射关系；4) 在线查询时，首先使用原生估计器进行基数估计，然后使用训练好的残差校正模型进行校正，得到最终的基数估计结果。TiCard支持多种残差校正模型，包括梯度提升回归器（GBR）和TabPFN。

**关键创新**：TiCard的关键创新在于其“EXPLAIN-only”的特征提取方式和“residual learning”的校正策略。通过仅使用EXPLAIN语句获取特征，TiCard避免了对数据库内部数据结构的直接访问，降低了侵入性。通过学习残差，TiCard能够利用原生估计器的先验知识，并专注于学习难以建模的复杂相关性。

**关键设计**：TiCard的关键设计包括：1) 特征工程：选择与基数估计相关的EXPLAIN信息作为特征，例如算子类型、输入大小等；2) 模型选择：根据实际需求选择合适的残差校正模型，例如GBR适用于需要高精度和低延迟的场景，而TabPFN适用于需要快速适应新工作负载的场景；3) 训练策略：采用离线训练的方式，使用EXPLAIN ANALYZE语句获取的真实基数作为标签，训练残差校正模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14358v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14358v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14358v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，TiCard在TPCH和Join Order Benchmark上显著提高了基数估计的准确性。在低跟踪设置下，TiCard-GBR将P90 Q-error从原生估计器的312.85降低到13.69，TiCard-TabPFN将P99 Q-error从37,974.37降低到3,416.50。这些结果表明，TiCard能够有效地校正原生估计器的偏差，并显著提升尾部查询的性能。

## 🎯 应用场景

TiCard可应用于各种数据库系统中，提升查询优化器的性能。通过提高基数估计的准确性，TiCard可以帮助优化器选择更优的查询计划，从而缩短查询执行时间，提高数据库系统的整体性能。此外，TiCard的低侵入性设计使其易于部署和集成，降低了维护成本。未来，TiCard可以进一步扩展到支持更复杂的查询和数据类型，并与其他AI4DB技术相结合，构建更智能的数据库系统。

## 📄 摘要（原文）

> Cardinality estimation is a key bottleneck for cost-based query optimization, yet deployable improvements remain difficult: classical estimators miss correlations, while learned estimators often require workload-specific training pipelines and invasive integration into the optimizer. This paper presents TiCard, a low intrusion, correction-based framework that augments (rather than replaces) a database's native estimator. TiCard learns multiplicative residual corrections using EXPLAIN-only features, and uses EXPLAIN ANALYZE only for offline labels. We study two practical instantiations: (i) a Gradient Boosting Regressor for sub-millisecond inference, and (ii) TabPFN, an in-context tabular foundation model that adapts by refreshing a small reference set without gradient retraining. On TiDB with TPCH and the Join Order Benchmark, in a low-trace setting (263 executions total; 157 used for learning), TiCard improves operator-level tail accuracy substantially: P90 Q-error drops from 312.85 (native) to 13.69 (TiCard-GBR), and P99 drops from 37,974.37 to 3,416.50 (TiCard-TabPFN), while a join-only policy preserves near-perfect median behavior. We position TiCard as an AI4DB building block focused on deployability: explicit scope, conservative integration policies, and an integration roadmap from offline correction to in-optimizer use.

