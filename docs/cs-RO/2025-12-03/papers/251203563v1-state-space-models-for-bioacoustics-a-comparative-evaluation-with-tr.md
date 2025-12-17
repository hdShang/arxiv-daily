---
layout: default
title: State Space Models for Bioacoustics: A comparative Evaluation with Transformers
---

# State Space Models for Bioacoustics: A comparative Evaluation with Transformers

**arXiv**: [2512.03563v1](https://arxiv.org/abs/2512.03563) | [PDF](https://arxiv.org/pdf/2512.03563.pdf)

**作者**: Chengyu Tang, Sanjeev Baskiyar

---

## 💡 一句话要点

**评估Mamba模型在生物声学中的效能，与Transformer模型对比性能与效率**

**关键词**: `生物声学` `Mamba模型` `Transformer对比` `自监督学习` `BEANS基准` `显存效率`

## 📋 核心要点

1. 核心问题：评估Mamba模型在生物声学任务中的适用性，与Transformer模型比较。
2. 方法要点：使用自监督学习预训练Mamba音频大语言模型，在BEANS基准上微调评估。
3. 实验或效果：BioMamba与AVES性能相当，但显存消耗显著更低，展示其潜力。

## 📄 摘要（原文）

> In this study, we evaluate the efficacy of the Mamba model in the field of bioacoustics. We first pretrain a Mamba-based audio large language model (LLM) on a large corpus of audio data using self-supervised learning. We fine-tune and evaluate BioMamba on the BEANS benchmark, a collection of diverse bioacoustic tasks including classification and detection, and compare its performance and efficiency with multiple baseline models, including AVES, a state-of-the-art Transformer-based model. The results show that BioMamba achieves comparable performance with AVES while consumption significantly less VRAM, demonstrating its potential in this domain.

