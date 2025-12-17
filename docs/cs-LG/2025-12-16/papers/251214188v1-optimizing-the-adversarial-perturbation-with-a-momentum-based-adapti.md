---
layout: default
title: Optimizing the Adversarial Perturbation with a Momentum-based Adaptive Matrix
---

# Optimizing the Adversarial Perturbation with a Momentum-based Adaptive Matrix

**arXiv**: [2512.14188v1](https://arxiv.org/abs/2512.14188) | [PDF](https://arxiv.org/pdf/2512.14188.pdf)

**作者**: Wei Tao, Sheng Long, Xin Liu, Wei Li, Qing Tao

**分类**: cs.LG

**发布日期**: 2025-12-16

**备注**: IEEE Transactions on Dependable and Secure Computing

---

## 💡 一句话要点

**提出基于动量的自适应矩阵攻击AdaMI，以解决对抗样本生成中的优化收敛和稳定性问题。**

**关键词**: `对抗样本生成` `优化攻击` `动量方法` `自适应矩阵` `迁移性提升` `稳定性优化` `计算机视觉安全`

## 📋 核心要点

1. 现有对抗攻击方法如PGD和MI-FGSM使用符号函数缩放扰动，存在优化理论上的收敛性和稳定性问题。
2. 提出AdaMI攻击，利用基于动量的自适应矩阵优化扰动，确保凸问题上的最优收敛，解决非收敛问题。
3. 实验显示AdaMI在多种网络上显著提升对抗样本迁移性，同时保持更好的稳定性和不可感知性。

## 📝 摘要（中文）

生成对抗样本可被表述为一个优化问题。在各种基于优化的攻击方法中，基于梯度的PGD和基于动量的MI-FGSM引起了广泛关注。然而，这些攻击都使用符号函数来缩放扰动，从优化理论的角度来看存在一些理论问题。本文首先揭示了PGD实际上是投影梯度法的一种特定重构，仅使用当前梯度来确定步长。进一步，我们展示了当使用带有累积梯度的传统自适应矩阵来缩放扰动时，PGD就变成了AdaGrad。受此分析启发，我们提出了一种新颖的基于动量的攻击方法AdaMI，其中扰动通过一个有趣的基于动量的自适应矩阵进行优化。AdaMI被证明在凸问题上能达到最优收敛，表明它解决了MI-FGSM的非收敛问题，从而确保了优化过程的稳定性。实验表明，所提出的基于动量的自适应矩阵可以作为一种通用且有效的技术，在不同网络间提升对抗样本的迁移性，同时保持更好的稳定性和不可感知性。

## 🔬 方法详解

论文提出AdaMI攻击方法，整体框架基于优化理论，将对抗样本生成视为一个优化问题。关键技术创新点是引入基于动量的自适应矩阵来缩放扰动，该矩阵结合了历史梯度信息，类似于优化算法中的动量机制。与现有方法的主要区别在于：PGD仅使用当前梯度，MI-FGSM引入动量但使用符号函数，而AdaMI通过自适应矩阵动态调整步长，避免了符号函数的局限性，从而在理论上保证凸问题的最优收敛，提高了优化过程的稳定性。

## 📊 实验亮点

AdaMI在多个基准网络上的实验表明，其对抗样本迁移性优于当前最先进方法，同时优化过程更稳定，扰动更不易被察觉，验证了基于动量的自适应矩阵的有效性。

## 🎯 应用场景

该研究可应用于计算机视觉和机器学习的安全领域，如对抗性防御、模型鲁棒性评估和隐私保护。通过生成更稳定、迁移性更强的对抗样本，有助于开发更健壮的AI系统，提升实际部署中的安全性。

## 📄 摘要（原文）

> Generating adversarial examples (AEs) can be formulated as an optimization problem. Among various optimization-based attacks, the gradient-based PGD and the momentum-based MI-FGSM have garnered considerable interest. However, all these attacks use the sign function to scale their perturbations, which raises several theoretical concerns from the point of view of optimization. In this paper, we first reveal that PGD is actually a specific reformulation of the projected gradient method using only the current gradient to determine its step-size. Further, we show that when we utilize a conventional adaptive matrix with the accumulated gradients to scale the perturbation, PGD becomes AdaGrad. Motivated by this analysis, we present a novel momentum-based attack AdaMI, in which the perturbation is optimized with an interesting momentum-based adaptive matrix. AdaMI is proved to attain optimal convergence for convex problems, indicating that it addresses the non-convergence issue of MI-FGSM, thereby ensuring stability of the optimization process. The experiments demonstrate that the proposed momentum-based adaptive matrix can serve as a general and effective technique to boost adversarial transferability over the state-of-the-art methods across different networks while maintaining better stability and imperceptibility.

