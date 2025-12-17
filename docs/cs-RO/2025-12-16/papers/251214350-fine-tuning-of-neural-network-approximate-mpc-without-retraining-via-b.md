---
layout: default
title: Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization
---

# Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14350" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14350</a>
  <a href="https://arxiv.org/pdf/2512.14350.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14350" onclick="toggleFavorite(this, '2512.14350', 'Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Henrik Hose, Paul Brunzema, Alexander von Rohr, Alexander Gräfe, Angela P. Schoellig, Sebastian Trimpe

**分类**: cs.RO, eess.SY

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于贝叶斯优化的神经近似MPC调参方法，无需重训练网络。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `近似模型预测控制` `贝叶斯优化` `神经网络` `参数调优` `机器人控制`

## 📋 核心要点

1. 传统AMPC在MPC参数调整后需重新训练网络，耗时且低效，限制了其应用。
2. 利用贝叶斯优化自动调整AMPC策略参数，无需重新训练，提升适应性和效率。
3. 硬件实验表明，该方法优于传统AMPC，并能有效处理复杂控制问题。

## 📝 摘要（中文）

近似模型预测控制（AMPC）旨在用神经网络模仿MPC的行为，从而避免在运行时求解昂贵的优化问题。然而，在部署过程中，通常需要微调底层MPC的参数。这使得AMPC在实践中变得不切实际，因为它需要重复生成新的数据集并重新训练神经网络。最近的研究通过使用MPC优化问题的近似敏感度来调整AMPC，而无需重新训练。目前，这种调整必须手动完成，这既费力又难以理解高维系统。为了解决这个问题，我们提出使用贝叶斯优化来根据实验数据调整AMPC策略的参数。通过将基于模型的控制与直接和局部学习相结合，我们的方法在硬件上实现了优于标称AMPC的性能，且只需最少的实验。这允许自动且数据高效地将AMPC适应于新的系统实例，并微调难以在MPC中直接实现的成本函数。我们在倒立摆小车上的摆动操作和欠驱动平衡独轮车机器人的偏航控制（一个具有挑战性的控制问题）的硬件实验中证明了所提出的方法。

## 🔬 方法详解

**问题定义**：现有近似模型预测控制（AMPC）方法在实际部署中，当底层MPC的参数需要调整时，必须重新生成数据集并重新训练神经网络。这个过程耗时且计算成本高昂，使得AMPC在实际应用中受到限制。此外，手动调整AMPC策略参数在高维系统中非常困难且不直观。

**核心思路**：本文的核心思路是利用贝叶斯优化（Bayesian Optimization）来自动调整AMPC策略的参数，而无需重新训练神经网络。贝叶斯优化是一种有效的全局优化方法，特别适用于目标函数评估成本高昂的情况。通过将实验数据作为反馈，贝叶斯优化能够高效地搜索最优的AMPC参数。

**技术框架**：该方法的技术框架主要包括以下几个步骤：1. 初始化AMPC策略；2. 在实际系统中运行AMPC策略并收集实验数据；3. 使用实验数据评估AMPC策略的性能；4. 使用贝叶斯优化算法，基于性能评估结果，选择下一组AMPC参数；5. 重复步骤2-4，直到找到最优的AMPC参数。其中，性能评估函数可以是任何能够反映AMPC策略控制效果的指标，例如跟踪误差、能量消耗等。

**关键创新**：该方法最重要的技术创新点在于将贝叶斯优化应用于AMPC策略的参数调整，实现了自动、数据高效的参数优化，避免了重新训练神经网络的需求。与传统的手动调整方法相比，该方法能够更快速、更有效地找到最优的AMPC参数，尤其是在高维系统中。

**关键设计**：关键设计包括：1. 贝叶斯优化算法的选择，例如高斯过程回归；2. 性能评估函数的定义，需要能够准确反映AMPC策略的控制效果；3. 实验数据的收集策略，需要保证数据的质量和多样性；4. 贝叶斯优化的超参数设置，例如探索-利用平衡。

## 📊 实验亮点

在倒立摆小车和欠驱动平衡独轮车的硬件实验中，该方法实现了优于标称AMPC的性能，证明了其有效性。实验结果表明，该方法能够以最小的实验代价，自动且数据高效地将AMPC适应于新的系统实例，并微调难以在MPC中直接实现的成本函数。

## 🎯 应用场景

该研究成果可广泛应用于机器人控制、自动驾驶、过程控制等领域。通过自动调整控制策略参数，可以提高控制系统的鲁棒性和适应性，降低人工干预的需求，并能更容易地将AMPC应用于新的系统实例和难以直接在MPC中实现的成本函数，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Approximate model-predictive control (AMPC) aims to imitate an MPC's behavior with a neural network, removing the need to solve an expensive optimization problem at runtime. However, during deployment, the parameters of the underlying MPC must usually be fine-tuned. This often renders AMPC impractical as it requires repeatedly generating a new dataset and retraining the neural network. Recent work addresses this problem by adapting AMPC without retraining using approximated sensitivities of the MPC's optimization problem. Currently, this adaption must be done by hand, which is labor-intensive and can be unintuitive for high-dimensional systems. To solve this issue, we propose using Bayesian optimization to tune the parameters of AMPC policies based on experimental data. By combining model-based control with direct and local learning, our approach achieves superior performance to nominal AMPC on hardware, with minimal experimentation. This allows automatic and data-efficient adaptation of AMPC to new system instances and fine-tuning to cost functions that are difficult to directly implement in MPC. We demonstrate the proposed method in hardware experiments for the swing-up maneuver on an inverted cartpole and yaw control of an under-actuated balancing unicycle robot, a challenging control problem.

