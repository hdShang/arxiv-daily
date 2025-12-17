---
layout: default
title: Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding
---

# Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding

**arXiv**: [2510.15253v1](https://arxiv.org/abs/2510.15253) | [PDF](https://arxiv.org/pdf/2510.15253.pdf)

**作者**: Sensen Gao, Shanshan Zhao, Xu Jiang, Lunhao Duan, Yong Xien Chng, Qing-Guo Chen, Weihua Luo, Kaifu Zhang, Jia-Wang Bian, Mingming Gong

---

## 💡 一句话要点

**提出多模态检索增强生成综述，以解决文档理解中结构丢失和上下文建模难题。**

**关键词**: `多模态检索增强生成` `文档理解` `检索模态` `图结构` `代理框架` `文档AI`

## 📋 核心要点

1. 核心问题：文档理解中OCR方法丢失结构细节，多模态大模型上下文建模困难。
2. 方法要点：引入多模态RAG，支持跨文本、表格、图表和布局的检索与推理。
3. 实验或效果：总结数据集、基准和应用，识别效率、细粒度表示和鲁棒性挑战。

## 📄 摘要（原文）

> Document understanding is critical for applications from financial analysis
> to scientific discovery. Current approaches, whether OCR-based pipelines
> feeding Large Language Models (LLMs) or native Multimodal LLMs (MLLMs), face
> key limitations: the former loses structural detail, while the latter struggles
> with context modeling. Retrieval-Augmented Generation (RAG) helps ground models
> in external data, but documents' multimodal nature, i.e., combining text,
> tables, charts, and layout, demands a more advanced paradigm: Multimodal RAG.
> This approach enables holistic retrieval and reasoning across all modalities,
> unlocking comprehensive document intelligence. Recognizing its importance, this
> paper presents a systematic survey of Multimodal RAG for document
> understanding. We propose a taxonomy based on domain, retrieval modality, and
> granularity, and review advances involving graph structures and agentic
> frameworks. We also summarize key datasets, benchmarks, and applications, and
> highlight open challenges in efficiency, fine-grained representation, and
> robustness, providing a roadmap for future progress in document AI.

