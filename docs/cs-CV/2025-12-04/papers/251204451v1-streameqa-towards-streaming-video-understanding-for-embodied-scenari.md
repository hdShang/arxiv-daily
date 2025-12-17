---
layout: default
title: StreamEQA: Towards Streaming Video Understanding for Embodied Scenarios
---

# StreamEQA: Towards Streaming Video Understanding for Embodied Scenarios

**arXiv**: [2512.04451v1](https://arxiv.org/abs/2512.04451) | [PDF](https://arxiv.org/pdf/2512.04451.pdf)

**作者**: Yifei Wang, Zhenkai Li, Tianwen Qian, Huanran Zheng, Zheng Wang, Yuqian Fu, Xiaoling Wang

---

## 💡 一句话要点

**提出StreamEQA基准以评估具身场景下的流式视频理解能力**

**关键词**: `流式视频理解` `具身智能` `视频问答基准` `长视频分析` `多模态大语言模型`

## 📋 核心要点

1. 核心问题：具身智能需在流式视频中持续感知与推理，现有模型能力不足
2. 方法要点：构建首个具身流式视频问答基准，涵盖感知、交互、规划三个层次
3. 实验或效果：评估13个先进模型，发现其在流式视频理解上仍面临挑战

## 📄 摘要（原文）

> As embodied intelligence advances toward real-world deployment, the ability to continuously perceive and reason over streaming visual inputs becomes essential. In such settings, an agent must maintain situational awareness of its environment, comprehend the interactions with surrounding entities, and dynamically plan actions informed by past observations, current contexts, and anticipated future events. To facilitate progress in this direction, we introduce StreamEQA, the first benchmark designed for streaming video question answering in embodied scenarios. StreamEQA evaluates existing MLLMs along two orthogonal dimensions: Embodied and Streaming. Along the embodied dimension, we categorize the questions into three levels: perception, interaction, and planning, which progressively assess a model's ability to recognize fine-grained visual details, reason about agent-object interactions, and perform high-level goal-directed reasoning. For the streaming dimension, questions are divided into backward, real-time, and forward reasoning, with each mode relying on a distinct temporal context. Built upon 156 independent long videos, StreamEQA defines 42 tasks and generates approximately 21K question-answer pairs with precise timestamps through a hybrid pipeline combining automated generation and human refinement. Evaluations of 13 state-of-the-art video-LLMs reveal that, despite strong performance on conventional benchmarks, these models still struggle with streaming video understanding in embodied scenarios. We hope StreamEQA will catalyze research on streaming video understanding for embodied applications.

