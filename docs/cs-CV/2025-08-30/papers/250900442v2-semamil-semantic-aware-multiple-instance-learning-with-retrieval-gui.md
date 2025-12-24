---
layout: default
title: "SemaMIL: Semantic-Aware Multiple Instance Learning with Retrieval-Guided State Space Modeling for Whole Slide Images"
---

# SemaMIL: Semantic-Aware Multiple Instance Learning with Retrieval-Guided State Space Modeling for Whole Slide Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00442" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00442v2</a>
  <a href="https://arxiv.org/pdf/2509.00442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00442v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00442v2', 'SemaMIL: Semantic-Aware Multiple Instance Learning with Retrieval-Guided State Space Modeling for Whole Slide Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lubin Gan, Xiaoman Wu, Jing Zhang, Zhifeng Wang, Linhao Qu, Siying Wu, Xiaoyan Sun

**分类**: cs.CV

**发布日期**: 2025-08-30 (更新: 2025-09-27)

---

## 💡 一句话要点

**提出SemaMIL以解决全切片图像中的多实例学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多实例学习` `全切片图像` `语义重排` `状态空间模型` `计算病理学` `特征提取` `深度学习`

## 📋 核心要点

1. 现有的多实例学习方法在处理全切片图像时，往往忽视了补丁之间的上下文关系，导致特征提取效果不佳。
2. SemaMIL通过语义重排和语义引导的检索状态空间模块，优化补丁的排列和选择，从而提升全局建模能力。
3. 在四个WSI子类型数据集上的实验结果表明，SemaMIL在准确性上超过了强基线，同时减少了计算复杂度。

## 📝 摘要（中文）

多实例学习（MIL）已成为计算病理学中从全切片图像（WSIs）提取判别特征的主要方法。基于注意力的MIL方法能够识别关键补丁，但往往忽视上下文关系。变换器模型虽然能够建模交互，但计算成本呈平方增长且容易过拟合。状态空间模型（SSMs）提供线性复杂度，但打乱补丁顺序会破坏组织学意义并降低可解释性。本文提出SemaMIL，结合语义重排（SR）和语义引导的检索状态空间模块（SRSM），在四个WSI子类型数据集上的评估显示，SemaMIL在较少的FLOPs和参数下实现了最先进的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多实例学习方法在全切片图像中对上下文关系的忽视，以及计算成本高和过拟合的问题。

**核心思路**：SemaMIL的核心思路是通过语义重排（SR）对补丁进行语义聚类和排列，同时利用语义引导的检索状态空间模块（SRSM）选择代表性查询以调整状态空间参数，从而实现更好的全局建模。

**技术框架**：SemaMIL的整体架构包括两个主要模块：语义重排模块和语义引导的检索状态空间模块。前者负责对补丁进行语义排序，后者则通过选择合适的查询来优化状态空间的参数。

**关键创新**：SemaMIL的创新点在于结合了语义重排和状态空间模型，克服了传统MIL方法的局限性，尤其是在上下文建模和计算效率方面。

**关键设计**：在设计中，采用了可逆排列的方式进行补丁重排，并在状态空间模块中引入了语义引导的查询选择机制，以提高模型的全局建模能力。

## 📊 实验亮点

在四个WSI子类型数据集上的实验结果显示，SemaMIL相比于强基线模型实现了最先进的准确性，且在计算复杂度上减少了FLOPs和参数数量，展现出更高的效率和效果。

## 🎯 应用场景

该研究的潜在应用领域包括医学图像分析、病理学诊断和生物医学研究。通过提升全切片图像的特征提取能力，SemaMIL有助于提高疾病检测的准确性和效率，未来可能对个性化医疗和精准医学产生深远影响。

## 📄 摘要（原文）

> Multiple instance learning (MIL) has become the leading approach for extracting discriminative features from whole slide images (WSIs) in computational pathology. Attention-based MIL methods can identify key patches but tend to overlook contextual relationships. Transformer models are able to model interactions but require quadratic computational cost and are prone to overfitting. State space models (SSMs) offer linear complexity, yet shuffling patch order disrupts histological meaning and reduces interpretability. In this work, we introduce SemaMIL, which integrates Semantic Reordering (SR), an adaptive method that clusters and arranges semantically similar patches in sequence through a reversible permutation, with a Semantic-guided Retrieval State Space Module (SRSM) that chooses a representative subset of queries to adjust state space parameters for improved global modeling. Evaluation on four WSI subtype datasets shows that, compared to strong baselines, SemaMIL achieves state-of-the-art accuracy with fewer FLOPs and parameters.

