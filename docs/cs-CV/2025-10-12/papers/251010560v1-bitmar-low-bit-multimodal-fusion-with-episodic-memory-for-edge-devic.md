---
layout: default
title: BitMar: Low-Bit Multimodal Fusion with Episodic Memory for Edge Devices
---

# BitMar: Low-Bit Multimodal Fusion with Episodic Memory for Edge Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10560" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10560v1</a>
  <a href="https://arxiv.org/pdf/2510.10560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10560v1" onclick="toggleFavorite(this, '2510.10560v1', 'BitMar: Low-Bit Multimodal Fusion with Episodic Memory for Edge Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Euhid Aman, Esteban Carlin, Hsing-Kuo Pao, Giovanni Beltrame, Ghaluh Indah Permata Sari, Yie-Tarng Chen

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-10-12

**备注**: 6 pages, BabyLM Workshop, EMNLP 2025

---

## 💡 一句话要点

**BitMar：面向边缘设备的低比特多模态融合与情景记忆模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `边缘计算` `低比特量化` `情景记忆` `图像描述` `BitNet` `Transformer`

## 📋 核心要点

1. 现有跨模态模型计算量大，难以在边缘设备上部署，限制了其应用范围。
2. BitMar提出一种量化的多模态Transformer，利用低比特编码器和情景记忆，降低计算和存储需求。
3. 实验表明，BitMar在低延迟和小模型体积下，实现了具有竞争力的图像描述和多模态理解性能。

## 📝 摘要（中文）

跨注意力Transformer和其他多模态视觉-语言模型在对齐和生成任务中表现出色，但其庞大且全精度的骨干网络使其难以部署在边缘设备上。记忆增强架构可以提高过去上下文的利用率，但大多数工作很少将其与面向边缘的激进量化相结合。我们提出了BitMar，一种量化的多模态Transformer，它提出了一种类似人类的外部情景记忆，用于在资源有限的硬件上进行有效的图像-文本生成。BitMar利用1.58比特的编码器，一个用于文本（BitNet风格），一个用于视觉（基于DiNOv2），以创建紧凑的嵌入，这些嵌入被组合并用于查询固定大小的键值情景记忆。在向量检索期间，BitNet解码器应用逐层调节，从而提高生成内容的上下文相关性。解码器还采用带有滑动窗口机制的注意力汇聚，以在严格的内存预算下处理长输入或流式输入。逐层调节和滑动窗口注意力的结合实现了强大的质量-速度权衡，以低延迟和小模型占用空间提供有竞争力的图像描述和多模态理解。这些特性使BitMar非常适合边缘部署。

## 🔬 方法详解

**问题定义**：现有跨模态视觉-语言模型，如基于Transformer的模型，通常具有庞大的参数量和计算复杂度，难以在资源受限的边缘设备上部署。这限制了它们在需要实时响应和本地处理的应用场景中的应用。现有方法通常忽略了模型量化与外部记忆结合，无法在保证性能的同时，有效降低资源消耗。

**核心思路**：BitMar的核心思路是利用低比特量化技术和情景记忆机制，在保证模型性能的同时，显著降低模型的计算复杂度和存储需求。通过低比特编码器提取紧凑的图像和文本嵌入，并利用情景记忆存储和检索相关信息，从而实现高效的跨模态信息融合和生成。

**技术框架**：BitMar的整体架构包括三个主要模块：低比特编码器、情景记忆模块和BitNet解码器。首先，使用1.58比特的文本（BitNet风格）和视觉（DiNOv2-based）编码器提取图像和文本的紧凑嵌入。然后，将这些嵌入组合起来，查询固定大小的键值情景记忆，检索相关信息。最后，BitNet解码器利用逐层调节和滑动窗口注意力机制，生成最终的文本描述或完成其他多模态理解任务。

**关键创新**：BitMar的关键创新在于以下几个方面：1) 采用极低比特（1.58bit）的编码器，显著降低了计算和存储开销；2) 引入情景记忆模块，增强了模型对上下文信息的利用能力；3) BitNet解码器采用逐层调节和滑动窗口注意力机制，提高了生成质量和处理长序列的能力。

**关键设计**：BitMar的关键设计包括：1) 使用BitNet风格的文本编码器和DiNOv2-based的视觉编码器，以实现高效的特征提取；2) 情景记忆模块采用固定大小的键值存储，以限制内存占用；3) BitNet解码器采用逐层调节，根据不同层的上下文信息调整生成过程；4) 滑动窗口注意力机制允许模型处理长输入序列，同时保持较低的内存占用。

## 📊 实验亮点

BitMar在低延迟和小模型体积下实现了具有竞争力的图像描述和多模态理解性能。通过1.58比特的编码器和情景记忆机制，显著降低了模型的计算复杂度和存储需求。实验结果表明，BitMar在边缘设备上能够实现高效的跨模态信息融合和生成，为边缘计算应用提供了新的解决方案。

## 🎯 应用场景

BitMar适用于各种边缘计算场景，例如智能监控、机器人导航、智能家居等。它可以用于图像描述生成、视觉问答、多模态对话等任务，为边缘设备提供强大的多模态理解能力。该研究有助于推动人工智能在资源受限环境中的应用，实现更智能、更高效的边缘计算。

## 📄 摘要（原文）

> Cross-attention transformers and other multimodal vision-language models excel at grounding and generation; however, their extensive, full-precision backbones make it challenging to deploy them on edge devices. Memory-augmented architectures enhance the utilization of past context; however, most works rarely pair them with aggressive edge-oriented quantization. We introduce BitMar, a quantized multimodal transformer that proposes an external human-like episodic memory for effective image-text generation on hardware with limited resources. BitMar utilizes 1.58-bit encoders, one for text (BitNet-style) and one for vision (DiNOv2-based), to create compact embeddings that are combined and used to query a fixed-size key-value episodic memory. During vector retrieval, the BitNet decoder applies per-layer conditioning, which increases the contextual relevance of generated content. The decoder also employs attention sinks with a sliding-window mechanism to process long or streaming inputs under tight memory budgets. The combination of per-layer conditioning and sliding-window attention achieves a strong quality-speed trade-off, delivering competitive captioning and multimodal understanding at low latency with a small model footprint. These characteristics make BitMar well-suited for edge deployment.

