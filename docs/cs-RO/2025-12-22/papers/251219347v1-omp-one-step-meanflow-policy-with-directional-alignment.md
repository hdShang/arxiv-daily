---
layout: default
title: "OMP: One-step Meanflow Policy with Directional Alignment"
---

# OMP: One-step Meanflow Policy with Directional Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19347" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19347v1</a>
  <a href="https://arxiv.org/pdf/2512.19347.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19347v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19347v1', 'OMP: One-step Meanflow Policy with Directional Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Han Fang, Yize Huang, Yuheng Zhao, Paul Weng, Xiao Li, Yutong Ban

**分类**: cs.RO

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出OMP：一种单步MeanFlow策略，通过方向对齐提升机器人操作性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `MeanFlow` `少样本学习` `方向对齐` `微分推导方程` `雅可比向量积` `生成策略`

## 📋 核心要点

1. 主流机器人操作策略，如扩散模型和Flow模型，分别存在推理延迟高和架构复杂的问题，限制了其应用。
2. OMP通过引入余弦损失对齐速度方向，并利用微分推导方程优化雅可比向量积，从而提升策略的泛化能力和轨迹精度。
3. 实验结果表明，OMP在Adroit和Meta-World任务上优于现有方法，尤其在Meta-World任务中表现出更强的少样本泛化能力。

## 📝 摘要（中文）

机器人操作是具身智能的关键能力。本文针对现有数据驱动的生成策略框架，如扩散模型推理延迟高、Flow模型架构复杂等问题，提出了一种改进的基于MeanFlow的策略OMP。该方法通过引入轻量级的余弦损失来对齐速度方向，并使用微分推导方程(DDE)优化雅可比向量积(JVP)算子。在Adroit和Meta-World任务上的实验表明，该方法在平均成功率上优于MP1和FlowPolicy，尤其是在具有挑战性的Meta-World任务中，有效增强了机器人操作策略的少样本泛化能力和轨迹精度，同时保持了实时性能，为高精度机器人操作提供了一种更鲁棒的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作任务中，现有生成策略（如扩散模型和Flow模型）存在的推理速度慢、模型复杂度高，以及MeanFlow方法泛化能力不足的问题。具体来说，MeanFlow方法由于其分散损失中的固定温度超参数，以及预测速度与真实速度方向的偏差，导致其在少样本学习场景下表现不佳。

**核心思路**：论文的核心思路是通过改进MeanFlow策略，使其在保持单步推理速度的同时，提升其少样本泛化能力和轨迹精度。具体而言，通过引入余弦损失来对齐预测速度和真实速度的方向，从而减少方向偏差；并使用微分推导方程（DDE）来优化雅可比向量积（JVP）算子，从而更有效地学习策略。

**技术框架**：OMP方法的核心框架是在MeanFlow的基础上进行改进。整体流程包括：1) 使用MeanFlow生成初始轨迹；2) 使用余弦损失对齐预测速度和真实速度的方向；3) 使用微分推导方程优化雅可比向量积算子；4) 使用优化后的策略进行机器人操作。

**关键创新**：论文的关键创新在于：1) 引入轻量级的余弦损失来对齐速度方向，这是一种简单而有效的方法，可以显著减少方向偏差；2) 使用微分推导方程（DDE）来优化雅可比向量积（JVP）算子，这可以更有效地学习策略，并提高轨迹精度。

**关键设计**：余弦损失的设计旨在最小化预测速度和真实速度之间的角度差异，其具体形式为：`loss = 1 - cos(theta)`，其中`theta`是两个速度向量之间的夹角。微分推导方程（DDE）用于计算雅可比向量积，其具体形式未知（需要查阅论文原文）。网络结构方面，论文使用了轻量级的网络结构，以保证实时性能。具体参数设置未知（需要查阅论文原文）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19347v1/figures/teaser_v1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19347v1/figures/overview_v4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19347v1/figures/Experiments.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，OMP在Adroit和Meta-World任务上均取得了显著的性能提升。尤其是在具有挑战性的Meta-World任务中，OMP的平均成功率优于MP1和FlowPolicy，表明其具有更强的少样本泛化能力。具体性能数据未知（需要查阅论文原文）。

## 🎯 应用场景

该研究成果可应用于各种需要高精度和实时性的机器人操作任务，例如工业自动化、医疗手术机器人、家庭服务机器人等。通过提高机器人操作的泛化能力和轨迹精度，可以使机器人在复杂和未知的环境中更好地完成任务，从而提高生产效率和服务质量。未来，该方法有望进一步扩展到更复杂的机器人系统和任务中。

## 📄 摘要（原文）

> Robot manipulation, a key capability of embodied AI, has turned to data-driven generative policy frameworks, but mainstream approaches like Diffusion Models suffer from high inference latency and Flow-based Methods from increased architectural complexity. While simply applying meanFlow on robotic tasks achieves single-step inference and outperforms FlowPolicy, it lacks few-shot generalization due to fixed temperature hyperparameters in its Dispersive Loss and misaligned predicted-true mean velocities. To solve these issues, this study proposes an improved MeanFlow-based Policies: we introduce a lightweight Cosine Loss to align velocity directions and use the Differential Derivation Equation (DDE) to optimize the Jacobian-Vector Product (JVP) operator. Experiments on Adroit and Meta-World tasks show the proposed method outperforms MP1 and FlowPolicy in average success rate, especially in challenging Meta-World tasks, effectively enhancing few-shot generalization and trajectory accuracy of robot manipulation policies while maintaining real-time performance, offering a more robust solution for high-precision robotic manipulation.

