---
layout: default
title: "LocoMamba: Vision-Driven Locomotion via End-to-End Deep Reinforcement Learning with Mamba"
---

# LocoMamba: Vision-Driven Locomotion via End-to-End Deep Reinforcement Learning with Mamba

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11849" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11849v3</a>
  <a href="https://arxiv.org/pdf/2508.11849.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11849v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11849v3', 'LocoMamba: Vision-Driven Locomotion via End-to-End Deep Reinforcement Learning with Mamba')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinuo Wang, Gavin Tao

**分类**: cs.RO, cs.AI, cs.CV, eess.IV, eess.SY

**发布日期**: 2025-08-16 (更新: 2025-12-14)

**备注**: 14 pages. This paper has been published in Advanced Engineering Informatics. Please cite the journal version: DOI: 10.1016/j.aei.2025.104230

**期刊**: Advanced Engineering Informatics, Vol. 70, Art. no. 104230 (2026)

**DOI**: [10.1016/j.aei.2025.104230](https://doi.org/10.1016/j.aei.2025.104230)

---

## 💡 一句话要点

**提出LocoMamba以解决视觉驱动的运动控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉驱动` `深度强化学习` `跨模态融合` `状态空间模型` `运动控制` `机器人导航` `训练效率`

## 📋 核心要点

1. 现有方法在复杂环境中的运动控制面临长程依赖捕捉和训练效率低下的问题。
2. LocoMamba通过选择性状态空间模型和Mamba层实现高效的序列建模，提升了状态表示和训练效率。
3. 在挑战性模拟环境中，LocoMamba相比于现有基线取得了更高的回报和成功率，且碰撞次数更少。

## 📝 摘要（中文）

我们介绍了LocoMamba，这是一种基于选择性状态空间模型的视觉驱动跨模态深度强化学习框架，特别利用Mamba实现近线性时间序列建模，有效捕捉长程依赖，并支持更长序列的高效训练。首先，我们通过多层感知机嵌入本体状态，并使用轻量级卷积神经网络对深度图像进行分块，生成紧凑的token以改善状态表示。其次，堆叠的Mamba层通过近线性时间的选择性扫描融合这些token，降低延迟和内存占用，保持对token长度和图像分辨率的鲁棒性，并提供一种归纳偏置以减轻过拟合。最后，我们在地形和外观随机化以及障碍物密度课程下，使用紧凑的状态中心奖励对策略进行端到端训练，平衡进展、平滑性和安全性。

## 🔬 方法详解

**问题定义**：本论文旨在解决在复杂环境中进行视觉驱动的运动控制时，现有方法在捕捉长程依赖和训练效率方面的不足。

**核心思路**：LocoMamba的核心思路是利用选择性状态空间模型和Mamba层，通过高效的序列建模来提升状态表示和训练效率，从而更好地应对复杂环境中的运动控制任务。

**技术框架**：LocoMamba的整体架构包括三个主要模块：首先是通过多层感知机嵌入本体状态，接着使用轻量级卷积神经网络对深度图像进行分块，最后通过堆叠的Mamba层进行token的融合和处理。

**关键创新**：LocoMamba的最重要创新在于其选择性状态空间模型和Mamba层的设计，使得序列建模的时间复杂度接近线性，显著提高了训练效率和模型的鲁棒性。

**关键设计**：在设计中，采用了紧凑的状态中心奖励机制，平衡了进展、平滑性和安全性，同时在训练过程中引入了地形和外观的随机化，以及障碍物密度的课程设置，以增强模型的泛化能力。

## 📊 实验亮点

在实验中，LocoMamba在具有静态和动态障碍物以及不平坦地形的挑战性模拟环境中表现出色，相比于最先进的基线方法，其回报和成功率显著提高，碰撞次数减少，且在相同计算预算下收敛所需的更新次数更少。

## 🎯 应用场景

LocoMamba的研究成果在机器人导航、自动驾驶和智能移动设备等领域具有广泛的应用潜力。通过提高运动控制的效率和安全性，该框架能够在复杂和动态环境中实现更高效的自主决策，推动相关技术的进步与发展。

## 📄 摘要（原文）

> We introduce LocoMamba, a vision-driven cross-modal DRL framework built on selective state-space models, specifically leveraging Mamba, that achieves near-linear-time sequence modeling, effectively captures long-range dependencies, and enables efficient training with longer sequences. First, we embed proprioceptive states with a multilayer perceptron and patchify depth images with a lightweight convolutional neural network, producing compact tokens that improve state representation. Second, stacked Mamba layers fuse these tokens via near-linear-time selective scanning, reducing latency and memory footprint, remaining robust to token length and image resolution, and providing an inductive bias that mitigates overfitting. Third, we train the policy end-to-end with Proximal Policy Optimization under terrain and appearance randomization and an obstacle-density curriculum, using a compact state-centric reward that balances progress, smoothness, and safety. We evaluate our method in challenging simulated environments with static and moving obstacles as well as uneven terrain. Compared with state-of-the-art baselines, our method achieves higher returns and success rates with fewer collisions, exhibits stronger generalization to unseen terrains and obstacle densities, and improves training efficiency by converging in fewer updates under the same compute budget.

