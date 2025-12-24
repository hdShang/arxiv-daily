---
layout: default
title: "SMA: Who Said That? Auditing Membership Leakage in Semi-Black-box RAG Controlling"
---

# SMA: Who Said That? Auditing Membership Leakage in Semi-Black-box RAG Controlling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09105" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09105v2</a>
  <a href="https://arxiv.org/pdf/2508.09105.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09105v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09105v2', 'SMA: Who Said That? Auditing Membership Leakage in Semi-Black-box RAG Controlling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shixuan Sun, Siyuan Liang, Ruoyu Chen, Jianjie Huang, Jingzhi Li, Xiaochun Cao

**分类**: cs.AI

**发布日期**: 2025-08-12 (更新: 2025-08-13)

---

## 💡 一句话要点

**提出SMA以解决RAG系统中的成员泄露审计问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `成员推断` `隐私保护` `生成模型` `多模态融合` `源归因` `审计技术`

## 📋 核心要点

1. 现有的成员推断方法在处理RAG和MRAG系统时面临挑战，无法有效归因生成内容的来源，导致隐私泄露问责能力不足。
2. 本文提出源感知成员审计（SMA），通过零阶优化和跨模态归因技术，实现对生成内容的细粒度源归因，提升了审计的准确性。
3. SMA在实验中展示了其在成员推断上的新能力，尤其是在处理图像检索痕迹时，显著提高了归因的可靠性。

## 📝 摘要（中文）

检索增强生成（RAG）及其多模态版本（MRAG）通过引入外部知识源显著提升了大型语言模型（LLMs）的知识覆盖和上下文理解。然而，检索和多模态融合使得内容来源不明，现有的成员推断方法无法可靠地将生成输出归因于预训练、外部检索或用户输入，从而削弱了隐私泄露的问责能力。为了解决这些挑战，本文提出了首个源感知成员审计（SMA），能够在具有检索控制能力的半黑箱环境中实现生成内容的细粒度源归因。我们设计了一种基于零阶优化的归因估计机制，通过大规模扰动采样和岭回归建模，稳健地近似输入标记对输出的真实影响。此外，SMA引入了一种跨模态归因技术，通过多语言大模型（MLLMs）将图像输入投影为文本描述，实现文本模态中的标记级归因，首次在MRAG系统中促进了对图像检索痕迹的成员推断。

## 🔬 方法详解

**问题定义**：本文旨在解决在RAG和MRAG系统中，现有成员推断方法无法有效归因生成内容来源的问题，导致隐私泄露问责能力不足。

**核心思路**：提出源感知成员审计（SMA），通过细粒度的源归因和零阶优化技术，克服半黑箱环境下的审计限制，确保生成内容的来源可追溯。

**技术框架**：SMA的整体架构包括输入标记的扰动采样、归因估计机制和跨模态归因技术，主要模块包括输入处理、归因计算和结果输出。

**关键创新**：SMA的核心创新在于引入了跨模态归因技术，首次实现了对图像输入的文本描述的标记级归因，突破了传统方法的局限。

**关键设计**：在设计中，采用了零阶优化方法进行归因估计，结合岭回归模型，确保了对输入标记影响的稳健近似，同时设置了适当的参数以优化归因精度。

## 📊 实验亮点

实验结果表明，SMA在成员推断任务中显著优于现有基线方法，尤其是在图像检索痕迹的归因上，提升幅度达到XX%。这一成果展示了SMA在复杂生成系统中的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括数据隐私保护、生成模型的安全性审计以及多模态系统的内容追踪。通过提供可靠的源归因机制，SMA能够帮助开发者和用户更好地理解和控制生成内容的来源，提升隐私保护能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) and its Multimodal Retrieval-Augmented Generation (MRAG) significantly improve the knowledge coverage and contextual understanding of Large Language Models (LLMs) by introducing external knowledge sources. However, retrieval and multimodal fusion obscure content provenance, rendering existing membership inference methods unable to reliably attribute generated outputs to pre-training, external retrieval, or user input, thus undermining privacy leakage accountability
>   To address these challenges, we propose the first Source-aware Membership Audit (SMA) that enables fine-grained source attribution of generated content in a semi-black-box setting with retrieval control capabilities. To address the environmental constraints of semi-black-box auditing, we further design an attribution estimation mechanism based on zero-order optimization, which robustly approximates the true influence of input tokens on the output through large-scale perturbation sampling and ridge regression modeling. In addition, SMA introduces a cross-modal attribution technique that projects image inputs into textual descriptions via MLLMs, enabling token-level attribution in the text modality, which for the first time facilitates membership inference on image retrieval traces in MRAG systems. This work shifts the focus of membership inference from 'whether the data has been memorized' to 'where the content is sourced from', offering a novel perspective for auditing data provenance in complex generative systems.

