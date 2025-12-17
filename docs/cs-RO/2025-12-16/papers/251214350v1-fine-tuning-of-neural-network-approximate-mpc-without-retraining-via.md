---
layout: default
title: Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization
---

# Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization

**arXiv**: [2512.14350v1](https://arxiv.org/abs/2512.14350) | [PDF](https://arxiv.org/pdf/2512.14350.pdf)

**作者**: Henrik Hose, Paul Brunzema, Alexander von Rohr, Alexander Gräfe, Angela P. Schoellig, Sebastian Trimpe

**分类**: cs.RO, eess.SY

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于贝叶斯优化的近似模型预测控制微调方法，无需重新训练神经网络，实现自动高效参数调整。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `近似模型预测控制` `贝叶斯优化` `神经网络控制` `参数微调` `机器人控制` `硬件实验` `数据高效学习` `自动适应`

## 📋 核心要点

1. 现有AMPC方法在部署时需手动微调参数，过程耗时且对高维系统不直观，限制了实际应用。
2. 提出结合贝叶斯优化与AMPC，利用实验数据自动调整参数，无需重新训练神经网络，实现高效适应。
3. 在倒立摆和独轮机器人硬件实验中，该方法性能优于名义AMPC，实验量最小，验证了其有效性。

## 📝 摘要（中文）

近似模型预测控制（AMPC）旨在通过神经网络模仿MPC的行为，避免运行时求解昂贵的优化问题。然而，在部署过程中，通常需要微调底层MPC的参数，这往往导致AMPC不实用，因为它需要重复生成新数据集并重新训练神经网络。最近的研究通过利用MPC优化问题的近似灵敏度来适应AMPC而无需重新训练，解决了这一问题。目前，这种适应必须手动完成，这既耗时又对高维系统不直观。为了解决这个问题，我们提出使用贝叶斯优化基于实验数据来调整AMPC策略的参数。通过将基于模型的控制与直接和局部学习相结合，我们的方法在硬件上实现了优于名义AMPC的性能，且实验量最小。这使得AMPC能够自动且数据高效地适应新系统实例，并微调到难以直接在MPC中实现的成本函数。我们在硬件实验中展示了所提出的方法，包括倒立摆的摆动上升操作和欠驱动平衡独轮机器人的偏航控制，这是一个具有挑战性的控制问题。

## 🔬 方法详解

论文提出一种基于贝叶斯优化的AMPC微调框架。整体框架包括：使用神经网络近似MPC策略，然后通过贝叶斯优化基于实验数据自动调整AMPC的参数，无需重新训练神经网络。关键技术创新点在于将贝叶斯优化与AMPC结合，利用模型预测控制的先验知识和局部学习，实现数据高效的参数优化。与现有方法的主要区别在于：现有方法依赖手动调整或基于近似灵敏度的适应，而本方法自动化程度高，能处理高维参数空间，且通过贝叶斯优化直接优化性能指标，避免了重新训练的开销。

## 📊 实验亮点

在倒立摆摆动上升和独轮机器人偏航控制的硬件实验中，该方法相比名义AMPC实现了性能提升，实验量最小，成功处理了欠驱动系统的挑战性控制问题。

## 🎯 应用场景

该研究适用于机器人控制、自动化系统等需要实时优化的领域，特别是在系统参数变化或成本函数复杂时，能自动适应新实例，提高控制性能，降低部署成本。

## 📄 摘要（原文）

> Approximate model-predictive control (AMPC) aims to imitate an MPC's behavior with a neural network, removing the need to solve an expensive optimization problem at runtime. However, during deployment, the parameters of the underlying MPC must usually be fine-tuned. This often renders AMPC impractical as it requires repeatedly generating a new dataset and retraining the neural network. Recent work addresses this problem by adapting AMPC without retraining using approximated sensitivities of the MPC's optimization problem. Currently, this adaption must be done by hand, which is labor-intensive and can be unintuitive for high-dimensional systems. To solve this issue, we propose using Bayesian optimization to tune the parameters of AMPC policies based on experimental data. By combining model-based control with direct and local learning, our approach achieves superior performance to nominal AMPC on hardware, with minimal experimentation. This allows automatic and data-efficient adaptation of AMPC to new system instances and fine-tuning to cost functions that are difficult to directly implement in MPC. We demonstrate the proposed method in hardware experiments for the swing-up maneuver on an inverted cartpole and yaw control of an under-actuated balancing unicycle robot, a challenging control problem.

