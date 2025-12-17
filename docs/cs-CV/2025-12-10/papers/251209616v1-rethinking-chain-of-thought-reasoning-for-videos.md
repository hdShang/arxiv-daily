---
layout: default
title: Rethinking Chain-of-Thought Reasoning for Videos
---

# Rethinking Chain-of-Thought Reasoning for Videos

**arXiv**: [2512.09616v1](https://arxiv.org/abs/2512.09616) | [PDF](https://arxiv.org/pdf/2512.09616.pdf)

**作者**: Yiwu Zhong, Zi-Yuan Hu, Yin Li, Liwei Wang

---

## 💡 一句话要点

**提出高效后训练与推理框架，通过压缩视觉令牌和简洁推理链提升视频多模态大语言模型的推理效率与性能。**

**关键词**: `视频推理` `多模态大语言模型` `推理效率` `视觉令牌压缩` `后训练框架`

## 📋 核心要点

1. 核心问题：现有视频多模态大语言模型依赖冗长推理链和大量视觉令牌，效率低下。
2. 方法要点：设计框架压缩视觉令牌并生成简洁推理轨迹，无需人工标注或监督微调。
3. 实验或效果：在多个基准测试中实现显著推理效率提升和竞争性性能表现。

## 📄 摘要（原文）

> Chain-of-thought (CoT) reasoning has been highly successful in solving complex tasks in natural language processing, and recent multimodal large language models (MLLMs) have extended this paradigm to video reasoning. However, these models typically build on lengthy reasoning chains and large numbers of input visual tokens. Motivated by empirical observations from our benchmark study, we hypothesize that concise reasoning combined with a reduced set of visual tokens can be sufficient for effective video reasoning. To evaluate this hypothesis, we design and validate an efficient post-training and inference framework that enhances a video MLLM's reasoning capability. Our framework enables models to operate on compressed visual tokens and generate brief reasoning traces prior to answering. The resulting models achieve substantially improved inference efficiency, deliver competitive performance across diverse benchmarks, and avoid reliance on manual CoT annotations or supervised fine-tuning. Collectively, our results suggest that long, human-like CoT reasoning may not be necessary for general video reasoning, and that concise reasoning can be both effective and efficient. Our code will be released at https://github.com/LaVi-Lab/Rethink_CoT_Video.

