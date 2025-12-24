---
layout: default
title: Parkour in the Wild: Learning a General and Extensible Agile Locomotion Policy Using Multi-expert Distillation and RL Fine-tuning
---

# Parkour in the Wild: Learning a General and Extensible Agile Locomotion Policy Using Multi-expert Distillation and RL Fine-tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11164" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11164v1</a>
  <a href="https://arxiv.org/pdf/2505.11164.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11164v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11164v1', 'Parkour in the Wild: Learning a General and Extensible Agile Locomotion Policy Using Multi-expert Distillation and RL Fine-tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikita Rudin, Junzhe He, Joshua Aurand, Marco Hutter

**分类**: cs.RO

**发布日期**: 2025-05-16

---

## 💡 一句话要点

**提出多专家蒸馏与强化学习结合的灵活步态控制框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `腿式机器人` `多专家蒸馏` `强化学习` `步态控制` `环境适应性` `复杂地形` `机器人导航`

## 📋 核心要点

1. 现有的腿式机器人控制方法在多样化和非结构化环境中的泛化能力不足，限制了其应用范围。
2. 本文提出的框架结合了多专家蒸馏与强化学习微调，通过训练特定地形的专家策略来提升步态技能。
3. 实验结果表明，该方法在多地形技能合成方面显著优于现有方法，展示了在复杂环境中的优越性能。

## 📝 摘要（中文）

腿式机器人在复杂地形中表现出色，适用于搜索救援和太空探索等应用。然而，现有控制方法在多样化和非结构化环境中的泛化能力较弱。本文提出了一种新颖的灵活步态控制框架，通过结合多专家蒸馏与强化学习（RL）微调，实现了稳健的泛化能力。首先，针对特定地形训练专家策略以发展专门的步态技能，然后通过DAgger算法将这些策略蒸馏为统一的基础策略。接着，在更广泛的地形集上对蒸馏策略进行RL微调，允许通过重复微调进一步适应新地形。实验结果显示，该方法在合成多地形技能方面显著优于现有方法，并在ANYmal D机器人上验证了其在复杂环境中的灵活性和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决腿式机器人在多样化和非结构化环境中控制策略泛化能力不足的问题。现有方法往往无法有效应对不同地形的挑战，限制了机器人的应用潜力。

**核心思路**：论文提出的核心思路是结合多专家蒸馏与强化学习微调，首先训练针对特定地形的专家策略，然后将其蒸馏为统一的基础策略，最后在更广泛的地形上进行微调，以实现更好的泛化能力。

**技术框架**：整体框架包括三个主要阶段：首先，针对不同地形训练多个专家策略；其次，通过DAgger算法将这些专家策略蒸馏为一个基础策略；最后，利用强化学习对蒸馏后的策略进行微调，以适应新的地形。

**关键创新**：最重要的技术创新在于将多专家蒸馏与强化学习微调相结合，形成了一种新的步态控制策略。这种方法与现有的单一专家策略或简单的微调方法有本质区别，能够更好地应对复杂环境。

**关键设计**：在技术细节上，论文采用了深度图像作为外部输入，设计了适应性强的损失函数，并在网络结构上进行了优化，以确保策略在多样化地形上的鲁棒性。具体的参数设置和网络架构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，所提出的框架在多地形技能合成方面相比现有方法有显著提升，具体表现为在多种复杂环境中，ANYmal D机器人能够以更高的灵活性和鲁棒性完成任务，性能提升幅度达到XX%（具体数据需查阅原文）。

## 🎯 应用场景

该研究的潜在应用领域包括搜索与救援、灾后重建、以及太空探索等场景。通过提升腿式机器人在复杂和多变环境中的导航能力，该框架能够为实际任务提供更高的灵活性和适应性，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Legged robots are well-suited for navigating terrains inaccessible to wheeled robots, making them ideal for applications in search and rescue or space exploration. However, current control methods often struggle to generalize across diverse, unstructured environments. This paper introduces a novel framework for agile locomotion of legged robots by combining multi-expert distillation with reinforcement learning (RL) fine-tuning to achieve robust generalization. Initially, terrain-specific expert policies are trained to develop specialized locomotion skills. These policies are then distilled into a unified foundation policy via the DAgger algorithm. The distilled policy is subsequently fine-tuned using RL on a broader terrain set, including real-world 3D scans. The framework allows further adaptation to new terrains through repeated fine-tuning. The proposed policy leverages depth images as exteroceptive inputs, enabling robust navigation across diverse, unstructured terrains. Experimental results demonstrate significant performance improvements over existing methods in synthesizing multi-terrain skills into a single controller. Deployment on the ANYmal D robot validates the policy's ability to navigate complex environments with agility and robustness, setting a new benchmark for legged robot locomotion.

