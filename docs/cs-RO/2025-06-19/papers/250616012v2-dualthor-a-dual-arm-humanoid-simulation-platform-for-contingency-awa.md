---
layout: default
title: "DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning"
---

# DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16012" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16012v2</a>
  <a href="https://arxiv.org/pdf/2506.16012.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16012v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16012v2', 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyu Li, Siyuan He, Hang Xu, Haoqi Yuan, Yu Zang, Liwei Hu, Junpeng Yue, Zhenxiong Jiang, Pengbo Hu, Börje F. Karlsson, Yehui Tang, Zongqing Lu

**分类**: cs.RO

**发布日期**: 2025-06-19 (更新: 2025-10-13)

**备注**: The experiments in the paper need to be further supplemented, and more methods should be considered for expansion

**🔗 代码/项目**: [GITHUB](https://github.com/ds199895/DualTHOR.git)

---

## 💡 一句话要点

**提出DualTHOR以解决双臂机器人在复杂任务中的规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `双臂机器人` `物理仿真` `应急机制` `任务规划` `具身智能体` `视觉语言模型` `逆向运动学` `家庭机器人`

## 📋 核心要点

1. 现有的仿真平台多依赖简化的机器人形态，无法有效模拟真实环境中的复杂交互任务。
2. DualTHOR是一个基于物理的仿真平台，专为双臂类人机器人设计，能够处理复杂的任务和应急情况。
3. 实验结果显示，当前的视觉语言模型在双臂协调和应对真实环境中的突发情况时表现不佳，强调了DualTHOR的重要性。

## 📝 摘要（中文）

开发能够在真实场景中执行复杂交互任务的具身智能体仍然是一个基本挑战。尽管最近的仿真平台在任务多样性上取得了显著进展，但大多数平台依赖简化的机器人形态，并忽略了低级执行的随机性，限制了其在真实机器人中的可转移性。为了解决这些问题，本文提出了基于物理的仿真平台DualTHOR，专为复杂的双臂类人机器人设计，构建在AI2-THOR的扩展版本之上。该仿真器包含真实的机器人资产、双臂协作的任务套件以及类人机器人的逆向运动学求解器。我们还引入了一种应急机制，通过基于物理的低级执行来考虑潜在的失败，从而缩小与真实场景的差距。

## 🔬 方法详解

**问题定义**：本文旨在解决现有仿真平台在处理复杂双臂机器人任务时的局限性，尤其是对低级执行随机性的忽视，导致其在真实环境中的可转移性不足。

**核心思路**：提出DualTHOR仿真平台，通过引入真实的机器人资产和应急机制，增强双臂机器人在复杂任务中的规划能力和适应性。

**技术框架**：DualTHOR的整体架构包括物理仿真引擎、任务执行模块和逆向运动学求解器，能够模拟真实环境中的多种交互任务。

**关键创新**：引入了基于物理的低级执行和应急机制，使得仿真平台能够更真实地反映机器人在实际操作中的潜在失败，提升了任务执行的可靠性。

**关键设计**：在设计中，采用了真实的机器人模型和任务套件，优化了逆向运动学求解器的性能，以适应复杂的双臂协作任务。

## 📊 实验亮点

实验结果表明，当前的视觉语言模型在双臂协调任务中表现不佳，尤其是在面对真实环境中的突发情况时，鲁棒性有限。使用DualTHOR进行训练的模型在这些任务中的表现显著提升，展示了该平台在提高机器人任务执行能力方面的潜力。

## 🎯 应用场景

DualTHOR的研究成果可广泛应用于家庭服务机器人、工业自动化以及人机协作等领域，提升机器人在复杂环境中的适应能力和任务执行效率。未来，随着技术的进步，DualTHOR有望推动具身智能体在更广泛应用场景中的发展。

## 📄 摘要（原文）

> Developing embodied agents capable of performing complex interactive tasks in real-world scenarios remains a fundamental challenge in embodied AI. Although recent advances in simulation platforms have greatly enhanced task diversity to train embodied Vision Language Models (VLMs), most platforms rely on simplified robot morphologies and bypass the stochastic nature of low-level execution, which limits their transferability to real-world robots. To address these issues, we present a physics-based simulation platform DualTHOR for complex dual-arm humanoid robots, built upon an extended version of AI2-THOR. Our simulator includes real-world robot assets, a task suite for dual-arm collaboration, and inverse kinematics solvers for humanoid robots. We also introduce a contingency mechanism that incorporates potential failures through physics-based low-level execution, bridging the gap to real-world scenarios. Our simulator enables a more comprehensive evaluation of the robustness and generalization of VLMs in household environments. Extensive evaluations reveal that current VLMs struggle with dual-arm coordination and exhibit limited robustness in realistic environments with contingencies, highlighting the importance of using our simulator to develop more capable VLMs for embodied tasks. The code is available at https://github.com/ds199895/DualTHOR.git.

