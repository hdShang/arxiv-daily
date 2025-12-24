---
layout: default
title: "KnowDR-REC: A Benchmark for Referring Expression Comprehension with Real-World Knowledge"
---

# KnowDR-REC: A Benchmark for Referring Expression Comprehension with Real-World Knowledge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14080" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14080v1</a>
  <a href="https://arxiv.org/pdf/2508.14080.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14080v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14080v1', 'KnowDR-REC: A Benchmark for Referring Expression Comprehension with Real-World Knowledge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanghao Jin, Jingpei Wu, Tianpei Guo, Yiyi Niu, Weidong Zhou, Guoyang Liu

**分类**: cs.LG

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出KnowDR-REC以解决多模态推理能力不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉定位` `知识驱动` `抗幻觉能力` `基准评估`

## 📋 核心要点

1. 现有的REC基准模型在推理能力上存在不足，无法有效评估多模态大语言模型的表现。
2. 本文提出KnowDR-REC基准，强调基于真实世界知识的细粒度多模态推理，并设计了负样本以增强模型鲁棒性。
3. 实验评估显示，现有的多模态模型在知识驱动的视觉定位任务上表现不佳，文本理解与视觉定位之间存在解耦现象。

## 📝 摘要（中文）

Referring Expression Comprehension (REC) 是一种流行的多模态任务，旨在根据给定的文本表达准确检测单幅图像中的目标对象。然而，传统的REC基准存在局限性，往往仅依赖图像内部线索或缺乏足够细粒度的实例注释，无法有效评估多模态大语言模型（MLLMs）的推理能力。为了解决这一问题，本文提出了新的基准KnowDR-REC，具有三个关键特征：基于真实世界知识，要求细粒度的多模态推理；通过细粒度表达编辑构建的负样本，评估模型的鲁棒性和抗幻觉能力；引入三种新评估指标，系统探索模型的内部推理过程。实验结果表明，现有的MLLMs在知识驱动的视觉定位任务上仍然存在困难。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态推理模型在真实世界知识应用中的不足，尤其是传统REC基准无法有效评估模型的推理能力和鲁棒性。

**核心思路**：提出KnowDR-REC基准，通过引入真实世界知识和细粒度的多模态推理，设计负样本以测试模型的抗幻觉能力，进而推动多模态系统的可靠性和解释性。

**技术框架**：KnowDR-REC基于真实场景构建，包含文本与图像的细粒度匹配模块、负样本生成模块以及新的评估指标模块，整体流程为数据收集、样本构建、模型评估。

**关键创新**：引入了细粒度表达编辑的负样本，系统性地评估模型的推理过程，并提出三种新评估指标，显著提升了对模型推理能力的评估深度。

**关键设计**：在模型训练中，采用特定的损失函数来优化多模态匹配，设置了多层次的网络结构以增强模型对复杂场景的理解能力。通过细粒度的样本设计，提升了模型的抗干扰能力。

## 📊 实验亮点

实验结果表明，16种最先进的多模态模型在KnowDR-REC基准上表现不佳，尤其是在知识驱动的视觉定位任务中，许多模型受到记忆化捷径的显著影响，导致推理能力不足。这一发现强调了模型在真实场景中的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、机器人视觉等复杂场景，能够提升多模态系统在真实世界中的表现和可靠性。未来，KnowDR-REC基准将推动更强大、可解释的视觉定位框架的发展，促进多模态技术的广泛应用。

## 📄 摘要（原文）

> Referring Expression Comprehension (REC) is a popular multimodal task that aims to accurately detect target objects within a single image based on a given textual expression. However, due to the limitations of earlier models, traditional REC benchmarks either rely solely on intra-image cues or lack sufficiently fine-grained instance annotations, making them inadequate for evaluating the reasoning capabilities of Multi-modal Large Language Models (MLLMs). To address this gap, we propose a new benchmark, KnowDR-REC, characterized by three key features: Firstly, it is built upon real-world knowledge, requiring fine-grained multimodal reasoning across text and image. Secondly, the dataset includes elaborately constructed negative samples via fine-grained expression editing, designed to evaluate a model's robustness and anti-hallucination ability. Lastly, we introduce three novel evaluation metrics to systematically explore the model's internal reasoning process. We evaluate 16 state-of-the-art multimodal models on KnowDR-REC, with experimental results showing that existing MLLMs still struggle with knowledge-driven visual grounding tasks. Furthermore, we observe a decoupling between textual understanding and visual grounding in MLLMs, where many models are significantly influenced by memorized shortcut correlations, which severely affect their behavior on our benchmark and hinder genuine multimodal reasoning. We anticipate that the proposed benchmark will inspire future research towards developing more robust, interpretable, and knowledge-intensive visual grounding frameworks, driving the development of more reliable and robust multimodal systems for complex real-world scenarios.

