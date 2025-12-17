---
layout: default
title: NMPC-based Motion Planning with Adaptive Weighting for Dynamic Object Interception
---

# NMPC-based Motion Planning with Adaptive Weighting for Dynamic Object Interception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15532" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15532v1</a>
  <a href="https://arxiv.org/pdf/2511.15532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15532v1" onclick="toggleFavorite(this, '2511.15532v1', 'NMPC-based Motion Planning with Adaptive Weighting for Dynamic Object Interception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Cai, Saksham Kohli, Steven Liu

**分类**: cs.RO, eess.SY

**发布日期**: 2025-11-19

**备注**: This work has been submitted to the IFAC World Congress for possible publication. Under review

---

## 💡 一句话要点

**提出基于自适应权重NMPC的运动规划方法，用于双臂协作机器人动态目标拦截**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `非线性模型预测控制` `双臂协作机器人` `动态目标拦截` `运动规划` `自适应权重`

## 📋 核心要点

1. 双臂协作机器人拦截快速移动物体，面临闭链约束下的协调难题，现有方法难以兼顾运动质量和控制力。
2. 提出自适应终端（AT）MPC公式，通过优化成本函数，在满足约束的同时，降低控制力，提升运动质量。
3. 实验表明，AT公式显著降低了执行器功率限制违规，平均规划周期仅19ms，优于系统采样时间，验证了实时性和鲁棒性。

## 📝 摘要（中文）

本文提出了一种基于非线性模型预测控制（NMPC）的运动规划器，用于双臂协作机器人系统的动态目标拦截任务。该系统通过协同操作机械臂末端的夹具来捕捉快速移动的物体，面临着显著的协调挑战和固有的闭链约束。该规划器将高层拦截规划与实时关节空间控制相结合。论文引入了一种自适应终端（AT）MPC公式，通过成本函数调整来优化性能，与依赖终端惩罚以实现快速收敛的原始终端（PT）方法形成对比。实验结果表明，AT公式能有效缓解PT策略中常见的执行器功率限制违规问题，从而产生更平滑的轨迹并显著降低控制力。在双臂协作机器人平台上进行的实验验证了该方法的实时性能，平均规划周期计算时间约为19毫秒，小于40毫秒的系统采样时间。结果表明，与PT基线相比，AT公式以最小的计算开销实现了显著改善的运动质量和鲁棒性，使其非常适合动态协作拦截任务。

## 🔬 方法详解

**问题定义**：本论文旨在解决双臂协作机器人动态拦截快速移动物体时，由于闭链约束和高动态性带来的运动规划难题。现有方法，如原始终端（PT）MPC，过度依赖终端惩罚以实现快速收敛，容易导致执行器功率限制违规，产生剧烈的控制动作，影响运动质量和系统稳定性。

**核心思路**：论文的核心思路是通过引入自适应终端（AT）MPC公式，对成本函数进行精细调整，从而在满足终端约束的同时，优化中间状态的控制力，避免执行器饱和。这种方法旨在平衡快速收敛和控制力优化，实现更平滑、更高效的运动轨迹。

**技术框架**：整体框架包含高层拦截规划和底层关节空间控制两个主要部分。高层规划确定拦截点和时间，底层NMPC规划器生成满足约束的关节空间轨迹。AT-MPC作为底层规划器的核心，负责实时优化轨迹，并根据系统状态自适应调整成本函数权重。

**关键创新**：最重要的技术创新在于AT-MPC公式中的自适应权重设计。与PT-MPC过度依赖终端惩罚不同，AT-MPC通过动态调整状态和控制输入的权重，在满足终端约束的同时，最小化控制力，从而避免执行器饱和，提高运动质量。

**关键设计**：AT-MPC的关键设计包括：1) 成本函数的设计，包含状态误差、控制输入和终端状态误差三部分；2) 自适应权重策略，根据系统状态动态调整状态和控制输入的权重，例如，当预测到执行器即将饱和时，增加控制输入的权重；3) 终端约束的设置，确保机器人能够在指定时间和位置完成拦截任务。

## 📊 实验亮点

实验结果表明，所提出的AT-MPC方法能够有效降低执行器功率限制违规，产生更平滑的运动轨迹。与PT基线相比，AT方法在运动质量和鲁棒性方面均有显著提升，且平均规划周期仅为19毫秒，远小于40毫秒的系统采样时间，验证了其在实时性方面的优势。这些结果表明，AT公式以最小的计算开销实现了显著改善的运动质量和鲁棒性。

## 🎯 应用场景

该研究成果可应用于高速分拣、空中目标拦截、柔性物体操作等领域。在工业自动化中，可用于高速拾取和放置任务，提高生产效率。在国防领域，可用于拦截无人机等空中目标。此外，该方法还可扩展到其他多机器人协作系统，具有广泛的应用前景。

## 📄 摘要（原文）

> Catching fast-moving objects serves as a benchmark for robotic agility, posing significant coordination challenges for cooperative manipulator systems holding a catcher, particularly due to inherent closed-chain constraints. This paper presents a nonlinear model predictive control (MPC)-based motion planner that bridges high-level interception planning with real-time joint space control, enabling dynamic object interception for systems comprising two cooperating arms. We introduce an Adaptive- Terminal (AT) MPC formulation featuring cost shaping, which contrasts with a simpler Primitive-Terminal (PT) approach relying heavily on terminal penalties for rapid convergence. The proposed AT formulation is shown to effectively mitigate issues related to actuator power limit violations frequently encountered with the PT strategy, yielding trajectories and significantly reduced control effort. Experimental results on a robotic platform with two cooperative arms, demonstrating excellent real time performance, with an average planner cycle computation time of approximately 19 ms-less than half the 40 ms system sampling time. These results indicate that the AT formulation achieves significantly improved motion quality and robustness with minimal computational overhead compared to the PT baseline, making it well-suited for dynamic, cooperative interception tasks.

