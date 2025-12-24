---
layout: default
title: "SViP: Sequencing Bimanual Visuomotor Policies with Object-Centric Motion Primitives"
---

# SViP: Sequencing Bimanual Visuomotor Policies with Object-Centric Motion Primitives

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18825" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18825v1</a>
  <a href="https://arxiv.org/pdf/2506.18825.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18825v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18825v1', 'SViP: Sequencing Bimanual Visuomotor Policies with Object-Centric Motion Primitives')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yizhou Chen, Hang Xu, Dongjie Yu, Zeqing Zhang, Yi Ren, Jia Pan

**分类**: cs.RO

**发布日期**: 2025-06-23

**备注**: Project website: https://sites.google.com/view/svip-bimanual

---

## 💡 一句话要点

**提出SViP框架以解决双手视觉运动策略的泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `双手操作` `视觉运动策略` `模仿学习` `任务规划` `运动规划` `泛化能力` `机器人技术` `智能制造`

## 📋 核心要点

1. 现有的视觉运动策略在小规模示范数据集下泛化能力有限，且在长时间任务中容易累积错误。
2. SViP框架通过将视觉运动策略与任务和运动规划相结合，利用语义场景图监控来分离操作，增强了策略的泛化能力。
3. 实验表明，SViP在仅使用20个示范的情况下，能够在未见过的任务中自动发现有效解决方案，并超越了现有的生成IL方法。

## 📝 摘要（中文）

模仿学习（IL）在高维视觉输入下的策略训练中已被证明在复杂的双手操作任务中直观且有效。然而，视觉运动策略的泛化能力仍然有限，尤其是在可用示范数据集较小的情况下。为了解决这些问题，本文提出了SViP框架，该框架将视觉运动策略与任务和运动规划（TAMP）无缝集成。SViP通过语义场景图监控将人类示范分为双手和单手操作，并利用关键场景图中的连续决策变量训练切换条件生成器。该生成器生成参数化的脚本原语，即使在遇到分布外观察时也能确保可靠性能。通过仅使用20个真实世界的示范，SViP展示了其在分布外初始条件下的泛化能力，并且在未见过的任务中自动发现有效解决方案。实验结果表明，SViP在实际应用中超越了现有的生成IL方法，显示出更广泛的适用性。

## 🔬 方法详解

**问题定义**：本论文旨在解决双手视觉运动策略在小规模示范数据集下的泛化能力不足问题，现有方法在长时间任务中容易累积错误，导致性能下降。

**核心思路**：提出SViP框架，通过将视觉运动策略与任务和运动规划（TAMP）结合，利用语义场景图监控将人类示范分为双手和单手操作，从而提高策略的泛化能力。

**技术框架**：SViP框架主要包括三个模块：1) 语义场景图监控，用于分离双手和单手操作；2) 切换条件生成器，基于关键场景图的连续决策变量生成参数化脚本原语；3) 约束建模，帮助在未见过的任务中自动发现有效解决方案。

**关键创新**：SViP的核心创新在于其将视觉运动策略与任务和运动规划的结合，利用语义场景图监控和切换条件生成器，确保在分布外观察下的可靠性能。这与现有方法的本质区别在于其更强的泛化能力和自动化解决方案发现能力。

**关键设计**：在设计中，关键参数设置包括切换条件生成器的训练过程，以及损失函数的选择，确保生成的脚本原语能够适应不同的操作场景。网络结构方面，采用了深度学习模型来处理高维视觉输入，提升了策略的学习效率。

## 📊 实验亮点

在实验中，SViP框架仅使用20个真实世界的示范，便能在分布外初始条件下实现有效的策略泛化，且在未见过的任务中自动发现解决方案。与现有的生成IL方法相比，SViP在性能上有显著提升，展示了更广泛的适用性。

## 🎯 应用场景

SViP框架的潜在应用领域包括机器人抓取、双手协作操作以及复杂的工业自动化任务。其能够在小规模示范数据下实现高效的策略泛化，具有重要的实际价值，未来可广泛应用于智能制造、服务机器人等领域，推动人机协作的发展。

## 📄 摘要（原文）

> Imitation learning (IL), particularly when leveraging high-dimensional visual inputs for policy training, has proven intuitive and effective in complex bimanual manipulation tasks. Nonetheless, the generalization capability of visuomotor policies remains limited, especially when small demonstration datasets are available. Accumulated errors in visuomotor policies significantly hinder their ability to complete long-horizon tasks. To address these limitations, we propose SViP, a framework that seamlessly integrates visuomotor policies into task and motion planning (TAMP). SViP partitions human demonstrations into bimanual and unimanual operations using a semantic scene graph monitor. Continuous decision variables from the key scene graph are employed to train a switching condition generator. This generator produces parameterized scripted primitives that ensure reliable performance even when encountering out-of-the-distribution observations. Using only 20 real-world demonstrations, we show that SViP enables visuomotor policies to generalize across out-of-distribution initial conditions without requiring object pose estimators. For previously unseen tasks, SViP automatically discovers effective solutions to achieve the goal, leveraging constraint modeling in TAMP formulism. In real-world experiments, SViP outperforms state-of-the-art generative IL methods, indicating wider applicability for more complex tasks. Project website: https://sites.google.com/view/svip-bimanual

