---
layout: default
title: Deep reinforcement learning-based longitudinal control strategy for automated vehicles at signalised intersections
---

# Deep reinforcement learning-based longitudinal control strategy for automated vehicles at signalised intersections

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08896" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08896v1</a>
  <a href="https://arxiv.org/pdf/2505.08896.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08896v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08896v1', 'Deep reinforcement learning-based longitudinal control strategy for automated vehicles at signalised intersections')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pankaj Kumar, Aditya Mishra, Pranamesh Chakraborty, Subrahmanya Swamy Peruru

**分类**: cs.AI, cs.RO

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出基于深度强化学习的自动驾驶车辆信号交叉口纵向控制策略**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `自动驾驶` `纵向控制` `信号交叉口` `交通安全` `效率优化` `决策策略`

## 📋 核心要点

1. 现有的自动驾驶车辆在信号交叉口的控制策略面临复杂的决策挑战，尤其是在黄灯和交通流变化时。
2. 本文提出了一种基于深度强化学习的纵向控制策略，通过设计综合奖励函数来优化车辆的加速和减速行为。
3. 实验结果表明，所提模型在效率和舒适性方面优于人类驾驶车辆，且在多种安全关键场景下表现出色。

## 📝 摘要（中文）

开发自动驾驶车辆在信号交叉口的控制策略是一项具有挑战性的任务，因为其决策过程复杂。本文提出了一种基于深度强化学习（DRL）的纵向控制策略，设计了综合奖励函数，重点关注基于距离的效率奖励、黄灯决策标准以及不对称加速/减速响应，同时考虑传统的安全和舒适性标准。该奖励函数与深度确定性策略梯度（DDPG）和软演员评论家（SAC）两种流行的DRL算法结合，能够处理加速/减速的连续动作空间。通过真实世界的领车轨迹和使用奥恩斯坦-乌伦贝克过程生成的模拟轨迹进行训练，结果表明，RL模型在保持安全的同时，成功实现了较低的距离间隔和较小的冲击力。进一步评估显示，DDPG模型在关键场景下表现出更平滑的动作特征。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶车辆在信号交叉口的纵向控制问题，现有方法在复杂决策和动态交通环境下表现不足，难以兼顾安全与效率。

**核心思路**：提出基于深度强化学习的控制策略，通过设计综合奖励函数，考虑多种因素（如距离间隔、黄灯决策等），以优化车辆的加速和减速行为。

**技术框架**：整体架构包括数据收集、模型训练和性能评估三个主要阶段。数据收集阶段结合真实和模拟的车辆轨迹，训练阶段使用DDPG和SAC算法进行模型训练，评估阶段通过CDF图进行性能比较。

**关键创新**：最重要的创新在于设计了综合奖励函数，特别关注黄灯决策和不对称加速/减速响应，这在现有方法中较少考虑。

**关键设计**：在奖励函数中，设置了基于距离的效率奖励、黄灯决策标准等，使用DDPG和SAC算法处理连续动作空间，确保模型在复杂场景下的鲁棒性。具体参数和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，所提DRL模型在保持安全的前提下，成功实现了较低的距离间隔和较小的冲击力，相较于人类驾驶车辆，效率提升显著。DDPG模型在关键场景下表现出更平滑的动作特征，验证了其在复杂交通环境中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车的控制系统、智能交通管理和城市交通优化。通过提高车辆在信号交叉口的决策能力，能够有效提升交通安全、效率和驾驶舒适性，对未来智能交通系统的发展具有重要影响。

## 📄 摘要（原文）

> Developing an autonomous vehicle control strategy for signalised intersections (SI) is one of the challenging tasks due to its inherently complex decision-making process. This study proposes a Deep Reinforcement Learning (DRL) based longitudinal vehicle control strategy at SI. A comprehensive reward function has been formulated with a particular focus on (i) distance headway-based efficiency reward, (ii) decision-making criteria during amber light, and (iii) asymmetric acceleration/ deceleration response, along with the traditional safety and comfort criteria. This reward function has been incorporated with two popular DRL algorithms, Deep Deterministic Policy Gradient (DDPG) and Soft-Actor Critic (SAC), which can handle the continuous action space of acceleration/deceleration. The proposed models have been trained on the combination of real-world leader vehicle (LV) trajectories and simulated trajectories generated using the Ornstein-Uhlenbeck (OU) process. The overall performance of the proposed models has been tested using Cumulative Distribution Function (CDF) plots and compared with the real-world trajectory data. The results show that the RL models successfully maintain lower distance headway (i.e., higher efficiency) and jerk compared to human-driven vehicles without compromising safety. Further, to assess the robustness of the proposed models, we evaluated the model performance on diverse safety-critical scenarios, in terms of car-following and traffic signal compliance. Both DDPG and SAC models successfully handled the critical scenarios, while the DDPG model showed smoother action profiles compared to the SAC model. Overall, the results confirm that DRL-based longitudinal vehicle control strategy at SI can help to improve traffic safety, efficiency, and comfort.

