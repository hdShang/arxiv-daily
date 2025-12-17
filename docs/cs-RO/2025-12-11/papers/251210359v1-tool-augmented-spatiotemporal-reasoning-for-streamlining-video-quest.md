---
layout: default
title: Tool-Augmented Spatiotemporal Reasoning for Streamlining Video Question Answering Task
---

# Tool-Augmented Spatiotemporal Reasoning for Streamlining Video Question Answering Task

**arXiv**: [2512.10359v1](https://arxiv.org/abs/2512.10359) | [PDF](https://arxiv.org/pdf/2512.10359.pdf)

**作者**: Sunqi Fan, Jiashuo Cui, Meng-Hao Guo, Shuojin Yang

---

## 💡 一句话要点

**提出STAR框架与视频工具包以增强多模态大语言模型在视频问答中的时空推理能力**

**关键词**: `视频问答` `时空推理` `多模态大语言模型` `工具增强` `视频分析`

## 📋 核心要点

1. 现有MLLMs在复杂视频问答中难以同时建模空间关系与时间动态因果推理
2. 引入可扩展视频工具包，通过STAR框架策略调度时空工具逐步定位关键区域
3. 在VideoMME和LongVideoBench基准上分别实现8.2%和4.6%的性能提升

## 📄 摘要（原文）

> Video Question Answering (VideoQA) task serves as a critical playground for evaluating whether foundation models can effectively perceive, understand, and reason about dynamic real-world scenarios. However, existing Multimodal Large Language Models (MLLMs) struggle with simultaneously modeling spatial relationships within video frames and understanding the causal dynamics of temporal evolution on complex and reasoning-intensive VideoQA task. In this work, we equip MLLM with a comprehensive and extensible Video Toolkit, to enhance MLLM's spatiotemporal reasoning capabilities and ensure the harmony between the quantity and diversity of tools. To better control the tool invocation sequence and avoid toolchain shortcut issues, we propose a Spatiotemporal Reasoning Framework (STAR) that strategically schedules temporal and spatial tools, thereby progressively localizing the key area in the video. Our STAR framework enhances GPT-4o using lightweight tools, achieving an 8.2% gain on VideoMME and 4.6% on LongVideoBench. We believe that our proposed Video Toolkit and STAR framework make an important step towards building autonomous and intelligent video analysis assistants. The code is publicly available at https://github.com/fansunqi/VideoTool.

