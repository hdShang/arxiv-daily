---
layout: default
title: SIMS-V: Simulated Instruction-Tuning for Spatial Video Understanding
---

# SIMS-V: Simulated Instruction-Tuning for Spatial Video Understanding

**arXiv**: [2511.04668v1](https://arxiv.org/abs/2511.04668) | [PDF](https://arxiv.org/pdf/2511.04668.pdf)

**作者**: Ellis Brown, Arijit Ray, Ranjay Krishna, Ross Girshick, Rob Fergus, Saining Xie

---

## 💡 一句话要点

**提出SIMS-V框架，利用3D模拟器生成空间视频数据以解决多模态模型空间推理不足问题**

**关键词**: `空间视频理解` `模拟数据生成` `多模态语言模型` `空间推理` `指令微调`

## 📋 核心要点

1. 多模态语言模型在时空空间推理方面存在困难，真实视频数据标注稀缺是瓶颈
2. 使用3D模拟器生成空间丰富视频数据，通过系统消融识别三种关键问题类型
3. 在7B参数模型上仅用25K模拟数据微调，超越大基线并在真实基准上表现优异

## 📄 摘要（原文）

> Despite impressive high-level video comprehension, multimodal language models
> struggle with spatial reasoning across time and space. While current spatial
> training approaches rely on real-world video data, obtaining diverse footage
> with precise spatial annotations remains a bottleneck. To alleviate this
> bottleneck, we present SIMS-V -- a systematic data-generation framework that
> leverages the privileged information of 3D simulators to create spatially-rich
> video training data for multimodal language models. Using this framework, we
> investigate which properties of simulated data drive effective real-world
> transfer through systematic ablations of question types, mixes, and scales. We
> identify a minimal set of three question categories (metric measurement,
> perspective-dependent reasoning, and temporal tracking) that prove most
> effective for developing transferable spatial intelligence, outperforming
> comprehensive coverage despite using fewer question types. These insights
> enable highly efficient training: our 7B-parameter video LLM fine-tuned on just
> 25K simulated examples outperforms the larger 72B baseline and achieves
> competitive performance with proprietary models on rigorous real-world spatial
> reasoning benchmarks. Our approach demonstrates robust generalization,
> maintaining performance on general video understanding while showing
> substantial improvements on embodied and real-world spatial tasks.

