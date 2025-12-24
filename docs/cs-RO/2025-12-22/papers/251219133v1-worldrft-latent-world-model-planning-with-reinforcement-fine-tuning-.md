---
layout: default
title: "WorldRFT: Latent World Model Planning with Reinforcement Fine-Tuning for Autonomous Driving"
---

# WorldRFT: Latent World Model Planning with Reinforcement Fine-Tuning for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19133" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19133v1</a>
  <a href="https://arxiv.org/pdf/2512.19133.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19133v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19133v1', 'WorldRFT: Latent World Model Planning with Reinforcement Fine-Tuning for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengxuan Yang, Ben Lu, Zhongpu Xia, Chao Han, Yinfeng Gao, Teng Zhang, Kun Zhan, XianPeng Lang, Yupeng Zheng, Qichao Zhang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-22

**备注**: AAAI 2026, first version

---

## 💡 一句话要点

**WorldRFT：通过强化微调的潜在世界模型规划，提升自动驾驶安全性与规划能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `潜在世界模型` `强化学习` `分层规划` `表征学习`

## 📋 核心要点

1. 现有基于重构的潜在世界模型在自动驾驶中存在感知与规划任务耦合，导致规划优化次优。
2. WorldRFT通过分层规划分解和局部感知交互细化，对齐场景表征学习与规划，并使用强化学习微调策略。
3. 实验表明，WorldRFT在nuScenes和NavSim上均达到SOTA，显著降低碰撞率并提升驾驶性能。

## 📝 摘要（中文）

本文提出WorldRFT，一个面向规划的潜在世界模型框架，旨在通过分层规划分解和局部感知交互细化机制，以及强化学习微调(RFT)，将场景表征学习与规划对齐，从而提升自动驾驶中安全关键策略的性能。WorldRFT集成了视觉-几何基础模型以增强3D空间感知，采用分层规划任务分解来指导表征优化，并利用局部感知迭代细化来推导面向规划的驾驶策略。此外，引入了组相对策略优化(GRPO)，通过轨迹高斯化和碰撞感知奖励来微调驾驶策略，从而系统地提高安全性。WorldRFT在nuScenes和NavSim基准测试中均达到了SOTA性能。在nuScenes上，碰撞率降低了83%（0.30% -> 0.05%）。在NavSim上，仅使用摄像头传感器输入，就达到了与基于激光雷达的SOTA方法DiffusionDrive相当的性能（87.8 vs. 88.1 PDMS）。

## 🔬 方法详解

**问题定义**：现有基于潜在世界模型的自动驾驶方法，通常以重构为导向进行表征学习，这使得感知和规划任务相互纠缠，导致规划性能无法达到最优。尤其是在安全关键场景下，这种耦合会带来潜在的安全风险。现有方法难以有效利用几何信息，并且缺乏针对规划任务的优化。

**核心思路**：WorldRFT的核心思路是将场景表征学习与规划任务对齐。通过引入分层规划任务分解，引导表征学习过程，使其更加关注与规划相关的特征。同时，利用局部感知交互细化机制，迭代优化驾驶策略，使其更好地适应局部环境。此外，通过强化学习微调，进一步提升策略的安全性和性能。

**技术框架**：WorldRFT框架主要包含以下几个模块：1) 视觉-几何基础模型：用于提取场景的3D空间信息。2) 分层规划任务分解：将复杂的驾驶任务分解为多个子任务，例如路径规划、速度控制等。3) 局部感知交互细化：通过迭代的方式，根据局部环境信息调整驾驶策略。4) 强化学习微调：使用组相对策略优化(GRPO)算法，对驾驶策略进行微调，提升安全性。

**关键创新**：WorldRFT的关键创新在于：1) 面向规划的表征学习：通过分层规划任务分解，引导表征学习过程，使其更加关注与规划相关的特征。2) 局部感知交互细化：通过迭代的方式，根据局部环境信息调整驾驶策略，提高策略的适应性。3) 组相对策略优化(GRPO)：通过轨迹高斯化和碰撞感知奖励，对驾驶策略进行微调，提升安全性。

**关键设计**：视觉-几何基础模型使用了预训练的视觉模型和几何先验知识，用于提取场景的3D空间信息。分层规划任务分解将驾驶任务分解为多个子任务，每个子任务对应一个独立的策略。局部感知交互细化模块使用循环神经网络(RNN)来建模驾驶策略的动态变化。组相对策略优化(GRPO)算法使用高斯分布来建模轨迹，并引入碰撞感知奖励来约束策略的学习过程。具体参数设置和损失函数细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19133v1/figure/fig1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19133v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19133v1/figure/subfig2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

WorldRFT在nuScenes数据集上将碰撞率降低了83%（0.30% -> 0.05%），显著提升了安全性。在NavSim数据集上，仅使用摄像头传感器输入，就达到了与基于激光雷达的SOTA方法DiffusionDrive相当的性能（87.8 vs. 88.1 PDMS），表明该方法具有很强的竞争力。

## 🎯 应用场景

WorldRFT的研究成果可应用于各种自动驾驶场景，包括城市道路、高速公路和停车场等。该方法能够提升自动驾驶系统的安全性、可靠性和规划能力，降低事故风险，提高交通效率。此外，该方法还可以应用于机器人导航、虚拟现实等领域，具有广泛的应用前景。

## 📄 摘要（原文）

> Latent World Models enhance scene representation through temporal self-supervised learning, presenting a perception annotation-free paradigm for end-to-end autonomous driving. However, the reconstruction-oriented representation learning tangles perception with planning tasks, leading to suboptimal optimization for planning. To address this challenge, we propose WorldRFT, a planning-oriented latent world model framework that aligns scene representation learning with planning via a hierarchical planning decomposition and local-aware interactive refinement mechanism, augmented by reinforcement learning fine-tuning (RFT) to enhance safety-critical policy performance. Specifically, WorldRFT integrates a vision-geometry foundation model to improve 3D spatial awareness, employs hierarchical planning task decomposition to guide representation optimization, and utilizes local-aware iterative refinement to derive a planning-oriented driving policy. Furthermore, we introduce Group Relative Policy Optimization (GRPO), which applies trajectory Gaussianization and collision-aware rewards to fine-tune the driving policy, yielding systematic improvements in safety. WorldRFT achieves state-of-the-art (SOTA) performance on both open-loop nuScenes and closed-loop NavSim benchmarks. On nuScenes, it reduces collision rates by 83% (0.30% -> 0.05%). On NavSim, using camera-only sensors input, it attains competitive performance with the LiDAR-based SOTA method DiffusionDrive (87.8 vs. 88.1 PDMS).

