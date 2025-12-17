---
layout: default
title: Large-Language Memorization During the Classification of United States Supreme Court Cases
---

# Large-Language Memorization During the Classification of United States Supreme Court Cases

**arXiv**: [2512.13654v1](https://arxiv.org/abs/2512.13654) | [PDF](https://arxiv.org/pdf/2512.13654.pdf)

**作者**: John E. Ortega, Dhruv D. Joshi, Matt P. Borkowski

---

## 💡 一句话要点

**研究大语言模型在美国最高法院案例分类中的记忆策略，提升分类准确性**

**关键词**: `大语言模型记忆` `最高法院案例分类` `参数高效微调` `提示记忆模型` `法律文本处理`

## 📋 核心要点

1. 核心问题：大语言模型在分类任务中可能产生幻觉，需探究其记忆机制以优化响应
2. 方法要点：采用参数高效微调、自动建模等最新技术，结合提示记忆模型如DeepSeek
3. 实验或效果：在15和279个主题的SCOTUS分类任务中，提示记忆模型比传统BERT模型准确率提高约2点

## 📄 摘要（原文）

> Large-language models (LLMs) have been shown to respond in a variety of ways for classification tasks outside of question-answering. LLM responses are sometimes called "hallucinations" since the output is not what is ex pected. Memorization strategies in LLMs are being studied in detail, with the goal of understanding how LLMs respond. We perform a deep dive into a classification task based on United States Supreme Court (SCOTUS) decisions. The SCOTUS corpus is an ideal classification task to study for LLM memory accuracy because it presents significant challenges due to extensive sentence length, complex legal terminology, non-standard structure, and domain-specific vocabulary. Experimentation is performed with the latest LLM fine tuning and retrieval-based approaches, such as parameter-efficient fine-tuning, auto-modeling, and others, on two traditional category-based SCOTUS classification tasks: one with 15 labeled topics and another with 279. We show that prompt-based models with memories, such as DeepSeek, can be more robust than previous BERT-based models on both tasks scoring about 2 points better than previous models not based on prompting.

