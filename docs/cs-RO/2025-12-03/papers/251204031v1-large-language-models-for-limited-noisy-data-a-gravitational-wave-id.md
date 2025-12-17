---
layout: default
title: Large Language Models for Limited Noisy Data: A Gravitational Wave Identification Study
---

# Large Language Models for Limited Noisy Data: A Gravitational Wave Identification Study

**arXiv**: [2512.04031v1](https://arxiv.org/abs/2512.04031) | [PDF](https://arxiv.org/pdf/2512.04031.pdf)

**作者**: Yixuan Li, Yuhao Lu, Yang Liu, Liang Li, R. Ruffini, Di Li, Rong-Gen Cai, Xiaoyan Zhu, Wenbin Lin, Yu Wang

---

## 💡 一句话要点

**研究大语言模型在有限噪声数据下用于引力波识别的优势**

**关键词**: `大语言模型` `引力波识别` `有限噪声数据` `天文数据处理` `非高斯噪声`

## 📋 核心要点

1. 核心问题：天文数据处理中非高斯、非平稳噪声和有限标注样本的挑战
2. 方法要点：利用大语言模型直接提取观测数据中的判别结构，避免依赖大规模模拟数据集
3. 实验或效果：仅用90个LIGO事件微调，达到97.4%的识别准确率，模型规模和数据集扩展可预测提升性能

## 📄 摘要（原文）

> This work investigates whether large language models (LLMs) offer advantages over traditional neural networks for astronomical data processing, in regimes with non-Gaussian, non-stationary noise and limited labeled samples. Gravitational wave observations provide an suitable test case, using only 90 LIGO events, finetuned LLMs achieve 97.4\% accuracy for identifying signals. Further experiments show that, in contrast to traditional networks that rely on large simulated datasets, additional simulated samples do not improve LLM performance, while scaling studies reveal predictable gains with increasing model size and dataset size. These results indicate that LLMs can extract discriminative structure directly from observational data and provide an efficient assessment for gravitational wave identification. The same strategy may extend to other astronomical domains with similar noise properties, such as radio or pulsar observations.

