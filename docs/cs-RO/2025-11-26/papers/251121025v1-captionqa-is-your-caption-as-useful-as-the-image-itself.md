---
layout: default
title: CaptionQA: Is Your Caption as Useful as the Image Itself?
---

# CaptionQA: Is Your Caption as Useful as the Image Itself?

**arXiv**: [2511.21025v1](https://arxiv.org/abs/2511.21025) | [PDF](https://arxiv.org/pdf/2511.21025.pdf)

**作者**: Shijia Yang, Yunong Liu, Bohan Zhai, Ximeng Sun, Zicheng Liu, Emad Barsoum, Manling Li, Chenfeng Xu

---

## 💡 一句话要点

**提出CaptionQA基准以评估图像描述在下游任务中的实用性**

**关键词**: `图像描述评估` `多模态基准` `下游任务效用` `LLM问答` `领域特定分类` `开源基准`

## 📋 核心要点

1. 核心问题：图像描述能否替代图像支持下游任务，现有评估方法忽略此问题
2. 方法要点：构建多领域基准，通过LLM使用描述回答多选题，直接测量描述效用
3. 实验或效果：评估显示描述与图像效用差距大，模型在传统基准相似但描述效用降32%

## 📄 摘要（原文）

> Image captions serve as efficient surrogates for visual content in multimodal systems such as retrieval, recommendation, and multi-step agentic inference pipelines. Yet current evaluation practices miss a fundamental question: Can captions stand-in for images in real downstream tasks? We propose a utility-based benchmark, CaptionQA, to evaluate model-generated captions, where caption quality is measured by how well it supports downstream tasks. CaptionQA is an extensible domain-dependent benchmark covering 4 domains--Natural, Document, E-commerce, and Embodied AI--each with fine-grained taxonomies (25 top-level and 69 subcategories) that identify useful information for domain-specific tasks. CaptionQA builds 33,027 densely annotated multiple-choice questions (50.3 per image on average) that explicitly require visual information to answer, providing a comprehensive probe of caption utility. In our evaluation protocol, an LLM answers these questions using captions alone, directly measuring whether captions preserve image-level utility and are utilizable by a downstream LLM. Evaluating state-of-the-art MLLMs reveals substantial gaps between the image and its caption utility. Notably, models nearly identical on traditional image-QA benchmarks lower by up to 32% in caption utility. We release CaptionQA along with an open-source pipeline for extension to new domains. The code is available at https://github.com/bronyayang/CaptionQA.

