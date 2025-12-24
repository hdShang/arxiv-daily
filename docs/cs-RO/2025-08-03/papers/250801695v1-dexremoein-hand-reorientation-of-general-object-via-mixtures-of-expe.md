---
layout: default
title: "DexReMoE:In-hand Reorientation of General Object via Mixtures of Experts"
---

# DexReMoE:In-hand Reorientation of General Object via Mixtures of Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01695" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01695v1</a>
  <a href="https://arxiv.org/pdf/2508.01695.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01695v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01695v1', 'DexReMoE:In-hand Reorientation of General Object via Mixtures of Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Wan, Xing Liu, Yunlong Dong

**分类**: cs.RO

**发布日期**: 2025-08-03

**备注**: 10 pages, 8 figures

---

## 💡 一句话要点

**提出DexReMoE以解决复杂物体的手中重定位问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `物体重定位` `专家混合模型` `强化学习` `复杂几何形状` `机器人操作`

## 📋 核心要点

1. 现有方法主要集中于单一物体或简单几何形状，难以处理复杂形状的重定位任务。
2. 本文提出DexReMoE，通过训练多个专家策略并结合物体类别信息，增强了对复杂物体的重定位能力。
3. 在150个物体的实验中，DexReMoE的平均成功计数为19.5，最坏情况性能显著提升，展示了其优越性。

## 📝 摘要（中文）

手中物体重定位为灵巧操作提供了能力，要求稳健的控制策略以管理多样的物体几何形状、保持稳定的抓取并执行精确的复杂方向轨迹。然而，现有研究主要集中于单一物体或简单几何形状，难以推广到复杂形状。本文提出了DexReMoE（灵巧重定位专家混合模型），通过为不同复杂形状训练多个专家策略，并在专家混合框架中整合，使得该方法能够在广泛的物体上进行推广。此外，我们将物体类别信息作为特权输入，以增强形状表示。我们的框架在模拟环境中使用强化学习进行训练，并在最具挑战性的场景中评估，即在向下的手中重定位悬空物体。DexReMoE在150个多样化物体上实现了19.5的平均连续成功计数，相较于基线方法，最坏情况性能从0.69提升至6.05。这些结果突显了DexReMoE框架在通用手中重定位中的可扩展性和适应性。

## 🔬 方法详解

**问题定义**：本文旨在解决复杂物体在手中重定位的挑战，现有方法在处理多样化和复杂几何形状时表现不佳，难以实现稳健的控制策略。

**核心思路**：DexReMoE采用专家混合模型，通过训练多个针对不同复杂形状的专家策略，提升了对多样物体的适应能力，并引入物体类别信息以增强形状表示。

**技术框架**：该框架包括多个专家策略的训练模块、物体类别信息的集成模块，以及基于强化学习的训练流程，确保在复杂场景下的有效重定位。

**关键创新**：DexReMoE的核心创新在于其专家混合模型的设计，使得不同专家能够针对特定物体形状进行优化，从而实现更广泛的适用性和更高的重定位成功率。

**关键设计**：在训练过程中，采用强化学习算法，设计了适应性损失函数以平衡不同专家的贡献，同时优化了网络结构以提高模型的学习效率和泛化能力。

## 📊 实验亮点

在150个多样化物体的实验中，DexReMoE实现了19.5的平均连续成功计数，相较于基线方法，最坏情况性能从0.69提升至6.05，显示出显著的性能提升和更强的适应性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、自动化装配和人机交互等。通过提升机器人在复杂环境下的物体重定位能力，能够显著提高其在实际操作中的灵活性和效率，推动智能制造和服务机器人技术的发展。

## 📄 摘要（原文）

> In hand object reorientation provides capability for dexterous manipulation, requiring robust control policies to manage diverse object geometries, maintain stable grasps, and execute precise complex orientation trajectories. However, prior works focus on single objects or simple geometries and struggle to generalize to complex shapes. In this work, we introduce DexReMoE (Dexterous Reorientation Mixture-of-Experts), in which multiple expert policies are trained for different complex shapes and integrated within a Mixture-of-Experts (MoE) framework, making the approach capable of generalizing across a wide range of objects. Additionally, we incorporate object category information as privileged inputs to enhance shape representation. Our framework is trained in simulation using reinforcement learning (RL) and evaluated on novel out-of-distribution objects in the most challenging scenario of reorienting objects held in the air by a downward-facing hand. In terms of the average consecutive success count, DexReMoE achieves a score of 19.5 across a diverse set of 150 objects. In comparison to the baselines, it also enhances the worst-case performance, increasing it from 0.69 to 6.05. These results underscore the scalability and adaptability of the DexReMoE framework for general-purpose in-hand reorientation.

