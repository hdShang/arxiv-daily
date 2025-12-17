---
layout: default
title: Error-Driven Prompt Optimization for Arithmetic Reasoning
---

# Error-Driven Prompt Optimization for Arithmetic Reasoning

**arXiv**: [2512.13323v1](https://arxiv.org/abs/2512.13323) | [PDF](https://arxiv.org/pdf/2512.13323.pdf)

**作者**: Árpád Pándy, Róbert Lakatos, András Hajdu

---

## 💡 一句话要点

**提出错误驱动提示优化框架，提升小语言模型在算术推理任务中的准确性，适用于隐私合规的工业部署。**

**关键词**: `算术推理` `提示优化` `小语言模型` `错误驱动学习` `隐私合规` `工业部署`

## 📋 核心要点

1. 核心问题：小语言模型在算术推理任务中表现有限，需在隐私合规环境下提升准确性。
2. 方法要点：通过聚类错误预测，迭代优化提示规则，以错误驱动方式改进模型性能。
3. 实验或效果：在Qwen3 4B模型上，该方法将准确率提升至70.8%，超越GPT-3.5 Turbo。

## 📄 摘要（原文）

> Recent advancements in artificial intelligence have sparked interest in industrial agents capable of supporting analysts in regulated sectors, such as finance and healthcare, within tabular data workflows. A key capability for such systems is performing accurate arithmetic operations on structured data while ensuring sensitive information never leaves secure, on-premises environments. Here, we introduce an error-driven optimization framework for arithmetic reasoning that enhances a Code Generation Agent (CGA), specifically applied to on-premises small language models (SLMs). Through a systematic evaluation of a leading SLM (Qwen3 4B), we find that while the base model exhibits fundamental limitations in arithmetic tasks, our proposed error-driven method, which clusters erroneous predictions to refine prompt-rules iteratively, dramatically improves performance, elevating the model's accuracy to 70.8\%. Our results suggest that developing reliable, interpretable, and industrially deployable AI assistants can be achieved not only through costly fine-tuning but also via systematic, error-driven prompt optimization, enabling small models to surpass larger language models (GPT-3.5 Turbo) in a privacy-compliant manner.

