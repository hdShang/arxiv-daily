---
layout: default
title: "DynaFlow: Dynamics-embedded Flow Matching for Physically Consistent Motion Generation from State-only Demonstrations"
---

# DynaFlow: Dynamics-embedded Flow Matching for Physically Consistent Motion Generation from State-only Demonstrations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19804" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19804v2</a>
  <a href="https://arxiv.org/pdf/2509.19804.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19804v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19804v2', 'DynaFlow: Dynamics-embedded Flow Matching for Physically Consistent Motion Generation from State-only Demonstrations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sowoo Lee, Dongyun Kang, Jaehyun Park, Hae-Won Park

**分类**: cs.RO

**发布日期**: 2025-09-24 (更新: 2025-10-28)

**备注**: 8 pages

---

## 💡 一句话要点

**DynaFlow：嵌入动力学的Flow Matching用于从状态演示中生成物理一致的运动**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `Flow Matching` `可微模拟` `机器人运动生成` `状态演示学习` `物理一致性` `四足机器人` `运动规划`

## 📋 核心要点

1. 现有方法难以从仅状态演示中生成物理上可行的机器人运动，DynaFlow旨在解决这一问题。
2. DynaFlow的核心思想是将可微模拟器嵌入到Flow Matching模型中，确保生成的轨迹在物理上是可行的。
3. 实验表明，DynaFlow生成的动作可以在真实的Go1四足机器人上成功部署，实现各种步态和长时程运动。

## 📝 摘要（中文）

本文介绍了一种名为DynaFlow的新框架，它将可微模拟器直接嵌入到Flow Matching模型中。通过在动作空间中生成轨迹，并通过模拟器将其映射到动态可行的状态轨迹，DynaFlow确保所有输出在构建上都是物理一致的。这种端到端可微架构支持仅基于状态演示的训练，允许模型同时生成物理一致的状态轨迹，并推断生成这些轨迹所需的底层动作序列。我们通过定量评估证明了该方法的有效性，并通过将生成的动作部署到真实的Go1四足机器人上，展示了其在现实世界中的适用性。机器人成功地再现了数据集中存在的各种步态，在开环控制中执行了长时程运动，并将不可行的运动学演示转化为动态可执行的、风格化的行为。这些硬件实验验证了DynaFlow能够从仅状态演示中生成可在真实硬件上部署的、高效的运动，从而有效地弥合了运动学数据和真实世界执行之间的差距。

## 🔬 方法详解

**问题定义**：现有机器人运动生成方法通常需要动作标签或者难以保证生成运动的物理可行性，尤其是在仅有状态演示的情况下。痛点在于如何从状态序列中推断出合理的动作序列，并确保生成的运动符合动力学约束。

**核心思路**：DynaFlow的核心思路是将一个可微的物理模拟器集成到Flow Matching框架中。Flow Matching负责生成动作序列，而模拟器则将这些动作转化为状态序列。通过这种方式，模型可以直接在动作空间中进行优化，并利用模拟器来保证生成的状态序列是物理上可行的。

**技术框架**：DynaFlow的整体架构包含两个主要部分：一个Flow Matching模块和一个可微模拟器。Flow Matching模块负责生成动作序列，它以初始状态和目标状态作为输入，输出一系列动作。这些动作被输入到可微模拟器中，模拟器根据动力学模型计算出相应的状态序列。整个系统是端到端可微的，因此可以通过反向传播来优化Flow Matching模块的参数。

**关键创新**：DynaFlow的关键创新在于将可微模拟器嵌入到Flow Matching框架中，从而实现了从状态演示中生成物理一致的运动。与传统的运动规划方法相比，DynaFlow不需要显式地定义动力学约束，而是通过模拟器来隐式地满足这些约束。此外，DynaFlow还可以从仅状态演示中学习，而不需要动作标签。

**关键设计**：DynaFlow的关键设计包括：1) 使用神经网络来参数化Flow Matching模块，使其能够生成复杂的动作序列；2) 使用可微的物理模拟器，例如PyTorch中的DiffTaichi，以便进行端到端训练；3) 设计合适的损失函数，例如状态重构损失和动作正则化损失，以保证生成的状态序列与演示数据相似，并且动作序列是平滑的。

## 📊 实验亮点

DynaFlow在Go1四足机器人上的实验结果表明，它可以成功地再现数据集中存在的各种步态，并在开环控制中执行长时程运动。此外，DynaFlow还可以将不可行的运动学演示转化为动态可执行的、风格化的行为。这些实验验证了DynaFlow能够从仅状态演示中生成可在真实硬件上部署的、高效的运动。

## 🎯 应用场景

DynaFlow具有广泛的应用前景，例如机器人运动规划、动画生成和虚拟现实。它可以用于控制各种类型的机器人，例如四足机器人、人形机器人和无人机。此外，DynaFlow还可以用于生成逼真的动画，例如人物行走和跑步的动画。在虚拟现实中，DynaFlow可以用于创建交互式的物理环境，让用户可以与虚拟物体进行交互。

## 📄 摘要（原文）

> This paper introduces DynaFlow, a novel framework that embeds a differentiable simulator directly into a flow matching model. By generating trajectories in the action space and mapping them to dynamically feasible state trajectories via the simulator, DynaFlow ensures all outputs are physically consistent by construction. This end-to-end differentiable architecture enables training on state-only demonstrations, allowing the model to simultaneously generate physically consistent state trajectories while inferring the underlying action sequences required to produce them. We demonstrate the effectiveness of our approach through quantitative evaluations and showcase its real-world applicability by deploying the generated actions onto a physical Go1 quadruped robot. The robot successfully reproduces diverse gait present in the dataset, executes long-horizon motions in open-loop control and translates infeasible kinematic demonstrations into dynamically executable, stylistic behaviors. These hardware experiments validate that DynaFlow produces deployable, highly effective motions on real-world hardware from state-only demonstrations, effectively bridging the gap between kinematic data and real-world execution.

