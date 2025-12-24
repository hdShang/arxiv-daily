---
layout: default
title: "MonetGPT: Solving Puzzles Enhances MLLMs' Image Retouching Skills"
---

# MonetGPT: Solving Puzzles Enhances MLLMs' Image Retouching Skills

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06176" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06176v1</a>
  <a href="https://arxiv.org/pdf/2505.06176.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06176v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06176v1', 'MonetGPT: Solving Puzzles Enhances MLLMs\' Image Retouching Skills')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Niladri Shekhar Dutt, Duygu Ceylan, Niloy J. Mitra

**分类**: cs.GR, cs.CV, cs.LG

**发布日期**: 2025-05-09

**备注**: Accepted at SIGGRAPH 2025 [ACM Transactions on Graphics]; Project website: https://monetgpt.github.io

**DOI**: [10.1145/3730926](https://doi.org/10.1145/3730926)

---

## 💡 一句话要点

**提出MonetGPT以提升多模态大语言模型的图像修饰能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像修饰` `多模态大语言模型` `生成性编辑` `程序性编辑` `可解释性` `身份保留` `视觉难题`

## 📋 核心要点

1. 现有的生成性编辑方法容易在不可预测的方式下改变图像对象的身份，缺乏专业性和可控性。
2. 本文提出通过训练MLLM解决视觉难题，使其理解图像处理操作，从而能够规划和建议修饰序列。
3. 实验表明，所提出的方法在可解释性和对象细节保留方面优于现有的图像编辑工具，具有显著的优势。

## 📝 摘要（中文）

图像修饰是原始照片后期处理中的重要任务。生成性编辑虽然为用户提供了新的工具，但可能会以不可接受的方式改变原始对象的身份。传统的程序性编辑虽然保守，但仍然受到专业人士的青睐。本文探讨了如何通过训练多模态大语言模型（MLLM）来批评原始照片、建议适当的修正方案，并利用预先编写的程序性图像操作实现这些修正。我们通过设计视觉难题来让MLLM了解图像处理操作，进而使其能够规划和提出编辑序列。实验结果表明，所提出的方法在可解释性和身份保留方面优于现有的生成性和其他程序性替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决图像修饰中生成性编辑方法的不足，尤其是其在身份保留和可控性方面的挑战。现有的程序性编辑虽然保守，但对于新手来说难以规划和执行。

**核心思路**：通过训练多模态大语言模型（MLLM）解决视觉难题，使其理解图像处理操作，从而能够批评原始照片并建议适当的修正方案。该方法结合了专家编辑的知识，提供了一种可解释且用户友好的修饰方式。

**技术框架**：整体架构包括三个主要阶段：首先，设计视觉难题以训练MLLM理解图像处理操作；其次，利用专家编辑的照片合成推理数据集；最后，基于预训练的LLM进行微调，以实现图像修饰的规划和建议。

**关键创新**：最重要的创新在于通过视觉难题训练MLLM，使其具备操作意识，能够在保留对象细节的同时进行有效的图像修饰。这一方法与传统的生成性编辑方法本质上不同，后者往往缺乏对操作的理解。

**关键设计**：在训练过程中，设计了特定的损失函数和参数设置，以确保模型能够有效地学习图像处理操作。此外，采用了预训练的LLM作为基础，结合视觉调整进行微调，以提升模型的修饰能力。

## 📊 实验亮点

实验结果显示，MonetGPT在可解释性和身份保留方面优于现有的生成性和程序性编辑方法。具体而言，模型在多个测试示例中表现出更高的编辑质量和用户满意度，显著提升了图像修饰的效果。

## 🎯 应用场景

该研究的潜在应用领域包括专业摄影、广告设计和社交媒体内容创作等。通过提供一种可解释且用户友好的图像修饰工具，MonetGPT能够帮助用户更高效地进行图像编辑，提升创作质量。未来，该技术可能会在自动化图像处理和个性化编辑工具中发挥重要作用。

## 📄 摘要（原文）

> Retouching is an essential task in post-manipulation of raw photographs. Generative editing, guided by text or strokes, provides a new tool accessible to users but can easily change the identity of the original objects in unacceptable and unpredictable ways. In contrast, although traditional procedural edits, as commonly supported by photoediting tools (e.g., Gimp, Lightroom), are conservative, they are still preferred by professionals. Unfortunately, professional quality retouching involves many individual procedural editing operations that is challenging to plan for most novices. In this paper, we ask if a multimodal large language model (MLLM) can be taught to critique raw photographs, suggest suitable remedies, and finally realize them with a given set of pre-authored procedural image operations. We demonstrate that MLLMs can be first made aware of the underlying image processing operations, by training them to solve specially designed visual puzzles. Subsequently, such an operation-aware MLLM can both plan and propose edit sequences. To facilitate training, given a set of expert-edited photos, we synthesize a reasoning dataset by procedurally manipulating the expert edits and then grounding a pretrained LLM on the visual adjustments, to synthesize reasoning for finetuning. The proposed retouching operations are, by construction, understandable by the users, preserve object details and resolution, and can be optionally overridden. We evaluate our setup on a variety of test examples and show advantages, in terms of explainability and identity preservation, over existing generative and other procedural alternatives. Code, data, models, and supplementary results can be found via our project website at https://monetgpt.github.io.

