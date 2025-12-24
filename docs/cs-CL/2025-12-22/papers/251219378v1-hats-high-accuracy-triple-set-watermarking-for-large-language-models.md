---
layout: default
title: "HATS: High-Accuracy Triple-Set Watermarking for Large Language Models"
---

# HATS: High-Accuracy Triple-Set Watermarking for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19378" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19378v1</a>
  <a href="https://arxiv.org/pdf/2512.19378.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19378v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19378v1', 'HATS: High-Accuracy Triple-Set Watermarking for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiqing Hu, Chenxu Zhao, Jiazhong Lu, Xiaolei Liu

**分类**: cs.CL

**发布日期**: 2025-12-22

**备注**: Camera-ready version of the paper accepted for oral presentation at the 11th International Conference on Computer and Communications (ICCC 2025)

**期刊**: In Proceedings of the 11th International Conference on Computer and Communications, 2025

---

## 💡 一句话要点

**提出高精度三集合水印方案HATS，用于保护大型语言模型生成文本的版权**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `水印技术` `版权保护` `文本生成` `统计检测`

## 📋 核心要点

1. 大型语言模型生成文本的滥用是一个日益严重的问题，需要有效的水印技术来追踪和识别生成来源。
2. 论文提出一种新颖的三集合水印方案，通过在生成过程中限制词汇采样空间，嵌入隐式信号。
3. 实验结果表明，该方案在保持文本质量的同时，显著提高了水印检测的准确性，降低了误报率。

## 📝 摘要（中文）

本文提出了一种针对大型语言模型（LLM）生成文本的水印技术，旨在遏制LLM生成文本的滥用。该水印技术在每个解码步骤将词汇表划分为三个集合（绿/黄/红），并限制采样仅在绿色和黄色集合中进行。在检测时，重放相同的划分，计算绿色集合的富集和红色集合的耗尽统计量，将其转换为单侧z分数，并通过Fisher方法聚合它们的p值，以判断一段文本是否被水印标记。在Llama 2 7B上实现了生成、检测和测试，并评估了真阳性率、假阳性率和文本质量。结果表明，三集合划分方案在固定FPR下实现了高检测精度，同时保持了可读性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）生成文本的版权保护问题。现有方法可能存在检测精度不高、对文本质量影响较大或容易被规避等痛点。因此，需要一种鲁棒且高效的水印方案，能够在不显著影响生成文本质量的前提下，准确地识别出由特定LLM生成的内容。

**核心思路**：论文的核心思路是将LLM的词汇表在每个解码步骤动态划分为三个互斥的集合：绿色集合、黄色集合和红色集合。生成过程被限制为主要从绿色和黄色集合中采样，从而在文本中引入一种统计偏差。这种偏差在检测阶段可以被用来判断文本是否被水印标记。

**技术框架**：该水印方案包含三个主要阶段：1) **词汇划分**：在每个解码步骤，根据预定义的规则（例如哈希函数）将词汇表划分为绿色、黄色和红色集合，并保持三者比例固定。2) **文本生成**：限制LLM的采样过程，使其主要从绿色和黄色集合中选择token。3) **水印检测**：对于待检测文本，重复词汇划分过程，计算绿色集合的富集程度和红色集合的耗尽程度，并基于统计检验判断文本是否包含水印。

**关键创新**：该方案的关键创新在于使用三集合划分，同时考虑了绿色集合的富集和红色集合的耗尽。相比于传统的二元划分，三集合划分能够更有效地利用词汇信息，提高水印的鲁棒性和检测精度。此外，通过Fisher方法聚合绿色富集和红色耗尽的p值，进一步提升了检测的可靠性。

**关键设计**：关键设计包括：1) **集合比例**：绿色、黄色和红色集合的比例需要仔细调整，以平衡检测精度和文本质量。2) **哈希函数**：用于词汇划分的哈希函数需要具有良好的随机性和均匀性，以避免引入偏差。3) **统计检验**：使用单侧z分数和Fisher方法进行统计检验，以评估水印存在的可能性。4) **阈值设定**：需要根据实际应用场景设定合适的阈值，以控制假阳性率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19378v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19378v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，HATS水印方案在Llama 2 7B模型上实现了高检测精度，同时保持了较低的假阳性率。具体来说，在固定假阳性率的情况下，HATS能够显著提高真阳性率，优于现有的水印方案。此外，实验还验证了HATS对文本质量的影响较小，能够生成可读性良好的文本。

## 🎯 应用场景

该研究成果可应用于保护大型语言模型生成内容的版权，防止恶意使用和传播。例如，可以用于识别和追踪由特定LLM生成的虚假新闻、恶意代码或侵权内容。此外，该技术还可以用于验证LLM生成内容的真实性，提升用户对LLM的信任度。

## 📄 摘要（原文）

> Misuse of LLM-generated text can be curbed by watermarking techniques that embed implicit signals into the output. We propose a watermark that partitions the vocabulary at each decoding step into three sets (Green/Yellow/Red) with fixed ratios and restricts sampling to the Green and Yellow sets. At detection time, we replay the same partitions, compute Green-enrichment and Red-depletion statistics, convert them to one-sided z-scores, and aggregate their p-values via Fisher's method to decide whether a passage is watermarked. We implement generation, detection, and testing on Llama 2 7B, and evaluate true-positive rate, false-positive rate, and text quality. Results show that the triple-partition scheme achieves high detection accuracy at fixed FPR while preserving readability.

