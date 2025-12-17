---
layout: default
title: Transformers for Tabular Data: A Training Perspective of Self-Attention via Optimal Transport
---

# Transformers for Tabular Data: A Training Perspective of Self-Attention via Optimal Transport

**arXiv**: [2512.09530v1](https://arxiv.org/abs/2512.09530) | [PDF](https://arxiv.org/pdf/2512.09530.pdf)

**作者**: Antonio Candelieri, Alessandro Quadrio

---

## 💡 一句话要点

**提出基于最优运输的自注意力训练方法，用于表格数据分类，以提升效率与可扩展性。**

**关键词**: `表格数据分类` `自注意力训练` `最优运输` `计算效率` `机器学习算法`

## 📋 核心要点

1. 核心问题：自注意力训练轨迹效率低，影响表格分类性能与计算成本。
2. 方法要点：通过最优运输度量分析自注意力映射，并设计基于OT的算法生成类特定分布进行对齐训练。
3. 实验或效果：在分类任务中实现与Transformer相当的精度，降低计算成本，但对虚拟分布设计敏感。

## 📄 摘要（原文）

> This thesis examines self-attention training through the lens of Optimal Transport (OT) and develops an OT-based alternative for tabular classification. The study tracks intermediate projections of the self-attention layer during training and evaluates their evolution using discrete OT metrics, including Wasserstein distance, Monge gap, optimality, and efficiency. Experiments are conducted on classification tasks with two and three classes, as well as on a biomedical dataset.
>   Results indicate that the final self-attention mapping often approximates the OT optimal coupling, yet the training trajectory remains inefficient. Pretraining the MLP section on synthetic data partially improves convergence but is sensitive to their initialization. To address these limitations, an OT-based algorithm is introduced: it generates class-specific dummy Gaussian distributions, computes an OT alignment with the data, and trains an MLP to generalize this mapping. The method achieves accuracy comparable to Transformers while reducing computational cost and scaling more efficiently under standardized inputs, though its performance depends on careful dummy-geometry design. All experiments and implementations are conducted in R.

