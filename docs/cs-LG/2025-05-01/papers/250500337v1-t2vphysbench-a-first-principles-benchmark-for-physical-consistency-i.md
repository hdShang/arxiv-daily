---
layout: default
title: "T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation"
---

# T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00337" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00337v1</a>
  <a href="https://arxiv.org/pdf/2505.00337.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00337v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00337v1', 'T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuyang Guo, Jiayan Huo, Zhenmei Shi, Zhao Song, Jiahao Zhang, Jiale Zhao

**分类**: cs.LG, cs.AI, cs.CL, cs.CV

**发布日期**: 2025-05-01

---

## 💡 一句话要点

**提出T2VPhysBench以评估文本到视频生成中的物理一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到视频生成` `物理一致性` `评估基准` `人类评估` `牛顿力学` `能量守恒` `现象效应`

## 📋 核心要点

1. 现有文本到视频生成模型在遵循基本物理法则方面存在显著不足，导致生成内容不真实或误导。
2. T2VPhysBench基准通过系统评估文本到视频生成模型是否遵循核心物理法则，填补了现有评估方法的空白。
3. 实验结果显示，所有模型在物理法则的合规性评估中平均得分低于0.60，揭示了当前模型的局限性。

## 📝 摘要（中文）

文本到视频生成模型近年来取得了显著进展，能够生成高质量的视频，兼顾美学和指令遵循。然而，这些模型在遵循基本物理法则方面的能力尚未得到充分测试，许多输出仍然违反基本约束，如刚体碰撞、能量守恒和重力动态。现有的物理评估基准通常依赖于自动化的像素级指标，忽视了人类判断和第一性原理物理。为填补这一空白，我们提出了T2VPhysBench，这是一个系统评估文本到视频系统是否遵循包括牛顿力学、守恒原则和现象效应在内的十二项核心物理法则的基准。我们的基准采用严格的人类评估协议，并包括三项针对性研究，结果揭示了当前架构的持续局限性，并为未来研究提供了具体的指导。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到视频生成模型在遵循物理法则方面的不足，现有方法多依赖于简单的像素级评估，缺乏对人类判断和物理原则的考量。

**核心思路**：我们提出T2VPhysBench基准，通过系统评估模型是否遵循十二项核心物理法则，采用严格的人类评估方法，以确保评估的全面性和准确性。

**技术框架**：该基准包括三个主要模块：整体合规性评估、提示消融实验和反事实鲁棒性测试，旨在全面分析模型在物理法则遵循方面的表现。

**关键创新**：T2VPhysBench的创新在于其系统性和第一性原理的评估方法，区别于现有的自动化评估，强调了人类评估的重要性。

**关键设计**：在评估过程中，我们设计了详细的提示和评估标准，确保能够准确捕捉模型在物理法则遵循上的表现，并通过多轮评估提高结果的可靠性。

## 📊 实验亮点

实验结果显示，所有评估的模型在物理法则的合规性上平均得分低于0.60，表明当前技术在遵循物理法则方面存在显著不足。此外，详细的提示并未显著改善模型的物理一致性，揭示了模型架构的根本局限性。

## 🎯 应用场景

该研究的潜在应用领域包括数字艺术创作、游戏开发和虚拟现实等，能够帮助开发者生成更符合物理规律的内容，提高用户体验和参与度。未来，该基准有望推动文本到视频生成技术向更高的物理一致性和真实感发展。

## 📄 摘要（原文）

> Text-to-video generative models have made significant strides in recent years, producing high-quality videos that excel in both aesthetic appeal and accurate instruction following, and have become central to digital art creation and user engagement online. Yet, despite these advancements, their ability to respect fundamental physical laws remains largely untested: many outputs still violate basic constraints such as rigid-body collisions, energy conservation, and gravitational dynamics, resulting in unrealistic or even misleading content. Existing physical-evaluation benchmarks typically rely on automatic, pixel-level metrics applied to simplistic, life-scenario prompts, and thus overlook both human judgment and first-principles physics. To fill this gap, we introduce \textbf{T2VPhysBench}, a first-principled benchmark that systematically evaluates whether state-of-the-art text-to-video systems, both open-source and commercial, obey twelve core physical laws including Newtonian mechanics, conservation principles, and phenomenological effects. Our benchmark employs a rigorous human evaluation protocol and includes three targeted studies: (1) an overall compliance assessment showing that all models score below 0.60 on average in each law category; (2) a prompt-hint ablation revealing that even detailed, law-specific hints fail to remedy physics violations; and (3) a counterfactual robustness test demonstrating that models often generate videos that explicitly break physical rules when so instructed. The results expose persistent limitations in current architectures and offer concrete insights for guiding future research toward truly physics-aware video generation.

