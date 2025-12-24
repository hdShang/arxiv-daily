---
layout: default
title: "TAViS: Text-bridged Audio-Visual Segmentation with Foundation Models"
---

# TAViS: Text-bridged Audio-Visual Segmentation with Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11436" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11436v2</a>
  <a href="https://arxiv.org/pdf/2506.11436.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11436v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11436v2', 'TAViS: Text-bridged Audio-Visual Segmentation with Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyang Luo, Nian Liu, Xuguang Yang, Salman Khan, Rao Muhammad Anwer, Hisham Cholakkal, Fahad Shahbaz Khan, Junwei Han

**分类**: cs.CV

**发布日期**: 2025-06-13 (更新: 2025-12-10)

**备注**: ICCV2025,code:https://github.com/Sssssuperior/TAViS

---

## 💡 一句话要点

**提出TAViS以解决音视频分割中的跨模态对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音视频分割` `跨模态对齐` `多模态学习` `文本桥接` `基础模型` `深度学习`

## 📋 核心要点

1. 现有音视频分割方法在跨模态对齐上存在不足，无法有效结合音频和视觉信息。
2. 本文提出的TAViS框架通过文本桥接设计，结合多模态基础模型和分割模型，实现音视频的精确分割和对齐。
3. 实验结果显示，TAViS在多个数据集上表现优异，尤其在零样本设置中显著提升了性能。

## 📝 摘要（中文）

音视频分割（AVS）面临有效对齐音频和视觉模态的基本挑战。尽管近期方法利用基础模型来应对数据稀缺问题，但往往依赖单一模态知识或以现成方式结合基础模型，未能有效解决跨模态对齐问题。本文提出了TAViS，一个新颖的框架，通过结合多模态基础模型（ImageBind）和分割基础模型（SAM2）来实现跨模态对齐和精确分割。为了解决模型间知识转移的困难和仅使用分割损失进行监督的不足，本文引入了文本桥接设计，包含伪文本提供类别原型信息和对齐监督策略。我们的方案在单源、多源和语义数据集上表现优异，并在零样本设置中表现突出。

## 🔬 方法详解

**问题定义**：本文旨在解决音视频分割中的跨模态对齐问题。现有方法往往依赖单一模态知识，未能有效整合音频与视觉信息，导致分割精度不足。

**核心思路**：论文提出的TAViS框架通过文本桥接设计，利用伪文本提供类别原型信息，同时保留音频和视觉输入的模态特征，从而实现更好的跨模态对齐与分割。

**技术框架**：TAViS框架主要包括两个模块：文本桥接混合提示机制和对齐监督策略。前者通过伪文本提供类别信息，后者利用文本对音视频模态进行对齐。

**关键创新**：TAViS的核心创新在于引入文本作为桥梁，解决了不同特征空间间的知识转移问题，并通过对齐监督策略提升了模型的整体性能。

**关键设计**：在模型设计中，采用了混合提示机制和对齐监督策略，确保了音频和视觉模态的有效结合。此外，损失函数的设计也考虑了多模态特征的对齐，增强了模型的学习能力。

## 📊 实验亮点

TAViS在多个数据集上均表现出色，尤其在零样本设置中，相较于基线方法，性能提升显著，具体提升幅度达到XX%。该方法在单源和多源数据集上均实现了优于现有技术的分割精度。

## 🎯 应用场景

该研究的潜在应用领域包括视频监控、自动驾驶、虚拟现实等场景，能够提升系统对复杂环境中音视频信息的理解和处理能力。未来，TAViS可能在多模态交互和智能助手等领域发挥重要作用，推动相关技术的发展。

## 📄 摘要（原文）

> Audio-Visual Segmentation (AVS) faces a fundamental challenge of effectively aligning audio and visual modalities. While recent approaches leverage foundation models to address data scarcity, they often rely on single-modality knowledge or combine foundation models in an off-the-shelf manner, failing to address the cross-modal alignment challenge. In this paper, we present TAViS, a novel framework that \textbf{couples} the knowledge of multimodal foundation models (ImageBind) for cross-modal alignment and a segmentation foundation model (SAM2) for precise segmentation. However, effectively combining these models poses two key challenges: the difficulty in transferring the knowledge between SAM2 and ImageBind due to their different feature spaces, and the insufficiency of using only segmentation loss for supervision. To address these challenges, we introduce a text-bridged design with two key components: (1) a text-bridged hybrid prompting mechanism where pseudo text provides class prototype information while retaining modality-specific details from both audio and visual inputs, and (2) an alignment supervision strategy that leverages text as a bridge to align shared semantic concepts within audio-visual modalities. Our approach achieves superior performance on single-source, multi-source, semantic datasets, and excels in zero-shot settings.

