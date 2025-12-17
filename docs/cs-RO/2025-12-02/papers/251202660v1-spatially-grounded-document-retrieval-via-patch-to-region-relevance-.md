---
layout: default
title: Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation
---

# Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation

**arXiv**: [2512.02660v1](https://arxiv.org/abs/2512.02660) | [PDF](https://arxiv.org/pdf/2512.02660.pdf)

**作者**: Agathoklis Georgiou

---

## 💡 一句话要点

**提出基于补丁到区域相关性传播的混合架构，以提升文档检索在RAG中的精确性。**

**关键词**: `文档检索` `视觉语言模型` `OCR` `相关性传播` `检索增强生成` `空间定位`

## 📋 核心要点

1. 问题：现有视觉语言模型返回整页而非特定区域，限制检索增强生成的精确上下文需求。
2. 方法：结合ColPali的补丁级相似度与OCR边界框，通过坐标映射和交集度量传播相关性。
3. 效果：无需额外训练，开源实现Snappy展示实用性，理论精度界限已建立。

## 📄 摘要（原文）

> Vision-language models (VLMs) like ColPali achieve state-of-the-art document retrieval by embedding pages as images and computing fine-grained similarity between query tokens and visual patches. However, they return entire pages rather than specific regions, limiting utility for retrieval-augmented generation (RAG) where precise context is paramount. Conversely, OCR-based systems extract structured text with bounding box coordinates but lack semantic grounding for relevance assessment. We propose a hybrid architecture that unifies these paradigms: using ColPali's patch-level similarity scores as spatial relevance filters over OCR-extracted regions. We formalize the coordinate mapping between vision transformer patch grids and OCR bounding boxes, introduce intersection metrics for relevance propagation, and establish theoretical bounds on retrieval precision. Our approach operates at inference time without additional training. We release Snappy, an open-source implementation demonstrating practical applicability, with empirical evaluation ongoing.

