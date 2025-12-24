---
layout: default
title: "Panda: A pretrained forecast model for chaotic dynamics"
---

# Panda: A pretrained forecast model for chaotic dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13755" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13755v2</a>
  <a href="https://arxiv.org/pdf/2505.13755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13755v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13755v2', 'Panda: A pretrained forecast model for chaotic dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeffrey Lai, Anthony Bao, William Gilpin

**分类**: cs.LG, cs.NE, nlin.CD, stat.ML

**发布日期**: 2025-05-19 (更新: 2025-10-13)

---

## 💡 一句话要点

**提出Panda模型以解决混沌动力学预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混沌动力学` `数据驱动模型` `零-shot学习` `补丁注意力机制` `偏微分方程` `神经缩放定律` `模型泛化` `动态系统理论`

## 📋 核心要点

1. 现有方法通常针对单个时间序列进行专门训练，或在缺乏动态结构的庞大时间序列数据库上训练，导致预测效果不佳。
2. Panda模型通过补丁注意力机制，利用合成数据集进行训练，旨在提高混沌系统的预测能力，尤其是在零-shot场景下。
3. 实验结果表明，Panda在未见混沌系统的短期准确性和长期统计特性上均表现优异，且具备预测偏微分方程的能力。

## 📝 摘要（中文）

混沌系统对微小误差极为敏感，这使得基于数据驱动的预测模型在流体流动或神经活动等真实动态系统中面临挑战。以动态系统理论为基础，本文提出了Panda模型，即非线性动力学的补丁注意力机制。Panda在一个新颖的合成数据集上进行训练，该数据集包含$2 	imes 10^4$个混沌动力学系统。尽管仅在低维常微分方程上训练，Panda却展现出零-shot预测未见混沌系统的能力，并能够在不重新训练的情况下预测偏微分方程。我们还展示了微分方程的神经缩放定律，强调了预训练模型在探究非线性动力学等抽象数学领域的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决混沌动力学系统的预测问题，现有方法在处理复杂动态系统时常常面临训练数据不足或模型泛化能力差的挑战。

**核心思路**：Panda模型通过补丁注意力机制，利用合成的混沌动力学数据集进行训练，旨在实现对未见系统的有效预测，特别是在零-shot学习场景中。

**技术框架**：Panda的整体架构包括数据生成模块、模型训练模块和预测模块。数据生成模块使用进化算法生成多种混沌系统，模型训练模块采用补丁注意力机制进行学习，预测模块则负责对新系统进行预测。

**关键创新**：Panda的主要创新在于其能够在未见的混沌系统上进行零-shot预测，并且在不重新训练的情况下能够处理偏微分方程，这与现有方法的训练依赖性形成鲜明对比。

**关键设计**：在模型设计中，Panda使用了特定的损失函数来优化预测精度，并采用了适合低维常微分方程的网络结构，以确保模型在复杂动态环境中的有效性。具体参数设置和网络结构细节在论文中进行了详细说明。

## 📊 实验亮点

实验结果显示，Panda在零-shot预测未见混沌系统时，短期预测准确性和长期统计特性均优于现有基线模型。此外，Panda在处理偏微分方程时表现出色，展示了其广泛的适用性和强大的预测能力。

## 🎯 应用场景

Panda模型在科学计算、气候预测、金融市场分析等领域具有广泛的应用潜力。其能够有效处理复杂的动态系统，为研究者提供了一种新的工具来探索和理解混沌现象，未来可能推动相关领域的理论发展和应用创新。

## 📄 摘要（原文）

> Chaotic systems are intrinsically sensitive to small errors, challenging efforts to construct predictive data-driven models of real-world dynamical systems such as fluid flows or neuronal activity. Prior efforts comprise either specialized models trained separately on individual time series, or foundation models trained on vast time series databases with little underlying dynamical structure. Motivated by dynamical systems theory, we present Panda, Patched Attention for Nonlinear Dynamics. We train Panda on a novel synthetic, extensible dataset of $2 \times 10^4$ chaotic dynamical systems that we discover using an evolutionary algorithm. Trained purely on simulated data, Panda exhibits emergent properties: zero-shot forecasting of unseen chaotic systems preserving both short-term accuracy and long-term statistics. Despite having been trained only on low-dimensional ordinary differential equations, Panda spontaneously develops the ability to predict partial differential equations without retraining. We also demonstrate a neural scaling law for differential equations, underscoring the potential of pretrained models for probing abstract mathematical domains like nonlinear dynamics.

