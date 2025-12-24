---
layout: default
title: "AgenticControl: An Automated Control Design Framework Using Large Language Models"
---

# AgenticControl: An Automated Control Design Framework Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19160" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19160v1</a>
  <a href="https://arxiv.org/pdf/2506.19160.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19160v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19160v1', 'AgenticControl: An Automated Control Design Framework Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Narimani, Seyyed Ali Emami

**分类**: eess.SY

**发布日期**: 2025-06-23

---

## 💡 一句话要点

**提出AgenticControl以解决复杂控制系统设计问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `控制系统设计` `大型语言模型` `多智能体协作` `鲁棒优化` `自动化控制` `实时适应性` `PID控制器` `强化学习`

## 📋 核心要点

1. 现有控制系统设计方法依赖专家知识，难以应对复杂和不确定的动态环境。
2. AgenticControl框架利用多智能体协作和大型语言模型自动化控制器设计，提升设计效率和适应性。
3. 在多个控制系统中验证了该框架的有效性，PID控制器的跟踪误差减少了55%，显示出显著的性能提升。

## 📝 摘要（中文）

传统控制系统设计依赖于专家知识和精确模型，面对复杂、非线性或不确定的动态时常显得力不从心。本文提出了AgenticControl，一个新颖的多智能体框架，通过协调的大型语言模型（LLM）代理自动化控制器设计。该框架通过结构化的JSON通信，处理控制器选择、场景设计、参数优化、性能评估和决策等任务。采用演员-评论家优化方法，系统在逐步增加复杂性的场景中迭代改进性能，以确保在名义条件、测量噪声、执行器干扰和参数不确定性下的鲁棒性。通过在四个不同控制系统（直流电机位置控制、球与梁、倒立摆和双倒立摆）上的验证，该框架在性能上与经典方法相当，且在PID控制器设计上显著优于MATLAB的PIDTuner，跟踪误差减少了55%。

## 🔬 方法详解

**问题定义**：本文旨在解决传统控制系统设计中对专家知识和精确模型的依赖，尤其是在面对复杂、非线性和不确定动态时的局限性。

**核心思路**：AgenticControl框架通过协调多个大型语言模型（LLM）代理，自动化控制器设计过程，利用结构化的JSON通信实现任务分配和协作。

**技术框架**：该框架包含多个模块，包括控制器选择、场景设计、参数优化、性能评估和决策制定。通过演员-评论家优化方法，系统在逐步增加复杂性的场景中迭代改进性能。

**关键创新**：最重要的创新在于多智能体的协作机制和鲁棒优化方法，使得系统能够在不确定性条件下保持高性能，并具备实时适应能力。

**关键设计**：框架中采用了结构化的JSON通信格式，关键参数设置和损失函数设计确保了优化过程的高效性，网络结构则支持实时学习和适应。

## 📊 实验亮点

在实验中，AgenticControl框架在多个控制系统上表现出色，特别是在PID控制器设计上，跟踪误差减少了55%，显著优于MATLAB的PIDTuner。此外，DeepSeek模型在优化过程中实现了最快的收敛速度，展示了LLM驱动控制设计的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自动化控制、机器人技术和智能制造等。通过引入大型语言模型，AgenticControl框架能够显著提升控制系统的设计效率和适应性，推动更复杂控制策略的实现，如模型预测控制和强化学习，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Traditional control system design, reliant on expert knowledge and precise models, struggles with complex, nonlinear, or uncertain dynamics. This paper introduces AgenticControl, a novel multi-agent framework that automates controller design using coordinated Large Language Model (LLM) agents. Through structured JSON communication, these agents handle tasks including controller selection, scenario design, parameter optimization, performance evaluation, and decision-making. Through an actor-critic optimization approach, the system iteratively improves performance while progressing through scenarios of increasing complexity to ensure robustness under nominal conditions, measurement noise, actuator disturbances, and parametric uncertainties. Key innovations include structured multi-agent collaboration, robust optimization mechanisms, and real-time adaptability via in-context learning. Validated across four diverse control systems, namely, DC Motor Position control, Ball and Beam, Inverted Pendulum, and Double Inverted Pendulum, the framework achieves competitive performance against classical methods. Its Full State Feedback solution closely matches Linear Quadratic Regulator (LQR) results, while the designed PID controller significantly outperforming MATLAB's PIDTuner, reducing PID tracking error by 55% through adaptive parameter exploration. A comparative study of five LLM models reveals distinct optimization profiles, with DeepSeek achieving the fastest convergence. This work demonstrates the potential of LLM-driven control design, paving the way for advanced techniques like model predictive control and reinforcement learning.

