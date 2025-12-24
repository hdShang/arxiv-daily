---
layout: default
title: "GraspQP: Differentiable Optimization of Force Closure for Diverse and Robust Dexterous Grasping"
---

# GraspQP: Differentiable Optimization of Force Closure for Diverse and Robust Dexterous Grasping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15002" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15002v1</a>
  <a href="https://arxiv.org/pdf/2508.15002.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15002v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15002v1', 'GraspQP: Differentiable Optimization of Force Closure for Diverse and Robust Dexterous Grasping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: René Zurbrügg, Andrei Cramariuc, Marco Hutter

**分类**: cs.RO

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出GraspQP以解决多样化和稳健的灵巧抓取问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `灵巧抓取` `力闭合` `优化算法` `机器人手` `数据集生成` `多样性提升` `物理可行性`

## 📋 核心要点

1. 现有抓取数据集生成方法多依赖于采样算法或简化的力闭合分析，导致抓取配置的多样性和质量不足。
2. 本文提出了一种基于二次规划的可微分力闭合能量公式，能够合成多样化且物理可行的抓取配置，涵盖多种抓取类型。
3. 实验结果表明，所提方法在抓取多样性和最终抓取预测的稳定性上显著优于现有方法，提供了5700个对象的新数据集。

## 📝 摘要（中文）

灵巧机器人手由于其多指设计的灵活性和适应性，能够在多种环境中进行多样化的任务特定抓取。然而，现有的数据集生成方法通常依赖于基于采样的算法或简化的力闭合分析，导致抓取配置的多样性不足。本文提出了一种合成大规模、多样化且物理可行的抓取的方法，超越简单的力量抓取，涵盖了更精细的操作，如夹持和三指精确抓取。我们引入了一种严格的、可微分的力闭合能量公式，并提出了一种改进的优化方法（MALA*），通过动态拒绝基于能量值分布的梯度步骤来提高性能。我们进行了广泛的评估，显示出抓取多样性和最终抓取预测的稳定性显著提升，并提供了一个包含5700个对象的新大规模抓取数据集。

## 🔬 方法详解

**问题定义**：本文旨在解决灵巧机器人手抓取配置生成中的多样性不足问题。现有方法往往集中于简单的力量抓取，缺乏对复杂抓取的支持。

**核心思路**：我们提出了一种新的合成方法，通过引入可微分的力闭合能量公式，能够生成多样化的抓取配置，包括夹持和三指精确抓取，提升了抓取的灵活性和适应性。

**技术框架**：整体方法包括数据生成模块、优化模块和评估模块。数据生成模块负责合成抓取配置，优化模块使用MALA*算法进行性能提升，评估模块则验证抓取的多样性和稳定性。

**关键创新**：最重要的创新在于引入了可微分的力闭合能量公式，并通过MALA*算法动态调整梯度步骤，从而显著提升了抓取配置的多样性和稳定性。

**关键设计**：在优化过程中，我们设置了特定的能量阈值和损失函数，以确保生成的抓取配置在物理上可行，并且能够涵盖多种抓取类型。

## 📊 实验亮点

实验结果显示，所提方法在抓取多样性上比基线方法提高了显著的比例，最终抓取预测的稳定性也得到了显著改善，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、自动化生产线、服务机器人等。通过提供多样化的抓取配置，能够提升机器人在复杂环境中的操作能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Dexterous robotic hands enable versatile interactions due to the flexibility and adaptability of multi-fingered designs, allowing for a wide range of task-specific grasp configurations in diverse environments. However, to fully exploit the capabilities of dexterous hands, access to diverse and high-quality grasp data is essential -- whether for developing grasp prediction models from point clouds, training manipulation policies, or supporting high-level task planning with broader action options. Existing approaches for dataset generation typically rely on sampling-based algorithms or simplified force-closure analysis, which tend to converge to power grasps and often exhibit limited diversity. In this work, we propose a method to synthesize large-scale, diverse, and physically feasible grasps that extend beyond simple power grasps to include refined manipulations, such as pinches and tri-finger precision grasps. We introduce a rigorous, differentiable energy formulation of force closure, implicitly defined through a Quadratic Program (QP). Additionally, we present an adjusted optimization method (MALA*) that improves performance by dynamically rejecting gradient steps based on the distribution of energy values across all samples. We extensively evaluate our approach and demonstrate significant improvements in both grasp diversity and the stability of final grasp predictions. Finally, we provide a new, large-scale grasp dataset for 5,700 objects from DexGraspNet, comprising five different grippers and three distinct grasp types.
>   Dataset and Code:https://graspqp.github.io/

