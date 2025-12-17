---
layout: default
title: Scenes as Tokens: Multi-Scale Normal Distributions Transform Tokenizer for General 3D Vision-Language Understanding
---

# Scenes as Tokens: Multi-Scale Normal Distributions Transform Tokenizer for General 3D Vision-Language Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21191" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21191v1</a>
  <a href="https://arxiv.org/pdf/2511.21191.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21191v1" onclick="toggleFavorite(this, '2511.21191v1', 'Scenes as Tokens: Multi-Scale Normal Distributions Transform Tokenizer for General 3D Vision-Language Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutao Tang, Cheng Zhao, Gaurav Mittal, Rohith Kukkala, Rama Chellappa, Cheng Peng, Mei Chen

**分类**: cs.CV

**发布日期**: 2025-11-26

---

## 💡 一句话要点

**提出NDTokenizer3D，用于通用3D视觉-语言理解的多尺度NDT Tokenizer**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D视觉-语言理解` `场景token化` `多尺度NDT` `点云处理` `人机交互` `3D场景理解` `Transformer` `LLM`

## 📋 核心要点

1. 现有3D视觉-语言模型在将3D场景token化为整体场景tokens，并将其应用于各种3D理解任务方面存在挑战。
2. NDTokenizer3D通过多尺度正态分布变换(NDT)表示和多尺度NDT解码器(MSDec)实现高效的3D场景token化和理解。
3. NDTokenizer3D在3D Referring Segmentation、3D Visual Question Answering和3D Dense Captioning等任务上取得了显著的性能提升。

## 📝 摘要（中文）

本文提出了一种名为NDTokenizer3D的通用3D视觉-语言模型(VLM)，旨在提升3D场景理解和推理能力。该模型通过将3D场景有效地token化为整体场景tokens，并利用这些tokens来处理各种3D理解任务，从而自然地支持人机交互，并将语言层面的推理与3D空间理解联系起来。NDTokenizer3D的核心是一个新颖的三阶段场景token化流程，它基于多尺度正态分布变换(NDT)表示，并结合了多尺度NDT解码器(MSDec)。该模型首先从原始高分辨率点云构建多尺度NDT表示，保留全局上下文和精细的几何细节。然后，MSDec逐步融合跨尺度NDT特征，生成可供LLM端点使用的整体场景tokens。此外，MSDec还被重新用作人机交互提示（点、框、掩码）和分割掩码解码的通用接口，从而将各种3D场景理解任务统一在一个架构中。这种紧凑而统一的设计使NDTokenizer3D成为一个精细的、通用的3D VLM，在3D Referring Segmentation、3D Visual Question Answering和3D Dense Captioning方面取得了显著的改进。

## 🔬 方法详解

**问题定义**：现有3D视觉-语言模型难以有效地将3D场景token化为整体的、可用于多种任务的场景tokens。这限制了模型在3D场景理解和推理方面的能力，尤其是在需要结合语言信息进行交互和理解的场景中。现有方法可能无法同时捕捉全局上下文和精细几何细节，或者缺乏统一的框架来处理不同类型的3D理解任务。

**核心思路**：本文的核心思路是利用多尺度正态分布变换(NDT)来表示3D场景，并设计一个多尺度NDT解码器(MSDec)来生成场景tokens。NDT能够有效地表示点云的概率分布，从而保留几何信息和上下文信息。MSDec则通过融合不同尺度的NDT特征，生成具有全局一致性和局部细节的场景tokens，这些tokens可以被LLM等模型直接使用。

**技术框架**：NDTokenizer3D包含三个主要阶段：1) 多尺度NDT表示：将原始点云转换为多尺度的NDT表示，捕捉不同尺度的几何信息。2) 多尺度NDT解码器(MSDec)：逐步融合跨尺度的NDT特征，生成整体场景tokens。3) 任务特定模块：利用生成的场景tokens进行各种3D理解任务，如3D Referring Segmentation、3D Visual Question Answering和3D Dense Captioning。MSDec还被用作人机交互提示和分割掩码解码的通用接口。

**关键创新**：该方法最重要的技术创新点在于提出了基于多尺度NDT的场景token化方法。与直接处理原始点云或使用体素化等方法相比，NDT能够更有效地表示点云的几何信息和概率分布，从而生成更具信息量的场景tokens。此外，MSDec的设计使得模型能够同时捕捉全局上下文和局部细节，从而提高了场景理解的准确性。

**关键设计**：多尺度NDT表示通过调整NDT的尺度参数来捕捉不同尺度的几何信息。MSDec采用逐步融合的方式，将不同尺度的NDT特征进行融合，从而生成最终的场景tokens。损失函数的设计需要根据具体的任务进行调整，例如，在3D Referring Segmentation任务中，可以使用交叉熵损失函数来优化分割结果。

## 📊 实验亮点

NDTokenizer3D在多个3D视觉-语言理解任务上取得了显著的性能提升。例如，在3D Referring Segmentation任务中，该模型相比现有方法取得了X%的提升（具体数据请参考原论文）。此外，该模型在3D Visual Question Answering和3D Dense Captioning任务上也表现出色，证明了其在通用3D场景理解方面的能力。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实、增强现实等领域。通过结合视觉和语言信息，机器人可以更好地理解周围环境，并与人类进行更自然的交互。例如，在自动驾驶中，模型可以理解“红色的车停在路边”等指令，从而做出更合理的决策。在虚拟现实中，模型可以根据用户的语言描述生成相应的3D场景。

## 📄 摘要（原文）

> Recent advances in 3D vision-language models (VLMs) highlight a strong potential for 3D scene understanding and reasoning. However, effectively tokenizing 3D scenes into holistic scene tokens, and leveraging these tokens across diverse 3D understanding tasks, remain highly challenging. We present NDTokenizer3D, a generalist 3D VLM that performs a wide range of 3D scene understanding tasks while naturally supporting human interactions, thereby bridging language-level reasoning with 3D spatial understanding. The core of our approach is a novel three-stage scene tokenization pipeline built upon a Multi-Scale Normal Distributions Transform (NDT) representation, paired with a Multi-Scale NDT Decoder (MSDec). Specifically, NDTokenizer3D first constructs a multi-scale NDT representation from raw high-resolution point clouds, preserving both global context and fine-grained geometric details. Next, the MSDec progressively fuses cross-scale NDT features, producing holistic scene tokens consumable by LLM endpoints. Beyond tokenization, MSDec is repurposed as a general interface for human-interactive prompting (points, boxes, masks) and segmentation-mask decoding, unifying diverse 3D scene understanding tasks within a single architecture. With this compact and unified design, NDTokenizer3D offers a fine-grained, general-purpose 3D VLM, achieving remarkable improvements in 3D Referring Segmentation, 3D Visual Question Answering, and 3D Dense Captioning.

