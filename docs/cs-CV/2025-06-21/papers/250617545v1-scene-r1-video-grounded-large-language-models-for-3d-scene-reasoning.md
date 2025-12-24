---
layout: default
title: "Scene-R1: Video-Grounded Large Language Models for 3D Scene Reasoning without 3D Annotations"
---

# Scene-R1: Video-Grounded Large Language Models for 3D Scene Reasoning without 3D Annotations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17545" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17545v1</a>
  <a href="https://arxiv.org/pdf/2506.17545.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17545v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17545v1', 'Scene-R1: Video-Grounded Large Language Models for 3D Scene Reasoning without 3D Annotations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Yuan, Shuyi Jiang, Chun-Mei Feng, Yaolun Zhang, Shuguang Cui, Zhen Li, Na Zhao

**分类**: cs.CV

**发布日期**: 2025-06-21

---

## 💡 一句话要点

**提出Scene-R1以解决无3D标注的3D场景推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D场景推理` `视频理解` `强化学习` `无监督学习` `多模态融合` `视觉问答` `模型透明性`

## 📋 核心要点

1. 现有的3D感知大型语言模型缺乏透明性，无法揭示决策过程，并依赖于预训练的3D检测器提供物体提议。
2. 本文提出Scene-R1框架，通过强化学习驱动的推理与两阶段的基础定位管道，学习在无3D标注的情况下进行3D场景推理。
3. Scene-R1在多个数据集上超越现有基线，提供透明的推理过程，展示了其在3D视觉问答任务中的有效性。

## 📝 摘要（中文）

目前，利用大型语言模型理解3D世界的研究逐渐增多。然而，现有的3D感知大型语言模型往往作为黑箱运作，输出边界框或文本答案，却无法揭示决策过程，并且依赖于预训练的3D检测器提供物体提议。本文提出了Scene-R1，这是一个视频驱动的框架，通过结合强化学习驱动的推理与两阶段的基础定位管道，学习在没有点位3D实例监督的情况下进行3D场景推理。在时间基础定位阶段，明确推理视频并选择与开放式查询最相关的视频片段。在后续的图像基础定位阶段，分析图像并预测2D边界框。最终，通过SAM2跟踪对象，生成RGB帧中的像素精确掩码，并将其投影回3D，从而消除了对基于3D检测器的提议的需求，同时捕捉细致的几何和材料线索。Scene-R1还可以适应3D视觉问答任务，直接回答来自视频的自由形式问题。我们的训练管道只需要任务级的2D框或文本标签，而无需密集的3D点位标签。Scene-R1在多个数据集上超越现有的开放词汇基线，同时提供透明的逐步推理。这些结果表明，基于强化学习的推理结合RGB-D视频提供了一条实用的、注释高效的可信3D场景理解路径。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D感知大型语言模型在推理过程中的不透明性及对3D检测器的依赖问题。现有方法往往无法提供清晰的决策依据，并且需要密集的3D标注数据。

**核心思路**：Scene-R1通过结合强化学习与两阶段的基础定位管道，能够在没有点位3D实例监督的情况下进行3D场景推理。该设计旨在提高推理的透明度和效率，同时减少对复杂标注的需求。

**技术框架**：Scene-R1的整体架构包括两个主要阶段：时间基础定位阶段和图像基础定位阶段。在时间基础定位阶段，系统分析视频并选择与查询相关的片段；在图像基础定位阶段，系统分析选定的图像并预测2D边界框。

**关键创新**：Scene-R1的主要创新在于其无须依赖3D检测器的物体提议，能够直接从RGB-D视频中提取信息，捕捉细致的几何和材料线索。这一方法显著提高了推理的准确性和效率。

**关键设计**：在训练过程中，Scene-R1仅需任务级的2D框或文本标签，而不需要密集的3D点位标签。该方法使用强化学习优化推理过程，确保了模型在不同任务中的适应性和表现。

## 📊 实验亮点

在多个数据集上，Scene-R1超越了现有的开放词汇基线，展示了其在3D场景推理中的有效性。具体而言，该模型在推理透明度和准确性方面均有显著提升，提供了逐步的推理过程，增强了用户对模型决策的信任。

## 🎯 应用场景

Scene-R1的研究成果在多个领域具有广泛的应用潜力，包括自动驾驶、虚拟现实和增强现实等场景理解任务。通过提供高效且透明的3D场景推理能力，该框架能够为智能系统提供更可靠的环境理解，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Currently, utilizing large language models to understand the 3D world is becoming popular. Yet existing 3D-aware LLMs act as black boxes: they output bounding boxes or textual answers without revealing how those decisions are made, and they still rely on pre-trained 3D detectors to supply object proposals. We introduce Scene-R1, a video-grounded framework that learns to reason about 3D scenes without any point-wise 3D instance supervision by pairing reinforcement-learning-driven reasoning with a two-stage grounding pipeline. In the temporal grounding stage, we explicitly reason about the video and select the video snippets most relevant to an open-ended query. In the subsequent image grounding stage, we analyze the image and predict the 2D bounding box. After that, we track the object using SAM2 to produce pixel-accurate masks in RGB frames, and project them back into 3D, thereby eliminating the need for 3D detector-based proposals while capturing fine geometry and material cues. Scene-R1 can also adapt to the 3D visual question answering task to answer free-form questions directly from video. Our training pipeline only needs task-level 2D boxes or textual labels without dense 3D point-wise labels. Scene-R1 surpasses existing open-vocabulary baselines on multiple datasets, while delivering transparent, step-by-step rationales. These results show that reinforcement-learning-based reasoning combined with RGB-D video alone offers a practical, annotation-efficient route to trustworthy 3D scene understanding.

