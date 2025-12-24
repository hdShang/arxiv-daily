---
layout: default
title: "LEAD: Iterative Data Selection for Efficient LLM Instruction Tuning"
---

# LEAD: Iterative Data Selection for Efficient LLM Instruction Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07437" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07437v1</a>
  <a href="https://arxiv.org/pdf/2505.07437.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07437v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07437v1', 'LEAD: Iterative Data Selection for Efficient LLM Instruction Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaotian Lin, Yanlin Qi, Yizhang Zhu, Themis Palpanas, Chengliang Chai, Nan Tang, Yuyu Luo

**分类**: cs.LG, cs.AI, cs.DB

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出LEAD框架以解决LLM指令调优中的数据选择效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `指令调优` `数据选择` `训练效率` `动态不确定性`

## 📋 核心要点

1. 现有的迭代模型感知数据选择方法在计算上开销巨大，导致效率瓶颈。
2. LEAD框架通过在标准训练循环内估计样本效用，消除了额外的模型推理需求。
3. 实验结果显示，LEAD在多个基准上平均性能提升6.1%-10.8%，训练时间减少5-10倍。

## 📝 摘要（中文）

指令调优已成为提升大型语言模型（LLMs）能力和对齐的重要范式。然而，现有的迭代模型感知数据选择方法存在显著的计算开销，因为它们依赖于反复进行全数据集模型推理来估计样本效用，从而造成效率瓶颈。本文提出了LEAD，一个高效的迭代数据选择框架，能够在标准训练循环内准确估计样本效用，消除了额外模型推理的高成本。LEAD的核心是引入实例级动态不确定性（IDU），结合瞬时训练损失、基于梯度的损失变化近似和历史损失信号的指数平滑。为了高效扩展到大规模数据集，LEAD采用两阶段的粗到细选择策略，通过多臂老虎机机制自适应优先选择信息丰富的聚类，随后使用IDU精确选择高效用样本。大量实验表明，LEAD显著优于现有最先进方法，平均模型性能提升6.1%-10.8%，同时仅使用2.5%的训练数据，整体训练时间减少5-10倍。

## 🔬 方法详解

**问题定义**：本文旨在解决现有迭代模型感知数据选择方法在指令调优中的效率瓶颈，现有方法需要反复进行全数据集推理，造成计算开销大。

**核心思路**：LEAD框架通过在标准训练循环内估计样本效用，避免了额外的模型推理，利用实例级动态不确定性（IDU）来综合考虑训练损失和历史信号。

**技术框架**：LEAD的整体架构包括两个主要阶段：第一阶段是粗略选择，通过多臂老虎机机制优先选择信息丰富的聚类；第二阶段是细致选择，使用IDU精确选择高效用样本。

**关键创新**：LEAD的核心创新在于引入了IDU作为效用函数，结合了瞬时损失、梯度近似和历史损失的平滑，显著提高了样本效用的估计精度。

**关键设计**：在IDU的设计中，考虑了瞬时训练损失和历史损失信号的平滑处理，确保了在大规模数据集上的高效选择。

## 📊 实验亮点

LEAD在四个不同基准上进行了广泛实验，结果显示其平均模型性能提升6.1%-10.8%，同时仅使用2.5%的训练数据，训练时间减少了5-10倍，显著优于现有最先进方法。

## 🎯 应用场景

LEAD框架在大型语言模型的指令调优中具有广泛的应用潜力，能够显著提高训练效率和模型性能。其高效的数据选择策略适用于各种自然语言处理任务，未来可能推动更大规模模型的训练与应用。

## 📄 摘要（原文）

> Instruction tuning has emerged as a critical paradigm for improving the capabilities and alignment of large language models (LLMs). However, existing iterative model-aware data selection methods incur significant computational overhead, as they rely on repeatedly performing full-dataset model inference to estimate sample utility for subsequent training iterations, creating a fundamental efficiency bottleneck. In this paper, we propose LEAD, an efficient iterative data selection framework that accurately estimates sample utility entirely within the standard training loop, eliminating the need for costly additional model inference. At its core, LEAD introduces Instance-Level Dynamic Uncertainty (IDU), a theoretically grounded utility function combining instantaneous training loss, gradient-based approximation of loss changes, and exponential smoothing of historical loss signals. To further scale efficiently to large datasets, LEAD employs a two-stage, coarse-to-fine selection strategy, adaptively prioritizing informative clusters through a multi-armed bandit mechanism, followed by precise fine-grained selection of high-utility samples using IDU. Extensive experiments across four diverse benchmarks show that LEAD significantly outperforms state-of-the-art methods, improving average model performance by 6.1%-10.8% while using only 2.5% of the training data and reducing overall training time by 5-10x.

