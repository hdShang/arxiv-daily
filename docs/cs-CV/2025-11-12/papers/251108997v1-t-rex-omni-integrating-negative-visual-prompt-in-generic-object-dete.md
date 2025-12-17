---
layout: default
title: T-Rex-Omni: Integrating Negative Visual Prompt in Generic Object Detection
---

# T-Rex-Omni: Integrating Negative Visual Prompt in Generic Object Detection

**arXiv**: [2511.08997v1](https://arxiv.org/abs/2511.08997) | [PDF](https://arxiv.org/pdf/2511.08997.pdf)

**作者**: Jiazhou Zhou, Qing Jiang, Kanghao Chen, Lutao Jiang, Yuanhuiyi Lyu, Ying-Cong Chen, Lei Zhang

---

## 💡 一句话要点

**提出T-Rex-Omni框架，通过负视觉提示解决开放集目标检测中的干扰物问题**

**关键词**: `开放集目标检测` `负视觉提示` `零样本检测` `长尾场景` `视觉提示编码器`

## 📋 核心要点

1. 开放集目标检测仅依赖正提示，易受视觉相似但语义不同的干扰物影响
2. 引入统一视觉提示编码器、训练免费负计算模块和负铰链损失，增强判别性
3. 零样本检测性能显著提升，在长尾场景LVIS-minival上达51.2 AP_r

## 📄 摘要（原文）

> Object detection methods have evolved from closed-set to open-set paradigms over the years. Current open-set object detectors, however, remain constrained by their exclusive reliance on positive indicators based on given prompts like text descriptions or visual exemplars. This positive-only paradigm experiences consistent vulnerability to visually similar but semantically different distractors. We propose T-Rex-Omni, a novel framework that addresses this limitation by incorporating negative visual prompts to negate hard negative distractors. Specifically, we first introduce a unified visual prompt encoder that jointly processes positive and negative visual prompts. Next, a training-free Negating Negative Computing (NNC) module is proposed to dynamically suppress negative responses during the probability computing stage. To further boost performance through fine-tuning, our Negating Negative Hinge (NNH) loss enforces discriminative margins between positive and negative embeddings. T-Rex-Omni supports flexible deployment in both positive-only and joint positive-negative inference modes, accommodating either user-specified or automatically generated negative examples. Extensive experiments demonstrate remarkable zero-shot detection performance, significantly narrowing the performance gap between visual-prompted and text-prompted methods while showing particular strength in long-tailed scenarios (51.2 AP_r on LVIS-minival). This work establishes negative prompts as a crucial new dimension for advancing open-set visual recognition systems.

