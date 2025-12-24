---
layout: default
title: "SPUS: A Lightweight and Parameter-Efficient Foundation Model for PDEs"
---

# SPUS: A Lightweight and Parameter-Efficient Foundation Model for PDEs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01370" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01370v1</a>
  <a href="https://arxiv.org/pdf/2510.01370.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01370v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01370v1', 'SPUS: A Lightweight and Parameter-Efficient Foundation Model for PDEs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abu Bucker Siddik, Diane Oyen, Alexander Most, Michal Kucer, Ayan Biswas

**分类**: cs.CV, cs.AI, cs.LG, physics.comp-ph

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**SPUS：一种轻量级且参数高效的偏微分方程基础模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏微分方程求解` `基础模型` `U-Net` `自回归预训练` `参数高效` `神经算子` `流体动力学`

## 📋 核心要点

1. 现有PDE求解基础模型依赖于大型Transformer架构，计算和参数开销巨大，限制了其应用。
2. SPUS采用轻量级残差U-Net架构，并结合自回归预训练策略，模拟数值求解器行为，学习底层物理。
3. 实验表明，SPUS在多个下游PDE任务上实现了最先进的泛化性能，同时显著减少了参数和微调数据需求。

## 📝 摘要（中文）

本文提出了一种小型偏微分方程U-Net求解器(SPUS)，它是一种紧凑而高效的基础模型(FM)，被设计为用于求解各种偏微分方程(PDEs)的统一神经算子。与现有最先进的PDE FM（主要基于具有高计算和参数开销的大型复杂Transformer架构）不同，SPUS利用了一种轻量级的基于残差U-Net的架构，该架构在该领域作为基础模型架构在很大程度上尚未被探索。为了在这种极简框架中实现有效的学习，我们利用了一种简单而强大的自回归预训练策略，该策略紧密地复制了数值求解器的行为以学习底层物理。SPUS在各种流体动力学PDE上进行预训练，并在跨越各种物理系统的6个具有挑战性的未见下游PDE上进行评估。实验结果表明，使用基于残差U-Net架构的SPUS在这些下游任务上实现了最先进的泛化，同时需要显著更少的参数和最少的微调数据，突出了其作为用于求解各种PDE系统的高度参数高效的FM的潜力。

## 🔬 方法详解

**问题定义**：现有基于Transformer的PDE求解基础模型参数量大，计算成本高昂，难以部署和应用。本文旨在设计一种参数高效、计算成本低的PDE基础模型，能够在各种PDE求解任务中实现良好的泛化性能。

**核心思路**：本文的核心思路是利用轻量级的残差U-Net架构作为PDE求解的基础模型，并通过自回归预训练策略来学习PDE的底层物理规律。U-Net结构擅长处理图像数据，而PDE的解也可以看作是空间上的分布，因此U-Net具有一定的优势。自回归预训练模仿了数值求解器的迭代过程，有助于模型学习PDE的演化规律。

**技术框架**：SPUS的整体框架包括预训练和微调两个阶段。在预训练阶段，SPUS在一个包含多种流体动力学PDE的数据集上进行自回归预训练。在微调阶段，SPUS在特定的下游PDE任务上进行微调，以适应不同的物理系统。

**关键创新**：SPUS的关键创新在于：1) 采用轻量级的残差U-Net架构作为PDE求解的基础模型，显著减少了参数量和计算成本；2) 提出了一种简单而有效的自回归预训练策略，能够有效地学习PDE的底层物理规律。

**关键设计**：SPUS的U-Net架构采用残差连接，以提高训练的稳定性。自回归预训练策略通过将PDE的解在时间或空间上的相邻点作为输入和输出，来模拟数值求解器的迭代过程。损失函数采用均方误差(MSE)，以衡量预测解与真实解之间的差异。

## 📊 实验亮点

实验结果表明，SPUS在6个具有挑战性的下游PDE任务上实现了最先进的泛化性能，同时参数量远小于现有的基于Transformer的PDE基础模型。例如，SPUS在某些任务上仅使用少量微调数据即可达到与现有模型相当甚至更好的性能，突显了其参数效率和泛化能力。

## 🎯 应用场景

SPUS作为一种轻量级且参数高效的PDE基础模型，具有广泛的应用前景。它可以应用于流体动力学、热传导、电磁学等多个领域，用于加速科学计算、优化工程设计、预测物理现象等。SPUS的低计算成本使其能够在资源受限的设备上部署，例如嵌入式系统和移动设备，从而实现实时的PDE求解和预测。

## 📄 摘要（原文）

> We introduce Small PDE U-Net Solver (SPUS), a compact and efficient foundation model (FM) designed as a unified neural operator for solving a wide range of partial differential equations (PDEs). Unlike existing state-of-the-art PDE FMs-primarily based on large complex transformer architectures with high computational and parameter overhead-SPUS leverages a lightweight residual U-Net-based architecture that has been largely underexplored as a foundation model architecture in this domain. To enable effective learning in this minimalist framework, we utilize a simple yet powerful auto-regressive pretraining strategy which closely replicates the behavior of numerical solvers to learn the underlying physics. SPUS is pretrained on a diverse set of fluid dynamics PDEs and evaluated across 6 challenging unseen downstream PDEs spanning various physical systems. Experimental results demonstrate that SPUS using residual U-Net based architecture achieves state-of-the-art generalization on these downstream tasks while requiring significantly fewer parameters and minimal fine-tuning data, highlighting its potential as a highly parameter-efficient FM for solving diverse PDE systems.

