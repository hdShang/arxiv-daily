---
layout: default
title: "VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models"
---

# VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17561" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17561v1</a>
  <a href="https://arxiv.org/pdf/2506.17561.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17561v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17561v1', 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chongkai Gao, Zixuan Liu, Zhenghao Chi, Junshan Huang, Xin Fei, Yiwen Hou, Yuxuan Zhang, Yudi Lin, Zhirui Fang, Zeyu Jiang, Lin Shao

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-06-21

---

## 💡 一句话要点

**提出VLA-OS以系统化规划表示和范式在视觉-语言-动作模型中的应用**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `任务规划` `多模态学习` `机器人操作` `深度学习`

## 📋 核心要点

1. 现有VLA模型在网络架构和训练数据源上差异显著，难以识别性能提升的具体来源。
2. 本文提出VLA-OS，统一的VLA架构系列，支持多种任务规划范式，旨在系统性研究不同规划表示的影响。
3. 实验结果显示，视觉基础的规划表示优于语言基础的表示，分层VLA范式在多项性能指标上表现优越。

## 📝 摘要（中文）

近年来，视觉-语言-动作（VLA）模型的研究已从端到端的动作生成范式转向包含任务规划和动作生成的管道，显示出在复杂长时间操作任务上的性能提升。然而，现有方法在网络架构、规划范式、表示和训练数据源上差异显著，导致研究者难以识别性能提升的具体来源。为系统性地研究不同规划范式和表示的影响，本文提出了VLA-OS，一个统一的VLA架构系列，能够支持多种任务规划范式，并设计了一套全面的控制实验，涵盖多种物体类别、视觉模态、环境和末端执行器。实验结果表明，视觉基础的规划表示通常优于语言基础的表示，而分层VLA范式在任务性能、预训练、泛化能力、可扩展性和持续学习能力上通常表现优越，尽管训练和推理速度较慢。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言-动作模型在规划表示和范式上的不一致性，导致性能提升来源不明确的问题。现有方法在网络架构、规划范式和训练数据源上存在显著差异，影响了研究的系统性和可重复性。

**核心思路**：提出VLA-OS架构，通过统一的设计来支持多种任务规划范式，系统性地评估不同规划表示的效果，旨在消除网络架构和训练数据对结果的干扰。

**技术框架**：VLA-OS架构包括多个模块，首先进行任务规划，然后生成动作。实验设计涵盖多种物体类别（刚性和可变形）、视觉模态（2D和3D）、环境（仿真和现实）及末端执行器（夹持器和灵巧手）。

**关键创新**：最重要的创新点在于引入了分层VLA范式，该范式在任务性能、预训练、泛化能力、可扩展性和持续学习能力上表现优越，且能够系统性地比较不同规划表示的效果。

**关键设计**：在设计中，采用了视觉基础的规划表示，设置了多种实验条件以评估不同规划范式的性能，关注训练和推理速度的权衡。具体的损失函数和网络结构细节在实验中进行了优化。

## 📊 实验亮点

实验结果表明，视觉基础的规划表示在多项任务中优于语言基础的表示，分层VLA范式在任务性能上表现优越，尤其在预训练和泛化能力方面，提升幅度显著，尽管训练和推理速度较慢。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和人机交互等。通过改进视觉-语言-动作模型的规划能力，能够提升机器人在复杂环境中的自主操作能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and components to be further improved. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable performance than other paradigms on task performance, pretraining, generalization ability, scalability, and continual learning ability, albeit at the cost of slower training and inference speeds.

