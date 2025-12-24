---
layout: default
title: "CaO$_2$: Rectifying Inconsistencies in Diffusion-Based Dataset Distillation"
---

# CaO$_2$: Rectifying Inconsistencies in Diffusion-Based Dataset Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22637" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22637v2</a>
  <a href="https://arxiv.org/pdf/2506.22637.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22637v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22637v2', 'CaO$_2$: Rectifying Inconsistencies in Diffusion-Based Dataset Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoxuan Wang, Zhenghao Zhao, Junyi Wu, Yuzhang Shang, Gaowen Liu, Yan Yan

**分类**: cs.CV

**发布日期**: 2025-06-27 (更新: 2025-07-09)

**备注**: ICCV 2025. Code is available at https://github.com/hatchetProject/CaO2

---

## 💡 一句话要点

**提出CaO$_2$以解决扩散模型数据蒸馏中的不一致性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `数据蒸馏` `条件感知优化` `目标引导采样` `计算机视觉` `机器学习`

## 📋 核心要点

1. 现有的扩散模型数据蒸馏方法存在目标不一致性和条件不一致性，导致生成图像与评估目标不匹配。
2. 本文提出的CaO$_2$框架通过条件感知优化和目标引导采样，解决了蒸馏过程中的不一致性问题。
3. CaO$_2$在ImageNet及其子集上表现优异，平均提升了2.3%的准确率，超越了最佳基线。

## 📝 摘要（中文）

最近扩散模型在数据集蒸馏中的应用展现了在创建紧凑的替代数据集方面的潜力，较传统的优化方法具有更高的效率和性能。然而，现有的扩散模型数据蒸馏方法忽视了评估过程，并在蒸馏过程中存在两种关键不一致性：目标不一致性和条件不一致性。为了解决这些问题，本文提出了条件感知优化与目标引导采样（CaO$_2$），这是一个两阶段的扩散模型框架，旨在将蒸馏过程与评估目标对齐。CaO$_2$在ImageNet及其子集上实现了最先进的性能，平均提高了2.3%的准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散模型数据蒸馏中的目标不一致性和条件不一致性问题。现有方法在蒸馏过程中未能有效对齐生成图像与评估目标，导致性能下降。

**核心思路**：CaO$_2$框架通过引入条件感知优化与目标引导采样，确保蒸馏过程与评估目标一致，从而提高生成图像的质量和准确性。

**技术框架**：该框架分为两个阶段：第一阶段采用概率引导的样本选择管道，第二阶段则对相应的潜在表示进行精细化处理，以提高条件似然性。

**关键创新**：CaO$_2$的主要创新在于其两阶段的优化策略，特别是通过条件感知优化来解决现有方法中的不一致性问题，这在传统的单阶段方法中并未实现。

**关键设计**：在样本选择过程中，CaO$_2$使用概率信息来指导样本的选择，同时在潜在表示的精细化阶段，采用特定的损失函数以优化条件似然性，确保生成图像与条件的一致性。

## 📊 实验亮点

CaO$_2$在ImageNet及其子集上实现了最先进的性能，平均提高了2.3%的准确率，超越了现有最佳基线。这一结果展示了其在数据蒸馏领域的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉中的图像生成、数据集优化以及机器学习模型的训练。通过提供更高效的数据蒸馏方法，CaO$_2$能够在大规模数据集的处理上显著提升模型性能，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> The recent introduction of diffusion models in dataset distillation has shown promising potential in creating compact surrogate datasets for large, high-resolution target datasets, offering improved efficiency and performance over traditional bi-level/uni-level optimization methods. However, current diffusion-based dataset distillation approaches overlook the evaluation process and exhibit two critical inconsistencies in the distillation process: (1) Objective Inconsistency, where the distillation process diverges from the evaluation objective, and (2) Condition Inconsistency, leading to mismatches between generated images and their corresponding conditions. To resolve these issues, we introduce Condition-aware Optimization with Objective-guided Sampling (CaO$_2$), a two-stage diffusion-based framework that aligns the distillation process with the evaluation objective. The first stage employs a probability-informed sample selection pipeline, while the second stage refines the corresponding latent representations to improve conditional likelihood. CaO$_2$ achieves state-of-the-art performance on ImageNet and its subsets, surpassing the best-performing baselines by an average of 2.3% accuracy.

