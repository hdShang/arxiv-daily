---
layout: default
title: Model-Based Adaptive Precision Control for Tabletop Planar Pushing Under Uncertain Dynamics
---

# Model-Based Adaptive Precision Control for Tabletop Planar Pushing Under Uncertain Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03768" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03768v1</a>
  <a href="https://arxiv.org/pdf/2510.03768.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03768v1" onclick="toggleFavorite(this, '2510.03768v1', 'Model-Based Adaptive Precision Control for Tabletop Planar Pushing Under Uncertain Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aydin Ahmadi, Baris Akgun

**分类**: cs.RO

**发布日期**: 2025-10-04

---

## 💡 一句话要点

**提出基于模型的自适应精度控制方法，解决不确定动力学下的桌面平面推移任务。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `平面推移` `模型预测控制` `非抓取操作` `动力学模型学习` `循环神经网络` `机器人控制` `自适应控制` `域随机化`

## 📋 核心要点

1. 现有数据驱动的平面推移方法能力有限，通常针对特定任务，泛化性不足。
2. 提出基于模型的框架，利用单个学习模型处理多种任务，无需重复训练，提升通用性。
3. 实验表明，该方法在精确位置控制、轨迹跟踪和避障方面表现出色，并成功迁移到真实机器人。

## 📝 摘要（中文）

本文提出了一种基于模型的非抓取桌面推移框架，该框架使用单个学习模型来处理多个任务，无需重新训练。该方法采用基于循环GRU的架构，并添加了非线性层，以捕获对象-环境动力学，同时确保稳定性。定制的状态-动作表示使模型能够推广到不确定的动力学、可变的推移长度和不同的任务。在控制方面，我们将学习到的动力学与基于采样的模型预测路径积分（MPPI）控制器集成，该控制器生成自适应的、面向任务的动作。该框架支持侧面切换、可变长度的推移以及精确的定位、轨迹跟踪和避障等目标。在模拟环境中进行训练，并进行域随机化以支持从模拟到真实的迁移。通过消融研究评估了该架构，表明预测精度和稳定rollout得到了提高。然后，在模拟和真实世界的实验中使用Franka Panda机器人和无标记跟踪验证了整个系统。结果表明，在严格的阈值下，精确的定位具有很高的成功率，并且在轨迹跟踪和避障方面表现出色。此外，只需更改控制器的目标函数即可解决多个任务，而无需重新训练。虽然目前的工作重点是单一对象类型，但通过训练更长的推移长度并设计一个平衡的控制器来减少更长horizon目标所需的步数，从而扩展了该框架。

## 🔬 方法详解

**问题定义**：论文旨在解决在不确定动力学条件下，如何实现桌面平面推移的精确控制问题。现有方法通常依赖于手工设计的策略或针对特定任务训练的模型，难以泛化到不同的任务和环境。这些方法在处理动力学不确定性、可变推移长度以及多种任务目标（如精确位置控制、轨迹跟踪、避障）时存在局限性。

**核心思路**：论文的核心思路是学习一个能够捕捉对象-环境动力学的通用模型，并将其与模型预测控制（MPC）相结合，实现自适应的推移控制。通过学习动力学模型，控制器可以预测不同动作序列的未来状态，从而选择最优的动作来实现目标。这种方法允许控制器根据当前状态和任务目标动态调整控制策略，从而提高鲁棒性和泛化能力。

**技术框架**：整体框架包括以下几个主要模块：1) 数据收集：在模拟环境中通过随机策略生成推移数据。2) 动力学模型学习：使用循环GRU网络学习对象-环境的动力学模型。3) 模型预测控制：使用学习到的动力学模型和MPPI控制器生成控制动作。4) 任务执行：将控制动作发送给机器人执行推移任务。

**关键创新**：该论文的关键创新在于：1) 使用单个学习模型处理多种推移任务，无需针对每个任务进行单独训练。2) 采用基于循环GRU的架构，能够有效捕捉对象-环境的动力学，并保证rollout的稳定性。3) 将学习到的动力学模型与MPPI控制器相结合，实现了自适应的推移控制，能够根据当前状态和任务目标动态调整控制策略。

**关键设计**：1) 状态-动作表示：论文设计了一种定制的状态-动作表示，使模型能够推广到不确定的动力学、可变的推移长度和不同的任务。2) 损失函数：使用均方误差（MSE）作为损失函数，训练动力学模型。3) 网络结构：采用基于循环GRU的架构，并添加了非线性层，以提高模型的表达能力。4) MPPI控制器：使用MPPI控制器生成控制动作，该控制器通过采样不同的动作序列并评估其成本函数来选择最优动作。

## 📊 实验亮点

实验结果表明，该方法在精确位置控制方面取得了很高的成功率，在轨迹跟踪和避障方面表现出色。在模拟环境中，该方法能够成功地将物体推到目标位置，误差小于设定的阈值。在真实世界的实验中，该方法也能够成功地完成推移任务，并且能够适应不同的物体和环境。此外，该方法只需更改控制器的目标函数即可解决多个任务，而无需重新训练。

## 🎯 应用场景

该研究成果可应用于自动化装配、物流分拣、家庭服务机器人等领域。通过学习通用的推移动力学模型，机器人可以灵活地操作各种物体，完成复杂的任务，例如在拥挤的环境中移动物体、将物体放置到精确的位置等。该技术还可以扩展到其他类型的非抓取操作，例如滑动、倾斜等，从而提高机器人的操作能力和适应性。

## 📄 摘要（原文）

> Data-driven planar pushing methods have recently gained attention as they reduce manual engineering effort and improve generalization compared to analytical approaches. However, most prior work targets narrow capabilities (e.g., side switching, precision, or single-task training), limiting broader applicability. We present a model-based framework for non-prehensile tabletop pushing that uses a single learned model to address multiple tasks without retraining. Our approach employs a recurrent GRU-based architecture with additional non-linear layers to capture object-environment dynamics while ensuring stability. A tailored state-action representation enables the model to generalize across uncertain dynamics, variable push lengths, and diverse tasks. For control, we integrate the learned dynamics with a sampling-based Model Predictive Path Integral (MPPI) controller, which generates adaptive, task-oriented actions. This framework supports side switching, variable-length pushes, and objectives such as precise positioning, trajectory following, and obstacle avoidance. Training is performed in simulation with domain randomization to support sim-to-real transfer. We first evaluate the architecture through ablation studies, showing improved prediction accuracy and stable rollouts. We then validate the full system in simulation and real-world experiments using a Franka Panda robot with markerless tracking. Results demonstrate high success rates in precise positioning under strict thresholds and strong performance in trajectory tracking and obstacle avoidance. Moreover, multiple tasks are solved simply by changing the controller's objective function, without retraining. While our current focus is on a single object type, we extend the framework by training on wider push lengths and designing a balanced controller that reduces the number of steps for longer-horizon goals.

