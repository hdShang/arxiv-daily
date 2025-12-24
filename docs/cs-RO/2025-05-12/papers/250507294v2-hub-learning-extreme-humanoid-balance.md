---
layout: default
title: "HuB: Learning Extreme Humanoid Balance"
---

# HuB: Learning Extreme Humanoid Balance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07294" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07294v2</a>
  <a href="https://arxiv.org/pdf/2505.07294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07294v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07294v2', 'HuB: Learning Extreme Humanoid Balance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tong Zhang, Boyuan Zheng, Ruiqian Nai, Yingdong Hu, Yen-Jen Wang, Geng Chen, Fanqi Lin, Jiongye Li, Chuye Hong, Koushil Sreenath, Yang Gao

**分类**: cs.RO, cs.AI, cs.LG, eess.SY

**发布日期**: 2025-05-12 (更新: 2025-08-17)

**备注**: CoRL 2025 (Oral Presentation). Project website: https://hub-robot.github.io

---

## 💡 一句话要点

**提出HuB框架以解决类人机器人平衡控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `类人机器人` `平衡控制` `强化学习` `仿真与现实` `运动能力` `鲁棒性训练` `策略学习`

## 📋 核心要点

1. 现有方法在类人机器人平衡控制中面临参考运动误差、形态不匹配和仿真与现实差距等挑战。
2. HuB框架通过整合参考运动精炼、平衡感知策略学习和鲁棒性训练，针对特定问题进行优化。
3. 在Unitree G1机器人上进行的实验表明，HuB在极端平衡任务中表现优异，稳定性显著高于基线方法。

## 📝 摘要（中文）

人类身体展现出卓越的运动能力，如单脚稳立或高踢腿，这些都需要精确的平衡控制。尽管近期研究利用强化学习追踪人类动作以获取技能，但在平衡密集型任务中应用这一范式仍然面临挑战。本文识别出三个主要障碍：参考运动误差导致的不稳定性、形态不匹配造成的学习困难，以及传感器噪声和未建模动态导致的仿真与现实差距。为此，我们提出了HuB（Humanoid Balance），一个统一框架，整合了参考运动精炼、平衡感知策略学习和仿真到现实的鲁棒性训练，针对每个挑战进行优化。我们在Unitree G1类人机器人上验证了该方法，成功应对了极具挑战性的准静态平衡任务，包括极端单腿姿势，如燕子平衡和李小龙的踢腿。我们的策略在强烈物理干扰下依然保持稳定，而基线方法则频繁失败。

## 🔬 方法详解

**问题定义**：本文旨在解决类人机器人在平衡控制任务中的不稳定性，现有方法在面对参考运动误差、形态不匹配和仿真与现实差距时表现不佳。

**核心思路**：HuB框架通过三个模块分别应对上述挑战，确保机器人在复杂平衡任务中能够稳定执行。该设计旨在提高策略的适应性和鲁棒性。

**技术框架**：HuB框架包括参考运动精炼模块、平衡感知策略学习模块和仿真到现实的鲁棒性训练模块。每个模块针对特定问题进行优化，形成一个闭环反馈系统。

**关键创新**：HuB的创新在于将平衡控制的多个挑战整合到一个统一框架中，显著提升了类人机器人的平衡能力，与传统方法相比，能够更好地应对动态环境中的干扰。

**关键设计**：在HuB中，采用了特定的损失函数来优化平衡策略，并设计了适应性强的网络结构，以处理不同的平衡任务和环境变化。

## 📊 实验亮点

实验结果显示，HuB在极端单腿姿势任务中表现出色，能够在强烈的物理干扰下保持稳定，而基线方法则无法完成这些任务。具体而言，HuB在面对足球强力击打时，依然能够维持平衡，展现出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人和运动训练等。通过提升类人机器人的平衡能力，可以使其在复杂环境中更有效地执行任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The human body demonstrates exceptional motor capabilities-such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters-both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances-such as a forceful soccer strike-while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

