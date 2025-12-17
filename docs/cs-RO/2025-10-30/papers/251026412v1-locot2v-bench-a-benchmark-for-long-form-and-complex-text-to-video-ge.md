---
layout: default
title: LoCoT2V-Bench: A Benchmark for Long-Form and Complex Text-to-Video Generation
---

# LoCoT2V-Bench: A Benchmark for Long-Form and Complex Text-to-Video Generation

**arXiv**: [2510.26412v1](https://arxiv.org/abs/2510.26412) | [PDF](https://arxiv.org/pdf/2510.26412.pdf)

**作者**: Xiangqing Zheng, Chengyue Wu, Kehai Chen, Min Zhang

---

## 💡 一句话要点

**提出LoCoT2V-Bench基准以解决长视频生成中复杂提示评估不足的问题**

**关键词**: `长视频生成` `文本到视频基准` `多维评估` `事件对齐` `叙事连贯性`

## 📋 核心要点

1. 现有基准依赖简化提示，忽视细粒度对齐和叙事连贯性等抽象维度
2. 引入现实复杂提示和多维评估框架，包括事件对齐和HERD等新指标
3. 评估九种模型，发现其在事件一致性和主题遵循方面表现不佳

## 📄 摘要（原文）

> Recently text-to-video generation has made impressive progress in producing
> short, high-quality clips, but evaluating long-form outputs remains a major
> challenge especially when processing complex prompts. Existing benchmarks
> mostly rely on simplified prompts and focus on low-level metrics, overlooking
> fine-grained alignment with prompts and abstract dimensions such as narrative
> coherence and thematic expression. To address these gaps, we propose
> LoCoT2V-Bench, a benchmark specifically designed for long video generation
> (LVG) under complex input conditions. Based on various real-world videos,
> LoCoT2V-Bench introduces a suite of realistic and complex prompts incorporating
> elements like scene transitions and event dynamics. Moreover, it constructs a
> multi-dimensional evaluation framework that includes our newly proposed metrics
> such as event-level alignment, fine-grained temporal consistency, content
> clarity, and the Human Expectation Realization Degree (HERD) that focuses on
> more abstract attributes like narrative flow, emotional response, and character
> development. Using this framework, we conduct a comprehensive evaluation of
> nine representative LVG models, finding that while current methods perform well
> on basic visual and temporal aspects, they struggle with inter-event
> consistency, fine-grained alignment, and high-level thematic adherence, etc.
> Overall, LoCoT2V-Bench provides a comprehensive and reliable platform for
> evaluating long-form complex text-to-video generation and highlights critical
> directions for future method improvement.

