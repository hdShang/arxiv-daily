---
layout: default
title: An Automated Tip-and-Cue Framework for Optimized Satellite Tasking and Visual Intelligence
---

# An Automated Tip-and-Cue Framework for Optimized Satellite Tasking and Visual Intelligence

**arXiv**: [2512.09670v1](https://arxiv.org/abs/2512.09670) | [PDF](https://arxiv.org/pdf/2512.09670.pdf)

**作者**: Gil Weissman, Amir Ivry, Israel Cohen

---

## 💡 一句话要点

**提出自动化Tip-and-Cue框架以优化卫星任务调度与视觉智能分析**

**关键词**: `卫星任务调度` `自动化地球观测` `视觉智能分析` `船舶追踪` `AI模型集成`

## 📋 核心要点

1. 核心问题：卫星星座增多，需自动化任务调度与视觉分析以提升地球观测效率
2. 方法要点：基于外部数据生成提示，优化任务调度，结合AI模型处理图像生成结构化报告
3. 实验或效果：通过船舶追踪场景验证，利用AIS数据预测轨迹并生成可操作输出

## 📄 摘要（原文）

> The proliferation of satellite constellations, coupled with reduced tasking latency and diverse sensor capabilities, has expanded the opportunities for automated Earth observation. This paper introduces a fully automated Tip-and-Cue framework designed for satellite imaging tasking and scheduling. In this context, tips are generated from external data sources or analyses of prior satellite imagery, identifying spatiotemporal targets and prioritizing them for downstream planning. Corresponding cues are the imaging tasks formulated in response, which incorporate sensor constraints, timing requirements, and utility functions. The system autonomously generates candidate tasks, optimizes their scheduling across multiple satellites using continuous utility functions that reflect the expected value of each observation, and processes the resulting imagery using artificial-intelligence-based models, including object detectors and vision-language models. Structured visual reports are generated to support both interpretability and the identification of new insights for downstream tasking. The efficacy of the framework is demonstrated through a maritime vessel tracking scenario, utilizing Automatic Identification System (AIS) data for trajectory prediction, targeted observations, and the generation of actionable outputs. Maritime vessel tracking is a widely researched application, often used to benchmark novel approaches to satellite tasking, forecasting, and analysis. The system is extensible to broader applications such as smart-city monitoring and disaster response, where timely tasking and automated analysis are critical.

