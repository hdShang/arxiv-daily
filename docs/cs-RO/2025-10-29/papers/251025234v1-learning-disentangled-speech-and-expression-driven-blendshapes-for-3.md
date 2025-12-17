---
layout: default
title: Learning Disentangled Speech- and Expression-Driven Blendshapes for 3D Talking Face Animation
---

# Learning Disentangled Speech- and Expression-Driven Blendshapes for 3D Talking Face Animation

**arXiv**: [2510.25234v1](https://arxiv.org/abs/2510.25234) | [PDF](https://arxiv.org/pdf/2510.25234.pdf)

**作者**: Yuxiang Mao, Zhijie Zhang, Zhiheng Zhang, Jiawei Liu, Chen Zeng, Shihong Xia

---

## 💡 一句话要点

**提出解耦语音与表情驱动的混合形状方法，以生成情感丰富的3D说话人脸动画。**

**关键词**: `3D面部动画` `语音驱动动画` `表情解耦` `混合形状学习` `稀疏约束` `FLAME模型映射`

## 📋 核心要点

1. 核心问题：缺乏真实情感3D说话人脸数据，难以生成情感表达的面部动画。
2. 方法要点：利用线性加法建模，结合稀疏约束损失学习解耦的语音和表情混合形状。
3. 实验或效果：通过感知研究验证，在保持唇同步准确性的同时提升情感表达性。

## 📄 摘要（原文）

> Expressions are fundamental to conveying human emotions. With the rapid
> advancement of AI-generated content (AIGC), realistic and expressive 3D facial
> animation has become increasingly crucial. Despite recent progress in
> speech-driven lip-sync for talking-face animation, generating emotionally
> expressive talking faces remains underexplored. A major obstacle is the
> scarcity of real emotional 3D talking-face datasets due to the high cost of
> data capture. To address this, we model facial animation driven by both speech
> and emotion as a linear additive problem. Leveraging a 3D talking-face dataset
> with neutral expressions (VOCAset) and a dataset of 3D expression sequences
> (Florence4D), we jointly learn a set of blendshapes driven by speech and
> emotion. We introduce a sparsity constraint loss to encourage disentanglement
> between the two types of blendshapes while allowing the model to capture
> inherent secondary cross-domain deformations present in the training data. The
> learned blendshapes can be further mapped to the expression and jaw pose
> parameters of the FLAME model, enabling the animation of 3D Gaussian avatars.
> Qualitative and quantitative experiments demonstrate that our method naturally
> generates talking faces with specified expressions while maintaining accurate
> lip synchronization. Perceptual studies further show that our approach achieves
> superior emotional expressivity compared to existing methods, without
> compromising lip-sync quality.

