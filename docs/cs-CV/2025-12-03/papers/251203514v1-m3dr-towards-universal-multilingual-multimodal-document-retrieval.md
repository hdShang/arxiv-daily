---
layout: default
title: M3DR: Towards Universal Multilingual Multimodal Document Retrieval
---

# M3DR: Towards Universal Multilingual Multimodal Document Retrieval

**arXiv**: [2512.03514v1](https://arxiv.org/abs/2512.03514) | [PDF](https://arxiv.org/pdf/2512.03514.pdf)

**作者**: Adithya S Kolavi, Vyoman Jain

---

## 💡 一句话要点

**提出M3DR框架以解决多语言多模态文档检索中的英语中心化问题**

**关键词**: `多模态文档检索` `跨语言对齐` `对比学习` `合成数据` `统一表示` `多语言基准`

## 📋 核心要点

1. 核心问题：现有多模态文档检索系统以英语为中心，在多语言场景下效果受限
2. 方法要点：利用合成多语言文档数据，通过对比训练学习跨语言和跨模态的统一表示
3. 实验或效果：在22种语言上验证性能，模型NetraEmbed和ColNetraEmbed在跨语言检索中相对提升约150%

## 📄 摘要（原文）

> Multimodal document retrieval systems have shown strong progress in aligning visual and textual content for semantic search. However, most existing approaches remain heavily English-centric, limiting their effectiveness in multilingual contexts. In this work, we present M3DR (Multilingual Multimodal Document Retrieval), a framework designed to bridge this gap across languages, enabling applicability across diverse linguistic and cultural contexts. M3DR leverages synthetic multilingual document data and generalizes across different vision-language architectures and model sizes, enabling robust cross-lingual and cross-modal alignment. Using contrastive training, our models learn unified representations for text and document images that transfer effectively across languages. We validate this capability on 22 typologically diverse languages, demonstrating consistent performance and adaptability across linguistic and script variations. We further introduce a comprehensive benchmark that captures real-world multilingual scenarios, evaluating models under monolingual, multilingual, and mixed-language settings. M3DR generalizes across both single dense vector and ColBERT-style token-level multi-vector retrieval paradigms. Our models, NetraEmbed and ColNetraEmbed achieve state-of-the-art performance with ~150% relative improvements on cross-lingual retrieval.

