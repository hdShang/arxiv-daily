---
layout: default
title: "PulseRide: A Robotic Wheelchair for Personalized Exertion Control with Human-in-the-Loop Reinforcement Learning"
---

# PulseRide: A Robotic Wheelchair for Personalized Exertion Control with Human-in-the-Loop Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05056" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05056v1</a>
  <a href="https://arxiv.org/pdf/2506.05056.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05056v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05056v1', 'PulseRide: A Robotic Wheelchair for Personalized Exertion Control with Human-in-the-Loop Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Azizul Zahid, Bibek Poudel, Danny Scott, Jason Scott, Scott Crouter, Weizi Li, Sai Swaminathan

**分类**: cs.RO, cs.HC

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出PulseRide以解决轮椅用户个性化运动控制问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `个性化辅助` `生理数据监测` `深度强化学习` `轮椅技术` `运动控制` `康复医学` `用户体验`

## 📋 核心要点

1. 现有的轮椅辅助系统主要关注障碍物规避和导航，未能有效解决用户的个性化运动需求。
2. PulseRide通过实时监测用户的生理数据，结合深度强化学习算法，提供个性化的推力辅助，帮助用户维持适度的身体活动。
3. 实验结果表明，PulseRide能使用户的心率在适度活动区间内保持71.7%的时间，并减少41.86%的肌肉收缩，延缓疲劳感的出现。

## 📝 摘要（中文）

保持活跃的生活方式对轮椅用户的生活质量至关重要，但面临诸多挑战。电动轮椅用户因缺乏活动而面临肥胖和身体机能下降的风险，而手动轮椅用户则因重复动作而遭受上肢损伤。为此，本文提出PulseRide，一个基于用户生理反应提供个性化辅助的轮椅系统。与传统的辅助系统不同，PulseRide实时整合心率和心电图等生理数据，利用人机交互强化学习方法调整推力，帮助用户保持适度的身体活动。初步测试结果显示，PulseRide在多种地形上有效延长了用户的心率在适度活动区间的时间，并显著减少了肌肉收缩，提升了舒适度和参与感。

## 🔬 方法详解

**问题定义**：本文旨在解决轮椅用户在保持身体活动时面临的个性化运动控制问题。现有方法往往忽视用户的生理反馈，导致运动效果不佳和潜在的伤害风险。

**核心思路**：PulseRide的核心思路是通过实时监测用户的生理数据（如心率和心电图），结合深度强化学习算法，动态调整推力辅助，以帮助用户维持在适度的身体活动范围内。

**技术框架**：PulseRide系统包括生理数据采集模块、数据处理模块和推力控制模块。生理数据通过传感器实时收集，经过处理后输入到强化学习算法中，系统根据用户的反馈调整推力。

**关键创新**：PulseRide的创新之处在于其人机交互强化学习方法，利用深度Q网络（DQN）算法实现个性化的推力调整。这一方法与传统的静态辅助系统有本质区别，能够根据用户的实时需求进行动态响应。

**关键设计**：系统设计中，关键参数包括心率阈值的设定和推力调整的策略。损失函数采用了与用户生理状态相关的动态调整机制，以确保用户在适度活动区间内获得最佳支持。

## 📊 实验亮点

实验结果显示，PulseRide能够使用户的心率在适度活动区间内保持71.7%的时间，较手动轮椅显著提升。同时，用户的肌肉收缩减少了41.86%，有效延缓了疲劳的出现，提升了整体的舒适度和参与感。

## 🎯 应用场景

PulseRide的潜在应用领域包括康复医学、老年护理和残疾人辅助技术等。该系统不仅能够提升轮椅用户的生活质量，还能为相关领域的研究提供新的思路和方法，推动个性化辅助技术的发展。

## 📄 摘要（原文）

> Maintaining an active lifestyle is vital for quality of life, yet challenging for wheelchair users. For instance, powered wheelchairs face increasing risks of obesity and deconditioning due to inactivity. Conversely, manual wheelchair users, who propel the wheelchair by pushing the wheelchair's handrims, often face upper extremity injuries from repetitive motions. These challenges underscore the need for a mobility system that promotes activity while minimizing injury risk. Maintaining optimal exertion during wheelchair use enhances health benefits and engagement, yet the variations in individual physiological responses complicate exertion optimization. To address this, we introduce PulseRide, a novel wheelchair system that provides personalized assistance based on each user's physiological responses, helping them maintain their physical exertion goals. Unlike conventional assistive systems focused on obstacle avoidance and navigation, PulseRide integrates real-time physiological data-such as heart rate and ECG-with wheelchair speed to deliver adaptive assistance. Using a human-in-the-loop reinforcement learning approach with Deep Q-Network algorithm (DQN), the system adjusts push assistance to keep users within a moderate activity range without under- or over-exertion. We conducted preliminary tests with 10 users on various terrains, including carpet and slate, to assess PulseRide's effectiveness. Our findings show that, for individual users, PulseRide maintains heart rates within the moderate activity zone as much as 71.7 percent longer than manual wheelchairs. Among all users, we observed an average reduction in muscle contractions of 41.86 percent, delaying fatigue onset and enhancing overall comfort and engagement. These results indicate that PulseRide offers a healthier, adaptive mobility solution, bridging the gap between passive and physically taxing mobility options.

