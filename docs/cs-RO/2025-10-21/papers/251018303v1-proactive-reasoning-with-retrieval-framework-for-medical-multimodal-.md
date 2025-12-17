---
layout: default
title: Proactive Reasoning-with-Retrieval Framework for Medical Multimodal Large Language Models
---

# Proactive Reasoning-with-Retrieval Framework for Medical Multimodal Large Language Models

**arXiv**: [2510.18303v1](https://arxiv.org/abs/2510.18303) | [PDF](https://arxiv.org/pdf/2510.18303.pdf)

**作者**: Lehan Wang, Yi Qin, Honglong Yang, Xiaomeng Li

---

## 💡 一句话要点

**提出Med-RwR框架以解决医学多模态大模型推理中的幻觉和事实错误问题**

**关键词**: `医学多模态大模型` `检索增强生成` `强化学习` `主动推理` `外部知识集成` `泛化能力`

## 📋 核心要点

1. 现有医学MLLMs依赖内部知识，导致推理幻觉和事实不准确
2. 设计主动检索外部知识的两阶段强化学习策略，结合视觉和文本信息
3. 在多个医学基准上显著提升性能，并在陌生领域展现强泛化能力

## 📄 摘要（原文）

> Incentivizing the reasoning ability of Multimodal Large Language Models
> (MLLMs) is essential for medical applications to transparently analyze medical
> scans and provide reliable diagnosis. However, existing medical MLLMs rely
> solely on internal knowledge during reasoning, leading to hallucinated
> reasoning and factual inaccuracies when encountering cases beyond their
> training scope. Although recent Agentic Retrieval-Augmented Generation (RAG)
> methods elicit the medical model's proactive retrieval ability during
> reasoning, they are confined to unimodal LLMs, neglecting the crucial visual
> information during reasoning and retrieval. Consequently, we propose the first
> Multimodal Medical Reasoning-with-Retrieval framework, Med-RwR, which actively
> retrieves external knowledge by querying observed symptoms or domain-specific
> medical concepts during reasoning. Specifically, we design a two-stage
> reinforcement learning strategy with tailored rewards that stimulate the model
> to leverage both visual diagnostic findings and textual clinical information
> for effective retrieval. Building on this foundation, we further propose a
> Confidence-Driven Image Re-retrieval (CDIR) method for test-time scaling when
> low prediction confidence is detected. Evaluation on various public medical
> benchmarks demonstrates Med-RwR's significant improvements over baseline
> models, proving the effectiveness of enhancing reasoning capabilities with
> external knowledge integration. Furthermore, Med-RwR demonstrates remarkable
> generalizability to unfamiliar domains, evidenced by 8.8% performance gain on
> our proposed EchoCardiography Benchmark (ECBench), despite the scarcity of
> echocardiography data in the training corpus. Our data, model, and codes will
> be made publicly available at https://github.com/xmed-lab/Med-RwR.

