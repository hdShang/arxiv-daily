---
layout: default
title: ACE-F: A Cross Embodiment Foldable System with Force Feedback for Dexterous Teleoperation
---

# ACE-F: A Cross Embodiment Foldable System with Force Feedback for Dexterous Teleoperation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20887" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20887v1</a>
  <a href="https://arxiv.org/pdf/2511.20887.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20887v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.20887v1', 'ACE-F: A Cross Embodiment Foldable System with Force Feedback for Dexterous Teleoperation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Yan, Jiajian Fu, Shiqi Yang, Lars Paulsen, Xuxin Cheng, Xiaolong Wang

**分类**: cs.RO

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**ACE-F：一种具有力反馈的跨具身可折叠遥操作系统**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `遥操作` `力反馈` `跨具身` `机器人控制` `人机交互`

## 📋 核心要点

1. 现有遥操作平台缺乏力反馈、跨具身泛化能力和便携性，限制了其在复杂任务中的应用。
2. ACE-F系统通过逆运动学和人机界面，结合广义软控制器，实现了精确的跨具身机器人控制。
3. 该系统创新性地将末端执行器位置偏差转化为虚拟力信号，无需额外传感器即可实现力反馈。

## 📝 摘要（中文）

遥操作系统对于高效收集多样化和高质量的机器人演示数据至关重要，尤其是在复杂的、富含接触的任务中。然而，当前的遥操作平台通常缺乏集成的力反馈、跨具身泛化以及便携式、用户友好的设计，限制了它们的实际部署。为了解决这些限制，我们介绍了一种具有集成力反馈的跨具身可折叠遥操作系统ACE-F。我们的方法利用逆运动学（IK）与精心设计的人机界面（HRI）相结合，使用户能够轻松地捕获精确和高质量的演示。我们进一步提出了一种广义的软控制器管道，集成了PD控制和逆动力学，以确保机器人安全和跨各种机器人具身的精确运动控制。至关重要的是，为了在没有额外传感器的情况下实现力反馈的跨具身泛化，我们创新性地将末端执行器的位置偏差解释为虚拟力信号，从而增强了数据收集并实现了在模仿学习中的应用。大量的遥操作实验证实，ACE-F显著简化了各种机器人具身的控制，使得灵巧的操作任务就像操作电脑鼠标一样直观。该系统已开源。

## 🔬 方法详解

**问题定义**：现有遥操作系统在复杂、接触丰富的任务中，难以提供高质量的机器人演示数据。主要痛点在于缺乏集成的力反馈，难以实现跨不同机器人形态的泛化，并且设计不够便携和用户友好，限制了实际应用。

**核心思路**：ACE-F的核心思路是设计一个可折叠、便携的遥操作设备，并结合逆运动学和广义软控制器，实现对不同机器人形态的精确控制。通过将末端执行器的位置偏差转化为虚拟力信号，无需额外传感器即可提供力反馈，从而提升操作的直观性和效率。

**技术框架**：ACE-F系统主要包含以下几个模块：1) 可折叠遥操作设备：提供便携式的人机交互界面。2) 逆运动学模块：将操作者的动作映射到机器人关节空间。3) 广义软控制器：结合PD控制和逆动力学，保证机器人运动的安全性和精确性。4) 虚拟力反馈模块：将末端执行器的位置偏差转化为虚拟力信号，反馈给操作者。

**关键创新**：ACE-F最重要的创新点在于其虚拟力反馈机制。传统力反馈需要额外的力传感器，而ACE-F通过将末端执行器的位置偏差解释为虚拟力信号，实现了无需额外传感器的力反馈。这种方法简化了系统设计，降低了成本，并提高了系统的鲁棒性。

**关键设计**：广义软控制器是关键设计之一，它集成了PD控制和逆动力学，可以根据不同的机器人形态进行调整，保证运动的稳定性和精确性。虚拟力反馈的强度需要根据实际任务进行调整，以提供最佳的操作体验。人机界面的设计也至关重要，需要保证操作的舒适性和直观性。

## 📊 实验亮点

实验结果表明，ACE-F系统能够显著简化对各种机器人形态的控制，使得灵巧操作任务像操作电脑鼠标一样直观。通过虚拟力反馈，操作者能够更好地感知环境，从而提高操作的精确性和效率。该系统为模仿学习提供了高质量的演示数据，加速了机器人技能学习。

## 🎯 应用场景

ACE-F系统可广泛应用于需要远程操作的场景，例如危险环境下的作业、医疗手术辅助、以及机器人技能学习的数据采集。该系统能够降低操作难度，提高操作效率，并为模仿学习提供高质量的训练数据，加速机器人智能化进程。

## 📄 摘要（原文）

> Teleoperation systems are essential for efficiently collecting diverse and high-quality robot demonstration data, especially for complex, contact-rich tasks. However, current teleoperation platforms typically lack integrated force feedback, cross-embodiment generalization, and portable, user-friendly designs, limiting their practical deployment. To address these limitations, we introduce ACE-F, a cross embodiment foldable teleoperation system with integrated force feedback. Our approach leverages inverse kinematics (IK) combined with a carefully designed human-robot interface (HRI), enabling users to capture precise and high-quality demonstrations effortlessly. We further propose a generalized soft-controller pipeline integrating PD control and inverse dynamics to ensure robot safety and precise motion control across diverse robotic embodiments. Critically, to achieve cross-embodiment generalization of force feedback without additional sensors, we innovatively interpret end-effector positional deviations as virtual force signals, which enhance data collection and enable applications in imitation learning. Extensive teleoperation experiments confirm that ACE-F significantly simplifies the control of various robot embodiments, making dexterous manipulation tasks as intuitive as operating a computer mouse. The system is open-sourced at: https://acefoldable.github.io/

