---
layout: default
title: LIME: Making LLM Data More Efficient with Linguistic Metadata Embeddings
---

# LIME: Making LLM Data More Efficient with Linguistic Metadata Embeddings

**arXiv**: [2512.07522v1](https://arxiv.org/abs/2512.07522) | [PDF](https://arxiv.org/pdf/2512.07522.pdf)

**作者**: Sebastian Sztwiertnia, Felix Friedrich, Kristian Kersting, Patrick Schramowski, Björn Deiseroth

---

## 💡 一句话要点

**提出LIME方法，通过语言元数据嵌入提升LLM预训练效率与性能**

**关键词**: `语言模型预训练` `元数据嵌入` `训练效率` `词元化改进` `生成任务性能` `推理增强`

## 📋 核心要点

1. 核心问题：预训练语言模型依赖大量高质量数据，但数据可用性受限，元数据作为训练信号未充分利用。
2. 方法要点：LIME将语法、语义和上下文属性的元数据嵌入到词元嵌入中，仅增加0.01%参数，计算开销可忽略。
3. 实验效果：LIME使模型适应训练数据分布的速度提升高达56%，并增强语言建模和生成任务性能，LIME+1变体可提升推理和算术准确性达38%和35%。

## 📄 摘要（原文）

> Pre-training decoder-only language models relies on vast amounts of high-quality data, yet the availability of such data is increasingly reaching its limits. While metadata is commonly used to create and curate these datasets, its potential as a direct training signal remains under-explored. We challenge this status quo and propose LIME (Linguistic Metadata Embeddings), a method that enriches token embeddings with metadata capturing syntax, semantics, and contextual properties. LIME substantially improves pre-training efficiency. Specifically, it adapts up to 56% faster to the training data distribution, while introducing only 0.01% additional parameters at negligible compute overhead. Beyond efficiency, LIME improves tokenization, leading to remarkably stronger language modeling capabilities and generative task performance. These benefits persist across model scales (500M to 2B). In addition, we develop a variant with shifted metadata, LIME+1, that can guide token generation. Given prior metadata for the next token, LIME+1 improves reasoning performance by up to 38% and arithmetic accuracy by up to 35%.

