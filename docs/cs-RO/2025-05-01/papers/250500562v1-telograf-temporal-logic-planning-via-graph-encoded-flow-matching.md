---
layout: default
title: "TeLoGraF: Temporal Logic Planning via Graph-encoded Flow Matching"
---

# TeLoGraF: Temporal Logic Planning via Graph-encoded Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00562" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00562v1</a>
  <a href="https://arxiv.org/pdf/2505.00562.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00562v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00562v1', 'TeLoGraF: Temporal Logic Planning via Graph-encoded Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Meng, Chuchu Fan

**分类**: cs.RO, cs.AI, cs.FL, cs.LG

**发布日期**: 2025-05-01

**备注**: Accepted to ICML2025

**🔗 代码/项目**: [GITHUB](https://github.com/mengyuest/TeLoGraF)

---

## 💡 一句话要点

**提出TeLoGraF以解决复杂任务的时序逻辑规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `时序逻辑规划` `图神经网络` `流匹配` `机器人控制` `自动驾驶` `智能制造` `复杂任务解决`

## 📋 核心要点

1. 现有方法主要局限于固定或参数化的STL规范，缺乏多样化的数据集和有效的编码器，限制了其应用范围。
2. TeLoGraF利用图神经网络编码器和流匹配技术，能够学习和解决一般的STL规范，提升了时序逻辑规划的灵活性。
3. 实验结果显示，TeLoGraF在五个不同的模拟环境中表现优异，STL满足率高于其他基线，推理速度提升显著。

## 📝 摘要（中文）

学习解决具有信号时序逻辑（STL）规范的复杂任务对许多现实应用至关重要。然而，大多数现有工作仅考虑固定或参数化的STL规范，缺乏多样化的STL数据集和有效提取时序逻辑信息的编码器。本文提出了TeLoGraF，即时序逻辑图编码流，通过图神经网络（GNN）编码器和流匹配来学习一般STL规范的解决方案。我们识别了四种常用的STL模板，并收集了总计20万条规范及其配对演示。在五个模拟环境中进行的广泛实验表明，我们的方法在STL满足率上优于其他基线，与经典STL规划算法相比，我们的方法在推理速度上快10-100倍，并且可以在任何系统动态下工作。此外，我们展示了图编码方法在解决复杂STL和对分布外STL规范的鲁棒性方面的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决复杂任务的时序逻辑规划问题，现有方法在处理多样化STL规范时存在局限性，无法有效提取时序逻辑信息。

**核心思路**：TeLoGraF通过图神经网络（GNN）编码器和流匹配技术，能够学习和处理一般的STL规范，从而提高规划的灵活性和效率。

**技术框架**：整体架构包括数据收集、GNN编码器设计、流匹配算法和推理模块。数据收集阶段涵盖了200K条STL规范及其配对演示，GNN编码器负责提取时序逻辑信息，流匹配算法用于生成解决方案。

**关键创新**：TeLoGraF的主要创新在于结合了图神经网络和流匹配技术，使其能够处理复杂的STL规范，并在推理速度上显著优于传统方法。

**关键设计**：在设计中，GNN编码器的结构经过优化，以提高对时序逻辑信息的提取能力，损失函数则针对STL满足率进行了调整，以确保模型的有效性和鲁棒性。

## 📊 实验亮点

实验结果表明，TeLoGraF在STL满足率上显著优于其他基线方法，推理速度提升10-100倍，能够在多种系统动态下高效工作，展示了其在复杂STL处理中的优势和鲁棒性。

## 🎯 应用场景

TeLoGraF的研究成果在机器人控制、自动驾驶、智能制造等领域具有广泛的应用潜力。通过有效处理复杂的时序逻辑规范，该方法能够提升系统的自主决策能力，适应多变的环境和任务需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Learning to solve complex tasks with signal temporal logic (STL) specifications is crucial to many real-world applications. However, most previous works only consider fixed or parametrized STL specifications due to the lack of a diverse STL dataset and encoders to effectively extract temporal logic information for downstream tasks. In this paper, we propose TeLoGraF, Temporal Logic Graph-encoded Flow, which utilizes Graph Neural Networks (GNN) encoder and flow-matching to learn solutions for general STL specifications. We identify four commonly used STL templates and collect a total of 200K specifications with paired demonstrations. We conduct extensive experiments in five simulation environments ranging from simple dynamical models in the 2D space to high-dimensional 7DoF Franka Panda robot arm and Ant quadruped navigation. Results show that our method outperforms other baselines in the STL satisfaction rate. Compared to classical STL planning algorithms, our approach is 10-100X faster in inference and can work on any system dynamics. Besides, we show our graph-encoding method's capability to solve complex STLs and robustness to out-distribution STL specifications. Code is available at https://github.com/mengyuest/TeLoGraF

