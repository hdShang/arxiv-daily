---
layout: default
title: VADER: Towards Causal Video Anomaly Understanding with Relation-Aware Large Language Models
---

# VADER: Towards Causal Video Anomaly Understanding with Relation-Aware Large Language Models

**arXiv**: [2511.07299v1](https://arxiv.org/abs/2511.07299) | [PDF](https://arxiv.org/pdf/2511.07299.pdf)

**作者**: Ying Cheng, Yu-Ho Lin, Min-Hung Chen, Fu-En Yang, Shang-Hong Lai

---

## 💡 一句话要点

**提出VADER框架，利用关系感知大语言模型增强视频异常理解中的因果推理。**

**关键词**: `视频异常理解` `因果推理` `关系建模` `大语言模型` `对象交互` `异常描述`

## 📋 核心要点

1. 核心问题：现有视频异常理解方法忽视对象间因果关系和交互，限制语义理解。
2. 方法要点：集成关键帧对象关系特征与视觉线索，通过CORE建模动态交互，结合LLM生成因果描述。
3. 实验效果：在多个真实世界基准测试中，VADER在异常描述、解释和因果推理任务表现优异。

## 📄 摘要（原文）

> Video anomaly understanding (VAU) aims to provide detailed interpretation and
> semantic comprehension of anomalous events within videos, addressing
> limitations of traditional methods that focus solely on detecting and
> localizing anomalies. However, existing approaches often neglect the deeper
> causal relationships and interactions between objects, which are critical for
> understanding anomalous behaviors. In this paper, we propose VADER, an
> LLM-driven framework for Video Anomaly unDErstanding, which integrates keyframe
> object Relation features with visual cues to enhance anomaly comprehension from
> video. Specifically, VADER first applies an Anomaly Scorer to assign per-frame
> anomaly scores, followed by a Context-AwarE Sampling (CAES) strategy to capture
> the causal context of each anomalous event. A Relation Feature Extractor and a
> COntrastive Relation Encoder (CORE) jointly model dynamic object interactions,
> producing compact relational representations for downstream reasoning. These
> visual and relational cues are integrated with LLMs to generate detailed,
> causally grounded descriptions and support robust anomaly-related question
> answering. Experiments on multiple real-world VAU benchmarks demonstrate that
> VADER achieves strong results across anomaly description, explanation, and
> causal reasoning tasks, advancing the frontier of explainable video anomaly
> analysis.

