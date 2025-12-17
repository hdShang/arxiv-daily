---
layout: default
title: Understanding Task Transfer in Vision-Language Models
---

# Understanding Task Transfer in Vision-Language Models

**arXiv**: [2511.18787v1](https://arxiv.org/abs/2511.18787) | [PDF](https://arxiv.org/pdf/2511.18787.pdf)

**作者**: Bhuvan Sachdeva, Karan Uppal, Abhinav Java, Vineeth N. Balasubramanian

---

## 💡 一句话要点

**提出Perfection Gap Factor以量化视觉语言模型任务迁移性**

**关键词**: `视觉语言模型` `任务迁移性` `Perfection Gap Factor` `正负迁移` `任务迁移图` `数据选择`

## 📋 核心要点

1. 核心问题：视觉语言模型在视觉感知任务中表现不佳，微调后任务间性能影响不可预测
2. 方法要点：引入PGF指标，构建任务迁移图，分析正负迁移模式
3. 实验或效果：评估三个模型在13个任务上，揭示任务间关系，指导数据选择

## 📄 摘要（原文）

> Vision-Language Models (VLMs) perform well on multimodal benchmarks but lag behind humans and specialized models on visual perception tasks like depth estimation or object counting. Finetuning on one task can unpredictably affect performance on others, making task-specific finetuning challenging. In this paper, we address this challenge through a systematic study of task transferability. We examine how finetuning a VLM on one perception task affects its zero-shot performance on others. To quantify these effects, we introduce Perfection Gap Factor (PGF), a metric that captures both the breadth and magnitude of transfer. Using three open-weight VLMs evaluated across 13 perception tasks, we construct a task-transfer graph that reveals previously unobserved relationships among perception tasks. Our analysis uncovers patterns of positive and negative transfer, identifies groups of tasks that mutually influence each other, organizes tasks into personas based on their transfer behavior and demonstrates how PGF can guide data selection for more efficient training. These findings highlight both opportunities for positive transfer and risks of negative interference, offering actionable guidance for advancing VLMs.

