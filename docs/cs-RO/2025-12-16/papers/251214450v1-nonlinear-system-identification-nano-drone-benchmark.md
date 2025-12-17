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

**提出基于Crazyflie 2.1纳米四旋翼的75k真实世界样本系统辨识基准，以评估非线性动态下的多步预测性能。**

**关键词**: `系统辨识` `非线性动态` `纳米四旋翼` `多步预测` `真实世界数据` `开源基准` `微型空中机器人` `控制建模`

## 📋 核心要点

1. 核心问题：现有系统辨识方法在真实世界噪声、非线性动态和开环不稳定性下难以准确预测，缺乏标准化基准进行公平比较。
2. 方法要点：基于Crazyflie 2.1纳米四旋翼构建包含75k样本的数据集，提供多步预测指标和开源工具以评估辨识算法。
3. 实验或效果：基准包含激进轨迹数据，基线模型展示了预测挑战，促进算法透明比较和微型空中机器人研究。

## 📝 摘要（中文）

我们引入了一个基于Crazyflie 2.1无刷纳米四旋翼（一种广泛用于机器人研究的重量低于50克的空中飞行器）的75k真实世界样本的系统辨识基准。该平台因其多输入多输出特性、开环不稳定性以及在敏捷机动下的非线性动态而成为一个具有挑战性的测试平台。数据集包含四条激进轨迹，同步记录了4维电机输入和13维输出测量。为了公平比较辨识方法，基准包括一套多时间范围预测指标，用于评估一步和多步误差传播。除了数据外，我们还提供了平台和实验设置的详细描述，以及基线模型，突出了在真实世界噪声和执行器非线性下准确预测的挑战。所有数据、脚本和参考实现均以开源形式发布在https://github.com/idsia-robotics/nanodrone-sysid-benchmark，以促进算法的透明比较并支持敏捷、微型空中机器人研究。

## 🔬 方法详解

论文的核心方法围绕构建一个系统辨识基准，整体框架包括数据采集、指标定义和开源实现。关键技术创新点在于利用Crazyflie 2.1纳米四旋翼的真实世界数据，涵盖多输入多输出、非线性动态和开环不稳定性，并引入多时间范围预测指标（如一步和多步误差传播）来全面评估辨识性能。与现有方法的主要区别在于提供了标准化、大规模的真实世界数据集和评估套件，强调在敏捷机动和噪声环境下的挑战，而非仅依赖仿真或简化模型。

## 📊 实验亮点

最重要的实验结果包括数据集包含75k真实世界样本，覆盖激进轨迹；基准提供多步预测指标，基线模型揭示了在噪声和非线性下的预测误差；开源发布促进了算法透明比较，为微型空中机器人研究提供了实用测试平台。

## 🎯 应用场景

该研究可应用于微型空中机器人（如无人机）的控制系统设计、动态建模优化和自主导航算法开发。潜在价值包括提升在复杂环境下的飞行稳定性、支持敏捷机动研究和促进机器人学习算法的真实世界验证。

## 📄 摘要（原文）

> We introduce a benchmark for system identification based on 75k real-world samples from the Crazyflie 2.1 Brushless nano-quadrotor, a sub-50g aerial vehicle widely adopted in robotics research. The platform presents a challenging testbed due to its multi-input, multi-output nature, open-loop instability, and nonlinear dynamics under agile maneuvers. The dataset comprises four aggressive trajectories with synchronized 4-dimensional motor inputs and 13-dimensional output measurements. To enable fair comparison of identification methods, the benchmark includes a suite of multi-horizon prediction metrics for evaluating both one-step and multi-step error propagation. In addition to the data, we provide a detailed description of the platform and experimental setup, as well as baseline models highlighting the challenge of accurate prediction under real-world noise and actuation nonlinearities. All data, scripts, and reference implementations are released as open-source at https://github.com/idsia-robotics/nanodrone-sysid-benchmark to facilitate transparent comparison of algorithms and support research on agile, miniaturized aerial robotics.

