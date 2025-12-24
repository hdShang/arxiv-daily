---
layout: default
title: "D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning"
---

# D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06804" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06804v1</a>
  <a href="https://arxiv.org/pdf/2508.06804.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06804v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06804v1', 'D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shu-Ang Yu, Feng Gao, Yi Wu, Chao Yu, Yu Wang

**分类**: cs.RO

**发布日期**: 2025-08-09

---

## 💡 一句话要点

**提出动态去噪扩散策略以解决实时部署瓶颈问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散策略` `去噪` `强化学习` `机器人控制` `实时推理` `动态分配` `视觉运动任务`

## 📋 核心要点

1. 现有的扩散策略在实时部署中面临去噪过程的效率瓶颈，固定去噪步骤无法适应不同动作的重要性。
2. D3P通过自适应分配去噪步骤，利用状态感知适配器优化每个动作的去噪过程，提升推理效率。
3. 在模拟任务中，D3P实现了2.2倍的推理速度提升，并在物理机器人上也取得了1.9倍的加速效果。

## 📝 摘要（中文）

扩散策略在学习复杂的机器人视觉运动任务中的动作分布方面表现出色，但其迭代去噪过程成为实时部署的主要瓶颈。现有加速方法对每个动作应用固定数量的去噪步骤，隐含地将所有动作视为同等重要。然而，实验表明，机器人任务通常包含关键和常规动作，这些动作对任务成功的影响不同。基于此，我们提出了动态去噪扩散策略（D3P），该策略在测试时自适应地为每个动作分配去噪步骤。D3P使用轻量级的状态感知适配器来为每个动作分配最佳的去噪步骤数量，并通过强化学习联合优化适配器和基础扩散策略，以平衡任务性能和推理效率。在模拟任务中，D3P实现了比基线快2.2倍的推理速度，同时未降低成功率。此外，我们还在物理机器人上验证了D3P的有效性，达到了1.9倍的加速效果。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有扩散策略在实时部署中因固定去噪步骤导致的效率瓶颈问题。现有方法未能考虑不同动作在任务成功中的重要性差异，导致资源浪费。

**核心思路**：D3P的核心思想是根据任务状态自适应地为每个动作分配去噪步骤，确保关键动作获得更多资源，而常规动作则减少去噪步骤，从而提高整体推理效率。

**技术框架**：D3P的整体架构包括一个状态感知适配器和基础扩散策略。适配器根据当前状态动态调整去噪步骤，基础扩散策略则负责生成动作分布。两者通过强化学习进行联合优化，以实现性能与效率的平衡。

**关键创新**：D3P的主要创新在于其动态去噪步骤分配机制，区别于传统方法的固定步骤分配，能够根据任务需求灵活调整，显著提高了推理速度和任务成功率。

**关键设计**：在设计中，适配器的参数设置经过精心调整，以确保其能够准确感知状态变化并做出合理的去噪步骤分配。此外，损失函数的设计也考虑了任务性能与推理效率之间的权衡。适配器和扩散策略的网络结构均经过优化，以实现高效的联合训练。

## 📊 实验亮点

D3P在模拟任务中实现了2.2倍的推理速度提升，且未降低成功率。在物理机器人实验中，D3P也达到了1.9倍的加速效果，显示出其在实际应用中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动化生产线以及智能家居等场景。通过提高机器人在复杂任务中的实时反应能力，D3P能够显著提升机器人在动态环境中的适应性和效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Diffusion policies excel at learning complex action distributions for robotic visuomotor tasks, yet their iterative denoising process poses a major bottleneck for real-time deployment. Existing acceleration methods apply a fixed number of denoising steps per action, implicitly treating all actions as equally important. However, our experiments reveal that robotic tasks often contain a mix of \emph{crucial} and \emph{routine} actions, which differ in their impact on task success. Motivated by this finding, we propose \textbf{D}ynamic \textbf{D}enoising \textbf{D}iffusion \textbf{P}olicy \textbf{(D3P)}, a diffusion-based policy that adaptively allocates denoising steps across actions at test time. D3P uses a lightweight, state-aware adaptor to allocate the optimal number of denoising steps for each action. We jointly optimize the adaptor and base diffusion policy via reinforcement learning to balance task performance and inference efficiency. On simulated tasks, D3P achieves an averaged 2.2$\times$ inference speed-up over baselines without degrading success. Furthermore, we demonstrate D3P's effectiveness on a physical robot, achieving a 1.9$\times$ acceleration over the baseline.

