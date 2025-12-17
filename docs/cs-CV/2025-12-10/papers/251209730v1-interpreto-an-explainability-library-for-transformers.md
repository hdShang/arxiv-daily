---
layout: default
title: Interpreto: An Explainability Library for Transformers
---

# Interpreto: An Explainability Library for Transformers

**arXiv**: [2512.09730v1](https://arxiv.org/abs/2512.09730) | [PDF](https://arxiv.org/pdf/2512.09730.pdf)

**作者**: Antonin Poché, Thomas Mullor, Gabriele Sarti, Frédéric Boisnard, Corentin Friedrich, Charlotte Claye, François Hoofd, Raphael Bernas, Céline Hudelot, Fanny Jourdan

---

## 💡 一句话要点

**提出Interpreto库以支持HuggingFace文本模型的后验可解释性分析**

**关键词**: `可解释性库` `Transformer模型` `后验解释` `概念解释` `HuggingFace集成`

## 📋 核心要点

1. 核心问题：为BERT到LLM的HuggingFace文本模型提供后验可解释性工具，弥补现有库在概念解释方面的不足。
2. 方法要点：集成归因和基于概念的解释方法，通过统一API支持分类和生成模型，强调概念功能。
3. 实验或效果：开源库包含文档、示例和教程，旨在提升数据科学家和终端用户的可解释性访问性。

## 📄 摘要（原文）

> Interpreto is a Python library for post-hoc explainability of text HuggingFace models, from early BERT variants to LLMs. It provides two complementary families of methods: attributions and concept-based explanations. The library connects recent research to practical tooling for data scientists, aiming to make explanations accessible to end users. It includes documentation, examples, and tutorials.
>   Interpreto supports both classification and generation models through a unified API. A key differentiator is its concept-based functionality, which goes beyond feature-level attributions and is uncommon in existing libraries.
>   The library is open source; install via pip install interpreto. Code and documentation are available at https://github.com/FOR-sight-ai/interpreto.

