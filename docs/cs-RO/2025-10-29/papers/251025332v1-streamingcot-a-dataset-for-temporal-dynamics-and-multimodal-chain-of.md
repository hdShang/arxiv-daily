---
layout: default
title: StreamingCoT: A Dataset for Temporal Dynamics and Multimodal Chain-of-Thought Reasoning in Streaming VideoQA
---

# StreamingCoT: A Dataset for Temporal Dynamics and Multimodal Chain-of-Thought Reasoning in Streaming VideoQA

**arXiv**: [2510.25332v1](https://arxiv.org/abs/2510.25332) | [PDF](https://arxiv.org/pdf/2510.25332.pdf)

**作者**: Yuhang Hu, Zhenyu Yang, Shihan Wang, Shengsheng Qian, Bin Wen, Fan Yang, Tingting Gao, Changsheng Xu

---

## 💡 一句话要点

**提出StreamingCoT数据集以解决流视频问答中动态推理和解释性不足的问题**

**关键词**: `流视频问答` `多模态推理` `时间动态理解` `链式思维` `数据集构建`

## 📋 核心要点

1. 核心问题：现有VideoQA数据集缺乏动态答案标注和显式推理过程，限制模型对时间演化的理解
2. 方法要点：构建动态分层标注架构，生成每秒描述和语义段，并提取基于对象状态转换的推理链
3. 实验或效果：未知，但数据集为流视频理解、复杂推理和多模态推断研究提供基础

## 📄 摘要（原文）

> The rapid growth of streaming video applications demands multimodal models
> with enhanced capabilities for temporal dynamics understanding and complex
> reasoning. However, current Video Question Answering (VideoQA) datasets suffer
> from two critical limitations: 1) Static annotation mechanisms fail to capture
> the evolving nature of answers in temporal video streams, and 2) The absence of
> explicit reasoning process annotations restricts model interpretability and
> logical deduction capabilities. To address these challenges, We introduce
> StreamingCoT, the first dataset explicitly designed for temporally evolving
> reasoning in streaming VideoQA and multimodal Chain-of-Thought (CoT) tasks. Our
> framework first establishes a dynamic hierarchical annotation architecture that
> generates per-second dense descriptions and constructs temporally-dependent
> semantic segments through similarity fusion, paired with question-answer sets
> constrained by temporal evolution patterns. We further propose an explicit
> reasoning chain generation paradigm that extracts spatiotemporal objects via
> keyframe semantic alignment, derives object state transition-based reasoning
> paths using large language models, and ensures logical coherence through
> human-verified validation. This dataset establishes a foundation for advancing
> research in streaming video understanding, complex temporal reasoning, and
> multimodal inference. Our StreamingCoT and its construction toolkit can be
> accessed at https://github.com/Fleeting-hyh/StreamingCoT.

