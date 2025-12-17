---
layout: default
title: HoneyBee: Data Recipes for Vision-Language Reasoners
---

# HoneyBee: Data Recipes for Vision-Language Reasoners

**arXiv**: [2510.12225v1](https://arxiv.org/abs/2510.12225) | [PDF](https://arxiv.org/pdf/2510.12225.pdf)

**作者**: Hritik Bansal, Devandra Singh Sachan, Kai-Wei Chang, Aditya Grover, Gargi Ghosh, Wen-tau Yih, Ramakanth Pasunuru

---

## 💡 一句话要点

**提出HoneyBee数据集以提升视觉语言模型的推理能力**

**关键词**: `视觉语言模型` `推理数据集` `链式思维` `数据干预` `模型缩放`

## 📋 核心要点

1. 核心问题：视觉语言推理训练数据集构建原则不明确，影响模型性能。
2. 方法要点：通过数据干预和规模扩展，优化图像-问题对和链式思维解决方案。
3. 实验或效果：HoneyBee数据集训练模型在MathVerse等任务上显著超越现有方法。

## 📄 摘要（原文）

> Recent advances in vision-language models (VLMs) have made them highly
> effective at reasoning tasks. However, the principles underlying the
> construction of performant VL reasoning training datasets remain poorly
> understood. In this work, we introduce several data curation approaches and
> study their impacts on VL reasoning capabilities by carefully controlling
> training and evaluation setups. We analyze the effects of context (image and
> question pair) sources, implement targeted data interventions, and explore
> scaling up images, questions, and chain-of-thought (CoT) solutions. Our
> findings reveal that (a) context source strategies significantly affect VLM
> performance, (b) interventions such as auxiliary signals from image captions
> and the inclusion of text-only reasoning yield substantial gains, and (c)
> scaling all data dimensions (e.g., unique questions per image and unique CoTs
> per image-question pair) consistently improves reasoning capability. Motivated
> by these insights, we introduce HoneyBee, a large-scale, high-quality CoT
> reasoning dataset with 2.5M examples consisting 350K image-question pairs. VLMs
> trained with HoneyBee outperform state-of-the-art models across model sizes.
> For instance, a HoneyBee-trained VLM with 3B parameters outperforms the SOTA
> model and the base model by 7.8% and 24.8%, respectively, on MathVerse.
> Furthermore, we propose a test-time scaling strategy that reduces decoding cost
> by 73% without sacrificing accuracy. Overall, this work presents improved
> strategies for VL reasoning dataset curation research.

