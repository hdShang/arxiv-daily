---
layout: default
title: UrbanVLA: A Vision-Language-Action Model for Urban Micromobility
---

# UrbanVLA: A Vision-Language-Action Model for Urban Micromobility

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23576" target="_blank" class="toolbar-btn">arXiv: 2510.23576v1</a>
    <a href="https://arxiv.org/pdf/2510.23576.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23576v1" 
            onclick="toggleFavorite(this, '2510.23576v1', 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Anqi Li, Zhiyong Wang, Jiazhao Zhang, Minghan Li, Yunpeng Qi, Zhibo Chen, Zhizheng Zhang, He Wang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-10-27

---

## 💡 一句话要点

**提出UrbanVLA，用于城市微出行场景下基于视觉-语言-动作的导航。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市微出行` `视觉语言动作模型` `机器人导航` `强化学习` `视觉语言对齐`

## 📋 核心要点

1. 现有导航方法难以应对真实城市环境的动态性和非结构化特性，通常只适用于短距离和可控场景。
2. UrbanVLA通过将视觉观察与路线航点对齐，并结合两阶段训练，实现城市环境下的可靠导航。
3. 实验表明，UrbanVLA在模拟和真实环境中均优于现有方法，提升显著，展现了良好的泛化能力。

## 📝 摘要（中文）

本文提出UrbanVLA，一个基于视觉-语言-动作（VLA）的框架，专为可扩展的城市导航而设计，尤其适用于城市微出行应用，如送货机器人。该方法显式地将带噪声的路线航点与执行过程中的视觉观察对齐，并据此规划机器人轨迹。为了使UrbanVLA掌握低级（如点目标到达和避障）和高级（如路线-视觉对齐）导航能力，采用了两阶段训练流程：首先使用模拟环境和从网络视频解析出的轨迹进行监督微调（SFT），然后使用模拟和真实世界数据的混合进行强化微调（RFT），以增强模型在真实环境中的安全性和适应性。实验表明，UrbanVLA在MetaUrban的SocialNav任务中超越了强大的基线55%以上，并在真实世界导航中表现出可靠性，展示了其在大型城市环境中的可扩展性和对真实世界不确定性的鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决城市微出行应用中，机器人如何在复杂、动态的城市环境中，根据长距离路线指令进行可靠导航的问题。现有方法通常难以应对真实城市环境的复杂性和不确定性，例如遮挡、光照变化、行人干扰等，导致导航性能下降。

**核心思路**：论文的核心思路是将视觉信息与语言指令（路线航点）相结合，通过视觉-语言对齐来增强机器人对环境的理解，并利用强化学习提升其在真实环境中的适应性。这种方法旨在弥合模拟环境与真实环境之间的差距，提高导航的鲁棒性和可靠性。

**技术框架**：UrbanVLA框架包含以下主要模块：1) 视觉感知模块，用于从摄像头获取图像信息；2) 语言理解模块，用于解析路线航点指令；3) 视觉-语言对齐模块，用于将视觉信息与路线航点进行关联；4) 轨迹规划模块，用于生成机器人的运动轨迹；5) 动作执行模块，用于控制机器人的运动。训练过程分为两个阶段：监督微调（SFT）和强化微调（RFT）。SFT阶段使用模拟环境和网络视频数据进行预训练，RFT阶段使用模拟和真实世界数据的混合进行微调。

**关键创新**：UrbanVLA的关键创新在于其显式的视觉-语言对齐机制，该机制能够有效地将路线航点与视觉观察进行关联，从而提高机器人对环境的理解和导航的准确性。此外，两阶段训练策略也至关重要，它使得模型能够从模拟环境迁移到真实环境，并具备良好的泛化能力。

**关键设计**：在视觉-语言对齐模块中，可能使用了注意力机制或Transformer结构，以实现视觉特征与语言特征的有效融合。在强化微调阶段，可能使用了Proximal Policy Optimization (PPO) 或其他类似的算法，并设计了合适的奖励函数，以鼓励机器人安全、高效地完成导航任务。具体的网络结构、损失函数和参数设置等细节，需要参考论文原文。

## 📊 实验亮点

UrbanVLA在MetaUrban的SocialNav任务中，性能超越了现有基线方法55%以上，表明其在模拟环境中的优越性。此外，UrbanVLA还在真实世界导航实验中表现出可靠性，验证了其在复杂城市环境中的泛化能力和鲁棒性。这些结果表明，UrbanVLA是一种有效的城市导航解决方案。

## 🎯 应用场景

UrbanVLA具有广泛的应用前景，可用于送货机器人、自动驾驶车辆、智能轮椅等城市微出行设备。该研究有助于提高这些设备在复杂城市环境中的导航能力，降低运营成本，并提升用户体验。未来，该技术有望应用于智慧城市建设，例如智能交通管理、环境监测等。

## 📄 摘要（原文）

> Urban micromobility applications, such as delivery robots, demand reliable navigation across large-scale urban environments while following long-horizon route instructions. This task is particularly challenging due to the dynamic and unstructured nature of real-world city areas, yet most existing navigation methods remain tailored to short-scale and controllable scenarios. Effective urban micromobility requires two complementary levels of navigation skills: low-level capabilities such as point-goal reaching and obstacle avoidance, and high-level capabilities, such as route-visual alignment. To this end, we propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework designed for scalable urban navigation. Our method explicitly aligns noisy route waypoints with visual observations during execution, and subsequently plans trajectories to drive the robot. To enable UrbanVLA to master both levels of navigation, we employ a two-stage training pipeline. The process begins with Supervised Fine-Tuning (SFT) using simulated environments and trajectories parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on a mixture of simulation and real-world data, which enhances the model's safety and adaptability in real-world settings. Experiments demonstrate that UrbanVLA surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban. Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both scalability to large-scale urban environments and robustness against real-world uncertainties.

