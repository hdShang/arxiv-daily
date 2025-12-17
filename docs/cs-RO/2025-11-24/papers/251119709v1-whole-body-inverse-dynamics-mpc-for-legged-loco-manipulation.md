---
layout: default
title: Whole-Body Inverse Dynamics MPC for Legged Loco-Manipulation
---

# Whole-Body Inverse Dynamics MPC for Legged Loco-Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19709" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19709v1</a>
  <a href="https://arxiv.org/pdf/2511.19709.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19709v1" onclick="toggleFavorite(this, '2511.19709v1', 'Whole-Body Inverse Dynamics MPC for Legged Loco-Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lukas Molnar, Jin Cheng, Gabriele Fadini, Dongho Kang, Fatemeh Zargarbashi, Stelian Coros

**分类**: cs.RO

**发布日期**: 2025-11-24

**备注**: 9 pages, 6 figures, to be published in IEEE Robotics and Automation Letters (Special Issue: Advancements in MPC and Learning Algorithms for Legged Robots)

---

## 💡 一句话要点

**提出基于全身逆动力学MPC的腿式机器人Loco-manipulation方法，实现运动与力规划的统一优化。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `Loco-manipulation` `全身控制` `模型预测控制` `逆动力学` `四足机器人`

## 📋 核心要点

1. Loco-manipulation需要协调全身运动以有效地操纵物体并保持运动稳定性，这给规划和控制带来了重大挑战。
2. 该论文提出了一种全身模型预测控制（MPC）框架，通过逆动力学直接优化关节扭矩，实现运动和力规划的统一。
3. 在Unitree B2四足机器人上进行了实验，配备Unitree Z1机械臂，实现了80Hz的实时控制，并验证了在复杂loco-manipulation任务中的有效性。

## 📝 摘要（中文）

本文提出了一种全身模型预测控制（MPC）框架，该框架通过全阶逆动力学直接优化关节扭矩，从而在单个预测层内实现统一的运动和力规划与执行。这种方法能够产生符合物理规律的全身行为，并考虑了系统的动力学和物理约束。我们使用开源软件框架（Pinocchio和CasADi）以及最先进的内点求解器Fatrop实现了我们的MPC公式。在配备Unitree Z1机械臂的Unitree B2四足机器人的真实实验中，我们的MPC公式实现了80 Hz的实时性能。我们展示了需要对末端执行器的位置和力进行精细控制的loco-manipulation任务，以执行诸如拉重物、推箱子和擦拭白板等真实世界的交互。

## 🔬 方法详解

**问题定义**：现有的loco-manipulation方法通常将运动规划和力控制分离，难以处理复杂的全身动力学约束和接触力优化。这导致在需要精细操作和稳定运动的场景中，机器人性能受限，例如在推、拉重物时难以保持平衡和精确控制末端执行器的力。

**核心思路**：该论文的核心思路是将运动规划和力控制集成到一个统一的MPC框架中，通过直接优化关节扭矩来实现全身运动的协调。利用全阶逆动力学模型，能够显式地考虑系统的动力学约束和外部接触力，从而生成更自然、更符合物理规律的全身运动。

**技术框架**：该方法采用模型预测控制（MPC）框架，以机器人全身动力学模型为基础，预测未来一段时间内的机器人状态。MPC控制器通过优化目标函数，计算出最优的关节扭矩序列。该目标函数通常包含运动目标（如末端执行器位置跟踪）、力目标（如接触力控制）以及稳定性和能量消耗等约束。整个框架使用Pinocchio和CasADi等开源库进行建模和优化，并使用Fatrop求解器进行实时求解。

**关键创新**：该方法最重要的创新点在于使用全阶逆动力学模型直接优化关节扭矩。与传统的基于简化模型的MPC方法相比，该方法能够更精确地描述机器人的动力学行为，并显式地考虑关节力矩限制、摩擦锥约束等物理约束。这种方法避免了运动学逆解和力分配等中间步骤，简化了控制流程，提高了控制精度和鲁棒性。

**关键设计**：该MPC框架的关键设计包括：1) 目标函数的设计，需要平衡运动目标、力目标和稳定性目标；2) 约束条件的设计，需要考虑关节力矩限制、摩擦锥约束、碰撞避免等；3) MPC的预测时域和控制频率的选择，需要在计算复杂度和控制性能之间进行权衡。此外，求解器的选择也至关重要，需要选择能够快速求解大规模非线性优化问题的求解器，如Fatrop。

## 📊 实验亮点

在Unitree B2四足机器人上的实验表明，该MPC框架能够以80Hz的实时频率运行，并成功完成了拉重物、推箱子和擦拭白板等loco-manipulation任务。这些任务需要机器人同时控制末端执行器的位置和力，并保持自身的平衡。实验结果表明，该方法能够有效地处理复杂的动力学约束和接触力，实现稳定和精确的loco-manipulation。

## 🎯 应用场景

该研究成果可应用于各种需要复杂运动和力控制的机器人任务，例如：在复杂地形上的物体搬运、建筑工地的辅助作业、灾难救援中的精细操作等。通过提高机器人在复杂环境中的适应性和操作能力，该研究有望推动机器人技术在工业、服务业和医疗等领域的广泛应用。

## 📄 摘要（原文）

> Loco-manipulation demands coordinated whole-body motion to manipulate objects effectively while maintaining locomotion stability, presenting significant challenges for both planning and control. In this work, we propose a whole-body model predictive control (MPC) framework that directly optimizes joint torques through full-order inverse dynamics, enabling unified motion and force planning and execution within a single predictive layer. This approach allows emergent, physically consistent whole-body behaviors that account for the system's dynamics and physical constraints. We implement our MPC formulation using open software frameworks (Pinocchio and CasADi), along with the state-of-the-art interior-point solver Fatrop. In real-world experiments on a Unitree B2 quadruped equipped with a Unitree Z1 manipulator arm, our MPC formulation achieves real-time performance at 80 Hz. We demonstrate loco-manipulation tasks that demand fine control over the end-effector's position and force to perform real-world interactions like pulling heavy loads, pushing boxes, and wiping whiteboards.

