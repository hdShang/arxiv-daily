---
layout: default
title: Large Language Models for Controllable Multi-property Multi-objective Molecule Optimization
---

# Large Language Models for Controllable Multi-property Multi-objective Molecule Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23987" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23987v1</a>
  <a href="https://arxiv.org/pdf/2505.23987.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23987v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23987v1', 'Large Language Models for Controllable Multi-property Multi-objective Molecule Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vishal Dey, Xiao Hu, Xia Ning

**分类**: cs.LG, cs.AI, cs.CL, q-bio.BM

**发布日期**: 2025-05-29

**🔗 代码/项目**: [GITHUB](https://github.com/ninglab/GeLLMO-C)

---

## 💡 一句话要点

**提出C-MuMOInstruct以解决多属性分子优化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分子优化` `药物设计` `指令调优` `多属性优化` `机器学习`

## 📋 核心要点

1. 现有的计算方法和指令调优的语言模型无法有效捕捉多属性分子优化中的细微目标，限制了其应用。
2. 本文提出C-MuMOInstruct数据集，并基于此开发GeLLMO-Cs模型，实现针对性的属性特定优化。
3. 实验表明，GeLLMO-Cs在多项任务中表现优异，成功率显著提升，并展现出零样本泛化能力。

## 📝 摘要（中文）

在现实世界的药物设计中，分子优化需要选择性地提升多个分子属性至药理相关水平，同时保持其他已满足标准的属性。然而，现有的计算方法和指令调优的语言模型未能捕捉到这种细微的属性特定目标，限制了它们的实际应用。为此，本文引入了C-MuMOInstruct，这是第一个专注于多属性优化的指令调优数据集，具有明确的属性特定目标。基于C-MuMOInstruct，我们开发了GeLLMO-Cs系列指令调优的语言模型，能够执行针对性的属性特定优化。实验结果显示，GeLLMO-Cs在5个分布内和5个分布外任务中均优于强基线，成功率提高了126%。

## 🔬 方法详解

**问题定义**：本文旨在解决在药物设计中多属性分子优化的挑战，现有方法无法有效处理属性特定的优化目标，导致实际应用受限。

**核心思路**：提出C-MuMOInstruct数据集，专注于多属性优化的指令调优，允许模型针对特定属性进行优化，从而提升优化的灵活性和准确性。

**技术框架**：整体架构包括数据集构建、模型训练和优化任务执行三个主要模块。C-MuMOInstruct提供了多样化的指令，GeLLMO-Cs模型则在此基础上进行训练。

**关键创新**：C-MuMOInstruct是首个针对多属性优化的指令调优数据集，GeLLMO-Cs模型在处理属性特定目标方面表现出色，显著优于现有方法。

**关键设计**：模型训练中采用了特定的损失函数和参数设置，以确保模型能够有效学习不同属性的优化目标，网络结构经过精心设计以支持多任务学习。

## 📊 实验亮点

实验结果显示，GeLLMO-Cs在5个分布内和5个分布外任务中均优于强基线，成功率提高了126%。此外，模型在新优化任务和未见指令上展现出令人印象深刻的零样本泛化能力，标志着其在实际应用中的潜力。

## 🎯 应用场景

该研究在药物设计、材料科学等领域具有广泛的应用潜力。通过实现多属性的分子优化，能够加速新药的研发过程，提高药物的有效性和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In real-world drug design, molecule optimization requires selectively improving multiple molecular properties up to pharmaceutically relevant levels, while maintaining others that already meet such criteria. However, existing computational approaches and instruction-tuned LLMs fail to capture such nuanced property-specific objectives, limiting their practical applicability. To address this, we introduce C-MuMOInstruct, the first instruction-tuning dataset focused on multi-property optimization with explicit, property-specific objectives. Leveraging C-MuMOInstruct, we develop GeLLMO-Cs, a series of instruction-tuned LLMs that can perform targeted property-specific optimization. Our experiments across 5 in-distribution and 5 out-of-distribution tasks show that GeLLMO-Cs consistently outperform strong baselines, achieving up to 126% higher success rate. Notably, GeLLMO-Cs exhibit impressive 0-shot generalization to novel optimization tasks and unseen instructions. This offers a step toward a foundational LLM to support realistic, diverse optimizations with property-specific objectives. C-MuMOInstruct and code are accessible through https://github.com/ninglab/GeLLMO-C.

