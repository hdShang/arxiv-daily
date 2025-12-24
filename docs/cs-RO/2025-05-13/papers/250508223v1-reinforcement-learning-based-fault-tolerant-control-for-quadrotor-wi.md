---
layout: default
title: Reinforcement Learning-based Fault-Tolerant Control for Quadrotor with Online Transformer Adaptation
---

# Reinforcement Learning-based Fault-Tolerant Control for Quadrotor with Online Transformer Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08223" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08223v1</a>
  <a href="https://arxiv.org/pdf/2505.08223.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08223v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08223v1', 'Reinforcement Learning-based Fault-Tolerant Control for Quadrotor with Online Transformer Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dohyun Kim, Jayden Dongwoo Lee, Hyochoong Bang, Jungho Bae

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-13

**备注**: Accpted at the 2025 IEEE International Conference on Robotics & Automation (ICRA) Workshop: Robots in the Wild

---

## 💡 一句话要点

**提出基于强化学习的容错控制框架以应对四旋翼故障问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `容错控制` `四旋翼` `变换器` `动态适应` `机器人技术` `故障管理`

## 📋 核心要点

1. 现有的容错控制方法往往依赖于多旋翼的先验模型，难以适应新的配置，限制了其应用范围。
2. 本文提出了一种混合强化学习的容错控制框架，结合了变换器的在线适应能力，能够实时适应未见的系统模型。
3. 实验结果显示，该方法在执行器故障情况下取得了95%的成功率，显著优于现有方法，展示了其在多旋翼控制中的有效性。

## 📝 摘要（中文）

多旋翼在各类机器人应用中扮演重要角色，但对执行器故障高度敏感，导致快速不稳定和任务可靠性下降。尽管已有多种基于强化学习的容错控制策略被广泛研究，但大多数方法需要先验的多旋翼模型知识或难以适应新配置。为了解决这些局限性，本文提出了一种新颖的混合强化学习容错控制框架，集成了基于变换器的在线适应模块。该框架利用变换器架构实时推断潜在表示，使其能够在不重新训练的情况下适应以前未见的系统模型。在PyBullet仿真中评估该方法，在执行器故障下实现了95%的成功率和0.129米的位置信息均方根误差（RMSE），优于现有适应方法的86%成功率和0.153米的RMSE。这些结果展示了该框架在动态和不确定环境中增强多旋翼适应性和可靠性的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决多旋翼在执行器故障情况下的控制问题，现有方法通常需要先验模型知识，难以适应新的动态环境。

**核心思路**：提出的框架结合了强化学习与变换器架构，能够实时推断潜在状态表示，从而在不重新训练的情况下适应新的系统模型。

**技术框架**：整体架构包括强化学习模块和变换器适应模块。强化学习模块负责学习控制策略，而变换器模块则实时处理输入数据，生成适应性表示。

**关键创新**：最重要的创新在于将变换器与强化学习结合，允许系统在面对未见的动态时进行快速适应，这一设计显著提高了容错能力。

**关键设计**：在网络结构上，采用了变换器的自注意力机制以捕捉状态之间的复杂关系，损失函数设计上则考虑了控制精度与适应性的平衡。具体参数设置和训练细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，提出的方法在执行器故障情况下实现了95%的成功率，位置信息均方根误差为0.129米，相较于现有方法的86%成功率和0.153米的RMSE，提升显著，展示了其在动态环境中的有效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括无人机巡检、灾害救援和物流运输等场景，能够在执行器故障时保持稳定性和任务执行能力。未来，该框架有望在更广泛的动态环境中应用，提升多旋翼的可靠性和适应性。

## 📄 摘要（原文）

> Multirotors play a significant role in diverse field robotics applications but remain highly susceptible to actuator failures, leading to rapid instability and compromised mission reliability. While various fault-tolerant control (FTC) strategies using reinforcement learning (RL) have been widely explored, most previous approaches require prior knowledge of the multirotor model or struggle to adapt to new configurations. To address these limitations, we propose a novel hybrid RL-based FTC framework integrated with a transformer-based online adaptation module. Our framework leverages a transformer architecture to infer latent representations in real time, enabling adaptation to previously unseen system models without retraining. We evaluate our method in a PyBullet simulation under loss-of-effectiveness actuator faults, achieving a 95% success rate and a positional root mean square error (RMSE) of 0.129 m, outperforming existing adaptation methods with 86% success and an RMSE of 0.153 m. Further evaluations on quadrotors with varying configurations confirm the robustness of our framework across untrained dynamics. These results demonstrate the potential of our framework to enhance the adaptability and reliability of multirotors, enabling efficient fault management in dynamic and uncertain environments. Website is available at http://00dhkim.me/paper/rl-ftc

