---
layout: default
title: HACL: History-Aware Curriculum Learning for Fast Locomotion
---

# HACL: History-Aware Curriculum Learning for Fast Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18429" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18429v2</a>
  <a href="https://arxiv.org/pdf/2505.18429.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18429v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18429v2', 'HACL: History-Aware Curriculum Learning for Fast Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prakhar Mishra, Amir Hossain Raj, Xuesu Xiao, Dinesh Manocha

**分类**: cs.RO

**发布日期**: 2025-05-23 (更新: 2025-11-18)

---

## 💡 一句话要点

**提出历史感知课程学习算法以解决快速运动问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `历史感知` `课程学习` `快速运动` `四足机器人` `双足机器人` `递归神经网络` `运动控制` `轨迹生成`

## 📋 核心要点

1. 核心问题：现有的运动控制算法在快速运动时难以保持稳定性，尤其是在复杂环境中。
2. 方法要点：提出历史感知课程学习（HACL）算法，通过考虑过去的运动信息来优化机器人运动轨迹。
3. 实验或效果：HACL在多种机器人上进行验证，取得了显著的速度提升，尤其在Unitree Go1上表现优异。

## 📝 摘要（中文）

本文针对四足和双足机器人在敏捷和快速运动中的稳定性问题，提出了一种新的算法。该算法通过引入历史感知课程学习（HACL）来考虑运动的时间特性，从而生成高速度的轨迹。我们利用递归神经网络（RNN）建模关节速度命令的历史信息，并通过隐藏状态帮助课程学习线性速度与角速度命令及其奖励之间的关系。实验验证表明，HACL在模拟环境和现实场景中均表现出色，尤其在Unitree Go1机器人上实现了6.7 m/s的峰值前进速度，较以往算法提升近20%。

## 🔬 方法详解

**问题定义**：本文旨在解决四足和双足机器人在快速运动时的稳定性问题。现有方法在处理高速度轨迹时，往往忽视了历史信息，导致运动不稳定。

**核心思路**：论文提出的HACL算法通过引入历史信息，利用递归神经网络（RNN）建模关节速度命令的历史，从而优化运动轨迹。这种设计使得算法能够更好地理解速度命令与奖励之间的关系。

**技术框架**：HACL的整体架构包括数据收集、RNN建模、课程学习和轨迹生成四个主要模块。首先收集运动数据，然后通过RNN分析历史信息，接着进行课程学习，最后生成高效的运动轨迹。

**关键创新**：HACL的核心创新在于将历史信息纳入课程学习框架中，使得算法能够动态调整运动策略。这与传统方法的静态策略形成鲜明对比。

**关键设计**：在参数设置上，HACL使用了特定的损失函数来平衡速度和稳定性，同时RNN的隐藏层设计使得模型能够有效捕捉时间序列特征。

## 📊 实验亮点

实验结果显示，HACL在Unitree Go1机器人上实现了6.7 m/s的峰值前进速度，接近给定命令速度7 m/s，较以往算法提升近20%。这一显著的性能提升证明了HACL在快速运动控制中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人以及自动驾驶等场景。通过提高机器人的运动稳定性和速度，HACL可以显著提升机器人在复杂环境中的适应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We address the problem of agile and rapid locomotion, a key characteristic of quadrupedal and bipedal robots. We present a new algorithm that maintains stability and generates high-speed trajectories by considering the temporal aspect of locomotion. Our formulation takes into account past information based on a novel history-aware curriculum Learning (HACL) algorithm. We model the history of joint velocity commands with respect to the observed linear and angular rewards using a recurrent neural net (RNN). The hidden state helps the curriculum learn the relationship between the forward linear velocity and angular velocity commands and the rewards over a given time-step. We validate our approach on the MIT Mini Cheetah,Unitree Go1, and Go2 robots in a simulated environment and on a Unitree Go1 robot in real-world scenarios. In practice, HACL achieves peak forward velocity of 6.7 m/s for a given command velocity of 7m/s and outperforms prior locomotion algorithms by nearly 20%.

