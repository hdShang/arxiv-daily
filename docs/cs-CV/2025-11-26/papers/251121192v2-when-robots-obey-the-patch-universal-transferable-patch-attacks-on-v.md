---
layout: default
title: "When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models"
---

# When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21192" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21192v2</a>
  <a href="https://arxiv.org/pdf/2511.21192.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21192v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21192v2', 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hui Lu, Yi Yu, Yiming Yang, Chenyu Yi, Qixin Zhang, Bingquan Shen, Alex C. Kot, Xudong Jiang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-26 (更新: 2025-11-30)

---

## 💡 一句话要点

**提出UPA-RFAS以解决VLA模型的通用可转移攻击问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `对抗攻击` `视觉-语言-动作` `补丁攻击` `跨模型转移` `鲁棒性增强` `信息对比损失` `机器人视觉` `安全性研究`

## 📋 核心要点

1. 现有的对抗攻击方法通常针对特定模型，缺乏通用性和可转移性，导致在黑箱环境中效果不佳。
2. 本文提出UPA-RFAS框架，通过共享特征空间学习物理补丁，增强跨模型的转移能力，解决了现有方法的局限性。
3. 实验结果显示，UPA-RFAS在不同VLA模型和任务中均能有效转移，展示了其在实际应用中的潜力。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型易受对抗攻击的影响，但现有的通用和可转移攻击研究仍然不足。大多数现有的攻击方法过拟合于单一模型，无法在黑箱设置中有效工作。为了解决这一问题，本文提出了一种系统性研究，针对VLA驱动的机器人在未知架构、微调变体和仿真到现实的转变下，提出了通用可转移的对抗补丁攻击。我们引入了UPA-RFAS（通过鲁棒特征、注意力和语义的通用补丁攻击），这是一个统一框架，旨在学习一个共享特征空间中的物理补丁，同时促进跨模型的转移。实验结果表明，UPA-RFAS在多种VLA模型、操作套件和物理执行中表现出一致的转移能力，揭示了基于补丁的攻击表面，并为未来的防御建立了强有力的基线。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉-语言-动作（VLA）模型在面对对抗攻击时的脆弱性，尤其是现有方法在黑箱设置中的通用性不足。

**核心思路**：UPA-RFAS框架通过在共享特征空间中学习一个物理补丁，结合多种损失函数和优化策略，促进补丁的跨模型转移。

**技术框架**：UPA-RFAS包括三个主要模块：特征空间目标、鲁棒性增强的两阶段最小-最大程序，以及VLA特定的损失函数。

**关键创新**：本文的主要创新在于引入了补丁注意力主导和补丁语义不对齐的损失函数，使得补丁在不同模型间的转移能力显著增强。

**关键设计**：采用$	ext{l}_1$偏差先验和信息对比损失（InfoNCE）来诱导可转移的表示变化，同时在两阶段优化中，内循环学习不可见的样本扰动，外循环则针对强化的邻域优化通用补丁。

## 📊 实验亮点

实验结果表明，UPA-RFAS在多种VLA模型上均能实现有效的补丁转移，尤其是在不同任务和视角下，表现出一致性和强大的攻击能力，为未来的防御研究提供了重要基线。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、自动驾驶、智能监控等，能够提高这些系统在面对对抗攻击时的鲁棒性。通过建立强有力的攻击基线，未来的防御机制可以更有效地针对这些攻击进行优化，提升整体安全性。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

