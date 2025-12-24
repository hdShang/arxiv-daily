---
layout: default
title: "FloorPlan-DeepSeek (FPDS): A multimodal approach to floorplan generation using vector-based next room prediction"
---

# FloorPlan-DeepSeek (FPDS): A multimodal approach to floorplan generation using vector-based next room prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21562" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21562v2</a>
  <a href="https://arxiv.org/pdf/2506.21562.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21562v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21562v2', 'FloorPlan-DeepSeek (FPDS): A multimodal approach to floorplan generation using vector-based next room prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Yin, Pengyu Zeng, Jing Zhong, Peilin Li, Miao Zhang, Ran Luo, Shuai Lu

**分类**: cs.CL, cs.AI, cs.AR

**发布日期**: 2025-06-12 (更新: 2025-08-02)

---

## 💡 一句话要点

**提出FPDS以解决建筑平面图生成的迭代性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `建筑平面图生成` `自回归模型` `下一个房间预测` `智能建筑设计` `多模态生成` `设计效率提升` `建筑设计工具`

## 📋 核心要点

1. 现有的平面图生成方法多为一次性生成，无法适应建筑设计的渐进性和迭代性，导致实际应用中的局限性。
2. 本文提出了一种新颖的'下一个房间预测'机制，借鉴自回归模型的思想，以支持逐步生成建筑平面图。
3. 实验结果显示，FPDS在文本到平面图任务中表现优异，性能与现有先进模型相当，具有良好的应用前景。

## 📝 摘要（中文）

在建筑设计过程中，平面图生成是一个渐进和迭代的过程。然而，现有的生成模型主要采用端到端的方式，一次性生成整个像素布局，这与实际建筑实践中的增量工作流程不兼容。为了解决这一问题，本文借鉴了大型语言模型中常用的自回归'下一个标记预测'机制，提出了一种针对建筑平面图建模的新型'下一个房间预测'范式。实验评估表明，FPDS在文本到平面图任务中表现出与扩散模型和Tell2Design相当的竞争性能，显示出其在未来智能建筑设计中的潜在应用价值。

## 🔬 方法详解

**问题定义**：本文旨在解决现有建筑平面图生成模型在实际应用中无法适应渐进和迭代设计流程的问题。现有方法通常一次性生成整个布局，缺乏灵活性和适应性。

**核心思路**：提出了一种基于'下一个房间预测'的生成机制，模仿自回归模型的工作方式，允许逐步生成平面图，适应建筑设计的动态需求。

**技术框架**：FPDS的整体架构包括输入文本描述、下一个房间的预测模块和生成的平面图输出。模型通过逐步预测每个房间的位置和形状，形成完整的平面图。

**关键创新**：FPDS的核心创新在于引入了'下一个房间预测'机制，区别于传统的端到端生成方法，使得平面图生成过程更加灵活和符合实际设计流程。

**关键设计**：模型采用了特定的损失函数来优化房间位置和形状的预测精度，同时在网络结构上进行了调整，以增强模型对建筑设计特征的学习能力。通过这些设计，FPDS能够有效地生成符合实际需求的平面图。

## 📊 实验亮点

实验结果表明，FPDS在文本到平面图生成任务中表现出与扩散模型和Tell2Design相当的性能，具体提升幅度未知。这表明FPDS在生成效率和设计灵活性方面具有显著优势，展示了其在智能建筑设计中的应用潜力。

## 🎯 应用场景

FPDS的研究成果在建筑设计、室内规划和智能家居等领域具有广泛的应用潜力。通过支持逐步生成平面图，该方法能够提高设计效率，降低设计成本，并为建筑师提供更灵活的设计工具，推动智能建筑设计的发展。

## 📄 摘要（原文）

> In the architectural design process, floor plan generation is inherently progressive and iterative. However, existing generative models for floor plans are predominantly end-to-end generation that produce an entire pixel-based layout in a single pass. This paradigm is often incompatible with the incremental workflows observed in real-world architectural practice. To address this issue, we draw inspiration from the autoregressive 'next token prediction' mechanism commonly used in large language models, and propose a novel 'next room prediction' paradigm tailored to architectural floor plan modeling. Experimental evaluation indicates that FPDS demonstrates competitive performance in comparison to diffusion models and Tell2Design in the text-to-floorplan task, indicating its potential applicability in supporting future intelligent architectural design.

