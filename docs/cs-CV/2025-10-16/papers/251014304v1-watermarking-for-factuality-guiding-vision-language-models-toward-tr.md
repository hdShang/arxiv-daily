---
layout: default
title: Watermarking for Factuality: Guiding Vision-Language Models Toward Truth via Tri-layer Contrastive Decoding
---

# Watermarking for Factuality: Guiding Vision-Language Models Toward Truth via Tri-layer Contrastive Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14304" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14304v1</a>
  <a href="https://arxiv.org/pdf/2510.14304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14304v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14304v1', 'Watermarking for Factuality: Guiding Vision-Language Models Toward Truth via Tri-layer Contrastive Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kyungryul Back, Seongbeom Park, Milim Kim, Mincheol Kwon, SangHyeok Lee, Hyunyoung Lee, Junhee Cho, Seunghyun Park, Jinkyu Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-16

**备注**: EMNLP 2025 Findings; Project: https://github.com/KR-0822/TCD

---

## 💡 一句话要点

**提出基于水印的三层对比解码方法，提升视觉-语言模型的事实性和视觉 grounding。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `幻觉抑制` `对比解码` `视觉 grounding` `水印技术`

## 📋 核心要点

1. 现有LVLMs易产生幻觉，过度依赖单一模态或记忆数据，缺乏有效的视觉 grounding。
2. 提出三层对比解码方法，利用水印相关问题评估视觉 grounding，指导模型生成更真实的响应。
3. 实验表明，该方法在多个基准测试中显著减少了幻觉，提升了视觉 grounding 性能。

## 📝 摘要（中文）

大型视觉-语言模型（LVLMs）在各种多模态任务上展现出令人鼓舞的结果，在某些情况下甚至达到了与人类相当的性能。然而，LVLMs仍然容易产生幻觉——它们常常过度依赖单一模态或记忆训练数据，而没有适当地 grounding 其输出。为了解决这个问题，我们提出了一种无需训练的、基于水印的三层对比解码方法，该方法包括三个步骤：（1）在解码层中选择一个成熟层和一个初级层；（2）使用与水印相关的问题来识别一个支点层，以评估该层是否具有良好的视觉 grounding；（3）应用三层对比解码来生成最终输出。在POPE、MME和AMBER等公共基准上的实验表明，我们的方法在减少LVLMs中的幻觉方面取得了最先进的性能，并生成了更具有视觉 grounding 的响应。

## 🔬 方法详解

**问题定义**：LVLMs 容易产生幻觉，即生成与输入图像不符或不真实的文本内容。现有方法难以有效提升模型的事实性和视觉 grounding 能力，模型容易过度依赖语言先验或记忆训练数据，忽略视觉信息。

**核心思路**：该论文的核心思路是通过引入水印机制，在解码过程中识别并利用具有良好视觉 grounding 的中间层，从而引导模型生成更符合事实的响应。通过对比不同解码层的输出，突出视觉信息的作用，抑制幻觉的产生。

**技术框架**：该方法包含三个主要步骤：1) **层选择**：在 LVLM 的解码层中选择一个“成熟层”（解码能力较强）和一个“初级层”（解码能力较弱）。2) **支点层识别**：使用与水印相关的问题（例如，询问图像中是否存在水印）来评估每个解码层对视觉信息的理解程度，选择一个“支点层”，该层被认为具有较好的视觉 grounding。3) **三层对比解码**：利用成熟层、初级层和支点层的输出，通过对比解码的方式生成最终的文本响应。

**关键创新**：该方法的主要创新在于：1) 引入水印机制来评估和选择具有良好视觉 grounding 的解码层。2) 提出三层对比解码策略，有效地融合不同解码层的优势，抑制幻觉的产生。3) 该方法是 training-free 的，无需额外的训练数据或参数调整，可以直接应用于现有的 LVLMs。

**关键设计**：具体来说，水印相关问题用于评估每个解码层输出的置信度，置信度最高的层被选为支点层。三层对比解码的具体实现方式未知，论文中可能使用了某种加权平均或选择机制来融合不同层的输出。损失函数未知，但目标是最大化生成文本与视觉信息的关联性，最小化幻觉的产生。

## 📊 实验亮点

该方法在 POPE、MME 和 AMBER 等多个公开基准测试中取得了 state-of-the-art 的性能，显著降低了 LVLMs 的幻觉率，并生成了更具有视觉 grounding 的响应。具体的性能提升数据未知，但摘要中明确指出优于现有方法。

## 🎯 应用场景

该研究成果可广泛应用于需要高可靠性和真实性的视觉-语言任务中，例如图像描述、视觉问答、机器人导航、医疗影像诊断等。通过减少 LVLMs 的幻觉，可以提高这些应用的可信度和实用性，并为未来的多模态人工智能系统奠定基础。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) have recently shown promising results on various multimodal tasks, even achieving human-comparable performance in certain cases. Nevertheless, LVLMs remain prone to hallucinations -- they often rely heavily on a single modality or memorize training data without properly grounding their outputs. To address this, we propose a training-free, tri-layer contrastive decoding with watermarking, which proceeds in three steps: (1) select a mature layer and an amateur layer among the decoding layers, (2) identify a pivot layer using a watermark-related question to assess whether the layer is visually well-grounded, and (3) apply tri-layer contrastive decoding to generate the final output. Experiments on public benchmarks such as POPE, MME and AMBER demonstrate that our method achieves state-of-the-art performance in reducing hallucinations in LVLMs and generates more visually grounded responses.

