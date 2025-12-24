---
layout: default
title: Speculative Decoding Reimagined for Multimodal Large Language Models
---

# Speculative Decoding Reimagined for Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14260" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14260v1</a>
  <a href="https://arxiv.org/pdf/2505.14260.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14260v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14260v1', 'Speculative Decoding Reimagined for Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luxi Lin, Zhihang Lin, Zhanpeng Zeng, Rongrong Ji

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-20

**备注**: 12 pages

**🔗 代码/项目**: [GITHUB](https://github.com/Lyn-Lucy/MSD)

---

## 💡 一句话要点

**提出多模态推测解码以加速多模态大语言模型推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推测解码` `大语言模型` `推理加速` `视觉感知` `语言建模` `模型训练` `文本处理` `视觉处理`

## 📋 核心要点

1. 现有的多模态推测解码方法未能实现与单模态大语言模型相同的推理加速效果，限制了其应用潜力。
2. 本文提出的多模态推测解码（MSD）方法，通过分离文本和视觉标记的处理，提升了多模态大语言模型的推理速度。
3. 实验结果显示，MSD在多模态基准上显著提高了LLaVA模型的推理速度，验证了其有效性和实用性。

## 📝 摘要（中文）

本文介绍了多模态推测解码（MSD），旨在加速多模态大语言模型（MLLMs）的推理。尽管推测解码已被证明可以加速大语言模型（LLMs）而不牺牲准确性，但现有的多模态推测解码方法未能实现与LLMs相同的加速效果。为此，本文专门为MLLMs重新构想了推测解码。通过对MLLM特性的分析，提出了MSD的两个关键设计原则：文本和视觉标记具有根本不同的特性，需在草拟过程中分开处理；语言建模能力和视觉感知能力对草拟模型至关重要。实验表明，MSD在多模态基准上使LLaVA-1.5-7B的推理速度提高了2.29倍，LLaVA-1.5-13B的推理速度提高了2.46倍，展示了其有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态推测解码方法在推理速度上的不足，特别是与单模态大语言模型相比，未能实现相同的加速效果。

**核心思路**：论文的核心思路是重新构想推测解码，针对多模态大语言模型的特性，提出分离处理文本和视觉标记的方案，以便更好地利用各自的特性。

**技术框架**：整体架构包括两个阶段的训练策略：第一阶段，草拟模型在仅文本的指令调优数据集上进行训练，以提升语言建模能力；第二阶段，逐步引入多模态数据，增强视觉感知能力。

**关键创新**：最重要的技术创新点在于将文本和视觉标记的处理解耦，允许根据各自特性进行优化，这与现有方法的整体处理方式形成了本质区别。

**关键设计**：在训练过程中，采用了分阶段的策略，第一阶段专注于文本数据，第二阶段引入视觉数据，确保模型在语言和视觉理解能力上均衡提升。

## 📊 实验亮点

实验结果表明，MSD在多模态基准上显著提升了推理速度，LLaVA-1.5-7B的推理速度提高了2.29倍，LLaVA-1.5-13B的推理速度提高了2.46倍，展示了其在多模态任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动内容生成、图像描述生成等多模态任务。通过加速推理过程，MSD能够在实际应用中提供更快速的响应，提升用户体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper introduces Multimodal Speculative Decoding (MSD) to accelerate Multimodal Large Language Models (MLLMs) inference. Speculative decoding has been shown to accelerate Large Language Models (LLMs) without sacrificing accuracy. However, current speculative decoding methods for MLLMs fail to achieve the same speedup as they do for LLMs. To address this, we reimagine speculative decoding specifically for MLLMs. Our analysis of MLLM characteristics reveals two key design principles for MSD: (1) Text and visual tokens have fundamentally different characteristics and need to be processed separately during drafting. (2) Both language modeling ability and visual perception capability are crucial for the draft model. For the first principle, MSD decouples text and visual tokens in the draft model, allowing each to be handled based on its own characteristics. For the second principle, MSD uses a two-stage training strategy: In stage one, the draft model is trained on text-only instruction-tuning datasets to improve its language modeling ability. In stage two, MSD gradually introduces multimodal data to enhance the visual perception capability of the draft model. Experiments show that MSD boosts inference speed by up to $2.29\times$ for LLaVA-1.5-7B and up to $2.46\times$ for LLaVA-1.5-13B on multimodal benchmarks, demonstrating its effectiveness. Our code is available at https://github.com/Lyn-Lucy/MSD.

