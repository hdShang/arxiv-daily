---
layout: default
title: Towards Nepali-language LLMs: Efficient GPT training with a Nepali BPE tokenizer
---

# Towards Nepali-language LLMs: Efficient GPT training with a Nepali BPE tokenizer

**arXiv**: [2512.14585v1](https://arxiv.org/abs/2512.14585) | [PDF](https://arxiv.org/pdf/2512.14585.pdf)

**作者**: Adarsha Shrestha, Basanta Pokharel, Binit Shrestha, Smriti Adhikari, Dinesh Gothe

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-16

**备注**: Work in progress

---

## 💡 一句话要点

**提出基于GPT-2的尼泊尔语大语言模型，通过定制BPE分词器和高效训练策略解决低资源语言生成难题。**

**关键词**: `低资源语言处理` `尼泊尔语大语言模型` `字节对编码分词器` `GPT-2架构` `FlashAttention优化` `文本生成` `自然语言处理` `训练策略优化`

## 📋 核心要点

1. 现有方法主要基于基础编码器架构，难以满足尼泊尔语复杂语法和黏着性形态下的文本生成需求。
2. 论文提出基于GPT-2的模型，结合定制BPE分词器和GPT-3启发的训练策略，优化学习率与架构。
3. 模型在尼泊尔语数据集上训练后，困惑度达21.80，能生成连贯的新闻文本，验证了其有效性。

## 📝 摘要（中文）

尼泊尔语作为一种低资源语言，拥有超过3200万使用者，因其复杂的语法、黏着性形态和高质量语料库的有限可用性，在自然语言处理领域持续面临挑战。迄今为止的大多数努力都集中在基础编码器架构上，这些架构对于尼泊尔语特定的文本生成仍然不足。本研究提出了一个基于GPT-2的尼泊尔语语言模型，采用了受GPT-3启发的多种训练策略，包括优化的学习率调度、批次缩放和架构改进。一个定制的16k字节对编码分词器专门在尼泊尔语文本上训练，以确保更一致的分割和改进的输入表示。该模型在一个组合数据集上进行了预训练，该数据集包括10.75GB清洗后的尼泊尔BERTa语料库和额外的网络爬取的尼泊尔新闻文章。集成了FlashAttention以减少内存使用并稳定训练。经过两个训练周期后，模型实现了3.168177的训练损失、3.081982的验证损失和21.80的最终困惑度，展示了其生成连贯的尼泊尔新闻风格文本的能力。

## 🔬 方法详解

论文采用GPT-2作为基础架构，核心创新在于定制16k BPE分词器专门针对尼泊尔语训练，确保更准确的分词和输入表示。方法整合了受GPT-3启发的训练策略，如优化学习率调度和批次缩放，并引入FlashAttention以提升训练效率和稳定性。与现有方法相比，主要区别在于从基础编码器转向生成式模型，并针对尼泊尔语低资源特性进行定制化优化，解决了传统方法在文本生成上的不足。

## 📊 实验亮点

模型在训练后达到21.80的困惑度，训练损失和验证损失分别为3.168177和3.081982，成功生成连贯的尼泊尔新闻风格文本，证明了定制分词器和高效训练策略的有效性。

## 🎯 应用场景

该研究可应用于尼泊尔语新闻自动生成、聊天机器人、内容创作和机器翻译等领域，为低资源语言的自然语言处理提供实际解决方案，促进尼泊尔语社区的数字化发展。

## 📄 摘要（原文）

> Nepali, a low-resource language spoken by over 32 million people, continues to face challenges in natural language processing (NLP) due to its complex grammar, agglutinative morphology, and limited availability of high-quality corpora. Most efforts to date have centered on basic encoder architectures; they remain insufficient for Nepali-specific text generation. This study presents a GPT-2-based Nepali language model trained using several training strategies inspired by GPT-3, including optimized learning rate schedules, batch scaling, and architectural refinements. A custom 16k Byte-Pair Encoding (BPE) tokenizer was trained exclusively on Nepali text to ensure more consistent segmentation and improved input representation. The model was pretrained on a combined dataset comprising a 10.75GB cleaned NepBERTa corpus and additional web-scraped Nepali news articles. FlashAttention was integrated to reduce memory usage and stabilize training. After two epochs, the model achieved a training loss of 3.168177, a validation loss of 3.081982, and a final perplexity of 21.80, demonstrating its capability to generate coherent Nepali news-style text.

