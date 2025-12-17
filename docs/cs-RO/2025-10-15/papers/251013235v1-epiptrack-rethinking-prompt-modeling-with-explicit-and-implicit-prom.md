---
layout: default
title: EPIPTrack: Rethinking Prompt Modeling with Explicit and Implicit Prompts for Multi-Object Tracking
---

# EPIPTrack: Rethinking Prompt Modeling with Explicit and Implicit Prompts for Multi-Object Tracking

**arXiv**: [2510.13235v1](https://arxiv.org/abs/2510.13235) | [PDF](https://arxiv.org/pdf/2510.13235.pdf)

**作者**: Yukuan Zhang, Jiarui Zhao, Shangqing Nie, Jin Kuang, Shengsheng Wang

---

## 💡 一句话要点

**提出EPIPTrack框架，利用显式和隐式提示解决多目标跟踪中语义提示适应性不足问题。**

**关键词**: `多目标跟踪` `视觉语言框架` `显式提示` `隐式提示` `动态建模` `语义对齐`

## 📋 核心要点

1. 现有方法依赖静态文本描述，缺乏对目标状态变化的适应性且易产生幻觉。
2. EPIPTrack通过显式提示转换运动信息为语言，隐式提示构建个性化知识表示，动态调整响应变化。
3. 在MOT17、MOT20和DanceTrack数据集上实验，表现优于现有跟踪器，具有强适应性和高性能。

## 📄 摘要（原文）

> Multimodal semantic cues, such as textual descriptions, have shown strong
> potential in enhancing target perception for tracking. However, existing
> methods rely on static textual descriptions from large language models, which
> lack adaptability to real-time target state changes and prone to
> hallucinations. To address these challenges, we propose a unified multimodal
> vision-language tracking framework, named EPIPTrack, which leverages explicit
> and implicit prompts for dynamic target modeling and semantic alignment.
> Specifically, explicit prompts transform spatial motion information into
> natural language descriptions to provide spatiotemporal guidance. Implicit
> prompts combine pseudo-words with learnable descriptors to construct
> individualized knowledge representations capturing appearance attributes. Both
> prompts undergo dynamic adjustment via the CLIP text encoder to respond to
> changes in target state. Furthermore, we design a Discriminative Feature
> Augmentor to enhance visual and cross-modal representations. Extensive
> experiments on MOT17, MOT20, and DanceTrack demonstrate that EPIPTrack
> outperforms existing trackers in diverse scenarios, exhibiting robust
> adaptability and superior performance.

