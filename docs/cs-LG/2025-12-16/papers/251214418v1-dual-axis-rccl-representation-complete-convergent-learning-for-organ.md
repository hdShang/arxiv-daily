---
layout: default
title: Dual-Axis RCCL: Representation-Complete Convergent Learning for Organic Chemical Space
---

# Dual-Axis RCCL: Representation-Complete Convergent Learning for Organic Chemical Space

**arXiv**: [2512.14418v1](https://arxiv.org/abs/2512.14418) | [PDF](https://arxiv.org/pdf/2512.14418.pdf)

**作者**: Dejun Hu, Zhiming Li, Jia-Rui Shen, Jia-Ning Tu, Zi-Hao Ye, Junliang Zhang

**分类**: cs.LG

**发布日期**: 2025-12-16

**备注**: 33 pages, 10 figures

---

## 💡 一句话要点

**提出双轴表示完全收敛学习策略，解决有机化学空间模型收敛与泛化难题。**

**关键词**: `化学空间建模` `表示完全性` `图神经网络` `分子表示学习` `收敛学习` `泛化能力` `数据集构建` `有机分子预测`

## 📋 核心要点

1. 核心问题：化学空间规模巨大（10^30-10^60），现有方法难以确保模型在该空间实现收敛学习，泛化能力受限。
2. 方法要点：提出双轴RCCL策略，结合局部价环境GCN编码和环/笼拓扑NBG编码，构建表示完全性框架指导数据集构建。
3. 实验或效果：开发FD25数据集，训练模型在外部基准上实现约1.0 kcal/mol MAE误差，展现强泛化能力。

## 📝 摘要（中文）

机器学习正在深刻重塑分子与材料建模，但面对化学空间的巨大规模（10^30-10^60），模型能否实现跨空间的收敛学习仍是一个开放的科学问题。我们引入了双轴表示完全收敛学习策略，该策略通过一种分子表示实现，该表示整合了基于现代价键理论的局部价环境图卷积网络编码，以及环/笼拓扑的无桥图编码，提供了化学空间覆盖的定量度量。该框架形式化了表示完全性，为构建支持大模型收敛学习的数据集建立了原则性基础。在此RCCL框架指导下，我们开发了FD25数据集，系统覆盖了13,302个局部价单元和165,726个环/笼拓扑，实现了对含H/C/N/O/F元素的有机分子的近乎完全组合覆盖。在FD25上训练的图神经网络表现出表示完全收敛学习和强大的分布外泛化能力，在外部基准测试中整体预测误差约为1.0 kcal/mol MAE。我们的结果建立了分子表示、结构完全性和模型泛化之间的定量联系，为可解释、可迁移和数据高效的分子智能奠定了基础。

## 🔬 方法详解

论文提出双轴表示完全收敛学习框架，核心方法包括：整体框架基于表示完全性概念，通过整合局部价环境和环/笼拓扑的双轴编码来量化化学空间覆盖。关键技术创新点在于结合图卷积网络编码局部价环境（基于现代价键理论）和无桥图编码环/笼拓扑，形成互补表示。与现有方法的主要区别在于，它首次形式化了表示完全性，为数据集构建提供原则性指导，确保模型能在整个化学空间实现收敛学习，而非依赖随机或经验性采样。

## 📊 实验亮点

最重要的实验结果包括：FD25数据集覆盖13,302个局部价单元和165,726个环/笼拓扑，实现近乎完全组合覆盖；训练模型在外部基准测试中整体预测误差约为1.0 kcal/mol MAE，显著优于传统方法，验证了表示完全收敛学习和强泛化能力。

## 🎯 应用场景

该研究在分子与材料建模领域具有广泛应用潜力，可用于药物发现、材料设计、催化剂开发等，通过提供可解释、可迁移的分子智能模型，提升数据效率和预测准确性，加速新分子和材料的研发进程。

## 📄 摘要（原文）

> Machine learning is profoundly reshaping molecular and materials modeling; however, given the vast scale of chemical space (10^30-10^60), it remains an open scientific question whether models can achieve convergent learning across this space. We introduce a Dual-Axis Representation-Complete Convergent Learning (RCCL) strategy, enabled by a molecular representation that integrates graph convolutional network (GCN) encoding of local valence environments, grounded in modern valence bond theory, together with no-bridge graph (NBG) encoding of ring/cage topologies, providing a quantitative measure of chemical-space coverage. This framework formalizes representation completeness, establishing a principled basis for constructing datasets that support convergent learning for large models. Guided by this RCCL framework, we develop the FD25 dataset, systematically covering 13,302 local valence units and 165,726 ring/cage topologies, achieving near-complete combinatorial coverage of organic molecules with H/C/N/O/F elements. Graph neural networks trained on FD25 exhibit representation-complete convergent learning and strong out-of-distribution generalization, with an overall prediction error of approximately 1.0 kcal/mol MAE across external benchmarks. Our results establish a quantitative link between molecular representation, structural completeness, and model generalization, providing a foundation for interpretable, transferable, and data-efficient molecular intelligence.

