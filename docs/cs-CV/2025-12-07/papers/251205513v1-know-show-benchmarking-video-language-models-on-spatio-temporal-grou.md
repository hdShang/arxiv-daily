---
layout: default
title: Know-Show: Benchmarking Video-Language Models on Spatio-Temporal Grounded Reasoning
---

# Know-Show: Benchmarking Video-Language Models on Spatio-Temporal Grounded Reasoning

**arXiv**: [2512.05513v1](https://arxiv.org/abs/2512.05513) | [PDF](https://arxiv.org/pdf/2512.05513.pdf)

**作者**: Chinthani Sugandhika, Chen Li, Deepu Rajan, Basura Fernando

---

## 💡 一句话要点

**提出Know-Show基准与GRAM插件，评估并增强视频语言模型的时空基础推理能力。**

**关键词**: `视频语言模型` `时空基础推理` `基准评估` `注意力机制` `多模态理解`

## 📋 核心要点

1. 核心问题：现有视频语言模型在时空基础推理方面存在显著差距，难以同时推理动作语义并基于视觉和时间证据进行定位。
2. 方法要点：构建Know-Show基准，整合五个互补场景，并设计GRAM插件，通过注意力视频令牌选择和显式时间戳编码实现细粒度基础。
3. 实验或效果：在多个开放和封闭模型上测试，揭示模型在细粒度手物交互等任务中的不足，GRAM能有效提升基础推理性能。

## 📄 摘要（原文）

> Large Video-Language Models (Video-LMs) have achieved impressive progress in multimodal understanding, yet their reasoning remains weakly grounded in space and time. We present Know-Show, a new benchmark designed to evaluate spatio-temporal grounded reasoning, the ability of a model to reason about actions and their semantics while simultaneously grounding its inferences in visual and temporal evidence. Know-Show unifies reasoning and localization within a single evaluation framework consisting of five complementary scenarios across spatial (person, object, person-object, and hand-object) and temporal dimensions. Built from Charades, Action Genome, and Ego4D with 2.5K human-authored questions, the benchmark exposes significant gaps between current Video-LMs and human reasoning. To bridge this gap, we propose GRAM, a training-free plug-in that augments Video-LMs with fine-grained grounding through attention-based video token selection and explicit timestamp encoding. Extensive experiments across open and closed Video-LMs (Qwen, VideoLLaVA, GPT-4o, and Gemini, etc.) reveal that existing models struggle to "show what they know" and vice versa, especially in fine-grained hand-object interactions. Know-Show establishes a unified standard for assessing grounded reasoning in video-language understanding and provides insights toward developing interpretable and reliable multimodal reasoning systems. We will release the code at https://github.com/LUNAProject22/Know-Show.

