---
layout: default
title: A Comparative Analysis of Retrieval-Augmented Generation Techniques for Bengali Standard-to-Dialect Machine Translation Using LLMs
---

# A Comparative Analysis of Retrieval-Augmented Generation Techniques for Bengali Standard-to-Dialect Machine Translation Using LLMs

**arXiv**: [2512.14179v1](https://arxiv.org/abs/2512.14179) | [PDF](https://arxiv.org/pdf/2512.14179.pdf)

**作者**: K. M. Jubair Sami, Dipto Sumit, Ariyan Hossain, Farig Sadeque

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-12-16

**备注**: Accepted to the Second Workshop on Bangla Language Processing (BLP) at IJCNLP-AACL 2025. 14 pages, 9 figures, 6 tables

---

## 💡 一句话要点

**提出两种检索增强生成管道，用于孟加拉语标准语到方言的机器翻译，解决低资源方言翻译难题。**

**关键词**: `检索增强生成` `孟加拉语翻译` `方言机器翻译` `低资源自然语言处理` `语言多样性保护` `大型语言模型应用` `词错误率优化` `无微调解决方案`

## 📋 核心要点

1. 核心问题：孟加拉语标准语到方言翻译面临数据稀缺和语言变异性挑战，现有方法在低资源环境下效果有限。
2. 方法要点：提出两种RAG管道，基于转录本和标准化句子对，利用检索增强生成技术提升翻译质量。
3. 实验或效果：句子对管道显著降低词错误率，较小模型通过RAG超越更大模型，验证检索策略的重要性。

## 📝 摘要（中文）

将标准语言翻译为区域方言是自然语言处理中的重要挑战，尤其在孟加拉语中，由于数据稀缺和语言变异性，这一问题尤为突出。本文提出并比较了两种新颖的检索增强生成（RAG）管道，用于标准语到方言的孟加拉语翻译。第一种是基于转录本的管道，利用音频转录中的大型方言句子上下文；第二种是更有效的标准化句子对管道，使用结构化的“方言:标准孟加拉语”句子对。我们在六种孟加拉语方言和多种大型语言模型上评估了这两种管道，使用BLEU、ChrF、WER和BERTScore等指标。研究结果表明，句子对管道始终优于基于转录本的管道，例如在吉大港方言中，将词错误率（WER）从76%降低到55%。关键的是，这种RAG方法使较小模型（如Llama-3.1-8B）能够超越更大模型（如GPT-OSS-120B），表明精心设计的检索策略可能比模型规模更为关键。这项工作为低资源方言翻译提供了一种有效、无需微调的解决方案，为保护语言多样性提供了实用蓝图。

## 🔬 方法详解

论文提出两种检索增强生成（RAG）管道框架：基于转录本的管道从音频转录中提取方言句子上下文，用于检索增强；标准化句子对管道则使用结构化的“方言:标准孟加拉语”句子对作为检索源。关键创新点在于将RAG技术应用于低资源方言翻译，通过检索相关上下文来增强大型语言模型的翻译能力，无需额外微调。与现有方法的主要区别在于，传统方法依赖大规模平行语料或复杂微调，而本方法通过检索策略有效利用有限数据，直接提升模型性能，特别适用于数据稀缺场景。

## 📊 实验亮点

句子对管道在吉大港方言上将词错误率从76%降至55%，较小模型Llama-3.1-8B通过RAG超越GPT-OSS-120B等更大模型，证明检索策略比模型规模更关键。

## 🎯 应用场景

该研究可应用于低资源语言方言翻译、语言多样性保护、跨方言通信辅助工具开发，以及教育、媒体和文化传承领域，为多语言社会提供实用技术支持。

## 📄 摘要（原文）

> Translating from a standard language to its regional dialects is a significant NLP challenge due to scarce data and linguistic variation, a problem prominent in the Bengali language. This paper proposes and compares two novel RAG pipelines for standard-to-dialectal Bengali translation. The first, a Transcript-Based Pipeline, uses large dialect sentence contexts from audio transcripts. The second, a more effective Standardized Sentence-Pairs Pipeline, utilizes structured local\_dialect:standard\_bengali sentence pairs. We evaluated both pipelines across six Bengali dialects and multiple LLMs using BLEU, ChrF, WER, and BERTScore. Our findings show that the sentence-pair pipeline consistently outperforms the transcript-based one, reducing Word Error Rate (WER) from 76\% to 55\% for the Chittagong dialect. Critically, this RAG approach enables smaller models (e.g., Llama-3.1-8B) to outperform much larger models (e.g., GPT-OSS-120B), demonstrating that a well-designed retrieval strategy can be more crucial than model size. This work contributes an effective, fine-tuning-free solution for low-resource dialect translation, offering a practical blueprint for preserving linguistic diversity.

