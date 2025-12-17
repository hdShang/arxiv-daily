---
layout: default
title: Temporal Tokenization Strategies for Event Sequence Modeling with Large Language Models
---

# Temporal Tokenization Strategies for Event Sequence Modeling with Large Language Models

**arXiv**: [2512.13618v1](https://arxiv.org/abs/2512.13618) | [PDF](https://arxiv.org/pdf/2512.13618.pdf)

**作者**: Zefang Liu, Nam Nguyen, Yinzhu Quan, Austin Zhang

---

## 💡 一句话要点

**比较多种时间标记化策略以优化大语言模型在事件序列建模中的性能**

**关键词**: `时间标记化` `事件序列建模` `大语言模型` `连续时间表示` `统计分布对齐`

## 📋 核心要点

1. 核心问题：连续时间表示是事件序列建模中的关键挑战，现有策略如字节级表示或日历标记的优劣未知。
2. 方法要点：首次实证研究五种时间标记化策略，包括朴素数字字符串、高精度字节级表示、人类语义日历标记、经典均匀分箱和自适应残差标量量化。
3. 实验或效果：在真实数据集上微调大语言模型，发现性能取决于标记化策略与数据统计特性的对齐，无单一最优策略。

## 📄 摘要（原文）

> Representing continuous time is a critical and under-explored challenge in modeling temporal event sequences with large language models (LLMs). Various strategies like byte-level representations or calendar tokens have been proposed. However, the optimal approach remains unclear, especially given the diverse statistical distributions of real-world event data, which range from smooth log-normal to discrete, spiky patterns. This paper presents the first empirical study of temporal tokenization for event sequences, comparing distinct encoding strategies: naive numeric strings, high-precision byte-level representations, human-semantic calendar tokens, classic uniform binning, and adaptive residual scalar quantization. We evaluate these strategies by fine-tuning LLMs on real-world datasets that exemplify these diverse distributions. Our analysis reveals that no single strategy is universally superior; instead, prediction performance depends heavily on aligning the tokenizer with the data's statistical properties, with log-based strategies excelling on skewed distributions and human-centric formats proving robust for mixed modalities.

