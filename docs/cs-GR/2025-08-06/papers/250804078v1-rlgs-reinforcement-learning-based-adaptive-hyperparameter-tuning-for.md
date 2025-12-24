---
layout: default
title: "RLGS: Reinforcement Learning-Based Adaptive Hyperparameter Tuning for Gaussian Splatting"
---

# RLGS: Reinforcement Learning-Based Adaptive Hyperparameter Tuning for Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04078" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04078v1</a>
  <a href="https://arxiv.org/pdf/2508.04078.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04078v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04078v1', 'RLGS: Reinforcement Learning-Based Adaptive Hyperparameter Tuning for Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhan Li, Huangying Zhan, Changyang Li, Qingan Yan, Yi Xu

**分类**: cs.GR, cs.CV, cs.LG

**发布日期**: 2025-08-06

**备注**: 14 pages, 9 figures

---

## 💡 一句话要点

**提出RLGS框架以自动化3D高斯点云的超参数调优**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `超参数调优` `强化学习` `3D高斯点云` `自动化` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有的3D高斯点云重建方法在超参数调优上依赖专家经验，导致结果不一致和性能不佳。
2. RLGS框架通过强化学习实现超参数的自适应调优，动态调整学习率和稠密化阈值，简化了调优过程。
3. 实验结果表明，RLGS在多个3DGS变体上均能提升渲染质量，特别是在TNT数据集上提升了0.7dB PSNR。

## 📝 摘要（中文）

在3D高斯点云（3DGS）中，超参数调优是一个劳动密集型且依赖专家的过程，常导致重建不一致和结果次优。本文提出RLGS，一个基于强化学习的插件式框架，通过轻量级策略模块自适应调整关键超参数，如学习率和稠密化阈值。该框架具有模型无关性，能够无缝集成到现有的3DGS流程中，而无需架构修改。我们展示了其在多种最先进的3DGS变体（包括Taming-3DGS和3DGS-MCMC）中的泛化能力，并验证了其在不同数据集上的鲁棒性。RLGS持续提升渲染质量，例如在固定高斯预算下，Taming-3DGS在Tanks and Temple（TNT）数据集上的PSNR提升了0.7dB，且即使在基线性能饱和时仍能继续获得增益。我们的结果表明，RLGS为3DGS训练中的超参数调优提供了一种有效且通用的自动化解决方案，填补了将强化学习应用于3DGS的空白。

## 🔬 方法详解

**问题定义**：本文旨在解决3D高斯点云重建中超参数调优的复杂性和不一致性，现有方法往往依赖于专家经验，导致重建效果不理想。

**核心思路**：RLGS框架利用强化学习的策略模块，自动化地调整关键超参数，如学习率和稠密化阈值，从而提高重建质量和一致性。

**技术框架**：RLGS的整体架构包括多个轻量级策略模块，这些模块能够与现有的3DGS流程无缝集成，且无需对架构进行修改。框架的设计使其具备模型无关性，适用于多种3DGS变体。

**关键创新**：RLGS的主要创新在于将强化学习应用于超参数调优，提供了一种自动化的解决方案，显著降低了对专家知识的依赖，与传统手动调优方法形成鲜明对比。

**关键设计**：RLGS的设计包括动态调整超参数的机制，采用轻量级的策略网络来学习最优的超参数配置，确保在不同数据集和模型上均能保持良好的性能。

## 📊 实验亮点

实验结果显示，RLGS在Tanks and Temple（TNT）数据集上将Taming-3DGS的PSNR提升了0.7dB，且在基线性能饱和时仍能继续提升，证明了其在多种3DGS变体上的有效性和鲁棒性。

## 🎯 应用场景

RLGS框架在3D高斯点云重建领域具有广泛的应用潜力，能够显著提高渲染质量和效率，适用于虚拟现实、游戏开发和计算机视觉等多个领域。未来，该框架还可扩展至其他需要超参数调优的深度学习任务，进一步推动自动化研究的发展。

## 📄 摘要（原文）

> Hyperparameter tuning in 3D Gaussian Splatting (3DGS) is a labor-intensive and expert-driven process, often resulting in inconsistent reconstructions and suboptimal results. We propose RLGS, a plug-and-play reinforcement learning framework for adaptive hyperparameter tuning in 3DGS through lightweight policy modules, dynamically adjusting critical hyperparameters such as learning rates and densification thresholds. The framework is model-agnostic and seamlessly integrates into existing 3DGS pipelines without architectural modifications. We demonstrate its generalization ability across multiple state-of-the-art 3DGS variants, including Taming-3DGS and 3DGS-MCMC, and validate its robustness across diverse datasets. RLGS consistently enhances rendering quality. For example, it improves Taming-3DGS by 0.7dB PSNR on the Tanks and Temple (TNT) dataset, under a fixed Gaussian budget, and continues to yield gains even when baseline performance saturates. Our results suggest that RLGS provides an effective and general solution for automating hyperparameter tuning in 3DGS training, bridging a gap in applying reinforcement learning to 3DGS.

