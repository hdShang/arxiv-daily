---
layout: default
title: "STSBench: A Spatio-temporal Scenario Benchmark for Multi-modal Large Language Models in Autonomous Driving"
---

# STSBench: A Spatio-temporal Scenario Benchmark for Multi-modal Large Language Models in Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06218" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06218v1</a>
  <a href="https://arxiv.org/pdf/2506.06218.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06218v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06218v1', 'STSBench: A Spatio-temporal Scenario Benchmark for Multi-modal Large Language Models in Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christian Fruhwirth-Reisinger, Dušan Malić, Wei Lin, David Schinagl, Samuel Schulter, Horst Possegger

**分类**: cs.CV

**发布日期**: 2025-06-06

**备注**: Dataset: https://huggingface.co/datasets/ivc-lrp/STSBench, Code: https://github.com/LRP-IVC/STSBench

---

## 💡 一句话要点

**提出STSBench以解决多模态大语言模型在自动驾驶中的时空推理问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时空推理` `多模态评估` `自动驾驶` `视觉-语言模型` `交通场景分析` `数据挖掘` `模型评估`

## 📋 核心要点

1. 现有基准主要针对单视角图像或视频的语义任务，缺乏对复杂交通场景的时空推理评估。
2. STSBench通过自动挖掘交通场景和生成评估问题，提供了一种新的评估框架，专注于多视角和激光雷达数据。
3. 实验结果显示，现有模型在推理交通动态方面存在显著不足，强调了对更强大时空推理模型的需求。

## 📝 摘要（中文）

我们介绍了STSBench，这是一个基于场景的框架，用于基准测试视觉-语言模型（VLMs）在自动驾驶中的整体理解能力。该框架能够自动从任何数据集中挖掘预定义的交通场景，并提供直观的用户界面以便于人类验证，同时生成多项选择题以评估模型。在NuScenes数据集上应用STSBench，我们提出了STSnu，这是第一个评估VLMs基于全面3D感知的时空推理能力的基准。与现有基准不同，STSnu评估驾驶专家VLMs在多视角摄像头或激光雷达视频上的端到端驾驶能力，特别关注自车行为和交通参与者之间复杂交互的推理能力。该基准涵盖43种多样化场景，生成971个经过人类验证的多项选择题，评估结果揭示了现有模型在复杂环境中推理基本交通动态的关键不足，强调了对时空推理模型的架构进步的迫切需求。

## 🔬 方法详解

**问题定义**：论文旨在解决现有视觉-语言模型在复杂交通环境中时空推理能力不足的问题。现有方法通常只关注单一视角的图像或视频，未能充分考虑多视角和动态交互的复杂性。

**核心思路**：STSBench通过构建一个场景基准框架，自动挖掘和评估多视角交通场景，提供了一种新的评估方式，旨在提升模型对时空动态的理解能力。

**技术框架**：该框架包括数据挖掘模块、用户验证界面和多项选择题生成模块。数据挖掘模块从数据集中提取交通场景，用户验证界面用于确保场景的准确性，而多项选择题生成模块则用于评估模型的推理能力。

**关键创新**：STSBench的核心创新在于其能够评估多视角和激光雷达数据下的时空推理能力，与传统基准相比，提供了更全面的评估视角。

**关键设计**：在设计中，STSBench设置了43种多样化的场景，生成971个经过人类验证的多项选择题，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果表明，现有模型在复杂交通动态推理方面存在显著不足，特别是在多视角和激光雷达数据的应用中。STSnu基准揭示了这些缺陷，强调了对新架构的需求，以提升模型的时空推理能力。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶系统的开发与优化，尤其是在复杂交通环境中的决策支持。通过提升视觉-语言模型的时空推理能力，未来可以实现更安全、更智能的自动驾驶技术，推动智能交通的发展。

## 📄 摘要（原文）

> We introduce STSBench, a scenario-based framework to benchmark the holistic understanding of vision-language models (VLMs) for autonomous driving. The framework automatically mines pre-defined traffic scenarios from any dataset using ground-truth annotations, provides an intuitive user interface for efficient human verification, and generates multiple-choice questions for model evaluation. Applied to the NuScenes dataset, we present STSnu, the first benchmark that evaluates the spatio-temporal reasoning capabilities of VLMs based on comprehensive 3D perception. Existing benchmarks typically target off-the-shelf or fine-tuned VLMs for images or videos from a single viewpoint and focus on semantic tasks such as object recognition, dense captioning, risk assessment, or scene understanding. In contrast, STSnu evaluates driving expert VLMs for end-to-end driving, operating on videos from multi-view cameras or LiDAR. It specifically assesses their ability to reason about both ego-vehicle actions and complex interactions among traffic participants, a crucial capability for autonomous vehicles. The benchmark features 43 diverse scenarios spanning multiple views and frames, resulting in 971 human-verified multiple-choice questions. A thorough evaluation uncovers critical shortcomings in existing models' ability to reason about fundamental traffic dynamics in complex environments. These findings highlight the urgent need for architectural advances that explicitly model spatio-temporal reasoning. By addressing a core gap in spatio-temporal evaluation, STSBench enables the development of more robust and explainable VLMs for autonomous driving.

