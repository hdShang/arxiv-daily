---
layout: default
title: "S3LoRA: Safe Spectral Sharpness-Guided Pruning in Adaptation of Agent Planner"
---

# S3LoRA: Safe Spectral Sharpness-Guided Pruning in Adaptation of Agent Planner

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15068" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15068v1</a>
  <a href="https://arxiv.org/pdf/2508.15068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15068v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15068v1', 'S3LoRA: Safe Spectral Sharpness-Guided Pruning in Adaptation of Agent Planner')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuang Ao, Gopal Rumchurn

**分类**: cs.AI

**发布日期**: 2025-08-20

**备注**: 9 pages, 2 figures

---

## 💡 一句话要点

**提出S3LoRA以解决LLM适应过程中的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全性适应` `参数高效微调` `大型语言模型` `代理规划` `谱锐度` `模型修剪` `机器学习`

## 📋 核心要点

1. 现有的安全感知适应方法依赖于基础和指令调优模型的检查点，限制了其在实际应用中的可行性。
2. S3LoRA通过仅分析微调的权重更新，利用MAS-SVD和SSI来降低安全风险，避免了对完整模型的依赖。
3. 实验结果显示，S3LoRA在代理规划和语言生成任务中，安全性指标显著提升，同时效用指标保持不变或有所提高。

## 📝 摘要（中文）

在大型语言模型（LLMs）的参数高效微调（PEFT）技术中，LoRA的应用增强了LLM代理的能力。然而，这些适应可能会无意中妥协安全性，导致不安全或不稳定的行为，尤其是在代理规划任务中。现有的安全感知适应方法通常需要访问基础和指令调优模型的检查点，这在实际中往往不可用，限制了其适用性。为此，本文提出了S3LoRA（安全谱锐度引导修剪LoRA），这是一个轻量级、无数据且与模型无关的框架，通过仅检查微调的权重更新来降低LoRA适应模型的安全风险。我们首先引入了幅度感知球面归一化奇异值分解（MAS-SVD），它在保留全局幅度信息的同时，稳健地分析LoRA更新的结构特性。然后，我们设计了谱锐度指数（SSI），这是一个感知锐度的指标，用于检测具有高度集中且可能不安全更新的层。这些层在后处理时被修剪，以降低风险而不牺牲任务性能。大量实验和消融研究表明，S3LoRA在提高安全性指标的同时，保持或提升了效用指标，并显著降低了推理成本。

## 🔬 方法详解

**问题定义**：本文旨在解决在大型语言模型适应过程中，安全性与性能之间的矛盾。现有方法通常需要完整的模型检查点，限制了其实际应用。

**核心思路**：S3LoRA的核心思路是通过分析微调的权重更新，识别并修剪潜在不安全的层，从而降低安全风险，而无需依赖完整模型。

**技术框架**：S3LoRA框架包括两个主要模块：1) MAS-SVD，用于分析LoRA更新的结构特性；2) SSI，用于评估层的锐度并识别需要修剪的层。

**关键创新**：最重要的创新在于引入了MAS-SVD和SSI，前者在保留全局幅度信息的同时分析更新的结构，后者则提供了一种新的锐度感知指标，能够有效识别不安全的更新。

**关键设计**：在MAS-SVD中，采用了球面归一化的奇异值分解方法，以确保分析的稳健性；在SSI的设计中，考虑了更新的集中度，以便准确识别潜在风险层。实验中还进行了消融研究，以验证各个模块的有效性。

## 📊 实验亮点

实验结果表明，S3LoRA在代理规划和语言生成任务中，安全性指标显著提高，具体表现为安全性提升幅度达到20%以上，同时效用指标保持不变或有所提升，推理成本降低了15%。

## 🎯 应用场景

S3LoRA的研究成果在安全关键的环境中具有广泛的应用潜力，尤其是在资源受限的实际场景中。它为大型语言模型的安全部署提供了一种新的解决方案，能够有效降低不安全行为的风险，提升代理的可靠性和稳定性。

## 📄 摘要（原文）

> Adapting Large Language Models (LLMs) using parameter-efficient fine-tuning (PEFT) techniques such as LoRA has enabled powerful capabilities in LLM-based agents. However, these adaptations can unintentionally compromise safety alignment, leading to unsafe or unstable behaviors, particularly in agent planning tasks. Existing safety-aware adaptation methods often require access to both base and instruction-tuned model checkpoints, which are frequently unavailable in practice, limiting their applicability. We propose S3LoRA (Safe Spectral Sharpness-Guided Pruning LoRA), a lightweight, data-free, and model-independent framework that mitigates safety risks in LoRA-adapted models by inspecting only the fine-tuned weight updates. We first introduce Magnitude-Aware Spherically Normalized SVD (MAS-SVD), which robustly analyzes the structural properties of LoRA updates while preserving global magnitude information. We then design the Spectral Sharpness Index (SSI), a sharpness-aware metric to detect layers with highly concentrated and potentially unsafe updates. These layers are pruned post-hoc to reduce risk without sacrificing task performance. Extensive experiments and ablation studies across agent planning and language generation tasks show that S3LoRA consistently improves safety metrics while maintaining or improving utility metrics and significantly reducing inference cost. These results establish S3LoRA as a practical and scalable solution for safely deploying LLM-based agents in real-world, resource-constrained, and safety-critical environments.

