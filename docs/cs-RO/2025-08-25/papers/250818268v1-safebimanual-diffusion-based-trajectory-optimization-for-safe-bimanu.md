---
layout: default
title: "SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation"
---

# SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18268" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18268v1</a>
  <a href="https://arxiv.org/pdf/2508.18268.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18268v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18268v1', 'SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyuan Deng, Wenkai Guo, Qianzhun Wang, Zhenyu Wu, Ziwei Wang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-25

**备注**: Project website is at: https://denghaoyuan123.github.io/SafeBimanip/

---

## 💡 一句话要点

**提出SafeBimanual以解决双手操作中的安全问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `双手操作` `轨迹优化` `安全约束` `扩散模型` `视觉-语言模型` `机器人技术` `人工智能`

## 📋 核心要点

1. 现有的基于扩散的双手操作方法未考虑物理安全约束，导致机器人和物体的潜在损害。
2. 本文提出SafeBimanual框架，通过施加安全约束优化双手操作轨迹，避免危险行为。
3. 在RoboTwin的模拟任务中，SafeBimanual成功率提高了13.7%，不安全交互减少了18.8%，在真实任务中成功率提升32.5%。

## 📝 摘要（中文）

双手操作在家庭服务和制造业中得到了广泛应用，能够完成复杂的协调任务。尽管近期基于扩散的策略学习方法在双手操作中取得了良好表现，但忽视了物理安全约束，导致机器人和物体的潜在损害。为此，本文提出了一种名为SafeBimanual的测试时轨迹优化框架，针对任何预训练的扩散基础双手操作策略，施加安全约束以避免危险行为并提高成功率。我们设计了多样的成本函数以适应不同的双臂协作模式，并通过视觉-语言模型动态生成最优安全约束。SafeBimanual在RoboTwin的8个模拟任务中成功率提高了13.7%，不安全交互减少了18.8%。在4个真实任务中的实验进一步验证了其实际价值，成功率提升了32.5%。

## 🔬 方法详解

**问题定义**：现有的基于扩散的双手操作策略未能考虑物理安全约束，导致机器人在执行任务时可能出现危险行为，损害机器人和物体的安全。

**核心思路**：SafeBimanual框架通过在测试时对预训练的双手操作策略施加安全约束，优化操作轨迹，从而避免危险行为并提高任务成功率。

**技术框架**：该框架包括多个模块：首先，设计多样的成本函数以适应不同的双臂协作模式；其次，利用扩散去噪过程进行轨迹优化；最后，结合视觉-语言模型动态生成最优安全约束。

**关键创新**：SafeBimanual的创新在于引入了动态生成的安全约束，能够针对不同的操作场景和任务需求进行调整，显著提升了双手操作的安全性和成功率。

**关键设计**：在设计中，采用了多样的成本函数来处理物体撕裂和手臂与物体之间的碰撞等问题，同时通过视觉-语言模型指定关键点及其关系，以指导成本函数的调度。

## 📊 实验亮点

SafeBimanual在RoboTwin的8个模拟任务中成功率提高了13.7%，不安全交互减少了18.8%。在4个真实任务中的实验结果显示，成功率提升了32.5%，验证了其在实际应用中的有效性和优势。

## 🎯 应用场景

SafeBimanual框架具有广泛的应用潜力，特别是在需要高安全性和高效率的双手操作场景中，如工业自动化、家庭服务机器人和医疗辅助设备等。通过提高操作的安全性，该研究将推动机器人技术在实际应用中的普及和发展。

## 📄 摘要（原文）

> Bimanual manipulation has been widely applied in household services and manufacturing, which enables the complex task completion with coordination requirements. Recent diffusion-based policy learning approaches have achieved promising performance in modeling action distributions for bimanual manipulation. However, they ignored the physical safety constraints of bimanual manipulation, which leads to the dangerous behaviors with damage to robots and objects. To this end, we propose a test-time trajectory optimization framework named SafeBimanual for any pre-trained diffusion-based bimanual manipulation policies, which imposes the safety constraints on bimanual actions to avoid dangerous robot behaviors with improved success rate. Specifically, we design diverse cost functions for safety constraints in different dual-arm cooperation patterns including avoidance of tearing objects and collision between arms and objects, which optimizes the manipulator trajectories with guided sampling of diffusion denoising process. Moreover, we employ a vision-language model (VLM) to schedule the cost functions by specifying keypoints and corresponding pairwise relationship, so that the optimal safety constraint is dynamically generated in the entire bimanual manipulation process. SafeBimanual demonstrates superiority on 8 simulated tasks in RoboTwin with a 13.7% increase in success rate and a 18.8% reduction in unsafe interactions over state-of-the-art diffusion-based methods. Extensive experiments on 4 real-world tasks further verify its practical value by improving the success rate by 32.5%.

