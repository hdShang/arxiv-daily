---
layout: default
title: "H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies"
---

# H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17627" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17627v1</a>
  <a href="https://arxiv.org/pdf/2505.17627.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17627v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17627v1', 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Geeta Chandra Raju Bethala, Hao Huang, Niraj Pudasaini, Abdullah Mohamed Ali, Shuaihang Yuan, Congcong Wen, Anthony Tzes, Yi Fang

**分类**: cs.RO

**发布日期**: 2025-05-23

**备注**: Code and videos available at https://h2compact.github.io/h2compact/

---

## 💡 一句话要点

**提出H2-COMPACT以解决人类与类人机器人协作搬运问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `人机协作` `类人机器人` `触觉引导` `深度强化学习` `行为克隆` `负载适应性` `运动控制`

## 📋 核心要点

1. 现有方法在类人机器人与人类的协作中缺乏有效的意图推断机制，导致响应不够灵敏。
2. 本研究提出了一种分层策略学习框架，通过触觉线索实现人类与类人机器人的协同搬运，提升了交互的自然性和稳定性。
3. 实验结果表明，所提方法在完成时间、轨迹偏差和速度同步等方面的表现与盲folded人类相当，展示了良好的协作能力。

## 📝 摘要（中文）

我们提出了一种分层策略学习框架，使得类人机器人能够仅通过触觉线索与人类合作搬运较长的负载。在上层，轻量级行为克隆网络接收来自双腕传感器的六轴力/扭矩流，并输出捕捉领导者施加力量的全身平面速度指令。在下层，深度强化学习策略在随机负载（0-3公斤）和摩擦条件下进行训练，并在MuJoCo和真实的Unitree G1上验证，将这些高层扭转映射到稳定的负载下关节轨迹。通过将意图解释（力->速度）与类人运动（速度->关节）解耦，我们的方法结合了对人类输入的直观响应与稳健的负载自适应行走。我们的类人机器人在实际试验中实现了与盲folded人类跟随者基线相当的协作搬运性能。

## 🔬 方法详解

**问题定义**：本研究旨在解决人类与类人机器人在协作搬运任务中的意图推断与响应问题。现有方法通常依赖于视觉或复杂的传感器，难以实现灵活的互动。

**核心思路**：我们提出的H2-COMPACT框架通过分层策略学习，利用触觉线索进行意图推断，并将其与类人机器人的运动控制相结合，以实现更自然的协作。

**技术框架**：该框架分为两个主要层次：上层使用行为克隆网络处理六轴力/扭矩数据，输出平面速度指令；下层则采用深度强化学习策略，将这些指令映射为稳定的关节轨迹。

**关键创新**：本研究的创新在于首次实现了通过触觉引导与全身类人控制的结合，显著提升了人类与类人机器人之间的协作效率。

**关键设计**：在训练过程中，我们使用了随机负载和摩擦条件，且数据收集不依赖于运动捕捉或标记，而是通过同步的RGB视频和力/扭矩读数进行。

## 📊 实验亮点

实验结果显示，所提H2-COMPACT框架在协作搬运任务中，完成时间、轨迹偏差和速度同步等指标均与盲folded人类相当，展示了良好的协作性能。这表明该方法在实际应用中具有可行性和有效性。

## 🎯 应用场景

该研究的潜在应用场景包括人机协作的物流、搬运和服务机器人等领域。通过提升类人机器人对人类意图的理解与响应能力，未来可实现更高效的协作工作流程，推动智能机器人在实际应用中的普及与发展。

## 📄 摘要（原文）

> We present a hierarchical policy-learning framework that enables a legged humanoid to cooperatively carry extended loads with a human partner using only haptic cues for intent inference. At the upper tier, a lightweight behavior-cloning network consumes six-axis force/torque streams from dual wrist-mounted sensors and outputs whole-body planar velocity commands that capture the leader's applied forces. At the lower tier, a deep-reinforcement-learning policy, trained under randomized payloads (0-3 kg) and friction conditions in Isaac Gym and validated in MuJoCo and on a real Unitree G1, maps these high-level twists to stable, under-load joint trajectories. By decoupling intent interpretation (force -> velocity) from legged locomotion (velocity -> joints), our method combines intuitive responsiveness to human inputs with robust, load-adaptive walking. We collect training data without motion-capture or markers, only synchronized RGB video and F/T readings, employing SAM2 and WHAM to extract 3D human pose and velocity. In real-world trials, our humanoid achieves cooperative carry-and-move performance (completion time, trajectory deviation, velocity synchrony, and follower-force) on par with a blindfolded human-follower baseline. This work is the first to demonstrate learned haptic guidance fused with full-body legged control for fluid human-humanoid co-manipulation. Code and videos are available on the H2-COMPACT website.

