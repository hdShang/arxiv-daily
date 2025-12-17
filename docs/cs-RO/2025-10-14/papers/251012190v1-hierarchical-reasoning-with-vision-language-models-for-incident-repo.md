---
layout: default
title: Hierarchical Reasoning with Vision-Language Models for Incident Reports from Dashcam Videos
---

# Hierarchical Reasoning with Vision-Language Models for Incident Reports from Dashcam Videos

**arXiv**: [2510.12190v1](https://arxiv.org/abs/2510.12190) | [PDF](https://arxiv.org/pdf/2510.12190.pdf)

**作者**: Shingo Yokoi, Kento Sasaki, Yu Yamaguchi

---

## 💡 一句话要点

**提出分层推理框架，用于从行车记录仪视频生成事故报告。**

**关键词**: `视觉语言模型` `分层推理` `事故报告生成` `行车记录仪视频` `模型集成`

## 📋 核心要点

1. 核心问题：自动驾驶模型在分布外场景中理解危险事件困难。
2. 方法要点：集成帧级描述、事故帧检测和细粒度推理于视觉语言模型。
3. 实验或效果：在2COOOL挑战中排名第2，CIDEr-D得分最高。

## 📄 摘要（原文）

> Recent advances in end-to-end (E2E) autonomous driving have been enabled by
> training on diverse large-scale driving datasets, yet autonomous driving models
> still struggle in out-of-distribution (OOD) scenarios. The COOOL benchmark
> targets this gap by encouraging hazard understanding beyond closed taxonomies,
> and the 2COOOL challenge extends it to generating human-interpretable incident
> reports. We present a hierarchical reasoning framework for incident report
> generation from dashcam videos that integrates frame-level captioning, incident
> frame detection, and fine-grained reasoning within vision-language models
> (VLMs). We further improve factual accuracy and readability through model
> ensembling and a Blind A/B Scoring selection protocol. On the official 2COOOL
> open leaderboard, our method ranks 2nd among 29 teams and achieves the best
> CIDEr-D score, producing accurate and coherent incident narratives. These
> results indicate that hierarchical reasoning with VLMs is a promising direction
> for accident analysis and for broader understanding of safety-critical traffic
> events. The implementation and code are available at
> https://github.com/riron1206/kaggle-2COOOL-2nd-Place-Solution.

