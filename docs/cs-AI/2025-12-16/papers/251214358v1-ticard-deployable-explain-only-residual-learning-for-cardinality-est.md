---
layout: default
title: TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation
---

# TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation

**arXiv**: [2512.14358v1](https://arxiv.org/abs/2512.14358) | [PDF](https://arxiv.org/pdf/2512.14358.pdf)

**作者**: Qizhi Wang

**分类**: cs.AI, cs.DB

**发布日期**: 2025-12-16

**备注**: 16 pages(/wo references), 4 figures, 10 tables

---

## 💡 一句话要点

**提出TiCard框架，通过可部署的仅解释残差学习解决数据库基数估计的部署难题**

**关键词**: `基数估计` `查询优化` `残差学习` `可部署AI` `数据库增强` `梯度提升回归` `表格基础模型` `AI4DB`

## 📋 核心要点

1. 核心问题：基数估计是查询优化的瓶颈，经典方法忽略相关性，学习型方法部署困难，需要侵入式集成。
2. 方法要点：提出TiCard框架，使用仅解释特征学习残差校正，增强而非替换原生估计器，实现低侵入性部署。
3. 实验或效果：在TiDB上测试，TiCard显著降低尾部Q误差，P90从312.85降至13.69，P99从37,974.37降至3,416.50。

## 📝 摘要（中文）

基数估计是基于成本的查询优化的关键瓶颈，但可部署的改进仍然困难：经典估计器忽略了相关性，而学习型估计器通常需要特定于工作负载的训练流程并侵入性地集成到优化器中。本文提出了TiCard，一个低侵入性、基于校正的框架，它增强（而非替换）数据库的原生估计器。TiCard使用仅解释特征学习乘法残差校正，并仅使用解释分析进行离线标签。我们研究了两种实际实例化：（i）用于亚毫秒推理的梯度提升回归器，以及（ii）TabPFN，一种上下文表格基础模型，通过刷新小型参考集而无需梯度重新训练来适应。在TiDB上使用TPCH和连接顺序基准测试，在低跟踪设置中（总共263次执行；157次用于学习），TiCard显著提高了操作员级别的尾部准确性：P90 Q误差从312.85（原生）降至13.69（TiCard-GBR），P99从37,974.37降至3,416.50（TiCard-TabPFN），而仅连接策略保持了近乎完美的中位数行为。我们将TiCard定位为专注于可部署性的AI4DB构建块：明确的范围、保守的集成策略以及从离线校正到优化器内使用的集成路线图。

## 🔬 方法详解

TiCard是一个基于校正的框架，整体框架包括使用EXPLAIN-only特征（如查询计划结构）学习乘法残差，以增强数据库原生估计器。关键技术创新点在于仅依赖EXPLAIN特征进行推理，避免侵入优化器，并使用EXPLAIN ANALYZE进行离线标签生成。与现有方法的主要区别在于：它不替换原生估计器，而是作为校正层，支持两种实例化——梯度提升回归器（GBR）用于快速推理，以及TabPFN基础模型用于上下文适应，无需重新训练。

## 📊 实验亮点

在低跟踪设置下，TiCard显著改善尾部准确性：P90 Q误差从原生312.85降至13.69（TiCard-GBR），P99从37,974.37降至3,416.50（TiCard-TabPFN），同时保持近乎完美的中位数行为，验证了框架的有效性和可部署性。

## 🎯 应用场景

该研究应用于数据库管理系统中的查询优化，特别是基数估计场景，可提升TPCH、Join Order Benchmark等基准测试的性能，实际价值在于为AI4DB提供可部署的构建块，支持从离线校正逐步集成到在线优化器，降低部署门槛。

## 📄 摘要（原文）

> Cardinality estimation is a key bottleneck for cost-based query optimization, yet deployable improvements remain difficult: classical estimators miss correlations, while learned estimators often require workload-specific training pipelines and invasive integration into the optimizer. This paper presents TiCard, a low intrusion, correction-based framework that augments (rather than replaces) a database's native estimator. TiCard learns multiplicative residual corrections using EXPLAIN-only features, and uses EXPLAIN ANALYZE only for offline labels. We study two practical instantiations: (i) a Gradient Boosting Regressor for sub-millisecond inference, and (ii) TabPFN, an in-context tabular foundation model that adapts by refreshing a small reference set without gradient retraining. On TiDB with TPCH and the Join Order Benchmark, in a low-trace setting (263 executions total; 157 used for learning), TiCard improves operator-level tail accuracy substantially: P90 Q-error drops from 312.85 (native) to 13.69 (TiCard-GBR), and P99 drops from 37,974.37 to 3,416.50 (TiCard-TabPFN), while a join-only policy preserves near-perfect median behavior. We position TiCard as an AI4DB building block focused on deployability: explicit scope, conservative integration policies, and an integration roadmap from offline correction to in-optimizer use.

