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

**提出TiCard框架，通过可部署的仅解释残差学习来增强数据库基数估计，解决传统方法缺失相关性和学习型方法部署困难的问题。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `基数估计` `查询优化` `残差学习` `可部署AI` `数据库增强` `梯度提升回归器` `表格基础模型` `低侵入集成`

## 📋 核心要点

1. 核心问题：传统基数估计器忽略数据相关性，而学习型方法通常需要复杂训练流程和侵入式集成，导致部署困难。
2. 方法要点：TiCard框架通过仅解释特征学习乘法残差校正，低侵入地增强数据库原生估计器，无需替换现有系统。
3. 实验或效果：在低跟踪设置下，TiCard显著降低尾部Q误差，如P90从312.85降至13.69，同时保持中位数准确性。

## 📝 摘要（中文）

基数估计是基于成本的查询优化的关键瓶颈，但可部署的改进仍然困难：传统估计器缺失相关性，而学习型估计器通常需要特定工作负载的训练流程和侵入式集成到优化器中。本文提出TiCard，一个低侵入、基于校正的框架，用于增强（而非替换）数据库的原生估计器。TiCard使用仅解释特征学习乘法残差校正，并仅使用解释分析进行离线标签。我们研究了两种实际实例化：（i）梯度提升回归器用于亚毫秒级推理，和（ii）TabPFN，一种上下文表格基础模型，通过刷新小参考集而无需梯度重新训练来适应。在TiDB上使用TPCH和连接顺序基准测试，在低跟踪设置中（总共263次执行；157次用于学习），TiCard显著提高了操作员级尾部准确性：P90 Q误差从312.85（原生）降至13.69（TiCard-GBR），P99从37,974.37降至3,416.50（TiCard-TabPFN），而仅连接策略保持了近乎完美的中位数行为。我们将TiCard定位为专注于可部署性的AI4DB构建块：明确的范围、保守的集成策略，以及从离线校正到优化器内使用的集成路线图。

## 🔬 方法详解

TiCard是一个基于校正的框架，整体上通过仅解释特征（如查询计划结构）学习乘法残差来增强数据库原生基数估计器。关键技术创新包括：使用EXPLAIN-only特征避免运行时数据访问，仅依赖EXPLAIN ANALYZE进行离线标签生成，以及提供两种实例化——梯度提升回归器（GBR）用于快速推理和TabPFN基础模型用于上下文适应。与现有方法的主要区别在于其低侵入性：它不替换原生估计器，而是作为校正层，通过保守集成策略（如仅连接策略）减少对优化器的干扰，并支持从离线到在线集成的路线图。

## 📊 实验亮点

在TiDB的TPCH和Join Order Benchmark测试中，TiCard在低跟踪设置（仅157次学习执行）下显著提升尾部准确性：P90 Q误差从原生312.85降至13.69（TiCard-GBR），P99从37,974.37降至3,416.50（TiCard-TabPFN），同时仅连接策略保持中位数Q误差接近1，展示了高效部署潜力。

## 🎯 应用场景

该研究主要应用于数据库查询优化领域，特别是基于成本的查询优化器，如TiDB等关系型数据库系统。潜在价值在于提供可部署的AI增强方案，通过低侵入方式提升基数估计准确性，减少查询执行时间，适用于需要高效数据处理的企业级应用和云数据库服务。

## 📄 摘要（原文）

> Cardinality estimation is a key bottleneck for cost-based query optimization, yet deployable improvements remain difficult: classical estimators miss correlations, while learned estimators often require workload-specific training pipelines and invasive integration into the optimizer. This paper presents TiCard, a low intrusion, correction-based framework that augments (rather than replaces) a database's native estimator. TiCard learns multiplicative residual corrections using EXPLAIN-only features, and uses EXPLAIN ANALYZE only for offline labels. We study two practical instantiations: (i) a Gradient Boosting Regressor for sub-millisecond inference, and (ii) TabPFN, an in-context tabular foundation model that adapts by refreshing a small reference set without gradient retraining. On TiDB with TPCH and the Join Order Benchmark, in a low-trace setting (263 executions total; 157 used for learning), TiCard improves operator-level tail accuracy substantially: P90 Q-error drops from 312.85 (native) to 13.69 (TiCard-GBR), and P99 drops from 37,974.37 to 3,416.50 (TiCard-TabPFN), while a join-only policy preserves near-perfect median behavior. We position TiCard as an AI4DB building block focused on deployability: explicit scope, conservative integration policies, and an integration roadmap from offline correction to in-optimizer use.

