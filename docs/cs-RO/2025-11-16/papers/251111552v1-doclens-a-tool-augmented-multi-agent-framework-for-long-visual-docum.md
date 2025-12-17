---
layout: default
title: DocLens : A Tool-Augmented Multi-Agent Framework for Long Visual Document Understanding
---

# DocLens : A Tool-Augmented Multi-Agent Framework for Long Visual Document Understanding

**arXiv**: [2511.11552v1](https://arxiv.org/abs/2511.11552) | [PDF](https://arxiv.org/pdf/2511.11552.pdf)

**作者**: Dawei Zhu, Rui Meng, Jiefeng Chen, Sujian Li, Tomas Pfister, Jinsung Yoon

---

## 💡 一句话要点

**提出DocLens多智能体框架以解决长视觉文档证据定位问题**

**关键词**: `长视觉文档理解` `多智能体框架` `证据定位` `工具增强` `视觉语言模型`

## 📋 核心要点

1. 核心问题：现有视觉语言模型在长文档中证据定位困难，导致性能受限和幻觉
2. 方法要点：采用工具增强多智能体框架，先导航到相关页面，再采样裁决生成可靠答案
3. 实验或效果：在MMLongBench-Doc和FinRAGBench-V上超越人类专家，尤其在视觉中心和无答案查询中表现突出

## 📄 摘要（原文）

> Comprehending long visual documents, where information is distributed across extensive pages of text and visual elements, is a critical but challenging task for modern Vision-Language Models (VLMs). Existing approaches falter on a fundamental challenge: evidence localization. They struggle to retrieve relevant pages and overlook fine-grained details within visual elements, leading to limited performance and model hallucination. To address this, we propose DocLens, a tool-augmented multi-agent framework that effectively ``zooms in'' on evidence like a lens. It first navigates from the full document to specific visual elements on relevant pages, then employs a sampling-adjudication mechanism to generate a single, reliable answer. Paired with Gemini-2.5-Pro, DocLens achieves state-of-the-art performance on MMLongBench-Doc and FinRAGBench-V, surpassing even human experts. The framework's superiority is particularly evident on vision-centric and unanswerable queries, demonstrating the power of its enhanced localization capabilities.

