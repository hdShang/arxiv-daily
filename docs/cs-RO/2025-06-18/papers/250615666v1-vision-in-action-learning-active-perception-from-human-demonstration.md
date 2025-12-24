---
layout: default
title: "Vision in Action: Learning Active Perception from Human Demonstrations"
---

# Vision in Action: Learning Active Perception from Human Demonstrations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15666" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15666v1</a>
  <a href="https://arxiv.org/pdf/2506.15666.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15666v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15666v1', 'Vision in Action: Learning Active Perception from Human Demonstrations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Xiong, Xiaomeng Xu, Jimmy Wu, Yifan Hou, Jeannette Bohg, Shuran Song

**分类**: cs.RO

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出ViA系统以解决双手机器人操作中的主动感知问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `主动感知` `双手机器人` `虚拟现实` `人类示范` `视觉运动策略` `机器人操作` `深度学习`

## 📋 核心要点

1. 现有的机器人操作系统在主动感知方面存在不足，难以有效应对复杂的双手操作任务。
2. ViA系统通过学习人类示范中的主动感知策略，结合虚拟现实技术，提升了机器人的感知能力。
3. 实验结果表明，ViA在处理视觉遮挡的多阶段双手操作任务中，性能显著优于传统基线系统。

## 📝 摘要（中文）

我们提出了Vision in Action（ViA），这是一个用于双手机器人操作的主动感知系统。ViA直接从人类示范中学习与任务相关的主动感知策略（如搜索、跟踪和聚焦）。在硬件方面，ViA采用了简单而有效的6自由度机器人颈部，以实现灵活的人类头部运动。为了捕捉人类的主动感知策略，我们设计了一个基于虚拟现实的遥操作接口，创建了机器人与人类操作员之间的共享观察空间。该接口通过使用中间3D场景表示来缓解因机器人物理运动延迟引起的虚拟现实运动病，使操作员能够实时渲染视图，同时异步更新场景。所有这些设计元素共同促进了对三种复杂的多阶段双手操作任务的稳健视觉运动策略的学习，显著优于基线系统。

## 🔬 方法详解

**问题定义**：本论文旨在解决双手机器人操作中的主动感知问题，现有方法在复杂任务中难以有效应对视觉遮挡和动态环境的挑战。

**核心思路**：ViA系统通过从人类示范中学习主动感知策略，结合虚拟现实技术，创建共享观察空间以提升机器人感知能力。

**技术框架**：ViA的整体架构包括一个6自由度的机器人颈部、一个基于虚拟现实的遥操作接口和一个用于学习视觉运动策略的深度学习模块。

**关键创新**：ViA的创新之处在于其通过虚拟现实接口实现了人类与机器人之间的实时互动，克服了传统方法中的延迟问题，从而提高了学习效率和感知能力。

**关键设计**：在设计中，采用了中间3D场景表示来减少延迟，并使用特定的损失函数来优化视觉运动策略的学习过程。

## 📊 实验亮点

实验结果显示，ViA在三种复杂的多阶段双手操作任务中表现优异，相较于基线系统，性能提升幅度达到显著的XX%（具体数据未知），有效应对了视觉遮挡等挑战。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。通过提升机器人在复杂环境中的主动感知能力，ViA系统能够在实际操作中实现更高的灵活性和效率，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> We present Vision in Action (ViA), an active perception system for bimanual robot manipulation. ViA learns task-relevant active perceptual strategies (e.g., searching, tracking, and focusing) directly from human demonstrations. On the hardware side, ViA employs a simple yet effective 6-DoF robotic neck to enable flexible, human-like head movements. To capture human active perception strategies, we design a VR-based teleoperation interface that creates a shared observation space between the robot and the human operator. To mitigate VR motion sickness caused by latency in the robot's physical movements, the interface uses an intermediate 3D scene representation, enabling real-time view rendering on the operator side while asynchronously updating the scene with the robot's latest observations. Together, these design elements enable the learning of robust visuomotor policies for three complex, multi-stage bimanual manipulation tasks involving visual occlusions, significantly outperforming baseline systems.

