---
layout: default
title: "ARMimic: Learning Robotic Manipulation from Passive Human Demonstrations in Augmented Reality"
---

# ARMimic: Learning Robotic Manipulation from Passive Human Demonstrations in Augmented Reality

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22914" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22914v1</a>
  <a href="https://arxiv.org/pdf/2509.22914.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22914v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22914v1', 'ARMimic: Learning Robotic Manipulation from Passive Human Demonstrations in Augmented Reality')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rohan Walia, Yusheng Wang, Ralf Römer, Masahiro Nishio, Angela P. Schoellig, Jun Ota

**分类**: cs.RO

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**ARMimic：利用增强现实中的被动人类演示学习机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `机器人操作` `模仿学习` `增强现实` `人机交互` `机器人示教`

## 📋 核心要点

1. 现有机器人模仿学习方法依赖繁琐的动觉示教或遥操作，存在硬件依赖性强、操作复杂等问题。
2. ARMimic利用消费级XR头显和摄像头，结合手部跟踪、AR机器人叠加和深度感知，实现轻量级、可扩展的数据收集。
3. 实验表明，ARMimic在操作任务中，相比遥操作减少50%演示时间，任务成功率比基线ACT提高11%。

## 📝 摘要（中文）

模仿学习是机器人技能获取的强大范例，但传统的示教方法（如动觉示教和遥操作）繁琐、硬件依赖性强且会中断工作流程。最近，使用扩展现实（XR）头显的被动观察在以自我为中心的演示收集方面显示出前景，但当前的方法需要额外的硬件、复杂的校准或受限的记录条件，从而限制了可扩展性和可用性。我们提出了ARMimic，这是一个新颖的框架，它通过轻量级和硬件最小化的设置，仅使用消费级XR头显和固定工作场所摄像头，实现可扩展的、无需机器人的数据收集。ARMimic集成了以自我为中心的手部跟踪、增强现实（AR）机器人叠加和实时深度感知，以确保具有碰撞意识的、运动学上可行的演示。统一的模仿学习管道是我们方法的核心，将人类和虚拟机器人轨迹视为可互换的，从而实现可以推广到不同形态和环境的策略。我们在两个操作任务（包括具有挑战性的长时程碗堆叠）上验证了ARMimic。在我们的实验中，与遥操作相比，ARMimic将演示时间减少了50％，并且比在遥操作数据上训练的最新基线ACT的任务成功率提高了11％。我们的结果表明，ARMimic能够实现安全、无缝和野外数据收集，为在各种现实世界环境中进行可扩展的机器人学习提供了巨大的潜力。

## 🔬 方法详解

**问题定义**：现有机器人模仿学习方法，如动觉示教和遥操作，存在硬件成本高、操作复杂、易中断工作流程等问题。尤其是在复杂操作任务中，数据收集效率和安全性难以保证。因此，需要一种更轻量级、更安全、更高效的机器人示教方法。

**核心思路**：ARMimic的核心思路是利用增强现实（AR）技术，让人类在虚拟环境中进行机器人操作的演示，并将人类的动作轨迹和虚拟机器人的轨迹视为可互换的数据，从而训练机器人策略。通过AR叠加，人类可以直接在真实环境中“看到”虚拟机器人，并进行交互，避免了直接操作真实机器人的风险和复杂性。

**技术框架**：ARMimic系统主要包含以下几个模块：1) 使用消费级XR头显进行以自我为中心的手部跟踪；2) 在AR环境中叠加虚拟机器人模型；3) 使用固定摄像头进行实时深度感知，以实现碰撞检测和环境理解；4) 统一的模仿学习管道，用于训练机器人策略。人类在AR环境中进行操作演示，系统记录人类手部和虚拟机器人的轨迹，并将其作为训练数据输入模仿学习模型。

**关键创新**：ARMimic的关键创新在于其轻量级、硬件最小化的数据收集方式，以及将人类和虚拟机器人轨迹视为可互换数据的统一模仿学习框架。与传统的遥操作或动觉示教相比，ARMimic无需复杂的硬件设备和校准过程，降低了数据收集的成本和难度。同时，通过AR叠加，人类可以在安全的环境中进行操作演示，避免了直接操作真实机器人的风险。

**关键设计**：ARMimic的关键设计包括：1) 使用消费级XR头显进行手部跟踪，降低了硬件成本；2) 使用实时深度感知进行碰撞检测，保证了操作的安全性；3) 设计了统一的模仿学习管道，将人类和虚拟机器人的轨迹视为可互换的数据，从而训练可以泛化到不同机器人形态和环境的策略。具体的损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，ARMimic在两个操作任务（包括具有挑战性的长时程碗堆叠）上表现出色。与遥操作相比，ARMimic将演示时间减少了50％，并且比在遥操作数据上训练的最新基线ACT的任务成功率提高了11％。这些结果验证了ARMimic在数据收集效率和任务性能方面的优势。

## 🎯 应用场景

ARMimic具有广泛的应用前景，可用于工业自动化、医疗机器人、家庭服务机器人等领域。通过该方法，可以快速、安全地收集机器人操作数据，并训练出高性能的机器人策略，从而提高机器人的智能化水平和应用范围。未来，ARMimic有望成为一种通用的机器人示教工具，促进机器人技术的普及和发展。

## 📄 摘要（原文）

> Imitation learning is a powerful paradigm for robot skill acquisition, yet conventional demonstration methods--such as kinesthetic teaching and teleoperation--are cumbersome, hardware-heavy, and disruptive to workflows. Recently, passive observation using extended reality (XR) headsets has shown promise for egocentric demonstration collection, yet current approaches require additional hardware, complex calibration, or constrained recording conditions that limit scalability and usability. We present ARMimic, a novel framework that overcomes these limitations with a lightweight and hardware-minimal setup for scalable, robot-free data collection using only a consumer XR headset and a stationary workplace camera. ARMimic integrates egocentric hand tracking, augmented reality (AR) robot overlays, and real-time depth sensing to ensure collision-aware, kinematically feasible demonstrations. A unified imitation learning pipeline is at the core of our method, treating both human and virtual robot trajectories as interchangeable, which enables policies that generalize across different embodiments and environments. We validate ARMimic on two manipulation tasks, including challenging long-horizon bowl stacking. In our experiments, ARMimic reduces demonstration time by 50% compared to teleoperation and improves task success by 11% over ACT, a state-of-the-art baseline trained on teleoperated data. Our results demonstrate that ARMimic enables safe, seamless, and in-the-wild data collection, offering great potential for scalable robot learning in diverse real-world settings.

