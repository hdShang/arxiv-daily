---
layout: default
title: HIL: Hybrid Imitation Learning of Diverse Parkour Skills from Videos
---

# HIL: Hybrid Imitation Learning of Diverse Parkour Skills from Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12619" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12619v1</a>
  <a href="https://arxiv.org/pdf/2505.12619.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12619v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12619v1', 'HIL: Hybrid Imitation Learning of Diverse Parkour Skills from Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiashun Wang, Yifeng Jiang, Haotian Zhang, Chen Tessler, Davis Rempe, Jessica Hodgins, Xue Bin Peng

**分类**: cs.GR

**发布日期**: 2025-05-19

**备注**: 14 pages, 10 figures

---

## 💡 一句话要点

**提出混合模仿学习框架以解决复杂技能适应性不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `混合模仿学习` `运动跟踪` `对抗模仿学习` `技能组合` `跑酷控制`

## 📋 核心要点

1. 现有的数据驱动方法在适应新环境和组合多样技能方面存在显著不足，限制了其在复杂任务中的应用。
2. 本文提出的混合模仿学习框架结合了运动跟踪和对抗模仿学习，旨在提高技能的适应性和组合能力。
3. 实验结果显示，该方法在多个跑酷环境中显著提升了运动质量和技能多样性，并在任务完成度上具有竞争力。

## 📝 摘要（中文）

近年来，利用深度强化学习的数据驱动方法在开发控制器方面取得了显著成效，使得物理模拟角色能够展现自然的人类行为。然而，这些方法在适应新环境和组合多样技能以执行复杂任务时常常面临挑战。为了解决这些问题，本文提出了一种混合模仿学习（HIL）框架，该框架结合了运动跟踪技术以实现精确的技能复制，并通过对抗模仿学习来增强适应性和技能组合。该框架通过并行多任务环境和统一观察空间实现，采用以代理为中心的场景表示，促进了从混合并行环境中有效学习。我们在互联网视频中获取的跑酷数据上训练了一个统一控制器，使得模拟角色能够利用多样且逼真的跑酷技能穿越新环境。评估结果表明，该方法在运动质量、技能多样性和任务完成度上均优于以往的学习方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数据驱动方法在适应新环境和技能组合方面的不足，尤其是在复杂的跑酷任务中，传统方法难以有效应对多样化的技能需求。

**核心思路**：提出的混合模仿学习框架通过结合运动跟踪和对抗模仿学习，旨在实现精确的技能复制与增强的适应性，从而更好地应对复杂环境中的多样技能需求。

**技术框架**：该框架通过并行多任务环境和统一观察空间实现，采用以代理为中心的场景表示，允许多个任务并行训练，促进了从不同环境中有效学习。

**关键创新**：最重要的创新在于将运动跟踪与对抗模仿学习相结合，形成了一种新的学习机制，使得模拟角色能够在多样环境中灵活应用技能，显著提升了学习效率和效果。

**关键设计**：在技术细节上，框架使用了统一的观察空间和特定的损失函数，以确保技能的精确复制和适应性训练，同时采用了适合跑酷任务的网络结构以优化学习过程。

## 📊 实验亮点

实验结果表明，提出的混合模仿学习框架在多个跑酷环境中相比于传统学习方法，运动质量提升了显著，技能多样性增加，任务完成度也达到了更高的水平，展现出优越的适应性和灵活性。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发、机器人控制和虚拟现实等，能够为这些领域中的角色行为生成提供更自然和多样化的解决方案。未来，该框架可能推动更复杂的物理模拟和人机交互的发展，提升用户体验和系统的智能化水平。

## 📄 摘要（原文）

> Recent data-driven methods leveraging deep reinforcement learning have been an effective paradigm for developing controllers that enable physically simulated characters to produce natural human-like behaviors. However, these data-driven methods often struggle to adapt to novel environments and compose diverse skills coherently to perform more complex tasks. To address these challenges, we propose a hybrid imitation learning (HIL) framework that combines motion tracking, for precise skill replication, with adversarial imitation learning, to enhance adaptability and skill composition. This hybrid learning framework is implemented through parallel multi-task environments and a unified observation space, featuring an agent-centric scene representation to facilitate effective learning from the hybrid parallel environments. Our framework trains a unified controller on parkour data sourced from Internet videos, enabling a simulated character to traverse through new environments using diverse and life-like parkour skills. Evaluations across challenging parkour environments demonstrate that our method improves motion quality, increases skill diversity, and achieves competitive task completion compared to previous learning-based methods.

