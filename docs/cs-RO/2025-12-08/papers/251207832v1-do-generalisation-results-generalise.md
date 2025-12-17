---
layout: default
title: Do Generalisation Results Generalise?
---

# Do Generalisation Results Generalise?

**arXiv**: [2512.07832v1](https://arxiv.org/abs/2512.07832) | [PDF](https://arxiv.org/pdf/2512.07832.pdf)

**作者**: Matteo Boglioni, Andrea Sgobbi, Gabriel Tavernini, Francesco Rita, Marius Mosbach, Tiago Pimentel

---

## 💡 一句话要点

**评估大语言模型在多个分布外数据集上的泛化结果相关性**

**关键词**: `大语言模型` `分布外泛化` `性能评估` `微调分析` `相关性研究`

## 📋 核心要点

1. 核心问题：现有评估通常基于单一分布外数据集，可能无法准确反映模型部署时的多样数据偏移。
2. 方法要点：通过微调过程中评估多个分布外测试集，并控制域内性能后计算部分相关性。
3. 实验或效果：分析OLMo2和OPT模型，发现泛化结果间相关性无统一趋势，取决于具体模型选择。

## 📄 摘要（原文）

> A large language model's (LLM's) out-of-distribution (OOD) generalisation ability is crucial to its deployment. Previous work assessing LLMs' generalisation performance, however, typically focuses on a single out-of-distribution dataset. This approach may fail to precisely evaluate the capabilities of the model, as the data shifts encountered once a model is deployed are much more diverse. In this work, we investigate whether OOD generalisation results generalise. More specifically, we evaluate a model's performance across multiple OOD testsets throughout a finetuning run; we then evaluate the partial correlation of performances across these testsets, regressing out in-domain performance. This allows us to assess how correlated are generalisation performances once in-domain performance is controlled for. Analysing OLMo2 and OPT, we observe no overarching trend in generalisation results: the existence of a positive or negative correlation between any two OOD testsets depends strongly on the specific choice of model analysed.

