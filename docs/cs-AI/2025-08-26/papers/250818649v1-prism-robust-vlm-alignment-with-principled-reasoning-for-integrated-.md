---
layout: default
title: "PRISM: Robust VLM Alignment with Principled Reasoning for Integrated Safety in Multimodality"
---

# PRISM: Robust VLM Alignment with Principled Reasoning for Integrated Safety in Multimodality

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18649" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18649v1</a>
  <a href="https://arxiv.org/pdf/2508.18649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18649v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18649v1', 'PRISM: Robust VLM Alignment with Principled Reasoning for Integrated Safety in Multimodality')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nanxi Li, Zhengyue Zhao, Chaowei Xiao

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-26

**🔗 代码/项目**: [GITHUB](https://github.com/SaFoLab-WISC/PRISM)

---

## 💡 一句话要点

**提出PRISM以解决视觉语言模型安全性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `安全防护` `多模态学习` `深度推理` `蒙特卡罗树搜索` `直接偏好优化` `鲁棒性` `链式推理`

## 📋 核心要点

1. 现有的视觉语言模型安全防护方法存在过度防御和浅层对齐的问题，难以应对复杂威胁。
2. PRISM通过引入安全意识的链式推理和直接偏好优化，提供了一种新的对齐方式，增强了模型的安全性。
3. 实验结果显示，PRISM在多个基准测试中显著降低了攻击成功率，提升了模型的鲁棒性和效用。

## 📝 摘要（中文）

保护视觉语言模型（VLMs）是一个关键挑战，现有方法往往面临过度防御导致效用下降或依赖浅层对齐，无法检测需要深度推理的复杂威胁。为此，我们提出PRISM（多模态集成安全的原则性推理），通过嵌入结构化的安全意识推理过程来对齐VLMs。我们的框架包括两个关键组件：PRISM-CoT，一个教授安全意识链式推理的数据集，以及通过蒙特卡罗树搜索（MCTS）生成的PRISM-DPO，进一步通过直接偏好优化来精炼推理，帮助获得精细的安全边界。全面评估表明，PRISM在攻击成功率上表现出色，包括在JailbreakV-28K上对Qwen2-VL的0.15%攻击成功率，以及在VLBreak上对LLaVA-1.5的90%提升。PRISM在自适应攻击下表现出强大的鲁棒性，显著增加对手的计算成本，并有效泛化到分布外挑战，在多图像MIS基准上将攻击成功率降低至8.70%。值得注意的是，这种鲁棒防御在保持模型效用的同时，甚至在某些情况下增强了模型的效用。为了促进可重复性，我们已将代码、数据和模型权重公开。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉语言模型（VLMs）在面对复杂威胁时的安全性问题。现有方法往往过度防御，导致模型效用下降，或依赖浅层对齐，无法有效检测深层次的攻击。

**核心思路**：PRISM的核心思想是通过引入结构化的安全意识推理过程，增强模型的防御能力。具体而言，PRISM-CoT用于教授模型安全意识的链式推理，而PRISM-DPO则通过直接偏好优化进一步精炼推理过程，以获得更精细的安全边界。

**技术框架**：PRISM框架主要由两个模块组成：PRISM-CoT和PRISM-DPO。PRISM-CoT负责生成安全意识的推理数据集，而PRISM-DPO则利用蒙特卡罗树搜索（MCTS）生成的样本进行优化，形成一个闭环的推理和优化过程。

**关键创新**：PRISM的创新之处在于将安全意识推理与直接偏好优化相结合，形成了一种新的防御机制。这种机制与现有方法的本质区别在于其深度推理能力，能够有效应对复杂的攻击策略。

**关键设计**：在设计上，PRISM采用了多层次的推理结构，并通过损失函数优化模型的安全边界。此外，PRISM-DPO的生成过程利用了蒙特卡罗树搜索技术，以确保生成样本的多样性和有效性。整体架构的设计旨在提高模型的鲁棒性和实用性。

## 📊 实验亮点

PRISM在多个基准测试中表现出色，JailbreakV-28K上对Qwen2-VL的攻击成功率仅为0.15%，在VLBreak上相比于之前最佳方法提升了90%。此外，PRISM在多图像MIS基准上将攻击成功率降低至8.70%，展现出强大的鲁棒性和效用保持能力。

## 🎯 应用场景

该研究的潜在应用领域包括安全性要求高的视觉语言处理任务，如自动内容审核、智能助手和多模态交互系统。通过增强模型的安全性，PRISM能够在实际应用中有效防范复杂攻击，提升用户信任度和系统稳定性。未来，该方法可能推动更广泛的多模态AI系统的安全性研究与应用。

## 📄 摘要（原文）

> Safeguarding vision-language models (VLMs) is a critical challenge, as existing methods often suffer from over-defense, which harms utility, or rely on shallow alignment, failing to detect complex threats that require deep reasoning. To this end, we introduce PRISM (Principled Reasoning for Integrated Safety in Multimodality), a system2-like framework that aligns VLMs by embedding a structured, safety-aware reasoning process. Our framework consists of two key components: PRISM-CoT, a dataset that teaches safety-aware chain-of-thought reasoning, and PRISM-DPO, generated via Monte Carlo Tree Search (MCTS) to further refine this reasoning through Direct Preference Optimization to help obtain a delicate safety boundary. Comprehensive evaluations demonstrate PRISM's effectiveness, achieving remarkably low attack success rates including 0.15% on JailbreakV-28K for Qwen2-VL and 90% improvement over the previous best method on VLBreak for LLaVA-1.5. PRISM also exhibits strong robustness against adaptive attacks, significantly increasing computational costs for adversaries, and generalizes effectively to out-of-distribution challenges, reducing attack success rates to just 8.70% on the challenging multi-image MIS benchmark. Remarkably, this robust defense is achieved while preserving, and in some cases enhancing, model utility. To promote reproducibility, we have made our code, data, and model weights available at https://github.com/SaFoLab-WISC/PRISM.

