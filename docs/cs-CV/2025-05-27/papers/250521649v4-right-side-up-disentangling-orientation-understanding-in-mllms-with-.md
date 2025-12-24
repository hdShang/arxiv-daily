---
layout: default
title: Right Side Up? Disentangling Orientation Understanding in MLLMs with Fine-grained Multi-axis Perception Tasks
---

# Right Side Up? Disentangling Orientation Understanding in MLLMs with Fine-grained Multi-axis Perception Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21649" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21649v4</a>
  <a href="https://arxiv.org/pdf/2505.21649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21649v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21649v4', 'Right Side Up? Disentangling Orientation Understanding in MLLMs with Fine-grained Multi-axis Perception Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keanu Nichols, Nazia Tasnim, Yuting Yan, Nicholas Ikechukwu, Elva Zou, Deepti Ghadiyaram, Bryan A. Plummer

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-06-04)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/appledora)

---

## 💡 一句话要点

**提出DORI基准以解决多模态系统的物体方向理解问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `物体方向理解` `多模态系统` `视觉-语言模型` `DORI基准` `机器人操作` `增强现实` `空间表示`

## 📋 核心要点

1. 现有的视觉-语言基准未能有效隔离物体方向理解能力，导致评估结果不准确。
2. 论文提出DORI基准，专注于物体方向感知的四个维度，提供系统化的评估框架。
3. 实验结果显示，现有模型在方向理解上存在显著不足，尤其在复杂任务中表现不佳。

## 📝 摘要（中文）

物体方向理解是视觉感知中的一项基本挑战，对于机器人操作和增强现实等应用至关重要。现有的视觉-语言基准未能单独评估这一能力，往往将其与位置关系和一般场景理解混淆。本文提出DORI（Discriminative Orientation Reasoning Intelligence），这是一个全面的基准，确立了物体方向感知作为主要评估目标。DORI评估方向理解的四个维度：正面对齐、旋转变换、相对方向关系和规范方向理解。通过从11个数据集中精心策划的任务，涵盖67个物体类别，DORI提供了多模态系统如何理解物体方向的深入见解。对15个最先进的视觉-语言模型的评估显示出关键的局限性，最佳模型在粗略任务上仅达到54.2%的准确率，在细粒度方向判断上仅为33.0%。

## 🔬 方法详解

**问题定义**：本文旨在解决物体方向理解的评估问题，现有方法未能单独评估这一能力，导致模型在实际应用中的表现不佳。

**核心思路**：DORI基准通过聚焦于物体方向感知的四个维度，提供了一个系统化的评估框架，帮助研究者理解多模态系统在方向理解方面的能力。

**技术框架**：DORI基准包括四个主要模块：正面对齐、旋转变换、相对方向关系和规范方向理解。每个模块通过精心设计的任务进行评估，涵盖多个数据集和物体类别。

**关键创新**：DORI是首个专门针对多模态系统方向意识的诊断框架，强调了方向理解的独立性和重要性，与现有方法相比，提供了更细致的评估标准。

**关键设计**：在任务设计中，DORI使用了来自11个数据集的任务，涵盖67个物体类别，采用了多种评估指标，确保了评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，15个最先进的视觉-语言模型在粗略任务上仅达到54.2%的准确率，而在细粒度方向判断上仅为33.0%。这些结果表明，现有模型在处理方向理解方面存在显著的局限性，尤其是在需要参考框架转换或复合旋转的任务中表现不佳。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、3D场景重建和人机交互等。通过改进物体方向理解，DORI基准可以帮助提升机器人在复杂环境中的操作能力，增强现实应用的交互体验，并推动多模态系统的进一步发展。

## 📄 摘要（原文）

> Object orientation understanding represents a fundamental challenge in visual perception critical for applications like robotic manipulation and augmented reality. Current vision-language benchmarks fail to isolate this capability, often conflating it with positional relationships and general scene understanding. We introduce DORI (Discriminative Orientation Reasoning Intelligence), a comprehensive benchmark establishing object orientation perception as a primary evaluation target. DORI assesses four dimensions of orientation comprehension: frontal alignment, rotational transformations, relative directional relationships, and canonical orientation understanding. Through carefully curated tasks from 11 datasets spanning 67 object categories across synthetic and real-world scenarios, DORI provides insights on how multi-modal systems understand object orientations. Our evaluation of 15 state-of-the-art vision-language models reveals critical limitations: even the best models achieve only 54.2% accuracy on coarse tasks and 33.0% on granular orientation judgments, with performance deteriorating for tasks requiring reference frame shifts or compound rotations. These findings demonstrate the need for dedicated orientation representation mechanisms, as models show systematic inability to perform precise angular estimations, track orientation changes across viewpoints, and understand compound rotations - suggesting limitations in their internal 3D spatial representations. As the first diagnostic framework specifically designed for orientation awareness in multimodal systems, DORI offers implications for improving robotic control, 3D scene reconstruction, and human-AI interaction in physical environments. DORI data: https://huggingface.co/datasets/appledora/DORI-Benchmark

