---
layout: default
title: Visual Representations inside the Language Model
---

# Visual Representations inside the Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04819" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04819v1</a>
  <a href="https://arxiv.org/pdf/2510.04819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04819v1" onclick="toggleFavorite(this, '2510.04819v1', 'Visual Representations inside the Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benlin Liu, Amita Kamath, Madeleine Grunde-McLaughlin, Winson Han, Ranjay Krishna

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-06

**备注**: Accepted to COLM 2025

---

## 💡 一句话要点

**分析多模态大语言模型内部视觉表征，揭示其感知能力瓶颈与改进方向**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉表征` `键值tokens` `感知能力` `可解释性`

## 📋 核心要点

1. 多模态大语言模型在感知任务上表现不佳，现有研究缺乏对其内部视觉表征的深入理解。
2. 通过分析视觉键值tokens在语言模型中的流动，揭示视觉信息在模型内部的处理方式和潜在瓶颈。
3. 实验表明，图像值tokens包含足够的感知信息，但语言模型对视觉信息的处理存在改进空间，例如通过文本前缀控制视觉信息。

## 📝 摘要（中文）

尽管已有大量工作分析视觉Transformer编码器和Transformer激活，我们仍然不清楚多模态大语言模型(MLM)在感知密集型任务上表现不佳的原因。本文通过研究主流MLM(LLaVA-OneVision, Qwen2.5-VL, Llama-3-LLaVA-NeXT)如何处理其视觉键值(key-value)tokens，提供了一个新的视角。我们首先研究视觉信息在语言模型中的流动，发现图像值tokens编码了足够的信息来零样本执行多个感知密集型任务：分割、语义对应、时间对应和指代表达式检测。我们发现，虽然语言模型确实增强了来自输入视觉编码投影的视觉信息（我们揭示这与MLM的整体感知能力相关），但它在几个任务上包含的视觉信息少于未经MLM微调的等效视觉编码器(SigLIP)。此外，我们发现语言模型后期层中与输入无关的图像键tokens对应的视觉信息包含降低整体MLM感知能力的人工痕迹。接下来，我们讨论控制语言模型中的视觉信息，表明向图像输入添加文本前缀可以提高视觉表征的感知能力。最后，我们揭示，如果语言模型能够更好地控制其视觉信息，它们的感知能力将显著提高；例如，在BLINK基准测试中33.3%的艺术风格问题中，语言模型中存在的感知信息没有传递到输出！我们的发现揭示了键值tokens在多模态系统中的作用，为MLM的更深层次的机制可解释性铺平了道路，并为训练其视觉编码器和语言模型组件提出了新的方向。

## 🔬 方法详解

**问题定义**：多模态大语言模型(MLM)在处理感知密集型任务时表现不佳，例如图像分割、语义对应等。现有的研究主要集中在视觉编码器和Transformer激活的分析，缺乏对语言模型内部如何处理视觉信息的深入理解，特别是视觉键值(key-value)tokens的作用。

**核心思路**：本文的核心思路是通过分析MLM内部视觉键值tokens所包含的视觉信息，来理解MLM在感知任务上的瓶颈。通过比较MLM内部视觉表征与原始视觉编码器的表征，以及研究不同层级的键值tokens，揭示视觉信息在语言模型中的流动和变化。

**技术框架**：本文的研究框架主要包括以下几个步骤：1) 选择主流的MLM模型，如LLaVA-OneVision, Qwen2.5-VL, Llama-3-LLaVA-NeXT；2) 分析视觉键值tokens在语言模型不同层级的激活；3) 使用零样本方式在感知任务上评估视觉表征的性能，包括分割、语义对应、时间对应和指代表达式检测；4) 比较MLM内部视觉表征与原始视觉编码器(SigLIP)的表征；5) 研究文本前缀对视觉表征的影响。

**关键创新**：本文最重要的技术创新点在于，它提供了一种新的视角来理解MLM的感知能力，即通过分析语言模型内部的视觉表征。与以往主要关注视觉编码器和Transformer激活的研究不同，本文深入研究了视觉键值tokens在语言模型中的作用，揭示了视觉信息在语言模型中的流动和变化，以及潜在的瓶颈。

**关键设计**：本文的关键设计包括：1) 选择具有代表性的MLM模型；2) 使用零样本方式评估视觉表征的性能，避免了微调带来的偏差；3) 比较MLM内部视觉表征与原始视觉编码器的表征，可以更清晰地了解语言模型对视觉信息的影响；4) 研究文本前缀对视觉表征的影响，探索控制视觉信息的方法。

## 📊 实验亮点

研究发现，图像值tokens包含足够的感知信息，可以零样本执行分割、语义对应等任务。同时，语言模型对视觉信息的处理存在改进空间，例如添加文本前缀可以提高视觉表征的感知能力。在BLINK基准测试中，33.3%的艺术风格问题中，语言模型中存在的感知信息没有传递到输出，表明模型对视觉信息的控制能力有待提高。

## 🎯 应用场景

该研究成果可应用于提升多模态大语言模型在视觉感知任务上的性能，例如图像理解、视频分析、机器人导航等。通过更好地控制和利用语言模型中的视觉信息，可以开发出更智能、更可靠的多模态人工智能系统，应用于自动驾驶、智能家居、医疗诊断等领域。

## 📄 摘要（原文）

> Despite interpretability work analyzing VIT encoders and transformer activations, we don't yet understand why Multimodal Language Models (MLMs) struggle on perception-heavy tasks. We offer an under-studied perspective by examining how popular MLMs (LLaVA-OneVision, Qwen2.5-VL, and Llama-3-LLaVA-NeXT) process their visual key-value tokens. We first study the flow of visual information through the language model, finding that image value tokens encode sufficient information to perform several perception-heavy tasks zero-shot: segmentation, semantic correspondence, temporal correspondence, and referring expression detection. We find that while the language model does augment the visual information received from the projection of input visual encodings-which we reveal correlates with overall MLM perception capability-it contains less visual information on several tasks than the equivalent visual encoder (SigLIP) that has not undergone MLM finetuning. Further, we find that the visual information corresponding to input-agnostic image key tokens in later layers of language models contains artifacts which reduce perception capability of the overall MLM. Next, we discuss controlling visual information in the language model, showing that adding a text prefix to the image input improves perception capabilities of visual representations. Finally, we reveal that if language models were able to better control their visual information, their perception would significantly improve; e.g., in 33.3% of Art Style questions in the BLINK benchmark, perception information present in the language model is not surfaced to the output! Our findings reveal insights into the role of key-value tokens in multimodal systems, paving the way for deeper mechanistic interpretability of MLMs and suggesting new directions for training their visual encoder and language model components.

