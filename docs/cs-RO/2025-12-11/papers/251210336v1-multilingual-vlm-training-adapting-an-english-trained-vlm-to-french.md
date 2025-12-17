---
layout: default
title: Multilingual VLM Training: Adapting an English-Trained VLM to French
---

# Multilingual VLM Training: Adapting an English-Trained VLM to French

**arXiv**: [2512.10336v1](https://arxiv.org/abs/2512.10336) | [PDF](https://arxiv.org/pdf/2512.10336.pdf)

**作者**: Jules Lahmi, Alexis Roger

---

## 💡 一句话要点

**比较翻译、LoRA和两阶段微调方法，以将英语视觉语言模型适配至法语。**

**关键词**: `视觉语言模型` `多语言适配` `微调策略` `数据集翻译` `性能评估`

## 📋 核心要点

1. 核心问题：英语视觉语言模型在非英语语言中性能受限，需扩展多语言能力。
2. 方法要点：评估翻译管道、LoRA微调和两阶段微调（视觉与语言分离）的性能与计算成本。
3. 实验或效果：使用翻译基准和专家评估，发现数据集翻译是性能瓶颈，数据质量影响训练与评估。

## 📄 摘要（原文）

> Artificial intelligence has made great progress in recent years, particularly in the development of Vision--Language Models (VLMs) that understand both visual and textual data. However, these advancements remain largely limited to English, reducing their accessibility for non--English speakers. It is essential to extend these capabilities to a broader range of languages. This paper explores the challenges of adapting an English-trained VLM to different languages. To this end, we will explore and compare different methods for their performance and computational cost. We consider a translation-based pipeline, LoRA finetuning, and a two-stage finetuning strategy that separates vision adaptation from language adaptation. To evaluate these methods, we use a combination of standard multimodal benchmarks translated into the target language and manual assessments by native experts. The results reveal that dataset translation remains a major bottleneck in multilingual VLM performance, with data quality limiting the effectiveness of training and evaluation. These findings suggest that future efforts should focus on native-language dataset collection and improved translation strategies.

