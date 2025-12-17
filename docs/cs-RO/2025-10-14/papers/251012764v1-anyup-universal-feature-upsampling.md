---
layout: default
title: AnyUp: Universal Feature Upsampling
---

# AnyUp: Universal Feature Upsampling

**arXiv**: [2510.12764v1](https://arxiv.org/abs/2510.12764) | [PDF](https://arxiv.org/pdf/2510.12764.pdf)

**作者**: Thomas Wimmer, Prune Truong, Marie-Julie Rakotosaona, Michael Oechsle, Federico Tombari, Bernt Schiele, Jan Eric Lenssen

---

## 💡 一句话要点

**提出AnyUp方法，实现通用特征上采样，无需特定编码器训练。**

**关键词**: `特征上采样` `通用方法` `推理时优化` `计算机视觉` `语义保持`

## 📋 核心要点

1. 现有基于学习的特征上采样方法需为每个特征提取器重新训练，缺乏通用性。
2. AnyUp采用推理时特征无关的上采样架构，提升上采样质量和语义保持。
3. 实验显示AnyUp在多种特征类型上达到新SOTA，高效适用于下游任务。

## 📄 摘要（原文）

> We introduce AnyUp, a method for feature upsampling that can be applied to
> any vision feature at any resolution, without encoder-specific training.
> Existing learning-based upsamplers for features like DINO or CLIP need to be
> re-trained for every feature extractor and thus do not generalize to different
> feature types at inference time. In this work, we propose an inference-time
> feature-agnostic upsampling architecture to alleviate this limitation and
> improve upsampling quality. In our experiments, AnyUp sets a new state of the
> art for upsampled features, generalizes to different feature types, and
> preserves feature semantics while being efficient and easy to apply to a wide
> range of downstream tasks.

