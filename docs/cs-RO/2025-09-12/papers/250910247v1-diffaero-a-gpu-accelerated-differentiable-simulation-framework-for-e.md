---
layout: default
title: "DiffAero: A GPU-Accelerated Differentiable Simulation Framework for Efficient Quadrotor Policy Learning"
---

# DiffAero: A GPU-Accelerated Differentiable Simulation Framework for Efficient Quadrotor Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10247" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10247v1</a>
  <a href="https://arxiv.org/pdf/2509.10247.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10247v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10247v1', 'DiffAero: A GPU-Accelerated Differentiable Simulation Framework for Efficient Quadrotor Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinhong Zhang, Runqing Wang, Yunfan Ren, Jian Sun, Hao Fang, Jie Chen, Gang Wang

**分类**: cs.RO

**发布日期**: 2025-09-12

**备注**: 8 pages, 11 figures, 1 table

**🔗 代码/项目**: [GITHUB](https://github.com/flyingbitac/diffaero)

---

## 💡 一句话要点

**DiffAero：用于高效四旋翼策略学习的GPU加速可微仿真框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `四旋翼控制` `可微仿真` `GPU加速` `强化学习` `自主导航`

## 📋 核心要点

1. 现有四旋翼控制策略学习仿真器在CPU-GPU数据传输上存在瓶颈，限制了训练效率和可微学习算法的应用。
2. DiffAero通过在GPU上并行化物理和渲染，消除了CPU-GPU数据传输瓶颈，并提供统一的GPU原生训练界面。
3. 实验表明，DiffAero结合混合学习算法，可以在消费级硬件上快速学习到鲁棒的飞行策略，显著提升训练效率。

## 📝 摘要（中文）

本文介绍DiffAero，一个轻量级、GPU加速且完全可微的仿真框架，专为高效的四旋翼控制策略学习而设计。DiffAero支持环境级和智能体级并行，并在统一的GPU原生训练界面中集成了多种动力学模型、可定制的传感器堆栈（IMU、深度相机和激光雷达）以及各种飞行任务。通过在GPU上完全并行化物理和渲染，DiffAero消除了CPU-GPU数据传输瓶颈，并实现了仿真吞吐量的数量级提升。与现有模拟器相比，DiffAero不仅提供高性能仿真，还可作为探索可微和混合学习算法的研究平台。广泛的基准测试和真实飞行实验表明，DiffAero与混合学习算法相结合，可以在消费级硬件上以小时为单位学习到鲁棒的飞行策略。

## 🔬 方法详解

**问题定义**：现有四旋翼控制策略学习仿真器通常依赖CPU进行物理计算，然后将数据传输到GPU进行渲染，这导致了显著的CPU-GPU数据传输瓶颈，限制了仿真速度和训练效率。此外，现有仿真器在可微性方面支持不足，难以直接应用可微学习算法进行策略优化。

**核心思路**：DiffAero的核心思路是将整个仿真流程，包括物理计算和渲染，都迁移到GPU上进行并行处理，从而消除CPU-GPU数据传输瓶颈。同时，DiffAero采用可微的物理引擎和渲染器，使得整个仿真过程可微，从而可以直接使用梯度下降等优化算法进行策略学习。

**技术框架**：DiffAero的整体架构包含以下几个主要模块：1) 动力学模型：支持多种四旋翼动力学模型，用户可以根据需要选择合适的模型。2) 传感器模型：集成了IMU、深度相机和激光雷达等多种传感器模型，可以模拟真实环境中的传感器数据。3) 渲染引擎：采用GPU加速的渲染引擎，可以生成逼真的视觉图像。4) 训练接口：提供统一的GPU原生训练接口，方便用户进行策略学习。

**关键创新**：DiffAero最重要的技术创新在于其完全GPU加速和可微的仿真框架。与现有仿真器相比，DiffAero将物理计算和渲染都迁移到GPU上进行并行处理，从而消除了CPU-GPU数据传输瓶颈，显著提升了仿真速度。此外，DiffAero采用可微的物理引擎和渲染器，使得整个仿真过程可微，从而可以直接使用梯度下降等优化算法进行策略学习。

**关键设计**：DiffAero的关键设计包括：1) GPU加速的物理引擎：采用CUDA等技术实现GPU加速的物理引擎，可以高效地进行动力学计算。2) 可微渲染器：采用可微渲染技术，可以计算渲染图像对控制参数的梯度。3) 并行化训练：支持环境级和智能体级并行，可以进一步提升训练效率。4) 混合学习算法：支持可微学习和强化学习等多种学习算法，可以灵活地进行策略优化。

## 📊 实验亮点

DiffAero在仿真吞吐量方面实现了数量级的提升，与现有仿真器相比，训练速度显著加快。结合混合学习算法，DiffAero可以在消费级硬件上以小时为单位学习到鲁棒的飞行策略。真实飞行实验验证了DiffAero训练的策略在实际环境中的有效性。

## 🎯 应用场景

DiffAero可应用于各种四旋翼无人机的控制策略学习和算法验证，例如自主导航、避障、目标跟踪等。该框架的高效性和可微性使其能够加速算法开发周期，并为探索新的学习算法提供平台。此外，DiffAero还可用于生成训练数据，用于训练在真实环境中部署的鲁棒控制策略，降低实机测试的成本和风险。

## 📄 摘要（原文）

> This letter introduces DiffAero, a lightweight, GPU-accelerated, and fully differentiable simulation framework designed for efficient quadrotor control policy learning. DiffAero supports both environment-level and agent-level parallelism and integrates multiple dynamics models, customizable sensor stacks (IMU, depth camera, and LiDAR), and diverse flight tasks within a unified, GPU-native training interface. By fully parallelizing both physics and rendering on the GPU, DiffAero eliminates CPU-GPU data transfer bottlenecks and delivers orders-of-magnitude improvements in simulation throughput. In contrast to existing simulators, DiffAero not only provides high-performance simulation but also serves as a research platform for exploring differentiable and hybrid learning algorithms. Extensive benchmarks and real-world flight experiments demonstrate that DiffAero and hybrid learning algorithms combined can learn robust flight policies in hours on consumer-grade hardware. The code is available at https://github.com/flyingbitac/diffaero.

