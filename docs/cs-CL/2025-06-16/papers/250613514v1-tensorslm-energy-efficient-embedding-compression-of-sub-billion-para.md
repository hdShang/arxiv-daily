---
layout: default
title: "TensorSLM: Energy-efficient Embedding Compression of Sub-billion Parameter Language Models on Low-end Devices"
---

# TensorSLM: Energy-efficient Embedding Compression of Sub-billion Parameter Language Models on Low-end Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13514" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13514v1</a>
  <a href="https://arxiv.org/pdf/2506.13514.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13514v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13514v1', 'TensorSLM: Energy-efficient Embedding Compression of Sub-billion Parameter Language Models on Low-end Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingxue Xu, Yao Lei Xu, Danilo P. Mandic

**分类**: cs.CL, cs.LG, math.NA

**发布日期**: 2025-06-16

**备注**: ICML 2025 Workshop on Tiny Titans: The next wave of On-Device Learning for Foundational Models (TTODLer-FM)

---

## 💡 一句话要点

**提出TensorSLM以解决低端设备上语言模型能效问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `嵌入压缩` `张量分解` `边缘计算` `能效优化` `低端设备` `机器学习`

## 📋 核心要点

1. 现有的大型语言模型在边缘设备上应用时面临能效和适应性不足的问题，尤其在电池寿命受限的情况下。
2. 本文提出了一种训练无关的嵌入压缩方法，利用张量-训练分解将嵌入向量转化为低维表示，以提高能效和适应性。
3. 实验结果表明，所提方法在压缩比和能耗上具有显著优势，同时保持了与原模型相当的语言任务性能。

## 📝 摘要（中文）

小型语言模型（SLMs）相较于大型语言模型（LLMs）具有更少的参数，适合在低端设备上部署。本文提出了一种基于张量分解的训练无关的嵌入压缩方法，旨在提高SLMs在边缘应用中的适应性和能效。通过将预训练的嵌入向量转换为低维矩阵乘积状态（MPS），我们在Raspberry Pi等低端设备上评估了压缩比、语言任务性能、延迟和能耗。以GPT-2和OPT模型为例，所提方法在保持语言任务性能的同时，实现了约2.0倍的嵌入层压缩，并将单次查询的能耗降低了一半。

## 🔬 方法详解

**问题定义**：本文旨在解决小型语言模型在低端设备上部署时的能效和适应性问题。现有方法通常未能考虑设备的电池寿命限制，导致能耗高且适应性差。

**核心思路**：提出了一种基于张量-训练分解（TTD）的训练无关嵌入压缩方法，通过将预训练的嵌入向量转化为低维矩阵乘积状态（MPS），以实现高效的嵌入表示。

**技术框架**：整体架构包括预训练嵌入的低维转换、低秩结构的提取及其在低端设备上的评估。主要模块包括嵌入压缩模块和性能评估模块。

**关键创新**：最重要的创新在于提出了一种无需训练的嵌入压缩方法，显著提高了小型语言模型在边缘设备上的能效和适应性，与现有方法相比，具有更高的压缩比和更低的能耗。

**关键设计**：在参数设置上，采用了低秩矩阵乘积状态表示，损失函数设计为保持语言任务性能的同时优化能耗，网络结构上则采用了适合低端设备的轻量级设计。

## 📊 实验亮点

实验结果显示，所提方法在压缩比上达到了约2.0倍，同时在语言任务性能上与原始模型相当。单次查询的能耗降低了一半，表明该方法在能效和性能之间取得了良好的平衡。

## 🎯 应用场景

该研究在移动设备、单板计算机等低端设备上具有广泛的应用潜力，尤其适用于需要高效能耗和快速响应的边缘计算场景，如智能助手、实时翻译和语音识别等。未来，随着设备性能的提升，该方法有望在更多实际应用中发挥重要作用。

## 📄 摘要（原文）

> Small Language Models (SLMs, or on-device LMs) have significantly fewer parameters than Large Language Models (LLMs). They are typically deployed on low-end devices, like mobile phones and single-board computers. Unlike LLMs, which rely on increasing model size for better generalisation, SLMs designed for edge applications are expected to have adaptivity to the deployment environments and energy efficiency given the device battery life constraints, which are not addressed in datacenter-deployed LLMs. This paper addresses these two requirements by proposing a training-free token embedding compression approach using Tensor-Train Decomposition (TTD). Each pre-trained token embedding vector is converted into a lower-dimensional Matrix Product State (MPS). We comprehensively evaluate the extracted low-rank structures across compression ratio, language task performance, latency, and energy consumption on a typical low-end device, i.e. Raspberry Pi. Taking the sub-billion parameter versions of GPT-2/Cerebres-GPT and OPT models as examples, our approach achieves a comparable language task performance to the original model with around $2.0\times$ embedding layer compression, while the energy consumption of a single query drops by half.

