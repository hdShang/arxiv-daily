---
layout: default
title: Innovative Design of Multi-functional Supernumerary Robotic Limbs with Ellipsoid Workspace Optimization
---

# Innovative Design of Multi-functional Supernumerary Robotic Limbs with Ellipsoid Workspace Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12186" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12186v1</a>
  <a href="https://arxiv.org/pdf/2511.12186.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12186v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.12186v1', 'Innovative Design of Multi-functional Supernumerary Robotic Limbs with Ellipsoid Workspace Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Huo, Jian Huang, Jie Zuo, Bo Yang, Zhongzheng Fu, Xi Li, Samer Mohammed

**分类**: cs.RO

**发布日期**: 2025-11-15

**期刊**: IEEE Transactions on Robotics, vol. 41, pp. 4699-4718, 2025

**DOI**: [10.1109/TRO.2025.3588763](https://doi.org/10.1109/TRO.2025.3588763)

---

## 💡 一句话要点

**提出基于椭球工作空间优化的多功能外骨骼机器人创新设计**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `外骨骼机器人` `多目标优化` `工作空间优化` `康复机器人` `萤火虫算法`

## 📋 核心要点

1. 通用外骨骼机器人设计面临上肢和下肢功能需求差异大的挑战，缺乏统一的理论框架。
2. 论文提出多目标优化设计理论，综合考虑工作空间相似性、支撑力、质量和惯性等多重因素。
3. 实验结果表明，优化后的外骨骼机器人抓握成功率提升，行走和坐站任务的肌肉活动降低。

## 📝 摘要（中文）

本文提出了一种多目标优化(MOO)设计理论，用于设计多功能外骨骼机器人(SRL)，旨在同时满足上肢和下肢的不同功能需求。该理论综合考虑了抓握工作空间相似性、行走工作空间相似性、坐站(STS)运动的支撑力以及整体质量和惯性。采用椭球几何向量量化方法表示工作空间，以降低计算复杂性。STS静态支撑力用于评估力传递的有效性。引入多子种群校正萤火虫算法，加速模型收敛到高维不规则Pareto前沿。优化后的方案用于原型重新设计和实验验证。实验结果表明，与优化前相比，抓握成功率平均提高7.2%，行走和STS任务期间的肌肉活动平均降低12.7%和25.1%。

## 🔬 方法详解

**问题定义**：现有外骨骼机器人设计难以兼顾上肢的抓握功能和下肢的行走、站立功能，缺乏一个通用的设计框架。传统方法在工作空间量化方面计算复杂度高，难以进行多目标优化。此外，如何评估外骨骼机器人在坐站过程中的辅助支撑能力也是一个挑战。

**核心思路**：论文的核心思路是通过多目标优化，在满足不同功能需求的同时，最小化外骨骼机器人的质量和惯性。利用椭球来近似表示工作空间，简化计算，并引入一种改进的萤火虫算法来加速优化过程。通过静态支撑力分析来评估外骨骼机器人在坐站过程中的辅助能力。

**技术框架**：该设计理论包含以下几个主要模块：1) 工作空间建模：使用椭球几何向量量化方法对抓握和行走工作空间进行建模。2) 支撑力评估：通过静态力分析评估外骨骼机器人在坐站过程中的支撑力。3) 多目标优化：综合考虑工作空间相似性、支撑力、质量和惯性等因素，构建多目标优化问题。4) 优化算法：采用多子种群校正萤火虫算法求解多目标优化问题。5) 原型设计与实验验证：根据优化结果重新设计外骨骼机器人原型，并通过实验验证其性能。

**关键创新**：论文的关键创新在于：1) 提出了一种基于椭球几何向量量化的工作空间表示方法，降低了计算复杂度。2) 引入了多子种群校正萤火虫算法，提高了多目标优化的收敛速度和稳定性。3) 综合考虑了多种功能需求，设计了一种多功能外骨骼机器人。与现有方法相比，该方法能够更有效地设计出满足多种功能需求的外骨骼机器人。

**关键设计**：在工作空间建模方面，使用椭球的长轴、短轴和方向向量来描述工作空间。在多目标优化方面，目标函数包括抓握工作空间相似性、行走工作空间相似性、坐站支撑力以及整体质量和惯性。多子种群校正萤火虫算法采用了吸引和排斥域策略，以提高算法的全局搜索能力。具体参数设置未知。

## 📊 实验亮点

实验结果表明，与优化前相比，优化后的外骨骼机器人抓握成功率平均提高7.2%，行走和坐站任务期间的肌肉活动平均降低12.7%和25.1%。这表明该设计理论能够有效提高外骨骼机器人的性能，降低使用者的体力消耗。

## 🎯 应用场景

该研究成果可应用于康复医疗领域，帮助偏瘫患者恢复肢体功能。同时，也可用于增强健康人的肢体能力，例如在工业生产、救援等场景中，提高工作效率和安全性。未来，该技术有望应用于外骨骼机器人、辅助机器人等领域，提升人类的生活质量。

## 📄 摘要（原文）

> Supernumerary robotic limbs (SRLs) offer substantial potential in both the rehabilitation of hemiplegic patients and the enhancement of functional capabilities for healthy individuals. Designing a general-purpose SRL device is inherently challenging, particularly when developing a unified theoretical framework that meets the diverse functional requirements of both upper and lower limbs. In this paper, we propose a multi-objective optimization (MOO) design theory that integrates grasping workspace similarity, walking workspace similarity, braced force for sit-to-stand (STS) movements, and overall mass and inertia. A geometric vector quantification method is developed using an ellipsoid to represent the workspace, aiming to reduce computational complexity and address quantification challenges. The ellipsoid envelope transforms workspace points into ellipsoid attributes, providing a parametric description of the workspace. Furthermore, the STS static braced force assesses the effectiveness of force transmission. The overall mass and inertia restricts excessive link length. To facilitate rapid and stable convergence of the model to high-dimensional irregular Pareto fronts, we introduce a multi-subpopulation correction firefly algorithm. This algorithm incorporates a strategy involving attractive and repulsive domains to effectively handle the MOO task. The optimized solution is utilized to redesign the prototype for experimentation to meet specified requirements. Six healthy participants and two hemiplegia patients participated in real experiments. Compared to the pre-optimization results, the average grasp success rate improved by 7.2%, while the muscle activity during walking and STS tasks decreased by an average of 12.7% and 25.1%, respectively. The proposed design theory offers an efficient option for the design of multi-functional SRL mechanisms.

