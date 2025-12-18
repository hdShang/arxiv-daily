---
layout: default
title: Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning
---

# Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16240" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16240v2</a>
  <a href="https://arxiv.org/pdf/2510.16240.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16240v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16240v2', 'Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lukas Zbinden, Nigel Nelson, Juo-Tung Chen, Xinhao Chen, Ji Woong Kim, Mahdi Azizian, Axel Krieger, Sean Huver

**分类**: cs.RO

**发布日期**: 2025-10-17 (更新: 2025-11-03)

**备注**: minor metadata and notation fixes; +3 citations

---

## 💡 一句话要点

**Cosmos-Surg-dVRK：基于世界基础模型的机器人手术策略在线自动评估**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手术机器人` `世界基础模型` `自主策略评估` `在线评估` `视频分类` `Cosmos-Surg-dVRK`

## 📋 核心要点

1. 现有手术机器人策略评估方法成本高昂、耗时且难以复现，限制了自主手术策略的开发。
2. Cosmos-Surg-dVRK通过微调世界基础模型，模拟真实手术环境，实现手术策略的在线自动化评估。
3. 实验表明，Cosmos-Surg-dVRK的评估结果与真实机器人平台结果高度相关，并与人工评估结果一致。

## 📝 摘要（中文）

本文提出Cosmos-Surg-dVRK，一个基于Cosmos世界基础模型（WFM）的手术微调模型，结合训练好的视频分类器，实现了手术策略的完全自动化在线评估和基准测试。针对达芬奇研究套件（dVRK）等物理机器人平台，直接评估手术策略面临成本高、耗时、可重复性差和执行差异大等问题。Cosmos-Surg-dVRK通过高保真地模拟复杂真实世界的手术任务（如软组织变形），提供了一种变革性的方法。该方法在两个不同的手术数据集上进行了评估。在桌面缝合垫任务中，该自动化流程在Cosmos-Surg-dVRK中的在线评估结果与真实dVRK Si平台上的策略结果之间实现了很强的相关性，并且V-JEPA 2导出的视频分类器与人工标注者之间也达成了良好的一致性。此外，Cosmos-Surg-dVRK中离体猪胆囊切除术的初步实验表明，其与真实世界评估结果具有良好的对齐性，突显了该平台在更复杂的手术程序中的潜力。

## 🔬 方法详解

**问题定义**：现有手术机器人策略的评估主要依赖于真实机器人平台，这带来了高昂的成本、漫长的评估周期以及难以保证的可重复性。此外，真实环境中的细微差异也会影响评估结果的准确性，阻碍了自主手术策略的快速迭代和优化。

**核心思路**：本文的核心思路是利用世界基础模型（WFM）来构建一个高保真度的手术模拟环境，从而实现手术策略的在线自动化评估。通过在WFM上运行手术策略，可以快速、低成本地评估其性能，并避免了真实机器人平台带来的各种限制。

**技术框架**：Cosmos-Surg-dVRK的整体框架包含两个主要组成部分：一是基于Cosmos WFM微调得到的手术模拟器，二是训练好的视频分类器。首先，使用手术数据集对Cosmos WFM进行微调，使其能够准确模拟手术过程中的软组织变形等复杂物理现象。然后，利用V-JEPA 2等方法训练一个视频分类器，用于自动评估模拟手术的质量。最后，将手术策略在模拟器中运行，并通过视频分类器对其性能进行评估。

**关键创新**：该方法最重要的创新点在于将世界基础模型应用于手术机器人策略的评估。与传统的基于物理引擎的模拟方法相比，WFM能够更好地模拟真实手术环境中的复杂物理现象，从而提高评估结果的准确性。此外，该方法还利用视频分类器实现了手术策略的自动化评估，避免了人工评估的主观性和耗时性。

**关键设计**：Cosmos WFM的微调使用了手术视频数据，目标是让模型学习手术场景下的物理规律和软组织形变。视频分类器基于V-JEPA 2架构，通过自监督学习提取视频特征，然后使用标注的手术质量数据进行微调。损失函数包括重构损失和分类损失，用于提高模型的模拟精度和评估准确性。

## 📊 实验亮点

在桌面缝合垫任务中，Cosmos-Surg-dVRK的在线评估结果与真实dVRK Si平台上的策略结果之间实现了很强的相关性。V-JEPA 2导出的视频分类器与人工标注者之间也达成了良好的一致性。离体猪胆囊切除术的初步实验表明，Cosmos-Surg-dVRK与真实世界评估结果具有良好的对齐性。

## 🎯 应用场景

Cosmos-Surg-dVRK可应用于自主手术策略的快速原型设计、在线评估和优化。它能够降低手术机器人研究的成本和时间，加速自主手术技术的发展。此外，该平台还可以用于手术技能培训和手术规划，为医生提供更安全、更有效的工具。

## 📄 摘要（原文）

> The rise of surgical robots and vision-language-action models has accelerated the development of autonomous surgical policies and efficient assessment strategies. However, evaluating these policies directly on physical robotic platforms such as the da Vinci Research Kit (dVRK) remains hindered by high costs, time demands, reproducibility challenges, and variability in execution. World foundation models (WFM) for physical AI offer a transformative approach to simulate complex real-world surgical tasks, such as soft tissue deformation, with high fidelity. This work introduces Cosmos-Surg-dVRK, a surgical finetune of the Cosmos WFM, which, together with a trained video classifier, enables fully automated online evaluation and benchmarking of surgical policies. We evaluate Cosmos-Surg-dVRK using two distinct surgical datasets. On tabletop suture pad tasks, the automated pipeline achieves strong correlation between online rollouts in Cosmos-Surg-dVRK and policy outcomes on the real dVRK Si platform, as well as good agreement between human labelers and the V-JEPA 2-derived video classifier. Additionally, preliminary experiments with ex-vivo porcine cholecystectomy tasks in Cosmos-Surg-dVRK demonstrate promising alignment with real-world evaluations, highlighting the platform's potential for more complex surgical procedures.

