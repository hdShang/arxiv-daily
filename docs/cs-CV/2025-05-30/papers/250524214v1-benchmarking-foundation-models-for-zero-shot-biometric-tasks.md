---
layout: default
title: Benchmarking Foundation Models for Zero-Shot Biometric Tasks
---

# Benchmarking Foundation Models for Zero-Shot Biometric Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24214" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24214v1</a>
  <a href="https://arxiv.org/pdf/2505.24214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24214v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24214v1', 'Benchmarking Foundation Models for Zero-Shot Biometric Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Redwan Sony, Parisa Farmanifard, Hamzeh Alzwairy, Nitish Shukla, Arun Ross

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出基于基础模型的零-shot生物识别任务基准评估**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基础模型` `生物识别` `零-shot学习` `多模态模型` `深度伪造检测` `虹膜识别` `面部验证`

## 📋 核心要点

1. 现有的生物识别技术在利用基础模型进行零-shot任务时面临挑战，尤其是在缺乏标注数据的情况下。
2. 本研究提出了一个基准评估框架，系统评估VLMs和MLLMs在多种生物识别任务中的性能，展示其在零-shot和少量样本条件下的有效性。
3. 实验结果显示，基础模型的嵌入在多项生物识别任务中表现出色，尤其是在面部验证和虹膜识别任务中，均未经过微调即可达到高准确率。

## 📝 摘要（中文）

基础模型的出现，尤其是视觉-语言模型（VLMs）和多模态大型语言模型（MLLMs），重新定义了人工智能的前沿，能够在多样化任务中实现显著的泛化能力，且几乎无需监督。然而，它们在生物识别和分析中的潜力尚未得到充分探索。本研究引入了一个全面的基准，评估了41个最先进的VLMs和MLLMs在六个生物识别任务中的零-shot和少量样本性能，包括面部验证、软生物特征属性预测（性别和种族）、虹膜识别、呈现攻击检测（PAD）和面部操控检测（如变形和深度伪造）。实验结果表明，这些基础模型的嵌入可以用于多种生物识别任务，且在面部验证中，未经过微调的情况下，在LFW数据集上获得了96.77%的真实匹配率（TMR），在虹膜识别中，IITD-R-Full数据集上TMR为97.55%。

## 🔬 方法详解

**问题定义**：本研究旨在解决基础模型在生物识别任务中的应用不足，尤其是在零-shot和少量样本情况下的性能评估。现有方法通常依赖于大量标注数据，限制了其在实际应用中的灵活性。

**核心思路**：本研究通过引入一个全面的基准评估框架，系统性地评估多种VLMs和MLLMs在生物识别任务中的表现，展示其在缺乏监督的情况下的潜力。

**技术框架**：整体架构包括数据集选择、模型嵌入提取、任务定义和性能评估四个主要模块。研究者使用41个VLMs进行实验，涵盖面部和虹膜等多个生物识别任务。

**关键创新**：最重要的创新在于首次系统性地评估基础模型在生物识别领域的零-shot能力，展示了其在多个任务中的有效性，与传统方法相比，显著降低了对标注数据的依赖。

**关键设计**：在实验中，采用了简单的分类器头来处理嵌入，进行深度伪造检测、虹膜的PAD和面部的软生物特征提取，确保了高准确率的同时，保持了模型的简洁性。

## 📊 实验亮点

实验结果显示，在面部验证任务中，未经过微调的情况下，在LFW数据集上获得了96.77%的真实匹配率（TMR），在虹膜识别任务中，IITD-R-Full数据集上TMR为97.55%。这些结果表明基础模型在生物识别任务中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括安全监控、身份验证和社交媒体内容审核等。通过利用基础模型的强大能力，可以在缺乏大量标注数据的情况下，提升生物识别系统的准确性和可靠性，推动人工智能在生物识别领域的应用发展。

## 📄 摘要（原文）

> The advent of foundation models, particularly Vision-Language Models (VLMs) and Multi-modal Large Language Models (MLLMs), has redefined the frontiers of artificial intelligence, enabling remarkable generalization across diverse tasks with minimal or no supervision. Yet, their potential in biometric recognition and analysis remains relatively underexplored. In this work, we introduce a comprehensive benchmark that evaluates the zero-shot and few-shot performance of state-of-the-art publicly available VLMs and MLLMs across six biometric tasks spanning the face and iris modalities: face verification, soft biometric attribute prediction (gender and race), iris recognition, presentation attack detection (PAD), and face manipulation detection (morphs and deepfakes). A total of 41 VLMs were used in this evaluation. Experiments show that embeddings from these foundation models can be used for diverse biometric tasks with varying degrees of success. For example, in the case of face verification, a True Match Rate (TMR) of 96.77 percent was obtained at a False Match Rate (FMR) of 1 percent on the Labeled Face in the Wild (LFW) dataset, without any fine-tuning. In the case of iris recognition, the TMR at 1 percent FMR on the IITD-R-Full dataset was 97.55 percent without any fine-tuning. Further, we show that applying a simple classifier head to these embeddings can help perform DeepFake detection for faces, Presentation Attack Detection (PAD) for irides, and extract soft biometric attributes like gender and ethnicity from faces with reasonably high accuracy. This work reiterates the potential of pretrained models in achieving the long-term vision of Artificial General Intelligence.

