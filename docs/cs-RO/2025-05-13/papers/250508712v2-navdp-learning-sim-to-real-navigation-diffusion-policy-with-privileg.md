---
layout: default
title: "NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance"
---

# NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08712" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08712v2</a>
  <a href="https://arxiv.org/pdf/2505.08712.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08712v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08712v2', 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang

**分类**: cs.RO

**发布日期**: 2025-05-13 (更新: 2025-05-15)

**备注**: Project Page: https://wzcai99.github.io/navigation-diffusion-policy.github.io/

---

## 💡 一句话要点

**提出NavDP以解决动态开放世界导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `导航策略` `扩散模型` `机器人学习` `模拟到真实` `轨迹生成` `批评学习` `自主导航`

## 📋 核心要点

1. 现有导航方法依赖于精确定位和昂贵的真实示例，难以适应动态开放世界环境。
2. NavDP框架通过扩散轨迹生成和批评函数选择，利用模拟中的全局信息进行训练，具备零-shot迁移能力。
3. NavDP在多种机器人平台上表现出色，成功率提高30%，并在不同环境中展现出良好的泛化能力。

## 📝 摘要（中文）

在动态开放世界环境中学习导航是机器人面临的重要挑战。大多数现有方法依赖于精确的定位和映射，或从昂贵的真实世界示例中学习。本文提出了导航扩散策略（NavDP），这是一个完全在模拟中训练的端到端框架，能够零-shot迁移到不同的真实环境中。NavDP的网络核心是基于扩散的轨迹生成与轨迹选择的批评函数的结合，条件仅基于从共享策略变换器编码的局部观察令牌。通过利用模拟中的全局环境特权信息，我们生成高质量的演示以训练扩散策略，并使用对比负样本来制定批评值函数目标。实验结果表明，NavDP在多种室内外环境中的四足、轮式和类人机器人上实现了最先进的性能和卓越的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在动态开放世界中导航的挑战，现有方法往往依赖于精确的定位和昂贵的真实世界示例，限制了其适应性和效率。

**核心思路**：NavDP通过在模拟环境中训练，结合扩散轨迹生成和批评函数选择，利用全局环境信息生成高质量的演示，从而实现零-shot迁移到真实环境。

**技术框架**：NavDP的整体架构包括轨迹生成模块和批评模块，前者负责生成候选轨迹，后者则对轨迹进行评估和选择，整个过程依赖于共享的策略变换器对局部观察的编码。

**关键创新**：NavDP的核心创新在于将扩散模型与批评学习相结合，利用模拟中的全局信息生成大量高质量轨迹，显著提高了训练效率和效果。

**关键设计**：在设计中，使用对比负样本来制定批评值函数目标，确保生成的轨迹具有较高的质量。此外，演示生成效率达到每天2500条轨迹/GPU，远超真实数据收集的效率。

## 📊 实验亮点

实验结果显示，NavDP在多种机器人平台上实现了最先进的性能，成功率提高了30%。在1244个场景中生成了363.2公里的轨迹数据，展示了其卓越的泛化能力和高效的数据生成能力。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人导航、智能交通系统和无人机飞行等。通过在模拟环境中高效训练，NavDP能够快速适应不同的真实环境，降低了机器人部署的成本和时间，具有广泛的实际价值和影响。

## 📄 摘要（原文）

> Learning navigation in dynamic open-world environments is an important yet challenging skill for robots. Most previous methods rely on precise localization and mapping or learn from expensive real-world demonstrations. In this paper, we propose the Navigation Diffusion Policy (NavDP), an end-to-end framework trained solely in simulation and can zero-shot transfer to different embodiments in diverse real-world environments. The key ingredient of NavDP's network is the combination of diffusion-based trajectory generation and a critic function for trajectory selection, which are conditioned on only local observation tokens encoded from a shared policy transformer. Given the privileged information of the global environment in simulation, we scale up the demonstrations of good quality to train the diffusion policy and formulate the critic value function targets with contrastive negative samples. Our demonstration generation approach achieves about 2,500 trajectories/GPU per day, 20$\times$ more efficient than real-world data collection, and results in a large-scale navigation dataset with 363.2km trajectories across 1244 scenes. Trained with this simulation dataset, NavDP achieves state-of-the-art performance and consistently outstanding generalization capability on quadruped, wheeled, and humanoid robots in diverse indoor and outdoor environments. In addition, we present a preliminary attempt at using Gaussian Splatting to make in-domain real-to-sim fine-tuning to further bridge the sim-to-real gap. Experiments show that adding such real-to-sim data can improve the success rate by 30\% without hurting its generalization capability.

