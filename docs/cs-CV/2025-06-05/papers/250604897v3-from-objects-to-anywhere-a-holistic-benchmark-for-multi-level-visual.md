---
layout: default
title: "From Objects to Anywhere: A Holistic Benchmark for Multi-level Visual Grounding in 3D Scenes"
---

# From Objects to Anywhere: A Holistic Benchmark for Multi-level Visual Grounding in 3D Scenes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04897" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04897v3</a>
  <a href="https://arxiv.org/pdf/2506.04897.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04897v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04897v3', 'From Objects to Anywhere: A Holistic Benchmark for Multi-level Visual Grounding in 3D Scenes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianxu Wang, Zhuofan Zhang, Ziyu Zhu, Yue Fan, Jing Xiong, Pengxiang Li, Xiaojian Ma, Qing Li

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-10-28)

**备注**: Update v3 of the NeurIPS 2025 Datasets and Benchmarks paper (v2), including additional evaluations of state-of-the-art multimodal large language models. Project page: https://anywhere-3d.github.io/

---

## 💡 一句话要点

**提出Anywhere3D-Bench以解决3D场景中的多层次视觉定位问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉定位` `多层次基准` `空间关系` `细粒度感知` `大型语言模型`

## 📋 核心要点

1. 现有3D视觉定位方法主要集中于物体层次，缺乏对更复杂空间关系和细粒度部分的理解。
2. 本文提出了一个新的基准数据集，Anywhere3D-Bench，涵盖多层次的视觉定位任务，促进对3D场景的全面理解。
3. 实验表明，当前最先进的模型在空间层次和部分层次任务上的准确率仅约30%和40%，显示出模型的局限性。

## 📝 摘要（中文）

3D视觉定位在复杂3D场景中已取得显著进展，但超越物体的指称表达定位仍未被探索。本文提出了Anywhere3D-Bench，一个包含2886个指称表达-3D边界框对的全面3D视觉定位基准，涵盖四个不同的定位层次：人类活动区域、物体之外的空闲空间、场景中的单个物体以及细粒度物体部分。实验结果显示，空间层次和部分层次的视觉定位面临最大挑战，现有模型在这些任务上的表现显著低于区域层次和物体层次任务。

## 🔬 方法详解

**问题定义**：本文旨在解决3D场景中超越物体的视觉定位问题，现有方法在处理空间关系和细粒度部分时存在显著不足。

**核心思路**：通过引入一个全面的基准数据集，Anywhere3D-Bench，论文鼓励研究者关注更复杂的空间和部分层次的视觉定位任务。

**技术框架**：整体架构包括数据集构建、模型评估和性能比较三个主要阶段，涵盖人类活动区域、空闲空间、物体和物体部分的定位。

**关键创新**：最重要的创新在于提出了多层次的视觉定位任务，尤其是空间层次和部分层次的挑战，这在现有文献中尚未得到充分重视。

**关键设计**：在模型评估中，采用了多种先进的3D视觉定位方法，并与大型语言模型和多模态语言模型进行比较，确保了实验的全面性和有效性。

## 📊 实验亮点

实验结果显示，当前最先进的模型在空间层次任务上的准确率仅为30%左右，而在部分层次任务上的准确率约为40%。这些结果表明，现有模型在理解和推理3D场景方面存在显著不足，尤其是在空间和细粒度层次的任务上。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、增强现实和虚拟现实等，能够帮助机器更好地理解和互动复杂的3D环境。随着技术的发展，未来可能在自动驾驶、智能家居等领域发挥重要作用。

## 📄 摘要（原文）

> 3D visual grounding has made notable progress in localizing objects within complex 3D scenes. However, grounding referring expressions beyond objects in 3D scenes remains unexplored. In this paper, we introduce Anywhere3D-Bench, a holistic 3D visual grounding benchmark consisting of 2,886 referring expression-3D bounding box pairs spanning four different grounding levels: human-activity areas, unoccupied space beyond objects, individual objects in the scene, and fine-grained object parts. We assess a range of state-of-the-art 3D visual grounding methods alongside large language models (LLMs) and multimodal LLMs (MLLMs) on Anywhere3D-Bench. Experimental results reveal that space-level and part-level visual grounding pose the greatest challenges: space-level tasks require a more comprehensive spatial reasoning ability, for example, modeling distances and spatial relations within 3D space, while part-level tasks demand fine-grained perception of object composition. Even the best-performing models, Google Gemini-2.5-Pro and OpenAI o3, achieve just around 30% accuracy on space-level tasks and around 40% on part-level tasks, significantly lower than its performance on area-level and object-level tasks. These findings underscore a critical gap in current models' capacity to understand and reason about 3D scenes beyond object-level semantics.

