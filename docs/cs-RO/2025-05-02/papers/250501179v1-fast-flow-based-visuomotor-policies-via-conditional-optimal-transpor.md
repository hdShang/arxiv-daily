---
layout: default
title: Fast Flow-based Visuomotor Policies via Conditional Optimal Transport Couplings
---

# Fast Flow-based Visuomotor Policies via Conditional Optimal Transport Couplings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01179" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01179v1</a>
  <a href="https://arxiv.org/pdf/2505.01179.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01179v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01179v1', 'Fast Flow-based Visuomotor Policies via Conditional Optimal Transport Couplings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andreas Sochopoulos, Nikolay Malkin, Nikolaos Tsagkas, João Moura, Michael Gienger, Sethu Vijayakumar

**分类**: cs.RO

**发布日期**: 2025-05-02

---

## 💡 一句话要点

**提出条件最优传输耦合以加速流基视觉运动策略**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `条件最优传输` `流基策略` `机器人控制` `动作生成` `实时控制`

## 📋 核心要点

1. 现有的扩散和流匹配策略在实时控制中面临计算开销大的挑战，限制了其应用。
2. 本文提出通过条件最优传输耦合来改善流ODE中的动作生成，特别是引入条件变量以增强少步性能。
3. 实验结果显示，所提策略在多种任务中成功率提高4%，且速度提升10倍，保持与现有方法相同的训练复杂度。

## 📝 摘要（中文）

扩散和流匹配策略在机器人应用中表现出色，但由于数值积分的计算开销，限制了其作为实时控制器的适用性。本文提出了一种利用条件最优传输耦合噪声与样本的方法，以在流ODE中强制执行直线解，从而提高机器人动作生成任务的性能。通过将条件变量纳入耦合过程，改进了少步性能。实验表明，所提策略在多样化的仿真任务中成功率提高4%，且速度提升10倍，同时在真实机器人任务中生成高质量和多样化的动作轨迹。

## 🔬 方法详解

**问题定义**：本文旨在解决现有扩散和流匹配策略在实时控制中的计算开销问题，尤其是数值积分导致的低效性。

**核心思路**：提出利用条件最优传输耦合噪声与样本，通过引入条件变量来改善流ODE中的动作生成，确保生成的动作轨迹更为高效和准确。

**技术框架**：整体方法包括噪声与样本的耦合过程，流ODE的求解，以及条件变量的整合，形成一个高效的动作生成框架。

**关键创新**：最重要的创新在于将条件变量纳入耦合过程，显著提升了少步性能，与传统方法相比，能够在更短的时间内生成高质量的动作轨迹。

**关键设计**：在参数设置上，保持与扩散策略相同的训练复杂度，损失函数设计为优化生成轨迹的多样性和质量，网络结构则采用流匹配的基本架构，确保高效的计算性能。

## 📊 实验亮点

实验结果显示，所提的少步策略在多样化的仿真任务中成功率提高4%，速度提升10倍，相较于扩散策略表现出显著的优势，同时在真实机器人任务中也能生成高质量的动作轨迹。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、智能制造和人机交互等场景。通过提高机器人动作生成的效率和质量，能够在实时控制和复杂任务中发挥重要作用，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Diffusion and flow matching policies have recently demonstrated remarkable performance in robotic applications by accurately capturing multimodal robot trajectory distributions. However, their computationally expensive inference, due to the numerical integration of an ODE or SDE, limits their applicability as real-time controllers for robots. We introduce a methodology that utilizes conditional Optimal Transport couplings between noise and samples to enforce straight solutions in the flow ODE for robot action generation tasks. We show that naively coupling noise and samples fails in conditional tasks and propose incorporating condition variables into the coupling process to improve few-step performance. The proposed few-step policy achieves a 4% higher success rate with a 10x speed-up compared to Diffusion Policy on a diverse set of simulation tasks. Moreover, it produces high-quality and diverse action trajectories within 1-2 steps on a set of real-world robot tasks. Our method also retains the same training complexity as Diffusion Policy and vanilla Flow Matching, in contrast to distillation-based approaches.

