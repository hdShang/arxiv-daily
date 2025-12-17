---
layout: default
title: SEASON: Mitigating Temporal Hallucination in Video Large Language Models via Self-Diagnostic Contrastive Decoding
---

# SEASON: Mitigating Temporal Hallucination in Video Large Language Models via Self-Diagnostic Contrastive Decoding

**arXiv**: [2512.04643v1](https://arxiv.org/abs/2512.04643) | [PDF](https://arxiv.org/pdf/2512.04643.pdf)

**作者**: Chang-Hsun Wu, Kai-Po Chang, Yu-Yang Sheng, Hung-Kai Chung, Kuei-Chun Wang, Yu-Chiang Frank Wang

---

## 💡 一句话要点

**提出SEASON方法以缓解视频大语言模型中的时间幻觉问题**

**关键词**: `视频大语言模型` `时间幻觉` `对比解码` `无需训练方法` `视频理解` `幻觉缓解`

## 📋 核心要点

1. 核心问题：视频大语言模型在响应查询时难以有效感知和利用视频中的时间信息，导致时间不一致或因果不合理的描述，引发严重幻觉。
2. 方法要点：SEASON是一种无需训练的方法，通过自适应诊断每个输出令牌的幻觉倾向，并对其对应的时间和空间负样本应用自适应对比解码，动态增强输出的时间和空间忠实性。
3. 实验或效果：在三个幻觉检测基准上优于现有无需训练的幻觉缓解方法，并在四个通用视频理解基准上进一步提升了视频大语言模型的性能。

## 📄 摘要（原文）

> Video Large Language Models (VideoLLMs) have shown remarkable progress in video understanding. However, these models still struggle to effectively perceive and exploit rich temporal information in videos when responding to user queries. Therefore, they often generate descriptions of events that are temporal inconsistent or causally implausible, causing severe hallucination issues. While most prior studies have focused on spatial hallucinations (e.g. object mismatches), temporal reasoning in video understanding remains relatively underexplored. To address this issue, we propose Self-Diagnostic Contrastive Decoding (SEASON), a training-free method that adaptively enhances temporal and spatial faithfulness for each output token. It achieves this by dynamically diagnosing each token's hallucination tendency and applying adaptive contrastive decoding against its corresponding temporal and spatial negatives. Extensive experiments demonstrate that SEASON outperforms all existing training-free hallucination mitigation approaches on three hallucination examination benchmarks, while further improves VideoLLMs across four general video understanding benchmarks. The code will be released upon acceptance.

