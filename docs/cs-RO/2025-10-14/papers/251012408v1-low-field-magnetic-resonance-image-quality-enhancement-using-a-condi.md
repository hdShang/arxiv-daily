---
layout: default
title: Low-Field Magnetic Resonance Image Quality Enhancement using a Conditional Flow Matching Model
---

# Low-Field Magnetic Resonance Image Quality Enhancement using a Conditional Flow Matching Model

**arXiv**: [2510.12408v1](https://arxiv.org/abs/2510.12408) | [PDF](https://arxiv.org/pdf/2510.12408.pdf)

**作者**: Huu Tien Nguyen, Ahmed Karam Eldaly

---

## 💡 一句话要点

**提出条件流匹配模型以增强低场磁共振图像质量**

**关键词**: `条件流匹配` `磁共振成像重建` `图像质量增强` `低场MRI` `生成模型`

## 📋 核心要点

1. 低场磁共振成像信号噪声比低，诊断质量差
2. 使用条件流匹配直接回归最优速度场，学习噪声到目标的连续流
3. 实验显示性能领先，泛化强，参数少，适用于资源有限环境

## 📄 摘要（原文）

> This paper introduces a novel framework for image quality transfer based on
> conditional flow matching (CFM). Unlike conventional generative models that
> rely on iterative sampling or adversarial objectives, CFM learns a continuous
> flow between a noise distribution and target data distributions through the
> direct regression of an optimal velocity field. We evaluate this approach in
> the context of low-field magnetic resonance imaging (LF-MRI), a rapidly
> emerging modality that offers affordable and portable scanning but suffers from
> inherently low signal-to-noise ratio and reduced diagnostic quality. Our
> framework is designed to reconstruct high-field-like MR images from their
> corresponding low-field inputs, thereby bridging the quality gap without
> requiring expensive infrastructure. Experiments demonstrate that CFM not only
> achieves state-of-the-art performance, but also generalizes robustly to both
> in-distribution and out-of-distribution data. Importantly, it does so while
> utilizing significantly fewer parameters than competing deep learning methods.
> These results underline the potential of CFM as a powerful and scalable tool
> for MRI reconstruction, particularly in resource-limited clinical environments.

