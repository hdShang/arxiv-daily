---
layout: default
title: "Targeted Lexical Injection: Unlocking Latent Cross-Lingual Alignment in Lugha-Llama via Early-Layer LoRA Fine-Tuning"
---

# Targeted Lexical Injection: Unlocking Latent Cross-Lingual Alignment in Lugha-Llama via Early-Layer LoRA Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15415" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15415v1</a>
  <a href="https://arxiv.org/pdf/2506.15415.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15415v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15415v1', 'Targeted Lexical Injection: Unlocking Latent Cross-Lingual Alignment in Lugha-Llama via Early-Layer LoRA Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stanley Ngugi

**分类**: cs.CL

**发布日期**: 2025-06-18

**备注**: 11 pages, 3 figures, 2 tables. Research on parameter-efficient fine-tuning (PEFT) for low-resource languages (Swahili). Investigates cross-lingual lexical alignment in Lugha-Llama using LoRA and contrastive learning

---

## 💡 一句话要点

**提出目标词汇注入方法以提升低资源语言模型的跨语言对齐能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低资源语言` `跨语言对齐` `目标词汇注入` `低秩适应` `机器翻译` `信息检索` `语言模型`

## 📋 核心要点

1. 现有大型语言模型在低资源语言的表现不足，尤其是在跨语言词汇对齐方面存在显著挑战。
2. 论文提出目标词汇注入（TLI）方法，通过对模型早期层进行低秩适应微调，增强跨语言对齐能力。
3. 实验结果显示，TLI方法显著提升了斯瓦希里语-英语词对的相似度，且在未见数据上也表现良好。

## 📝 摘要（中文）

大型语言模型（LLMs）在低资源语言（LRLs）如斯瓦希里语的表现往往不尽如人意，主要由于数据稀缺和预训练时的代表性不足。本文提出了一种新颖的目标词汇注入（TLI）方法，通过对Lugha-Llama-8B-wura模型的早期层进行低秩适应（LoRA）微调，显著提升了斯瓦希里语与英语词对的输出级别的词汇对齐能力。实验结果显示，经过TLI微调后，623个训练的斯瓦希里语-英语词对的平均余弦相似度从0.3211提升至0.4113，且对63个未见控制词对的相似度提升也显著。这表明TLI有效地增强了模型在低资源语言中的跨语言知识传播能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在低资源语言（如斯瓦希里语）中的跨语言词汇对齐不足的问题。现有方法未能充分利用模型早期层的潜在知识，导致最终输出表现不佳。

**核心思路**：论文提出的目标词汇注入（TLI）方法，通过对模型早期层进行低秩适应（LoRA）微调，利用早期层的强对齐能力来提升最终输出的词汇对齐效果。

**技术框架**：TLI方法的整体架构包括两个主要阶段：首先识别模型早期层的最佳嵌入，然后通过对这些嵌入进行微调来优化模型的输出。

**关键创新**：TLI的核心创新在于利用模型早期层的高相似度特性，针对性地进行微调，从而有效提升了低资源语言模型的跨语言对齐能力。这一方法与传统的全层微调方法有本质区别。

**关键设计**：在TLI中，采用了低秩适应（LoRA）技术，并结合对比学习目标进行微调。关键参数设置包括选择早期层的嵌入作为微调目标，以及设计适当的损失函数以优化相似度提升。

## 📊 实验亮点

实验结果显示，经过目标词汇注入（TLI）微调后，623个斯瓦希里语-英语词对的平均余弦相似度从0.3211提升至0.4113，提升幅度达到28.08%。此外，对63个未见控制词对的相似度也从0.3143提升至0.4033，提升幅度为28.32%。这些结果表明TLI在跨语言对齐方面的显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括机器翻译、跨语言信息检索和多语言对话系统等。通过提升低资源语言的模型性能，TLI方法能够帮助更好地服务于多语言用户，促进语言的多样性和包容性。未来，该方法有望在更多低资源语言的研究中得到应用，推动相关技术的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities, yet their performance in low-resource languages (LRLs), such as Swahili, often lags due to data scarcity and underrepresentation in pre-training. A key challenge is achieving robust cross-lingual lexical alignment, crucial for tasks like translation and cross-lingual information retrieval. This paper introduces Targeted Lexical Injection (TLI), a novel and efficient fine-tuning approach. We first demonstrate that Lugha-Llama-8B-wura, a Swahili-centric LLM, exhibits strong, near-perfect lexical alignment for Swahili-English word pairs in its early internal layers (specifically Layer 2, with ~0.99998 average cosine similarity based on a pilot study), a capability not fully reflected in its final output representations (baseline ~0.32 similarity on our evaluation set). TLI leverages this insight by using Low-Rank Adaptation (LoRA) and a contrastive learning objective to fine-tune the model, specifically targeting embeddings from this empirically identified optimal early layer. Our experiments show that TLI significantly improves the output-level lexical alignment for 623 trained Swahili-English word pairs, increasing average cosine similarity from 0.3211 to 0.4113 (+28.08%, p < 1.33 x 10^-240). More importantly, these improvements generalize remarkably well to 63 unseen control word pairs, with similarity increasing from 0.3143 to 0.4033 (+28.32%, p < 7.17 x 10^-27). These findings suggest TLI enhances the model's ability to preserve and propagate its inherent early-layer cross-lingual knowledge, offering a parameter-efficient and effective strategy for improving lexical alignment in LRL-focused LLMs.

