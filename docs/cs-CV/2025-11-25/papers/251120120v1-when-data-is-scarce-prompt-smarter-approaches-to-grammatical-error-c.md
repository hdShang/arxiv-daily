---
layout: default
title: "When Data is Scarce, Prompt Smarter"... Approaches to Grammatical Error Correction in Low-Resource Settings
---

# "When Data is Scarce, Prompt Smarter"... Approaches to Grammatical Error Correction in Low-Resource Settings

**arXiv**: [2511.20120v1](https://arxiv.org/abs/2511.20120) | [PDF](https://arxiv.org/pdf/2511.20120.pdf)

**作者**: Somsubhra De, Harsh Kumar, Arun Prakash A

---

## 💡 一句话要点

**提出提示策略结合LLMs以解决低资源印地语系语言的语法纠错问题**

**关键词**: `语法纠错` `低资源语言` `提示策略` `大型语言模型` `多语言适应`

## 📋 核心要点

1. 核心问题：印地语系语言因资源稀缺和复杂形态学，语法纠错进展缓慢。
2. 方法要点：使用LLMs如GPT-4.1，结合零样本和少样本提示策略进行轻量适应。
3. 实验或效果：在多个语言共享任务中取得领先，如泰米尔语GLEU达91.57。

## 📄 摘要（原文）

> Grammatical error correction (GEC) is an important task in Natural Language Processing that aims to automatically detect and correct grammatical mistakes in text. While recent advances in transformer-based models and large annotated datasets have greatly improved GEC performance for high-resource languages such as English, the progress has not extended equally. For most Indic languages, GEC remains a challenging task due to limited resources, linguistic diversity and complex morphology. In this work, we explore prompting-based approaches using state-of-the-art large language models (LLMs), such as GPT-4.1, Gemini-2.5 and LLaMA-4, combined with few-shot strategy to adapt them to low-resource settings. We observe that even basic prompting strategies, such as zero-shot and few-shot approaches, enable these LLMs to substantially outperform fine-tuned Indic-language models like Sarvam-22B, thereby illustrating the exceptional multilingual generalization capabilities of contemporary LLMs for GEC. Our experiments show that carefully designed prompts and lightweight adaptation significantly enhance correction quality across multiple Indic languages. We achieved leading results in the shared task--ranking 1st in Tamil (GLEU: 91.57) and Hindi (GLEU: 85.69), 2nd in Telugu (GLEU: 85.22), 4th in Bangla (GLEU: 92.86), and 5th in Malayalam (GLEU: 92.97). These findings highlight the effectiveness of prompt-driven NLP techniques and underscore the potential of large-scale LLMs to bridge resource gaps in multilingual GEC.

