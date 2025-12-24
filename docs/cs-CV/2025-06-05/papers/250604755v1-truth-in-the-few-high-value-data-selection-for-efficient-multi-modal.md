---
layout: default
title: "Truth in the Few: High-Value Data Selection for Efficient Multi-Modal Reasoning"
---

# Truth in the Few: High-Value Data Selection for Efficient Multi-Modal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04755" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04755v1</a>
  <a href="https://arxiv.org/pdf/2506.04755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04755v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04755v1', 'Truth in the Few: High-Value Data Selection for Efficient Multi-Modal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shenshen Li, Kaiyuan Deng, Lei Wang, Hao Yang, Chong Peng, Peng Yan, Fumin Shen, Heng Tao Shen, Xing Xu

**分类**: cs.CV, cs.AI, cs.MM

**发布日期**: 2025-06-05

**🔗 代码/项目**: [GITHUB](https://github.com/Leo-ssl/RAP)

---

## 💡 一句话要点

**提出RAP方法以高效选择多模态推理中的高价值数据**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `数据选择` `高价值数据` `因果推理` `注意力机制` `计算效率` `机器学习`

## 📋 核心要点

1. 现有方法普遍依赖大量训练数据，导致数据冗余和高昂的计算成本。
2. 论文提出的RAP方法通过识别认知样本，优化数据选择，提升多模态推理效率。
3. 实验结果显示，RAP在六个数据集上使用9.3%的数据实现了性能提升，计算成本显著降低。

## 📝 摘要（中文）

尽管多模态大语言模型（MLLMs）在复杂推理任务中取得了显著进展，但普遍认为需要大量训练数据来提升其多模态推理能力，导致数据冗余和计算成本高昂。本文挑战这一假设，提出了一种新的数据选择范式——推理激活潜力（RAP），通过评估样本激发真实多模态推理的潜力来识别认知样本。RAP使用两种互补的估计器：因果差异估计器（CDE）和注意力置信度估计器（ACE），并引入难度感知替换模块（DRM）以确保复杂性。实验表明，RAP方法仅使用9.3%的训练数据，性能优越，计算成本降低超过43%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态推理中对大量训练数据的依赖问题，现有方法导致数据冗余和计算成本高昂。

**核心思路**：通过识别仅需少量高价值的认知样本，RAP方法能够在保持推理能力的同时，显著减少所需数据量。

**技术框架**：RAP方法包括两个主要模块：因果差异估计器（CDE）和注意力置信度估计器（ACE），并结合难度感知替换模块（DRM）以确保样本的复杂性。

**关键创新**：RAP的核心创新在于通过CDE和ACE的组合，能够有效识别出对推理有实际贡献的样本，与传统方法相比，显著降低了对冗余数据的依赖。

**关键设计**：CDE基于潜在结果模型原理，ACE利用token级自注意力机制，DRM则替换简单实例以增加认知挑战性，确保推理的复杂性和有效性。

## 📊 实验亮点

实验结果表明，RAP方法在六个数据集上仅使用9.3%的训练数据，依然实现了优越的性能，计算成本降低超过43%。这一结果显著优于传统方法，展示了高价值数据选择的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、图像理解和多模态交互等。通过高效的数据选择，RAP方法能够在资源有限的情况下提升多模态模型的推理能力，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> While multi-modal large language models (MLLMs) have made significant progress in complex reasoning tasks via reinforcement learning, it is commonly believed that extensive training data is necessary for improving multi-modal reasoning ability, inevitably leading to data redundancy and substantial computational costs. However, can smaller high-value datasets match or outperform full corpora for multi-modal reasoning in MLLMs? In this work, we challenge this assumption through a key observation: meaningful multi-modal reasoning is triggered by only a sparse subset of training samples, termed cognitive samples, whereas the majority contribute marginally. Building on this insight, we propose a novel data selection paradigm termed Reasoning Activation Potential (RAP), which identifies cognitive samples by estimating each sample's potential to stimulate genuine multi-modal reasoning by two complementary estimators: 1) Causal Discrepancy Estimator (CDE) based on the potential outcome model principle, eliminates samples that overly rely on language priors by comparing outputs between multi-modal and text-only inputs; 2) Attention Confidence Estimator (ACE), which exploits token-level self-attention to discard samples dominated by irrelevant but over-emphasized tokens in intermediate reasoning stages. Moreover, we introduce a Difficulty-aware Replacement Module (DRM) to substitute trivial instances with cognitively challenging ones, thereby ensuring complexity for robust multi-modal reasoning. Experiments on six datasets show that our RAP method consistently achieves superior performance using only 9.3% of the training data, while reducing computational costs by over 43%. Our code is available at https://github.com/Leo-ssl/RAP.

