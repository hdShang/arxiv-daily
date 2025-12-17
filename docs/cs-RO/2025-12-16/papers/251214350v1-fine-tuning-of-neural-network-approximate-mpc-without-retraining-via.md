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

**提出基于贝叶斯优化的近似模型预测控制微调方法，无需重新训练神经网络即可适应新系统实例和成本函数。**

**关键词**: `近似模型预测控制` `贝叶斯优化` `神经网络微调` `机器人控制` `自适应控制` `硬件实验` `数据高效学习` `优化参数调整`

## 📋 核心要点

1. 现有AMPC在部署时需手动微调参数，过程繁琐且不直观，尤其对高维系统不实用。
2. 提出结合贝叶斯优化与AMPC，利用实验数据自动调整策略参数，实现无需重新训练的适应。
3. 在倒立摆和独轮机器人硬件实验中，方法以最小实验量显著提升性能，优于名义AMPC。

## 📝 摘要（中文）

近似模型预测控制（AMPC）旨在用神经网络模仿MPC的行为，从而避免在运行时求解昂贵的优化问题。然而，在部署过程中，通常需要对底层MPC的参数进行微调，这往往需要反复生成新数据集并重新训练神经网络，使得AMPC不实用。最近的研究通过利用MPC优化问题的近似灵敏度来适应AMPC而无需重新训练，但当前这种适应必须手动完成，对于高维系统来说既费力又不直观。为解决这一问题，我们提出使用贝叶斯优化基于实验数据来调整AMPC策略的参数。通过将基于模型的控制与直接局部学习相结合，我们的方法在硬件上实现了优于名义AMPC的性能，且实验量最小。这使得AMPC能够自动且数据高效地适应新系统实例，并微调到难以直接在MPC中实现的成本函数。我们在硬件实验中展示了所提方法，包括倒立摆的摆起动作和欠驱动平衡独轮机器人的偏航控制，这是一个具有挑战性的控制问题。

## 🔬 方法详解

论文提出一个整体框架，将近似模型预测控制（AMPC）与贝叶斯优化（BO）相结合。核心思想是利用BO基于少量实验数据自动搜索AMPC策略的最优参数，而无需重新训练神经网络。关键技术创新点在于将模型基控制（通过AMPC近似MPC）与直接局部学习（通过BO优化参数）融合，实现数据高效的适应。与现有方法的主要区别在于：现有方法依赖手动调整或基于近似灵敏度的适应，而本方法自动化参数微调过程，避免了重新训练神经网络的成本，并能处理难以直接实现的成本函数。

## 📊 实验亮点

在倒立摆摆起和欠驱动独轮机器人偏航控制的硬件实验中，所提方法以最小实验量实现了优于名义AMPC的性能，成功适应新系统实例并优化了难以直接实现的成本函数，验证了其自动化和数据高效的优势。

## 🎯 应用场景

该研究适用于机器人控制、自动化系统和实时优化领域，特别是在需要快速适应新硬件实例或复杂成本函数的场景中，如无人机导航、工业机械臂和智能车辆控制，具有提升系统鲁棒性和降低部署成本的实际价值。

## 📄 摘要（原文）

> Approximate model-predictive control (AMPC) aims to imitate an MPC's behavior with a neural network, removing the need to solve an expensive optimization problem at runtime. However, during deployment, the parameters of the underlying MPC must usually be fine-tuned. This often renders AMPC impractical as it requires repeatedly generating a new dataset and retraining the neural network. Recent work addresses this problem by adapting AMPC without retraining using approximated sensitivities of the MPC's optimization problem. Currently, this adaption must be done by hand, which is labor-intensive and can be unintuitive for high-dimensional systems. To solve this issue, we propose using Bayesian optimization to tune the parameters of AMPC policies based on experimental data. By combining model-based control with direct and local learning, our approach achieves superior performance to nominal AMPC on hardware, with minimal experimentation. This allows automatic and data-efficient adaptation of AMPC to new system instances and fine-tuning to cost functions that are difficult to directly implement in MPC. We demonstrate the proposed method in hardware experiments for the swing-up maneuver on an inverted cartpole and yaw control of an under-actuated balancing unicycle robot, a challenging control problem.

