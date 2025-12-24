---
layout: default
title: Visuospatial Cognitive Assistant
---

# Visuospatial Cognitive Assistant

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12312" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12312v4</a>
  <a href="https://arxiv.org/pdf/2505.12312.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12312v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12312v4', 'Visuospatial Cognitive Assistant')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Feng

**分类**: cs.CV, cs.AI, cs.CL, cs.LG, cs.RO

**发布日期**: 2025-05-18 (更新: 2025-09-09)

**备注**: 31 pages, 10 figures, 6 tables

---

## 💡 一句话要点

**提出ViCA以解决视频基础空间认知挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频基础空间认知` `视觉语言模型` `复杂推理` `数据集构建` `机器人导航` `增强现实` `智能家居` `空间推理`

## 📋 核心要点

1. 当前的视觉语言模型在处理视频基础空间认知时面临挑战，尤其是在复杂推理和3D元数据查询方面。
2. 本文提出了ViCA-322K数据集和ViCA-7B模型，前者提供了丰富的问答对，后者在多项任务上实现了性能突破。
3. ViCA-7B在VSI-Bench任务上超越了现有模型，特别是在绝对距离上提升了26.1，展示了其优越的推理能力。

## 📝 摘要（中文）

视频基础的空间认知对于机器人和具身人工智能至关重要，但对现有的视觉语言模型（VLMs）提出了挑战。本文的两项关键贡献首先是引入ViCA-322K，这是一个包含322,003个来自真实室内视频的问答对的数据集，提供了对3D元数据驱动查询和视频基础复杂推理的监督。其次，我们开发了ViCA-7B，在ViCA-322K上进行微调，在所有八个VSI-Bench任务上实现了新的最先进水平，超越了现有模型，包括更大的模型（例如，在绝对距离上提升了26.1）。为了提高可解释性，我们提出了ViCA-Thinking-2.68K，一个包含明确推理链的数据集，并微调ViCA-7B以创建ViCA-7B-Thinking，一个能够阐述其空间推理的模型。我们的工作强调了针对性数据的重要性，并提出了改进时间-空间建模的路径。我们发布所有资源以促进稳健的视觉空间智能研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言模型在视频基础空间认知和复杂推理中的不足，尤其是在处理3D元数据查询时的挑战。

**核心思路**：通过构建ViCA-322K数据集，提供丰富的问答对，结合ViCA-7B模型的微调，提升模型在空间推理任务中的表现。

**技术框架**：整体架构包括数据集构建、模型训练和推理链生成三个主要模块。数据集提供了多样化的问答对，模型则在此基础上进行微调以优化性能。

**关键创新**：最重要的创新在于ViCA-322K数据集的构建和ViCA-7B模型的设计，使其在空间推理任务上超越了现有的视觉语言模型。

**关键设计**：在模型训练中，采用了特定的损失函数和网络结构设计，以确保模型能够有效地进行空间推理和生成明确的推理链。

## 📊 实验亮点

ViCA-7B在所有八个VSI-Bench任务上实现了新的最先进水平，特别是在绝对距离任务上提升了26.1，显著超越了现有的更大模型，展示了其在空间推理方面的卓越性能。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、增强现实和智能家居系统等。通过提升模型在空间认知和推理方面的能力，可以为这些领域提供更为智能和灵活的解决方案，推动具身人工智能的发展。

## 📄 摘要（原文）

> Video-based spatial cognition is vital for robotics and embodied AI but challenges current Vision-Language Models (VLMs). This paper makes two key contributions. First, we introduce ViCA (Visuospatial Cognitive Assistant)-322K, a diverse dataset of 322,003 QA pairs from real-world indoor videos (ARKitScenes, ScanNet, ScanNet++), offering supervision for 3D metadata-grounded queries and video-based complex reasoning. Second, we develop ViCA-7B, fine-tuned on ViCA-322K, which achieves new state-of-the-art on all eight VSI-Bench tasks, outperforming existing models, including larger ones (e.g., +26.1 on Absolute Distance). For interpretability, we present ViCA-Thinking-2.68K, a dataset with explicit reasoning chains, and fine-tune ViCA-7B to create ViCA-7B-Thinking, a model that articulates its spatial reasoning. Our work highlights the importance of targeted data and suggests paths for improved temporal-spatial modeling. We release all resources to foster research in robust visuospatial intelligence.

