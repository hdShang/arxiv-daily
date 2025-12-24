---
layout: default
title: "CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation"
---

# CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01600" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01600v1</a>
  <a href="https://arxiv.org/pdf/2508.01600.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01600v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01600v1', 'CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sung-Wook Lee, Xuhui Kang, Brandon Yang, Yen-Ling Kuo

**分类**: cs.RO

**发布日期**: 2025-08-03

**备注**: To appear in Proceedings of the Conference on Robot Learning (CoRL) 2025

---

## 💡 一句话要点

**提出CLASS以解决异构数据集下机器人操作的泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `行为克隆` `对比学习` `动作序列` `动态时间规整` `机器人操作` `泛化能力` `视觉变化`

## 📋 核心要点

1. 现有的行为克隆方法在处理异构数据集时容易过拟合单个演示，导致泛化能力不足。
2. 本文提出的CLASS方法通过对比学习和动态时间规整，利用相似动作序列进行弱监督，提升了行为表示的学习效果。
3. 在多个仿真和真实任务中，CLASS方法显著提高了机器人操作的成功率，尤其在视觉变化显著的情况下表现优异。

## 📝 摘要（中文）

近年来，行为克隆（BC）在机器人操作中取得了显著进展，但在处理异构数据集时面临重大挑战，尤其是在视觉变化和对象外观不同的情况下，性能下降。为了解决这一问题，本文提出了通过动作序列监督的对比学习方法（CLASS），该方法利用动态时间规整（DTW）识别的相似动作序列进行弱监督，并优化了带有相似性加权正样本对的软InfoNCE损失。我们在5个仿真基准和3个真实任务上评估了CLASS，结果显示其在仅使用表示的检索控制中取得了竞争性结果。尤其是在显著视觉变化下，经过CLASS预训练的扩散策略的平均成功率达到了75%，而其他基线方法未能表现出竞争力。

## 🔬 方法详解

**问题定义**：本文旨在解决行为克隆在异构数据集下的泛化能力不足问题。现有方法往往过拟合个别演示，无法有效捕捉共享结构，导致在不同视觉条件下性能下降。

**核心思路**：论文提出的CLASS方法通过对比学习框架，利用动态时间规整（DTW）识别的相似动作序列进行弱监督，优化行为表示的学习过程，从而增强模型的泛化能力。

**技术框架**：CLASS的整体架构包括相似动作序列的识别、对比学习损失的优化和行为表示的学习。主要模块包括DTW相似性计算、软InfoNCE损失函数和行为表示网络。

**关键创新**：CLASS的核心创新在于将对比学习与动作序列监督结合，利用相似性加权的正样本对来优化损失函数，从而有效提升了模型在异构数据集上的表现。

**关键设计**：在损失函数设计上，采用了软InfoNCE损失，结合相似性加权的正样本对。此外，网络结构经过精心设计，以适应不同的动作序列输入，确保学习到的表示具有较强的泛化能力。

## 📊 实验亮点

在实验中，经过CLASS预训练的扩散策略在显著视觉变化下的平均成功率达到了75%，而其他基线方法未能在同样条件下表现出竞争力，显示了CLASS在处理异构数据集时的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和智能家居等。通过提高机器人在复杂环境中的操作能力，CLASS方法能够显著提升机器人在实际应用中的表现，推动智能机器人技术的进一步发展。

## 📄 摘要（原文）

> Recent advances in Behavior Cloning (BC) have led to strong performance in robotic manipulation, driven by expressive models, sequence modeling of actions, and large-scale demonstration data. However, BC faces significant challenges when applied to heterogeneous datasets, such as visual shift with different camera poses or object appearances, where performance degrades despite the benefits of learning at scale. This stems from BC's tendency to overfit individual demonstrations rather than capture shared structure, limiting generalization. To address this, we introduce Contrastive Learning via Action Sequence Supervision (CLASS), a method for learning behavioral representations from demonstrations using supervised contrastive learning. CLASS leverages weak supervision from similar action sequences identified via Dynamic Time Warping (DTW) and optimizes a soft InfoNCE loss with similarity-weighted positive pairs. We evaluate CLASS on 5 simulation benchmarks and 3 real-world tasks to achieve competitive results using retrieval-based control with representations only. Most notably, for downstream policy learning under significant visual shifts, Diffusion Policy with CLASS pre-training achieves an average success rate of 75%, while all other baseline methods fail to perform competitively. Project webpage: https://class-robot.github.io.

