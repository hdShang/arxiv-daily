---
layout: default
title: Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization
---

# Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14350" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14350v1</a>
  <a href="https://arxiv.org/pdf/2512.14350.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14350v1" onclick="toggleFavorite(this, '2512.14350v1', 'Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Henrik Hose, Paul Brunzema, Alexander von Rohr, Alexander Gräfe, Angela P. Schoellig, Sebastian Trimpe

**分类**: cs.RO, eess.SY

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于贝叶斯优化的AMPC调参方法，无需重训练神经网络**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `近似模型预测控制` `贝叶斯优化` `神经网络` `参数调优` `机器人控制`

## 📋 核心要点

1. 传统AMPC在MPC参数调整后需重新训练神经网络，耗时且低效，限制了其在实际部署中的应用。
2. 利用贝叶斯优化自动调整AMPC策略参数，结合模型控制与局部学习，实现数据高效的参数优化。
3. 硬件实验表明，该方法在倒立摆和平衡独轮车控制上优于传统AMPC，验证了其有效性。

## 📝 摘要（中文）

近似模型预测控制(AMPC)旨在用神经网络模仿MPC的行为，从而避免在运行时求解昂贵的优化问题。然而，在部署期间，通常需要对底层MPC的参数进行微调。这使得AMPC在实践中变得不切实际，因为它需要重复生成新的数据集并重新训练神经网络。最近的研究通过使用MPC优化问题的近似敏感性来调整AMPC，而无需重新训练。目前，这种调整必须手动完成，这既费力，对于高维系统来说也可能不直观。为了解决这个问题，我们提出使用贝叶斯优化来根据实验数据调整AMPC策略的参数。通过将基于模型的控制与直接和局部学习相结合，我们的方法在硬件上实现了优于标称AMPC的性能，并且只需最少的实验。这允许AMPC自动且数据高效地适应新的系统实例，并微调难以直接在MPC中实现的成本函数。我们在倒立摆小车上的摆动操作和欠驱动平衡独轮车机器人的偏航控制（一个具有挑战性的控制问题）的硬件实验中展示了所提出的方法。

## 🔬 方法详解

**问题定义**：现有的近似模型预测控制(AMPC)方法在实际部署中，当底层MPC的参数需要调整时，需要重新生成数据集并重新训练神经网络，这使得AMPC的部署和维护成本很高，限制了其应用范围。手动调整AMPC策略参数既费时又容易出错，尤其是在高维系统中。

**核心思路**：本文的核心思路是利用贝叶斯优化(Bayesian Optimization)来自动调整AMPC策略的参数，而无需重新训练神经网络。贝叶斯优化是一种高效的全局优化算法，特别适用于目标函数评估成本高昂的情况。通过将模型预测控制与直接和局部学习相结合，可以实现数据高效的参数调整。

**技术框架**：该方法的技术框架主要包括以下几个步骤：1) 初始化AMPC策略；2) 在实际系统中运行AMPC策略并收集实验数据；3) 使用实验数据构建目标函数，该目标函数反映了AMPC策略的性能；4) 使用贝叶斯优化算法优化AMPC策略的参数，以最大化目标函数；5) 重复步骤2-4，直到AMPC策略的性能达到期望水平。

**关键创新**：该方法最重要的技术创新点在于将贝叶斯优化应用于AMPC策略的参数调整，从而实现了自动、数据高效的参数优化，避免了重新训练神经网络的需要。与手动调整参数相比，贝叶斯优化可以更有效地探索参数空间，找到更优的参数组合。此外，该方法结合了模型预测控制和直接学习，可以充分利用先验知识和实验数据。

**关键设计**：在贝叶斯优化中，需要选择合适的代理模型(surrogate model)和采集函数(acquisition function)。本文可能采用了高斯过程(Gaussian Process)作为代理模型，并使用期望提升(Expected Improvement)或置信上限(Upper Confidence Bound)作为采集函数。目标函数的设计需要根据具体的控制任务进行调整，例如，可以采用跟踪误差、控制输入能量等指标。

## 📊 实验亮点

该论文在倒立摆小车和平衡独轮车的硬件实验中验证了所提出方法的有效性。实验结果表明，该方法在硬件上实现了优于标称AMPC的性能，并且只需最少的实验。具体来说，该方法能够自动调整AMPC策略的参数，使其适应新的系统实例，并微调难以直接在MPC中实现的成本函数。这些实验结果表明，该方法具有很强的实用价值。

## 🎯 应用场景

该研究成果可广泛应用于机器人控制、自动驾驶、过程控制等领域。通过自动调整AMPC策略参数，可以使系统快速适应新的环境和任务，提高控制性能和鲁棒性。此外，该方法还可以用于微调难以直接在MPC中实现的成本函数，例如，考虑能耗、磨损等因素的成本函数。未来，该方法有望应用于更复杂的控制系统，例如，多机器人协同控制、智能交通系统等。

## 📄 摘要（原文）

> Approximate model-predictive control (AMPC) aims to imitate an MPC's behavior with a neural network, removing the need to solve an expensive optimization problem at runtime. However, during deployment, the parameters of the underlying MPC must usually be fine-tuned. This often renders AMPC impractical as it requires repeatedly generating a new dataset and retraining the neural network. Recent work addresses this problem by adapting AMPC without retraining using approximated sensitivities of the MPC's optimization problem. Currently, this adaption must be done by hand, which is labor-intensive and can be unintuitive for high-dimensional systems. To solve this issue, we propose using Bayesian optimization to tune the parameters of AMPC policies based on experimental data. By combining model-based control with direct and local learning, our approach achieves superior performance to nominal AMPC on hardware, with minimal experimentation. This allows automatic and data-efficient adaptation of AMPC to new system instances and fine-tuning to cost functions that are difficult to directly implement in MPC. We demonstrate the proposed method in hardware experiments for the swing-up maneuver on an inverted cartpole and yaw control of an under-actuated balancing unicycle robot, a challenging control problem.

