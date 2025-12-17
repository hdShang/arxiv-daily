---
layout: default
title: Cross-Lingual Interleaving for Speech Language Models
---

# Cross-Lingual Interleaving for Speech Language Models

**arXiv**: [2512.01865v1](https://arxiv.org/abs/2512.01865) | [PDF](https://arxiv.org/pdf/2512.01865.pdf)

**作者**: Adel Moumen, Guangzhi Sun, Philip C. Woodland

---

## 💡 一句话要点

**提出跨语言交错方法以构建多语言语音语言模型，解决数据稀缺问题。**

**关键词**: `语音语言模型` `跨语言学习` `无监督训练` `语义评估` `多语言对话`

## 📋 核心要点

1. 核心问题：语音语言模型发展以英语为中心，跨语言学习因数据稀缺而困难。
2. 方法要点：无文本监督下混合跨语言语音标记，实现跨语言交错训练。
3. 实验或效果：在匹配训练标记预算下，提升单语语义准确性，增强跨语言延续和对齐。

## 📄 摘要（原文）

> Spoken Language Models (SLMs) aim to learn linguistic competence directly from speech using discrete units, widening access to Natural Language Processing (NLP) technologies for languages with limited written resources. However, progress has been largely English-centric due to scarce spoken evaluation benchmarks and training data, making cross-lingual learning difficult. We present a cross-lingual interleaving method that mixes speech tokens across languages without textual supervision. We also release an EN-FR training dataset, TinyStories (~42k hours), together with EN-FR spoken StoryCloze and TopicCloze benchmarks for cross-lingual semantic evaluation, both synthetically generated using GPT-4. On 360M and 1B SLMs under matched training-token budgets, interleaving improves monolingual semantic accuracy, enables robust cross-lingual continuation, and strengthens cross-lingual hidden-state alignment. Taken together, these results indicate that cross-lingual interleaving is a simple, scalable route to building multilingual SLMs that understand and converse across languages. All resources will be made open-source to support reproducibility.

