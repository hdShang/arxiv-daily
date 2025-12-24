---
layout: default
title: Structured Agent Distillation for Large Language Model
---

# Structured Agent Distillation for Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13820" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13820v2</a>
  <a href="https://arxiv.org/pdf/2505.13820.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13820v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13820v2', 'Structured Agent Distillation for Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Liu, Zhenglun Kong, Peiyan Dong, Changdi Yang, Tianqi Li, Hao Tang, Geng Yuan, Wei Niu, Wenbin Zhang, Pu Zhao, Xue Lin, Dong Huang, Yanzhi Wang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-20 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出结构化代理蒸馏以解决大语言模型压缩问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代理蒸馏` `推理与行动` `模型压缩` `结构感知监督`

## 📋 核心要点

1. 现有的大型语言模型在推理和行动方面表现出色，但其高推理成本和模型体积限制了实际应用。
2. 本文提出结构化代理蒸馏，通过将轨迹分为推理和行动两个部分，采用特定损失函数进行对齐，从而压缩模型。
3. 实验结果显示，该方法在多个基准测试中优于传统的令牌级蒸馏和模仿学习，压缩效果显著且性能下降最小。

## 📝 摘要（中文）

大型语言模型（LLMs）在决策代理方面展现出强大的能力，但其高推理成本和模型体积限制了实际应用。本文提出结构化代理蒸馏框架，通过将大型LLM代理压缩为较小的学生模型，同时保持推理的准确性和行动的一致性。与标准的令牌级蒸馏不同，我们的方法将轨迹分为{[REASON]}和{[ACT]}两个部分，针对每个部分应用特定的损失函数，以对齐教师模型的行为。这种结构感知的监督使得紧凑的代理能够更好地复制教师的决策过程。实验结果表明，该方法在ALFWorld、HotPotQA-ReAct和WebShop上均优于令牌级和模仿学习基线，实现了显著的压缩和最小的性能下降。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在实际应用中的高推理成本和模型体积问题。现有的蒸馏方法往往无法有效保持推理的准确性和行动的一致性。

**核心思路**：提出结构化代理蒸馏框架，将模型的决策过程分为推理和行动两个部分，分别进行蒸馏，以更好地保留教师模型的行为特征。

**技术框架**：整体架构包括两个主要模块：推理模块和行动模块。每个模块根据其特性应用特定的损失函数，以实现更高效的对齐。

**关键创新**：最重要的创新在于采用结构感知的监督方法，通过分段对齐推理和行动，显著提高了蒸馏效果，与传统的令牌级蒸馏方法相比，能够更好地保留决策过程。

**关键设计**：在损失函数设计上，针对推理和行动分别设置了不同的损失函数，以确保每个部分的对齐效果。此外，模型结构经过优化，以支持这种分段蒸馏的需求。

## 📊 实验亮点

实验结果表明，结构化代理蒸馏方法在ALFWorld、HotPotQA-ReAct和WebShop上均优于传统的令牌级蒸馏和模仿学习基线，压缩率显著，性能下降幅度最小，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化决策系统和机器人控制等。通过有效压缩大型语言模型，能够在资源受限的环境中实现高效的推理和决策，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit strong capabilities as decision-making agents by interleaving reasoning and actions, as seen in ReAct-style frameworks. Yet, their practical deployment is constrained by high inference costs and large model sizes. We propose Structured Agent Distillation, a framework that compresses large LLM-based agents into smaller student models while preserving both reasoning fidelity and action consistency. Unlike standard token-level distillation, our method segments trajectories into {[REASON]} and {[ACT]} spans, applying segment-specific losses to align each component with the teacher's behavior. This structure-aware supervision enables compact agents to better replicate the teacher's decision process. Experiments on ALFWorld, HotPotQA-ReAct, and WebShop show that our approach consistently outperforms token-level and imitation learning baselines, achieving significant compression with minimal performance drop. Scaling and ablation results further highlight the importance of span-level alignment for efficient and deployable agents.

