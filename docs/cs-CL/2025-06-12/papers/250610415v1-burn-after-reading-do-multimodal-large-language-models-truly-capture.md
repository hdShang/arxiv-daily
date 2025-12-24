---
layout: default
title: "Burn After Reading: Do Multimodal Large Language Models Truly Capture Order of Events in Image Sequences?"
---

# Burn After Reading: Do Multimodal Large Language Models Truly Capture Order of Events in Image Sequences?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10415" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10415v1</a>
  <a href="https://arxiv.org/pdf/2506.10415.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10415v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10415v1', 'Burn After Reading: Do Multimodal Large Language Models Truly Capture Order of Events in Image Sequences?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingjin Song, Yupei Du, Denis Paperno, Albert Gatt

**分类**: cs.CL, cs.CV

**发布日期**: 2025-06-12

**备注**: 27 pages, 14 figures. Accepted to ACL 2025

**🔗 代码/项目**: [GITHUB](https://github.com/yjsong22/TempVS)

---

## 💡 一句话要点

**提出TempVS基准以评估多模态大语言模型的事件顺序理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `时间推理` `事件关系推理` `图像序列理解` `基准测试`

## 📋 核心要点

1. 现有的多模态大语言模型在理解图像序列中的事件顺序方面存在显著不足，无法有效推理事件之间的关系。
2. 论文提出了TempVS基准，通过事件关系推理、句子排序和图像排序等测试，评估MLLMs的时间理解能力。
3. 实验结果显示，38种最先进的MLLMs在TempVS基准上的表现远低于人类，揭示了模型在时间推理方面的不足。

## 📝 摘要（中文）

本文介绍了TempVS基准，专注于多模态大语言模型（MLLMs）在图像序列中的时间基础和推理能力。TempVS包含三个主要测试（事件关系推理、句子排序和图像排序），每个测试都附带基本的基础测试。该基准要求MLLMs依赖视觉和语言两种模态来理解事件的时间顺序。我们评估了38种最先进的MLLMs，结果显示这些模型在解决TempVS时表现不佳，与人类能力相比存在显著的性能差距。我们还提供了细致的见解，指出未来研究的有希望方向。TempVS基准数据和代码可在https://github.com/yjsong22/TempVS获取。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在图像序列中理解事件顺序的能力不足。现有方法在时间推理和事件关系理解上存在显著挑战，导致模型性能低下。

**核心思路**：论文提出TempVS基准，要求模型同时利用视觉和语言信息来进行时间顺序的理解和推理。通过设计多种测试，评估模型在不同任务中的表现。

**技术框架**：TempVS基准包括三个主要测试模块：事件关系推理、句子排序和图像排序，每个模块都有基础的时间理解测试。这些模块共同构成了评估MLLMs时间推理能力的整体框架。

**关键创新**：TempVS基准的设计是本研究的核心创新，提供了一个系统化的评估方式，填补了现有多模态模型在时间推理能力评估方面的空白。

**关键设计**：在测试设计中，采用了多样化的事件关系和排序任务，确保模型在不同情境下的表现得到全面评估。具体的参数设置和损失函数设计尚未详细披露，需进一步研究。

## 📊 实验亮点

实验结果表明，38种最先进的多模态大语言模型在TempVS基准上的平均表现显著低于人类，显示出在事件顺序理解方面的明显不足。这一发现强调了当前模型在时间推理能力上的局限性，为未来的研究指明了方向。

## 🎯 应用场景

该研究的潜在应用领域包括视频理解、智能监控和人机交互等。通过提升多模态大语言模型在时间推理方面的能力，可以显著改善这些领域的智能系统表现，推动相关技术的进步与应用。未来，TempVS基准可能成为多模态模型研究的重要参考标准。

## 📄 摘要（原文）

> This paper introduces the TempVS benchmark, which focuses on temporal grounding and reasoning capabilities of Multimodal Large Language Models (MLLMs) in image sequences. TempVS consists of three main tests (i.e., event relation inference, sentence ordering and image ordering), each accompanied with a basic grounding test. TempVS requires MLLMs to rely on both visual and linguistic modalities to understand the temporal order of events. We evaluate 38 state-of-the-art MLLMs, demonstrating that models struggle to solve TempVS, with a substantial performance gap compared to human capabilities. We also provide fine-grained insights that suggest promising directions for future research. Our TempVS benchmark data and code are available at https://github.com/yjsong22/TempVS.

