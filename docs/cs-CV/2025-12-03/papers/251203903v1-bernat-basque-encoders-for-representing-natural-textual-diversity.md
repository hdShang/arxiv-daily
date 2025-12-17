---
layout: default
title: BERnaT: Basque Encoders for Representing Natural Textual Diversity
---

# BERnaT: Basque Encoders for Representing Natural Textual Diversity

**arXiv**: [2512.03903v1](https://arxiv.org/abs/2512.03903) | [PDF](https://arxiv.org/pdf/2512.03903.pdf)

**作者**: Ekhi Azurmendi, Joseba Fernandez de Landa, Jaione Bengoetxea, Maite Heredia, Julen Etxaniz, Mikel Zubillaga, Ander Soraluze, Aitor Soroa

---

## 💡 一句话要点

**提出BERnaT模型以解决巴斯克语语言多样性建模问题，通过结合标准与非标准文本提升模型泛化能力。**

**关键词**: `语言模型` `语言多样性` `巴斯克语` `编码器模型` `自然语言理解` `语料库构建`

## 📋 核心要点

1. 核心问题：语言模型依赖过滤后的标准文本，可能排除非标准语言变体，导致偏见和鲁棒性降低。
2. 方法要点：构建包含标准、社交媒体和历史来源的巴斯克语语料库，预训练三种配置的编码器模型。
3. 实验或效果：在标准与多样化子集上评估，显示结合多样化数据的模型在所有任务类型中表现更优，不损害标准基准准确性。

## 📄 摘要（原文）

> Language models depend on massive text corpora that are often filtered for quality, a process that can unintentionally exclude non-standard linguistic varieties, reduce model robustness and reinforce representational biases. In this paper, we argue that language models should aim to capture the full spectrum of language variation (dialectal, historical, informal, etc.) rather than relying solely on standardized text. Focusing on Basque, a morphologically rich and low-resource language, we construct new corpora combining standard, social media, and historical sources, and pre-train the BERnaT family of encoder-only models in three configurations: standard, diverse, and combined. We further propose an evaluation framework that separates Natural Language Understanding (NLU) tasks into standard and diverse subsets to assess linguistic generalization. Results show that models trained on both standard and diverse data consistently outperform those trained on standard corpora, improving performance across all task types without compromising standard benchmark accuracy. These findings highlight the importance of linguistic diversity in building inclusive, generalizable language models.

