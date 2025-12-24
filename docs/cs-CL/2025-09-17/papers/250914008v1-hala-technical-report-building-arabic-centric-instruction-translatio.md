---
layout: default
title: "Hala Technical Report: Building Arabic-Centric Instruction & Translation Models at Scale"
---

# Hala Technical Report: Building Arabic-Centric Instruction & Translation Models at Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14008" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14008v1</a>
  <a href="https://arxiv.org/pdf/2509.14008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14008v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14008v1', 'Hala Technical Report: Building Arabic-Centric Instruction & Translation Models at Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hasan Abed Al Kader Hammoud, Mohammad Zbeeb, Bernard Ghanem

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-17

**备注**: Technical Report

---

## 💡 一句话要点

**提出Hala模型以提升阿拉伯语指令与翻译的质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿拉伯语处理` `指令翻译` `模型压缩` `双语监督` `轻量级模型` `自然语言处理` `深度学习`

## 📋 核心要点

1. 现有的阿拉伯语指令和翻译模型在质量和效率上存在不足，难以满足大规模应用需求。
2. Hala模型通过压缩教师模型并利用双语监督数据，结合轻量级语言模型进行微调，提升了翻译质量和处理速度。
3. 在阿拉伯语基准测试中，Hala模型在小型和纳米类别中均取得了最先进的结果，显示出显著的性能提升。

## 📝 摘要（中文）

本文介绍了Hala，一个以阿拉伯语为中心的指令和翻译模型系列，采用我们的翻译与调优管道构建。我们首先将强大的阿拉伯语与英语教师模型压缩至FP8格式，实现约2倍的吞吐量提升且无质量损失，并利用其生成高保真的双语监督数据。接着，我们对轻量级语言模型LFM2-1.2B进行微调，以将高质量的英语指令集翻译成阿拉伯语，构建了一个百万规模的专门用于指令跟随的语料库。Hala模型在多个参数规模下训练，并在阿拉伯语基准测试中取得了领先的结果，超越了基础模型。我们发布了模型、数据、评估和方法，以加速阿拉伯语自然语言处理的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决阿拉伯语指令和翻译模型在质量和效率上的不足，现有方法难以满足大规模应用的需求。

**核心思路**：通过压缩强大的阿拉伯语与英语教师模型至FP8格式，提升吞吐量，同时利用生成的高保真双语监督数据对轻量级语言模型进行微调，以提高翻译质量。

**技术框架**：整体架构包括教师模型压缩、双语监督数据生成、轻量级语言模型微调及最终的模型训练，涵盖多个参数规模的Hala模型。

**关键创新**：Hala模型的核心创新在于通过slerp合并技术平衡阿拉伯语专业化与基础模型的优势，提升了模型的整体性能。

**关键设计**：在模型训练中，采用了不同参数设置（350M、700M、1.2B和9B），并设计了适合阿拉伯语的损失函数和网络结构，以确保模型的高效性和准确性。

## 📊 实验亮点

Hala模型在阿拉伯语基准测试中表现出色，尤其在纳米（≤2B）和小型（7-9B）类别中，均取得了最先进的结果，超越了基础模型，展示了显著的性能提升。具体而言，模型在翻译质量和处理效率上均实现了显著的改进，推动了阿拉伯语NLP的研究进展。

## 🎯 应用场景

Hala模型在阿拉伯语自然语言处理领域具有广泛的应用潜力，尤其是在教育、翻译和信息检索等场景中。其高质量的指令翻译能力能够帮助阿拉伯语用户更好地理解和使用技术产品，推动相关领域的发展。未来，Hala模型的研究成果可能会促进阿拉伯语处理技术的进一步创新与应用。

## 📄 摘要（原文）

> We present Hala, a family of Arabic-centric instruction and translation models built with our translate-and-tune pipeline. We first compress a strong AR$\leftrightarrow$EN teacher to FP8 (yielding $\sim$2$\times$ higher throughput with no quality loss) and use it to create high-fidelity bilingual supervision. A lightweight language model LFM2-1.2B is then fine-tuned on this data and used to translate high-quality English instruction sets into Arabic, producing a million-scale corpus tailored to instruction following. We train Hala models at 350M, 700M, 1.2B, and 9B parameters, and apply slerp merging to balance Arabic specialization with base-model strengths. On Arabic-centric benchmarks, Hala achieves state-of-the-art results within both the "nano" ($\leq$2B) and "small" (7-9B) categories, outperforming their bases. We release models, data, evaluation, and recipes to accelerate research in Arabic NLP.

