---
layout: default
title: Elastic Weight Consolidation for Knowledge Graph Continual Learning: An Empirical Evaluation
---

# Elastic Weight Consolidation for Knowledge Graph Continual Learning: An Empirical Evaluation

**arXiv**: [2512.01890v1](https://arxiv.org/abs/2512.01890) | [PDF](https://arxiv.org/pdf/2512.01890.pdf)

**作者**: Gaganpreet Jhajj, Fuhua Lin

---

## 💡 一句话要点

**评估弹性权重巩固在知识图谱持续学习中缓解灾难性遗忘的效果**

**关键词**: `知识图谱持续学习` `灾难性遗忘` `弹性权重巩固` `链接预测` `TransE嵌入` `FB15k-237`

## 📋 核心要点

1. 核心问题：知识图谱持续更新时，神经嵌入模型面临灾难性遗忘。
2. 方法要点：采用弹性权重巩固正则化方法，基于TransE嵌入在FB15k-237数据集上评估。
3. 实验或效果：EWC将遗忘率从12.62%降至6.85%，任务划分策略影响遗忘程度。

## 📄 摘要（原文）

> Knowledge graphs (KGs) require continual updates as new information emerges, but neural embedding models suffer from catastrophic forgetting when learning new tasks sequentially. We evaluate Elastic Weight Consolidation (EWC), a regularization-based continual learning method, on KG link prediction using TransE embeddings on FB15k-237. Across multiple experiments with five random seeds, we find that EWC reduces catastrophic forgetting from 12.62% to 6.85%, a 45.7% reduction compared to naive sequential training. We observe that the task partitioning strategy affects the magnitude of forgetting: relation-based partitioning (grouping triples by relation type) exhibits 9.8 percentage points higher forgetting than randomly partitioned tasks (12.62% vs 2.81%), suggesting that task construction influences evaluation outcomes. While focused on a single embedding model and dataset, our results demonstrate that EWC effectively mitigates catastrophic forgetting in KG continual learning and highlight the importance of evaluation protocol design.

