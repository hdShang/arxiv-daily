---
layout: default
title: GRoQ-LoCO: Generalist and Robot-agnostic Quadruped Locomotion Control using Offline Datasets
---

# GRoQ-LoCO: Generalist and Robot-agnostic Quadruped Locomotion Control using Offline Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10973" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10973v3</a>
  <a href="https://arxiv.org/pdf/2505.10973.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10973v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10973v3', 'GRoQ-LoCO: Generalist and Robot-agnostic Quadruped Locomotion Control using Offline Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Narayanan PP, Sarvesh Prasanth Venkatesan, Srinivas Kantha Reddy, Shishir Kolathaya

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-16 (更新: 2025-05-24)

**备注**: 18pages, 16figures, 6tables

---

## 💡 一句话要点

**提出GRoQ-LoCO以解决四足机器人通用运动控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `四足机器人` `运动控制` `离线学习` `通用策略` `行为融合` `动态适应性` `数据驱动`

## 📋 核心要点

1. 现有方法在腿部运动控制中面临动态连续性和实时适应的挑战，难以实现跨机器人和地形的通用性。
2. 论文提出GRoQ-LoCO框架，通过离线数据集学习通用运动策略，利用专家演示实现行为融合，且不依赖于机器人特定编码。
3. 实验结果显示，该方法在多种四足机器人上实现了成功的零-shot迁移，且在不同地形上无需微调即可运行。

## 📝 摘要（中文）

近年来，大规模离线训练的进展展示了通用策略学习在复杂机器人任务中的潜力。然而，将这些原则应用于腿部运动仍然面临挑战，尤其是在动态连续性和实时适应不同地形及机器人形态方面。本文提出了GRoQ-LoCO，一个可扩展的基于注意力的框架，能够在多个四足机器人和地形上学习单一的通用运动策略，完全依赖离线数据集。该方法利用来自两种不同运动行为的专家演示，训练出一个能够融合行为的通用模型。实验结果表明，该框架在不同四足机器人和地形上实现了零-shot迁移，且在Unitree Go1等硬件上成功部署，展示了离线数据驱动学习在多样化四足机器人形态和行为上的广泛适应性。

## 🔬 方法详解

**问题定义**：本文旨在解决四足机器人在多样化地形上实现通用运动控制的问题。现有方法往往依赖于特定机器人或实时优化，限制了其适应性和通用性。

**核心思路**：GRoQ-LoCO框架通过离线数据集学习通用运动策略，利用来自不同机器人和运动行为的专家演示，避免了对机器人特定编码的依赖，从而实现跨机器人和地形的通用性。

**技术框架**：该框架包括数据收集、模型训练和策略部署三个主要模块。数据收集阶段获取不同机器人在不同地形上的运动数据，模型训练阶段利用这些数据训练通用策略，最后在目标机器人上进行策略部署。

**关键创新**：最重要的创新在于提出了一种不依赖于机器人特定编码的通用运动策略学习方法，能够在多种四足机器人上实现零-shot迁移，显著提高了适应性和灵活性。

**关键设计**：在模型设计上，采用了基于注意力机制的网络结构，结合了不同运动行为的专家演示，损失函数设计上注重行为融合的效果，确保模型能够在多样化的地形上稳定运行。

## 📊 实验亮点

实验结果表明，GRoQ-LoCO在多种四足机器人上实现了零-shot迁移，成功在Unitree Go1等机器人上进行硬件部署，且在不同地形上无需微调即可运行，展示了其在通用运动控制方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人和探索机器人等，能够在复杂和多变的环境中实现高效的运动控制。其通用性和适应性为未来机器人技术的发展提供了新的思路，可能会推动机器人在实际应用中的广泛部署。

## 📄 摘要（原文）

> Recent advancements in large-scale offline training have demonstrated the potential of generalist policy learning for complex robotic tasks. However, applying these principles to legged locomotion remains a challenge due to continuous dynamics and the need for real-time adaptation across diverse terrains and robot morphologies. In this work, we propose GRoQ-LoCO, a scalable, attention-based framework that learns a single generalist locomotion policy across multiple quadruped robots and terrains, relying solely on offline datasets. Our approach leverages expert demonstrations from two distinct locomotion behaviors - stair traversal (non-periodic gaits) and flat terrain traversal (periodic gaits) - collected across multiple quadruped robots, to train a generalist model that enables behavior fusion. Crucially, our framework operates solely on proprioceptive data from all robots without incorporating any robot-specific encodings. The policy is directly deployable on an Intel i7 nuc, producing low-latency control outputs without any test-time optimization. Our extensive experiments demonstrate zero-shot transfer across highly diverse quadruped robots and terrains, including hardware deployment on the Unitree Go1, a commercially available 12kg robot. Notably, we evaluate challenging cross-robot training setups where different locomotion skills are unevenly distributed across robots, yet observe successful transfer of both flat walking and stair traversal behaviors to all robots at test time. We also show preliminary walking on Stoch 5, a 70kg quadruped, on flat and outdoor terrains without requiring any fine tuning. These results demonstrate the potential of offline, data-driven learning to generalize locomotion across diverse quadruped morphologies and behaviors.

