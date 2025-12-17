---
layout: default
title: R-AVST: Empowering Video-LLMs with Fine-Grained Spatio-Temporal Reasoning in Complex Audio-Visual Scenarios
---

# R-AVST: Empowering Video-LLMs with Fine-Grained Spatio-Temporal Reasoning in Complex Audio-Visual Scenarios

**arXiv**: [2511.16901v1](https://arxiv.org/abs/2511.16901) | [PDF](https://arxiv.org/pdf/2511.16901.pdf)

**作者**: Lu Zhu, Tiantian Geng, Yangye Chen, Teng Wang, Ping Lu, Feng Zheng

---

## 💡 一句话要点

**提出R-AVST数据集与AVST-Zero模型以增强复杂视听场景中的细粒度时空推理**

**关键词**: `视听时空推理` `多模态大语言模型` `强化学习` `数据集构建` `视频理解` `细粒度标注`

## 📋 核心要点

1. 当前多模态大模型在复杂真实世界视听事件中表现不足，缺乏细粒度时空推理能力。
2. 构建R-AVST数据集，含5K视频与27K对象，并定义三个核心任务生成8K问答对。
3. 提出AVST-Zero模型，基于强化学习优化行为，实验显示在R-AVST上性能优越。

## 📄 摘要（原文）

> Recently, rapid advancements have been made in multimodal large language models (MLLMs), especially in video understanding tasks. However, current research focuses on simple video scenarios, failing to reflect the complex and diverse nature of real-world audio-visual events in videos. To bridge this gap, we firstly introduce R-AVST, a dataset for audio-visual reasoning featuring fine-grained spatio-temporal annotations. In constructing this, we design a pipeline consisting of LLM-based key object extraction, automatic spatial annotation and manual quality inspection, resulting in over 5K untrimmed videos with 27K objects across 100 types of audio-visual events. Building on this dataset, we define three core tasks for spatio-temporal reasoning in audio-visual scenes and generate more than 8K high-quality, evenly distributed question-answer pairs to effectively benchmark model performance. To further enhance reasoning, we propose AVST-Zero, a reinforcement learning-based model that avoids intermediate supervision, directly optimizing behavior via carefully designed multi-dimensional rewards. Extensive experiments validate the effectiveness of our R-AVST in advancing audio-visual spatio-temporal reasoning, upon which AVST-Zero demonstrates competitive performance compared to existing models. To the best of our knowledge, R-AVST is the first dataset designed for real-world audio-visual spatio-temporal reasoning, and AVST-Zero offers a novel perspective for tackling future challenges in this domain.

