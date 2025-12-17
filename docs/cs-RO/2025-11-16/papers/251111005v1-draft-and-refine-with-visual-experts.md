---
layout: default
title: Draft and Refine with Visual Experts
---

# Draft and Refine with Visual Experts

**arXiv**: [2511.11005v1](https://arxiv.org/abs/2511.11005) | [PDF](https://arxiv.org/pdf/2511.11005.pdf)

**作者**: Sungheon Jeong, Ryozo Masukawa, Jihong Park, Sanggeon Yun, Wenjun Huang, Hanning Chen, Mahdi Imani, Mohsen Imani

---

## 💡 一句话要点

**提出Draft and Refine框架以解决大型视觉语言模型依赖语言先验导致幻觉的问题**

**关键词**: `大型视觉语言模型` `视觉利用度量` `多模态代理系统` `视觉接地` `幻觉减少` `问答基准`

## 📋 核心要点

1. 核心问题：大型视觉语言模型过度依赖语言先验，产生未基于视觉证据的幻觉响应
2. 方法要点：使用问题条件利用度量量化视觉依赖，并通过外部视觉专家反馈迭代优化响应
3. 实验或效果：在VQA和字幕基准测试中，准确率提升且幻觉减少，无需重新训练

## 📄 摘要（原文）

> While recent Large Vision-Language Models (LVLMs) exhibit strong multimodal reasoning abilities, they often produce ungrounded or hallucinated responses because they rely too heavily on linguistic priors instead of visual evidence. This limitation highlights the absence of a quantitative measure of how much these models actually use visual information during reasoning. We propose Draft and Refine (DnR), an agent framework driven by a question-conditioned utilization metric. The metric quantifies the model's reliance on visual evidence by first constructing a query-conditioned relevance map to localize question-specific cues and then measuring dependence through relevance-guided probabilistic masking. Guided by this metric, the DnR agent refines its initial draft using targeted feedback from external visual experts. Each expert's output (such as boxes or masks) is rendered as visual cues on the image, and the model is re-queried to select the response that yields the largest improvement in utilization. This process strengthens visual grounding without retraining or architectural changes. Experiments across VQA and captioning benchmarks show consistent accuracy gains and reduced hallucination, demonstrating that measuring visual utilization provides a principled path toward more interpretable and evidence-driven multimodal agent systems.

