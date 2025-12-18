---
layout: default
title: MobiDock: Design and Control of A Modular Self Reconfigurable Bimanual Mobile Manipulator via Robotic Docking
---

# MobiDock: Design and Control of A Modular Self Reconfigurable Bimanual Mobile Manipulator via Robotic Docking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27178" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27178v1</a>
  <a href="https://arxiv.org/pdf/2510.27178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27178v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27178v1', 'MobiDock: Design and Control of A Modular Self Reconfigurable Bimanual Mobile Manipulator via Robotic Docking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuan-Thuan Nguyen, Khac Nam Nguyen, Ngoc Duy Tran, Thi Thoa Mac, Anh Nguyen, Hoang Hiep Ly, Tung D. Ta

**分类**: cs.RO

**发布日期**: 2025-10-31

**备注**: ICRA2026 submited

---

## 💡 一句话要点

**MobiDock：基于机器人对接的模块化自重构双臂移动操作机器人设计与控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模块化机器人` `自重构系统` `移动操作机器人` `机器人对接` `多机器人协同` `计算机视觉` `AprilTag`

## 📋 核心要点

1. 多机器人系统在协同操作时面临控制协调和动态稳定性的挑战，限制了其在复杂环境中的应用。
2. MobiDock通过物理对接将多个独立机器人重构为一个统一的平台，简化了控制并提高了整体系统的性能。
3. 实验表明，MobiDock对接后的系统在动态稳定性、精度和任务完成速度方面均优于独立协作的机器人。

## 📝 摘要（中文）

本研究提出了MobiDock，一个模块化自重构移动操作机器人系统，旨在解决多机器人系统，特别是移动操作机器人在协同工作时面临的控制协调和动态稳定性挑战。MobiDock允许两个独立的机器人通过物理连接形成一个统一的移动双臂平台，从而将复杂的多机器人控制问题简化为单个系统的管理。该系统采用基于计算机视觉（使用AprilTag标记）的自主对接策略和一个新型螺纹锁紧机构。实验结果表明，对接后的配置在动态稳定性和操作效率方面优于两个独立协作的机器人。具体而言，统一系统的均方根（RMS）加速度和加加速度值更低，角精度更高，并且完成任务的速度明显更快。这些发现证实了物理重构是一种强大的设计原则，可以简化协同控制，提高真实环境中复杂任务的稳定性和性能。

## 🔬 方法详解

**问题定义**：多机器人系统，尤其是移动操作机器人，在协同工作时面临控制协调和动态稳定性的挑战。现有方法通常依赖复杂的软件算法进行协调，但难以保证在动态环境中的稳定性和效率。MobiDock旨在解决这一问题，通过物理连接简化控制，提高系统的整体性能。

**核心思路**：MobiDock的核心思路是通过物理重构将多个独立的移动机器人连接成一个统一的平台。这种物理连接将复杂的多机器人控制问题转化为对单个系统的控制，从而简化了控制算法的设计和实现。此外，物理连接还能提高系统的整体刚性和稳定性。

**技术框架**：MobiDock系统包含两个独立的移动机器人，每个机器人配备一个机械臂和一个对接机构。对接过程包括以下几个阶段：1) 机器人使用视觉系统（AprilTag）进行定位和导航；2) 机器人自主移动到对接位置；3) 使用螺纹锁紧机构进行物理连接；4) 系统切换到统一控制模式。

**关键创新**：MobiDock的关键创新在于其模块化自重构的设计和基于机器人对接的控制策略。与传统的多机器人协同方法相比，MobiDock通过物理连接实现了更紧密的协作，从而提高了系统的稳定性和效率。此外，新型螺纹锁紧机构的设计也保证了对接的可靠性和强度。

**关键设计**：MobiDock系统采用AprilTag作为视觉定位的标记，通过摄像头获取AprilTag的位置信息，实现机器人的自主导航和对接。螺纹锁紧机构的设计需要考虑对接的精度、锁紧的强度和解锁的便捷性。控制算法需要根据对接后的系统动力学特性进行调整，以保证系统的稳定性和性能。

## 📊 实验亮点

实验结果表明，MobiDock对接后的系统在动态稳定性方面表现更优，RMS加速度和加加速度值显著降低。在角精度方面，对接后的系统也优于独立协作的机器人。此外，对接后的系统完成任务的速度明显更快，验证了物理重构在提高系统性能方面的有效性。

## 🎯 应用场景

MobiDock系统可应用于多种场景，例如：大型物体的搬运、复杂环境下的装配、灾难救援等。通过模块化设计，MobiDock可以根据任务需求灵活配置，提高机器人的适应性和效率。未来，MobiDock有望在工业自动化、物流、医疗等领域发挥重要作用。

## 📄 摘要（原文）

> Multi-robot systems, particularly mobile manipulators, face challenges in control coordination and dynamic stability when working together. To address this issue, this study proposes MobiDock, a modular self-reconfigurable mobile manipulator system that allows two independent robots to physically connect and form a unified mobile bimanual platform. This process helps transform a complex multi-robot control problem into the management of a simpler, single system. The system utilizes an autonomous docking strategy based on computer vision with AprilTag markers and a new threaded screw-lock mechanism. Experimental results show that the docked configuration demonstrates better performance in dynamic stability and operational efficiency compared to two independently cooperating robots. Specifically, the unified system has lower Root Mean Square (RMS) Acceleration and Jerk values, higher angular precision, and completes tasks significantly faster. These findings confirm that physical reconfiguration is a powerful design principle that simplifies cooperative control, improving stability and performance for complex tasks in real-world environments.

