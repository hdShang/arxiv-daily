---
layout: default
title: Video-CoM: Interactive Video Reasoning via Chain of Manipulations
---

# Video-CoM: Interactive Video Reasoning via Chain of Manipulations

**arXiv**: [2511.23477v1](https://arxiv.org/abs/2511.23477) | [PDF](https://arxiv.org/pdf/2511.23477.pdf)

**作者**: Hanoona Rasheed, Mohammed Zumri, Muhammad Maaz, Ming-Hsuan Yang, Fahad Shahbaz Khan, Salman Khan

---

## 💡 一句话要点

**提出Video-CoM模型，通过操作链实现交互式视频推理，以解决现有模型被动处理视频导致的语义瓶颈问题。**

**关键词**: `交互式视频推理` `操作链` `多模态大语言模型` `强化学习优化` `视频理解基准`

## 📋 核心要点

1. 核心问题：现有多模态大语言模型在视频理解中被动编码视频，无法动态重看或验证证据，限制了细粒度时空推理。
2. 方法要点：引入交互式视频推理范式，模型通过操作链执行迭代视觉动作，并利用强化学习优化策略，结合步骤级推理奖励。
3. 实验或效果：在九个视频推理基准上表现优异，平均性能提升3.6%，训练数据量显著少于可比大规模模型。

## 📄 摘要（原文）

> Recent multimodal large language models (MLLMs) have advanced video understanding, yet most still "think about videos" ie once a video is encoded, reasoning unfolds entirely in text, treating visual input as a static context. This passive paradigm creates a semantic bottleneck: models cannot rewatch, refocus, or verify evidence, leading to shallow visual reasoning on tasks requiring fine grained spatio temporal understanding. In this work, we introduce Interactive Video Reasoning, a new paradigm that transforms video into an active cognitive workspace, enabling models to "think with videos". Our model, Video CoM, reasons through a Chain of Manipulations (CoM), performing iterative visual actions to gather and refine evidence. To support this behavior, we construct Video CoM Instruct, an 18K instruction tuning dataset curated for multi step manipulation reasoning. Beyond supervised learning, we further optimize the manipulation policy via reinforcement learning with reasoning aware Group Relative Policy Optimization (GRPO). Unlike prior work that relies solely on sparse answer rewards, our method introduces step level reasoning rewards, guiding the model toward grounded and consistent reasoning. Video CoM achieves strong results across nine video reasoning benchmarks, improving average performance by 3.6 percent over recent state of the art models, while training on only 25K SFT and 3K GRPO video samples, significantly fewer than comparable large scale models. Ablation studies demonstrate that reasoning aware rewards improve both accuracy and interpretability. Code: https://github.com/mbzuai-oryx/Video-CoM

