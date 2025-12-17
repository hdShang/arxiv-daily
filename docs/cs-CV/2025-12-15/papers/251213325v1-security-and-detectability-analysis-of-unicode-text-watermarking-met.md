---
layout: default
title: Security and Detectability Analysis of Unicode Text Watermarking Methods Against Large Language Models
---

# Security and Detectability Analysis of Unicode Text Watermarking Methods Against Large Language Models

**arXiv**: [2512.13325v1](https://arxiv.org/abs/2512.13325) | [PDF](https://arxiv.org/pdf/2512.13325.pdf)

**作者**: Malte Hellmeier

---

## 💡 一句话要点

**分析Unicode文本水印方法在大语言模型下的安全性与可检测性**

**关键词**: `文本水印` `大语言模型` `安全性分析` `Unicode编码` `模型检测`

## 📋 核心要点

1. 核心问题：现有Unicode文本水印方法在大语言模型下的安全性和不可检测性缺乏验证
2. 方法要点：在受控测试环境中实现并分析十种Unicode文本水印方法
3. 实验或效果：实验表明最新推理模型能检测水印文本，但所有模型无法提取水印

## 📄 摘要（原文）

> Securing digital text is becoming increasingly relevant due to the widespread use of large language models. Individuals' fear of losing control over data when it is being used to train such machine learning models or when distinguishing model-generated output from text written by humans. Digital watermarking provides additional protection by embedding an invisible watermark within the data that requires protection. However, little work has been taken to analyze and verify if existing digital text watermarking methods are secure and undetectable by large language models. In this paper, we investigate the security-related area of watermarking and machine learning models for text data. In a controlled testbed of three experiments, ten existing Unicode text watermarking methods were implemented and analyzed across six large language models: GPT-5, GPT-4o, Teuken 7B, Llama 3.3, Claude Sonnet 4, and Gemini 2.5 Pro. The findings of our experiments indicate that, especially the latest reasoning models, can detect a watermarked text. Nevertheless, all models fail to extract the watermark unless implementation details in the form of source code are provided. We discuss the implications for security researchers and practitioners and outline future research opportunities to address security concerns.

