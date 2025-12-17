---
layout: default
title: Multi-Agent AI Framework for Road Situation Detection and C-ITS Message Generation
---

# Multi-Agent AI Framework for Road Situation Detection and C-ITS Message Generation

**arXiv**: [2511.06892v1](https://arxiv.org/abs/2511.06892) | [PDF](https://arxiv.org/pdf/2511.06892.pdf)

**作者**: Kailin Tong, Selim Solmaz, Kenan Mujkic, Gottfried Allmer, Bo Leng

---

## 💡 一句话要点

**提出多智能体AI框架，结合MLLM与视觉感知，用于道路状况检测与C-ITS消息生成。**

**关键词**: `多智能体AI框架` `多模态大语言模型` `道路状况检测` `C-ITS消息生成` `视觉感知` `智能交通系统`

## 📋 核心要点

1. 传统方法在未知场景中失效且缺乏语义解释，影响交通推荐可靠性。
2. 框架整合多模态大语言模型与视觉感知，协调智能体进行检测、决策和消息生成。
3. 在自定义数据集上评估，召回率达100%，但存在误检和特定任务性能下降问题。

## 📄 摘要（原文）

> Conventional road-situation detection methods achieve strong performance in
> predefined scenarios but fail in unseen cases and lack semantic interpretation,
> which is crucial for reliable traffic recommendations. This work introduces a
> multi-agent AI framework that combines multimodal large language models (MLLMs)
> with vision-based perception for road-situation monitoring. The framework
> processes camera feeds and coordinates dedicated agents for situation
> detection, distance estimation, decision-making, and Cooperative Intelligent
> Transport System (C-ITS) message generation. Evaluation is conducted on a
> custom dataset of 103 images extracted from 20 videos of the TAD dataset. Both
> Gemini-2.0-Flash and Gemini-2.5-Flash were evaluated. The results show 100\%
> recall in situation detection and perfect message schema correctness; however,
> both models suffer from false-positive detections and have reduced performance
> in terms of number of lanes, driving lane status and cause code. Surprisingly,
> Gemini-2.5-Flash, though more capable in general tasks, underperforms
> Gemini-2.0-Flash in detection accuracy and semantic understanding and incurs
> higher latency (Table II). These findings motivate further work on fine-tuning
> specialized LLMs or MLLMs tailored for intelligent transportation applications.

