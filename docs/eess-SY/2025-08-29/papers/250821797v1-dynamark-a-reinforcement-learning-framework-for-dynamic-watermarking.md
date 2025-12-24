---
layout: default
title: "DynaMark: A Reinforcement Learning Framework for Dynamic Watermarking in Industrial Machine Tool Controllers"
---

# DynaMark: A Reinforcement Learning Framework for Dynamic Watermarking in Industrial Machine Tool Controllers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21797" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21797v1</a>
  <a href="https://arxiv.org/pdf/2508.21797.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21797v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21797v1', 'DynaMark: A Reinforcement Learning Framework for Dynamic Watermarking in Industrial Machine Tool Controllers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Navid Aftabi, Abhishek Hanchate, Satish Bukkapatnam, Dan Li

**分类**: eess.SY, cs.AI, cs.CR, cs.LG, stat.AP

**发布日期**: 2025-08-29

---

## 💡 一句话要点

**提出DynaMark框架以解决工业机床控制器的动态水印问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动态水印` `强化学习` `工业控制` `安全性` `马尔可夫决策过程` `贝叶斯更新` `能耗优化`

## 📋 核心要点

1. 现有动态水印方案假设线性高斯动态，无法适应工业机床控制器的时变特性，导致安全性不足。
2. DynaMark框架通过强化学习将动态水印建模为马尔可夫决策过程，在线学习并自适应调整水印参数。
3. 在实验中，DynaMark在保持轨迹的同时，水印能耗降低70%，且检测延迟与采样间隔相当。

## 📝 摘要（中文）

随着工业4.0的推进，网络化的机床控制器（MTCs）成为重放攻击的主要目标，这些攻击利用过时的传感器数据操控执行器。动态水印技术能够揭示此类篡改，但现有方案假设线性高斯动态并使用恒定水印统计，因而对MTCs的时变和部分专有行为存在脆弱性。为此，本文提出DynaMark，一个将动态水印建模为马尔可夫决策过程（MDP）的强化学习框架。DynaMark在线学习自适应策略，动态调整零均值高斯水印的协方差，最大化控制性能、能耗和检测信心的独特奖励函数。通过在西门子Sinumerik 828D控制器数字双胞胎上的实验，DynaMark实现了水印能耗降低70%，并保持了名义轨迹。

## 🔬 方法详解

**问题定义**：本文旨在解决工业机床控制器中动态水印技术的不足，现有方法对时变和部分专有行为的适应性差，导致安全性脆弱。

**核心思路**：DynaMark框架通过强化学习将动态水印建模为马尔可夫决策过程，能够在线学习并动态调整水印的协方差，提升检测信心和控制性能。

**技术框架**：DynaMark的整体架构包括数据采集模块、强化学习模块和水印生成模块。数据采集模块负责获取传感器数据，强化学习模块通过反馈优化水印策略，水印生成模块则根据学习结果生成动态水印。

**关键创新**：DynaMark的主要创新在于其自适应水印策略的在线学习能力，能够根据实时数据和反馈动态调整水印参数，区别于传统的恒定水印方案。

**关键设计**：DynaMark采用独特的奖励函数，平衡控制性能、能耗和检测信心。还开发了贝叶斯信念更新机制，以实现线性系统中的实时检测信心。

## 📊 实验亮点

实验结果表明，DynaMark在西门子Sinumerik 828D控制器数字双胞胎上实现了水印能耗降低70%，同时保持了名义轨迹，检测延迟与采样间隔相当。此外，物理步进电机测试台验证了该方法的快速报警能力和较小的控制性能下降，超越了现有基准。

## 🎯 应用场景

DynaMark框架在工业自动化领域具有广泛的应用潜力，尤其是在需要高安全性和实时监控的机床控制系统中。其动态水印技术能够有效防范重放攻击，提升系统的安全性和可靠性，未来可扩展至其他工业控制系统和智能制造领域。

## 📄 摘要（原文）

> Industry 4.0's highly networked Machine Tool Controllers (MTCs) are prime targets for replay attacks that use outdated sensor data to manipulate actuators. Dynamic watermarking can reveal such tampering, but current schemes assume linear-Gaussian dynamics and use constant watermark statistics, making them vulnerable to the time-varying, partly proprietary behavior of MTCs. We close this gap with DynaMark, a reinforcement learning framework that models dynamic watermarking as a Markov decision process (MDP). It learns an adaptive policy online that dynamically adapts the covariance of a zero-mean Gaussian watermark using available measurements and detector feedback, without needing system knowledge. DynaMark maximizes a unique reward function balancing control performance, energy consumption, and detection confidence dynamically. We develop a Bayesian belief updating mechanism for real-time detection confidence in linear systems. This approach, independent of specific system assumptions, underpins the MDP for systems with linear dynamics. On a Siemens Sinumerik 828D controller digital twin, DynaMark achieves a reduction in watermark energy by 70% while preserving the nominal trajectory, compared to constant variance baselines. It also maintains an average detection delay equivalent to one sampling interval. A physical stepper-motor testbed validates these findings, rapidly triggering alarms with less control performance decline and exceeding existing benchmarks.

