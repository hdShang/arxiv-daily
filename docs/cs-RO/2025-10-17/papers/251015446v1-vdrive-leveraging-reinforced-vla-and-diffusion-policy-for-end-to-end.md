---
layout: default
title: VDRive: Leveraging Reinforced VLA and Diffusion Policy for End-to-end Autonomous Driving
---

# VDRive: Leveraging Reinforced VLA and Diffusion Policy for End-to-end Autonomous Driving

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15446" target="_blank" class="toolbar-btn">arXiv: 2510.15446v1</a>
    <a href="https://arxiv.org/pdf/2510.15446.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15446v1" 
            onclick="toggleFavorite(this, '2510.15446v1', 'VDRive: Leveraging Reinforced VLA and Diffusion Policy for End-to-end Autonomous Driving')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ziang Guo, Zufeng Zhang

**分类**: cs.RO

**发布日期**: 2025-10-17

**备注**: 1st version

---

## 💡 一句话要点

**VDRive：利用强化VLA和扩散策略实现端到端自动驾驶**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `端到端学习` `视觉-语言-动作模型` `扩散策略` `强化学习`

## 📋 核心要点

1. 现有自动驾驶方法在动态环境和极端情况下，车辆状态理解和决策的鲁棒性面临挑战。
2. VDRive通过建模状态-动作映射，结合视觉-语言-动作模型和扩散策略，实现语境和几何上的驾驶引导。
3. 实验表明，VDRive在Bench2Drive和nuScenes数据集上取得了最先进的性能，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种新颖的端到端自动驾驶流程VDRive，它通过显式地建模状态-动作映射来解决动态环境和极端情况对自动驾驶鲁棒性的挑战，从而实现可解释和鲁棒的决策。VDRive利用视觉-语言-动作模型(VLA)在状态理解方面的优势，并结合基于生成扩散策略的动作头，从而在语境和几何上引导驾驶。在语境上，VLA通过token生成预训练来预测未来的观测，这些观测通过条件向量量化变分自编码器(CVQ-VAE)表示为离散代码。在几何上，我们对VLA进行强化学习微调，以基于当前的驾驶条件预测未来的轨迹和动作。VLA为动作策略头提供当前状态token和预测状态token，以生成分层动作和轨迹。在策略训练期间，一个学习到的评论家评估策略生成的动作，并提供基于梯度的反馈，形成一个actor-critic框架，从而实现基于强化的策略学习流程。实验表明，我们的VDRive在Bench2Drive闭环基准测试和nuScenes开环规划中都取得了最先进的性能。

## 🔬 方法详解

**问题定义**：自动驾驶面临动态环境和极端情况带来的挑战，现有方法在状态理解和决策方面鲁棒性不足，难以应对复杂场景。论文旨在解决端到端自动驾驶中状态理解和决策的鲁棒性问题，提升自动驾驶系统的安全性和可靠性。

**核心思路**：论文的核心思路是利用视觉-语言-动作模型（VLA）进行状态理解，并结合生成扩散策略进行动作预测，从而实现语境和几何上的驾驶引导。通过显式建模状态-动作映射，提高决策的可解释性和鲁棒性。

**技术框架**：VDRive的整体框架包含以下几个主要模块：1) 基于条件向量量化变分自编码器(CVQ-VAE)的离散状态表示；2) 基于视觉-语言-动作模型(VLA)的状态理解和未来观测预测；3) 基于生成扩散策略的动作策略头，用于生成分层动作和轨迹；4) 基于Actor-Critic的强化学习训练框架，用于优化动作策略。VLA提供当前和预测的状态token给动作策略头，动作策略头生成动作，Critic评估动作并提供反馈。

**关键创新**：论文的关键创新在于将视觉-语言-动作模型与生成扩散策略相结合，用于端到端自动驾驶。VLA负责状态理解和未来预测，扩散策略负责动作生成，二者协同工作，提高了自动驾驶系统的鲁棒性和可解释性。此外，使用强化学习对VLA进行微调，进一步提升了其性能。

**关键设计**：CVQ-VAE用于将连续的观测数据编码为离散的token表示，便于VLA进行处理。VLA通过token生成预训练来学习驾驶场景的上下文信息。动作策略头采用分层结构，生成粗粒度的轨迹和细粒度的动作。强化学习训练采用Actor-Critic框架，Critic网络评估动作的质量，并提供梯度反馈给Actor网络，从而优化动作策略。

## 📊 实验亮点

VDRive在Bench2Drive闭环基准测试和nuScenes开环规划中取得了最先进的性能。在Bench2Drive上，VDRive显著优于现有方法，证明了其在复杂驾驶场景中的鲁棒性。在nuScenes上，VDRive也取得了具有竞争力的结果，验证了其在真实世界数据集上的有效性。这些实验结果表明，VDRive是一种有前景的端到端自动驾驶解决方案。

## 🎯 应用场景

VDRive具有广泛的应用前景，可应用于各种自动驾驶场景，包括城市道路、高速公路和越野环境。该研究成果有助于提升自动驾驶系统的安全性、可靠性和智能化水平，加速自动驾驶技术的商业化落地。此外，该方法还可以扩展到其他机器人控制领域，例如无人机和移动机器人。

## 📄 摘要（原文）

> In autonomous driving, dynamic environment and corner cases pose significant challenges to the robustness of ego vehicle's state understanding and decision making. We introduce VDRive, a novel pipeline for end-to-end autonomous driving that explicitly models state-action mapping to address these challenges, enabling interpretable and robust decision making. By leveraging the advancement of the state understanding of the Vision Language Action Model (VLA) with generative diffusion policy-based action head, our VDRive guides the driving contextually and geometrically. Contextually, VLA predicts future observations through token generation pre-training, where the observations are represented as discrete codes by a Conditional Vector Quantized Variational Autoencoder (CVQ-VAE). Geometrically, we perform reinforcement learning fine-tuning of the VLA to predict future trajectories and actions based on current driving conditions. VLA supplies the current state tokens and predicted state tokens for the action policy head to generate hierarchical actions and trajectories. During policy training, a learned critic evaluates the actions generated by the policy and provides gradient-based feedback, forming an actor-critic framework that enables a reinforcement-based policy learning pipeline. Experiments show that our VDRive achieves state-of-the-art performance in the Bench2Drive closed-loop benchmark and nuScenes open-loop planning.

