---
layout: default
title: "Beyond the Visible: Benchmarking Occlusion Perception in Multimodal Large Language Models"
---

# Beyond the Visible: Benchmarking Occlusion Perception in Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04059" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04059v1</a>
  <a href="https://arxiv.org/pdf/2508.04059.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04059v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04059v1', 'Beyond the Visible: Benchmarking Occlusion Perception in Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaochen Liu, Kaiwen Gao, Shuyi Liang, Bin Xiao, Limeng Qiao, Lin Ma, Tingting Jiang

**分类**: cs.CV

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出O-Bench以解决多模态大语言模型的遮挡感知问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遮挡感知` `多模态大语言模型` `视觉问答` `数据集构建` `性能评估` `空间理解` `智能机器人`

## 📋 核心要点

1. 现有多模态大语言模型在遮挡感知方面的表现尚未得到充分研究，存在显著的性能差距。
2. 本文提出O-Bench基准，专门设计用于评估遮挡感知，构建了包含1,365幅图像和4,588个问答对的数据集。
3. 对22个MLLMs的评估结果显示，当前模型在遮挡感知任务上无法与人类水平相媲美，且存在多种失效模式。

## 📝 摘要（中文）

遮挡感知是人类空间理解的重要基础，涉及视觉识别与推理的整合。尽管多模态大语言模型（MLLMs）展现出显著能力，但其在遮挡感知上的表现仍未得到充分探索。为此，本文提出了O-Bench，这是首个专门针对遮挡感知的视觉问答基准。基于SA-1B，我们通过新颖的分层合成方法构建了1,365幅具有语义一致的遮挡场景图像，并注释了4,588个问答对。对22个代表性MLLMs的评估显示，当前模型与人类之间存在显著性能差距，且无法通过模型扩展或思维过程弥补。我们还识别出三种典型失效模式，包括过于保守的偏见、脆弱的整体预测和对定量任务的困难。我们相信O-Bench不仅能为遮挡感知提供重要的评估工具，还能激励MLLMs在视觉智能方面的进一步发展。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在遮挡感知任务中的不足，现有方法在处理遮挡场景时表现不佳，无法有效整合视觉信息与推理能力。

**核心思路**：论文提出O-Bench基准，通过构建具有语义一致性的遮挡场景图像，来系统性地评估和提升MLLMs在遮挡感知方面的能力。

**技术框架**：O-Bench基于SA-1B数据集，采用分层合成方法生成图像，并通过半自动化工作流程注释问答对，形成完整的评估体系。

**关键创新**：O-Bench是首个专门针对遮挡感知的视觉问答基准，填补了现有评估工具的空白，提供了系统化的评估标准。

**关键设计**：在数据构建中，采用了分层合成技术，确保生成图像的语义一致性；问答对的注释则通过可靠的半自动化流程完成，保证了数据的质量和多样性。

## 📊 实验亮点

实验结果显示，22个代表性MLLMs在遮挡感知任务上的表现与人类基线存在显著差距，无法通过简单的模型扩展来弥补。具体而言，模型在处理遮挡场景时表现出过于保守的偏见和对定量任务的困难，揭示了当前技术的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、增强现实等，需要高水平空间理解和视觉推理的场景。O-Bench的发布将推动多模态大语言模型在遮挡感知方面的研究，提升其在复杂环境中的应用能力。

## 📄 摘要（原文）

> Occlusion perception, a critical foundation for human-level spatial understanding, embodies the challenge of integrating visual recognition and reasoning. Though multimodal large language models (MLLMs) have demonstrated remarkable capabilities, their performance on occlusion perception remains under-explored. To address this gap, we introduce O-Bench, the first visual question answering (VQA) benchmark specifically designed for occlusion perception. Based on SA-1B, we construct 1,365 images featuring semantically coherent occlusion scenarios through a novel layered synthesis approach. Upon this foundation, we annotate 4,588 question-answer pairs in total across five tailored tasks, employing a reliable, semi-automatic workflow. Our extensive evaluation of 22 representative MLLMs against the human baseline reveals a significant performance gap between current MLLMs and humans, which, we find, cannot be sufficiently bridged by model scaling or thinking process. We further identify three typical failure patterns, including an overly conservative bias, a fragile gestalt prediction, and a struggle with quantitative tasks. We believe O-Bench can not only provide a vital evaluation tool for occlusion perception, but also inspire the development of MLLMs for better visual intelligence. Our benchmark will be made publicly available upon paper publication.

