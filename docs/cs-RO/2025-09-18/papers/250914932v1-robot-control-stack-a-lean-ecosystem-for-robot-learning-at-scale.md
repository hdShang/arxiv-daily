---
layout: default
title: "Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale"
---

# Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14932" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14932v1</a>
  <a href="https://arxiv.org/pdf/2509.14932.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14932v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14932v1', 'Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobias Jülg, Pierre Krack, Seongjin Bien, Yannik Blei, Khaled Gamal, Ken Nakahara, Johannes Hechtl, Roberto Calandra, Wolfram Burgard, Florian Walter

**分类**: cs.RO, cs.LG

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**提出Robot Control Stack (RCS)，用于大规模机器人学习的精简生态系统**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人学习` `控制栈` `仿真到现实` `视觉语言动作模型` `通用策略` `机器人控制` `机器人软件框架`

## 📋 核心要点

1. 传统机器人软件框架难以满足大规模机器人学习的需求，仿真环境与真实环境存在差距，限制了策略的迁移。
2. Robot Control Stack (RCS) 旨在构建一个精简、模块化且易于扩展的生态系统，统一模拟和物理机器人的接口，促进sim-to-real迁移。
3. 实验评估了RCS在VLA和RL策略开发中的可用性和性能，并分析了仿真数据对真实世界策略性能的提升效果。

## 📝 摘要（中文）

视觉-语言-动作模型（VLA）标志着机器人学习的重大转变。它们用大规模数据收集和特定设置的微调取代了专家策略的专用架构和任务定制组件。在这种以模型和可扩展训练为中心的机器学习工作流程中，传统的机器人软件框架成为瓶颈，而机器人仿真仅为从真实世界实验过渡提供有限的支持。在这项工作中，我们通过引入Robot Control Stack（RCS）来弥合这一差距，RCS是一个从头开始设计的精简生态系统，旨在支持大规模通用策略的机器人学习研究。RCS的核心是一个模块化且易于扩展的分层架构，具有用于模拟和物理机器人的统一接口，从而促进了从仿真到现实的迁移。尽管其占用空间和依赖性最小，但它提供了完整的功能集，从而可以在仿真中进行真实世界的实验和大规模训练。我们的贡献是双重的：首先，我们介绍了RCS的架构并解释了其设计原则。其次，我们评估了其在VLA和RL策略开发周期中的可用性和性能。我们的实验还对Octo，OpenVLA和Pi Zero在多个机器人上进行了广泛的评估，并阐明了仿真数据如何提高真实世界策略的性能。我们的代码，数据集，权重和视频可在https://robotcontrolstack.github.io/上找到。

## 🔬 方法详解

**问题定义**：现有机器人学习框架在处理大规模数据和通用策略时存在瓶颈。传统机器人软件框架难以适应机器学习驱动的工作流程，而机器人仿真在连接仿真环境和真实环境方面支持不足，导致策略难以从仿真环境迁移到真实环境。

**核心思路**：RCS的核心思路是构建一个精简、模块化且易于扩展的机器人控制栈，它提供统一的接口，支持模拟和物理机器人，从而简化了从仿真到真实世界的迁移过程。通过最小化依赖和提供完整的功能集，RCS旨在支持大规模训练和真实世界实验。

**技术框架**：RCS采用分层架构，包含硬件抽象层、控制层、感知层和策略层。硬件抽象层提供统一的接口，屏蔽了不同机器人平台的差异。控制层实现底层的运动控制和力控制。感知层处理来自传感器的数据，提取有用的特征。策略层执行高级的决策和规划。整个框架的设计注重模块化和可扩展性，方便用户根据需求定制和扩展。

**关键创新**：RCS的关键创新在于其精简的设计和统一的接口。与传统的机器人软件框架相比，RCS减少了不必要的复杂性，降低了学习成本。统一的接口使得策略可以在仿真环境和真实环境之间无缝切换，加速了机器人学习的迭代过程。

**关键设计**：RCS的设计注重模块化和可配置性。用户可以根据自己的需求选择和配置不同的模块。RCS还提供了丰富的工具和库，方便用户进行数据收集、模型训练和策略部署。此外，RCS还支持多种机器人平台和传感器，具有良好的兼容性。

## 📊 实验亮点

论文通过实验验证了RCS的可用性和性能。实验结果表明，RCS能够有效地支持VLA和RL策略的开发，并能够利用仿真数据提高真实世界策略的性能。论文还对Octo、OpenVLA和Pi Zero在多个机器人上进行了评估，为机器人学习的研究提供了有价值的参考。

## 🎯 应用场景

RCS可应用于各种机器人学习场景，例如工业自动化、服务机器人、自动驾驶等。它能够加速机器人策略的开发和部署，降低开发成本，提高机器人的智能化水平。RCS的模块化设计和统一接口使其易于集成到现有的机器人系统中，具有广泛的应用前景。

## 📄 摘要（原文）

> Vision-Language-Action models (VLAs) mark a major shift in robot learning. They replace specialized architectures and task-tailored components of expert policies with large-scale data collection and setup-specific fine-tuning. In this machine learning-focused workflow that is centered around models and scalable training, traditional robotics software frameworks become a bottleneck, while robot simulations offer only limited support for transitioning from and to real-world experiments. In this work, we close this gap by introducing Robot Control Stack (RCS), a lean ecosystem designed from the ground up to support research in robot learning with large-scale generalist policies. At its core, RCS features a modular and easily extensible layered architecture with a unified interface for simulated and physical robots, facilitating sim-to-real transfer. Despite its minimal footprint and dependencies, it offers a complete feature set, enabling both real-world experiments and large-scale training in simulation. Our contribution is twofold: First, we introduce the architecture of RCS and explain its design principles. Second, we evaluate its usability and performance along the development cycle of VLA and RL policies. Our experiments also provide an extensive evaluation of Octo, OpenVLA, and Pi Zero on multiple robots and shed light on how simulation data can improve real-world policy performance. Our code, datasets, weights, and videos are available at: https://robotcontrolstack.github.io/

