---
layout: default
title: Nonlinear System Identification Nano-drone Benchmark
---

# Nonlinear System Identification Nano-drone Benchmark

**arXiv**: [2512.14450v1](https://arxiv.org/abs/2512.14450) | [PDF](https://arxiv.org/pdf/2512.14450.pdf)

**作者**: Riccardo Busetto, Elia Cereda, Marco Forgione, Gabriele Maroni, Dario Piga, Daniele Palossi

**分类**: eess.SY, cs.RO

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/idsia-robotics/nanodrone-sysid-benchmark)

---

## 💡 一句话要点

**提出基于Crazyflie 2.1纳米四旋翼的75k真实世界样本系统辨识基准，以解决敏捷微型无人机非线性动力学建模挑战。**

🎯 **匹配领域**: **强化学习**

**关键词**: `系统辨识基准` `非线性动力学` `微型无人机` `真实世界数据` `多步预测` `开源数据集` `机器人控制` `敏捷机动`

## 📋 核心要点

1. 现有系统辨识方法在微型无人机等非线性、不稳定平台上缺乏标准化评估基准，难以公平比较算法性能。
2. 论文提出基于Crazyflie 2.1纳米四旋翼的真实世界数据集和基准框架，包含多步预测指标和开源实现。
3. 基准提供了75k样本数据和基线模型，展示了在噪声和非线性下预测的挑战，支持算法透明比较。

## 📝 摘要（中文）

我们引入了一个基于Crazyflie 2.1无刷纳米四旋翼（一种广泛用于机器人研究的重量低于50克的飞行器）75k真实世界样本的系统辨识基准。该平台因其多输入多输出特性、开环不稳定性以及敏捷机动下的非线性动力学而成为一个具有挑战性的测试平台。数据集包含四条激进轨迹，具有同步的4维电机输入和13维输出测量。为了公平比较辨识方法，该基准包括一套多步长预测指标，用于评估一步和多步误差传播。除了数据外，我们还提供了平台和实验设置的详细描述，以及基线模型，突出了在真实世界噪声和执行器非线性下准确预测的挑战。所有数据、脚本和参考实现均以开源形式发布在https://github.com/idsia-robotics/nanodrone-sysid-benchmark，以促进算法的透明比较并支持敏捷微型空中机器人研究。

## 🔬 方法详解

论文的核心方法是构建一个系统辨识基准框架，整体框架包括数据采集、基准定义和评估指标。关键技术创新点在于：基于Crazyflie 2.1纳米四旋翼平台，采集了75k真实世界样本，涵盖四条激进轨迹，提供4维电机输入和13维输出测量的同步数据；引入多步长预测指标，如一步和多步误差传播评估，以全面衡量辨识模型的性能。与现有方法的主要区别在于：该基准专注于微型无人机的非线性、不稳定动力学，提供开源数据和脚本，促进透明和可重复的比较，而传统基准可能缺乏真实世界噪声和非线性的考虑。

## 📊 实验亮点

最重要的实验结果包括：基准数据集包含75k真实世界样本，覆盖激进机动下的非线性动力学；基线模型展示了在真实噪声和执行器非线性下预测的显著挑战，如多步误差累积；开源实现促进了算法透明比较，为后续研究提供了可靠基础。

## 🎯 应用场景

该研究在敏捷微型空中机器人领域具有广泛应用，如无人机控制、自主导航和系统优化。潜在应用包括：为研究人员提供标准测试平台，加速非线性系统辨识算法开发；支持微型无人机在复杂环境中的精准建模，提升飞行稳定性和机动性；促进机器人学中真实世界数据驱动的建模研究。

## 📄 摘要（原文）

> We introduce a benchmark for system identification based on 75k real-world samples from the Crazyflie 2.1 Brushless nano-quadrotor, a sub-50g aerial vehicle widely adopted in robotics research. The platform presents a challenging testbed due to its multi-input, multi-output nature, open-loop instability, and nonlinear dynamics under agile maneuvers. The dataset comprises four aggressive trajectories with synchronized 4-dimensional motor inputs and 13-dimensional output measurements. To enable fair comparison of identification methods, the benchmark includes a suite of multi-horizon prediction metrics for evaluating both one-step and multi-step error propagation. In addition to the data, we provide a detailed description of the platform and experimental setup, as well as baseline models highlighting the challenge of accurate prediction under real-world noise and actuation nonlinearities. All data, scripts, and reference implementations are released as open-source at https://github.com/idsia-robotics/nanodrone-sysid-benchmark to facilitate transparent comparison of algorithms and support research on agile, miniaturized aerial robotics.

