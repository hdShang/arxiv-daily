---
layout: default
title: Text-Queried Audio Source Separation via Hierarchical Modeling
---

# Text-Queried Audio Source Separation via Hierarchical Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21025" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21025v2</a>
  <a href="https://arxiv.org/pdf/2505.21025.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21025v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21025v2', 'Text-Queried Audio Source Separation via Hierarchical Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinlei Yin, Xiulian Peng, Xue Jiang, Zhiwei Xiong, Yan Lu

**分类**: cs.SD, cs.AI, cs.LG, eess.AS

**发布日期**: 2025-05-27 (更新: 2025-12-02)

**备注**: Accepted by TASLP

---

## 💡 一句话要点

**提出HSM-TSS框架以解决文本查询音频源分离问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `音频源分离` `文本查询` `跨模态学习` `分层模型` `语义感知`

## 📋 核心要点

1. 现有方法在声学与文本对齐及语义感知分离方面存在建模困难，且依赖大量标注数据。
2. 本文提出HSM-TSS框架，通过全局与局部语义特征分离，解决音频源分离问题。
3. 实验结果显示，HSM-TSS在数据效率和语义一致性方面均优于现有方法，达到了最先进的分离性能。

## 📝 摘要（中文）

基于自然语言查询的目标音频源分离为通过任意文本描述提取音频事件提供了新思路。现有方法面临两个主要挑战：一是难以在单阶段架构中有效建模声学与文本的对齐及语义感知分离，二是依赖大规模准确标注的训练数据以弥补跨模态学习与分离的低效。为此，本文提出了一种分层解构框架HSM-TSS，将任务分解为全局-局部语义引导的特征分离与结构保持的声学重构。该方法引入双阶段机制，分别在全局和局部语义特征空间中进行语义分离，最终在复杂的听觉场景中实现了优越的分离性能与语义一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决基于文本查询的音频源分离问题。现有方法在声学与文本的对齐及语义感知分离方面存在困难，且通常依赖大量准确标注的数据，导致跨模态学习效率低下。

**核心思路**：本文提出的HSM-TSS框架通过分层解构，将音频源分离任务分为全局和局部语义特征的分离，利用双阶段机制提高分离效果。这样的设计使得模型能够更好地处理复杂的听觉场景。

**技术框架**：HSM-TSS框架包括两个主要阶段：首先在全局语义特征空间中进行全局语义分离，使用Q-Audio架构对音频和文本模态进行对齐；接着，基于预测的全局特征，在AudioMAE特征上进行局部语义分离，并进行声学重构。

**关键创新**：HSM-TSS的主要创新在于引入了双阶段的语义分离机制，能够在不同的语义特征空间中进行操作，从而实现更高效的音频源分离。这一方法与现有单阶段架构的本质区别在于其分层处理的能力。

**关键设计**：在模型设计中，采用了Q-Audio架构作为全局语义编码器，确保音频与文本的有效对齐。此外，局部语义分离阶段使用AudioMAE特征以保持时间-频率结构，增强了声学重构的质量。

## 📊 实验亮点

实验结果表明，HSM-TSS在音频源分离任务中达到了最先进的性能，尤其在复杂听觉场景中，分离效果显著优于基线方法，具体性能提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

该研究在音频处理、音乐制作、虚拟现实和增强现实等领域具有广泛的应用潜力。通过灵活的声音操控能力，用户可以根据文本描述进行音频事件的提取和修改，提升了用户体验和创作自由度。

## 📄 摘要（原文）

> Target audio source separation with natural language queries presents a promising paradigm for extracting arbitrary audio events through arbitrary text descriptions. Existing methods mainly face two challenges, the difficulty in jointly modeling acoustic-textual alignment and semantic-aware separation within a blindly-learned single-stage architecture, and the reliance on large-scale accurately-labeled training data to compensate for inefficient cross-modal learning and separation. To address these challenges, we propose a hierarchical decomposition framework, HSM-TSS, that decouples the task into global-local semantic-guided feature separation and structure-preserving acoustic reconstruction. Our approach introduces a dual-stage mechanism for semantic separation, operating on distinct global and local semantic feature spaces. We first perform global-semantic separation through a global semantic feature space aligned with text queries. A Q-Audio architecture is employed to align audio and text modalities, serving as pretrained global-semantic encoders. Conditioned on the predicted global feature, we then perform the second-stage local-semantic separation on AudioMAE features that preserve time-frequency structures, followed by acoustic reconstruction. We also propose an instruction processing pipeline to parse arbitrary text queries into structured operations, extraction or removal, coupled with audio descriptions, enabling flexible sound manipulation. Our method achieves state-of-the-art separation performance with data-efficient training while maintaining superior semantic consistency with queries in complex auditory scenes.

