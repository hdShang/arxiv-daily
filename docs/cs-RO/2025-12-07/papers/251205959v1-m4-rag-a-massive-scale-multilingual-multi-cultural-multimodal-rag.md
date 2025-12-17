---
layout: default
title: M4-RAG: A Massive-Scale Multilingual Multi-Cultural Multimodal RAG
---

# M4-RAG: A Massive-Scale Multilingual Multi-Cultural Multimodal RAG

**arXiv**: [2512.05959v1](https://arxiv.org/abs/2512.05959) | [PDF](https://arxiv.org/pdf/2512.05959.pdf)

**作者**: David Anugraha, Patrick Amadeus Irawan, Anshul Singh, En-Shiun Annie Lee, Genta Indra Winata

---

## 💡 一句话要点

**提出M4-RAG基准以评估多语言多模态检索增强生成在视觉问答中的性能**

**关键词**: `多语言多模态检索增强生成` `视觉问答基准` `文化多样性评估` `受控检索环境` `模型规模与性能分析`

## 📋 核心要点

1. 核心问题：多语言多模态检索增强生成在视觉问答中研究不足，现有模型受限于静态数据。
2. 方法要点：构建大规模基准，覆盖42种语言和56种方言，包含8万对文化多样图像-问题，并建立受控检索环境。
3. 实验或效果：系统评估显示检索增强对小模型有益，但对大模型性能可能下降，揭示模型规模与检索效果不匹配。

## 📄 摘要（原文）

> Vision-language models (VLMs) have achieved strong performance in visual question answering (VQA), yet they remain constrained by static training data. Retrieval-Augmented Generation (RAG) mitigates this limitation by enabling access to up-to-date, culturally grounded, and multilingual information; however, multilingual multimodal RAG remains largely underexplored. We introduce M4-RAG, a massive-scale benchmark covering 42 languages and 56 regional dialects and registers, comprising over 80,000 culturally diverse image-question pairs for evaluating retrieval-augmented VQA across languages and modalities. To balance realism with reproducibility, we build a controlled retrieval environment containing millions of carefully curated multilingual documents relevant to the query domains, approximating real-world retrieval conditions while ensuring consistent experimentation. Our systematic evaluation reveals that although RAG consistently benefits smaller VLMs, it fails to scale to larger models and often even degrades their performance, exposing a critical mismatch between model size and current retrieval effectiveness. M4-RAG provides a foundation for advancing next-generation RAG systems capable of reasoning seamlessly across languages, modalities, and cultural contexts.

