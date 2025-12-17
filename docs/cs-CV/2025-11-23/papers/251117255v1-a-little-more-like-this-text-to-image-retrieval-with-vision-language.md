---
layout: default
title: A Little More Like This: Text-to-Image Retrieval with Vision-Language Models Using Relevance Feedback
---

# A Little More Like This: Text-to-Image Retrieval with Vision-Language Models Using Relevance Feedback

**arXiv**: [2511.17255v1](https://arxiv.org/abs/2511.17255) | [PDF](https://arxiv.org/pdf/2511.17255.pdf)

**作者**: Bulat Khaertdinov, Mirela Popa, Nava Tintarev

---

## 💡 一句话要点

**提出基于相关性反馈的机制，以提升视觉语言模型的文本到图像检索性能**

**关键词**: `视觉语言模型` `文本到图像检索` `相关性反馈` `伪相关反馈` `生成相关反馈` `注意力反馈摘要器`

## 📋 核心要点

1. 核心问题：视觉语言模型检索性能提升常需微调或更大模型，缺乏推理时优化方法
2. 方法要点：引入四种反馈策略，包括伪相关反馈、生成相关反馈和注意力反馈摘要器
3. 实验或效果：在Flickr30k和COCO数据集上，反馈策略使MRR@5提升1-5%，增强鲁棒性

## 📄 摘要（原文）

> Large vision-language models (VLMs) enable intuitive visual search using natural language queries. However, improving their performance often requires fine-tuning and scaling to larger model variants. In this work, we propose a mechanism inspired by traditional text-based search to improve retrieval performance at inference time: relevance feedback. While relevance feedback can serve as an alternative to fine-tuning, its model-agnostic design also enables use with fine-tuned VLMs. Specifically, we introduce and evaluate four feedback strategies for VLM-based retrieval. First, we revise classical pseudo-relevance feedback (PRF), which refines query embeddings based on top-ranked results. To address its limitations, we propose generative relevance feedback (GRF), which uses synthetic captions for query refinement. Furthermore, we introduce an attentive feedback summarizer (AFS), a custom transformer-based model that integrates multimodal fine-grained features from relevant items. Finally, we simulate explicit feedback using ground-truth captions as an upper-bound baseline. Experiments on Flickr30k and COCO with the VLM backbones show that GRF, AFS, and explicit feedback improve retrieval performance by 3-5% in MRR@5 for smaller VLMs, and 1-3% for larger ones, compared to retrieval with no feedback. Moreover, AFS, similarly to explicit feedback, mitigates query drift and is more robust than GRF in iterative, multi-turn retrieval settings. Our findings demonstrate that relevance feedback can consistently enhance retrieval across VLMs and open up opportunities for interactive and adaptive visual search.

