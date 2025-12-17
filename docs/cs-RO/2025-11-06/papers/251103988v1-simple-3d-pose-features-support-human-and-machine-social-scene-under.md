---
layout: default
title: Simple 3D Pose Features Support Human and Machine Social Scene Understanding
---

# Simple 3D Pose Features Support Human and Machine Social Scene Understanding

**arXiv**: [2511.03988v1](https://arxiv.org/abs/2511.03988) | [PDF](https://arxiv.org/pdf/2511.03988.pdf)

**作者**: Wenshuo Qin, Leyla Isik

---

## 💡 一句话要点

**提出3D社交姿态特征以提升人机社交场景理解性能**

**关键词**: `3D姿态估计` `社交交互识别` `视觉特征提取` `人类行为理解` `AI视觉模型`

## 📋 核心要点

1. 核心问题：人类社交交互识别在AI视觉系统中仍具挑战，可能因缺乏3D姿态信息。
2. 方法要点：结合姿态与深度估计算法提取3D关节位置，并推导紧凑3D社交姿态特征。
3. 实验或效果：3D姿态特征优于多数AI模型，并提升现成模型性能，匹配人类判断。

## 📄 摘要（原文）

> Humans can quickly and effortlessly extract a variety of information about
> others' social interactions from visual input, ranging from visuospatial cues
> like whether two people are facing each other to higher-level information. Yet,
> the computations supporting these abilities remain poorly understood, and
> social interaction recognition continues to challenge even the most advanced AI
> vision systems. Here, we hypothesized that humans rely on 3D visuospatial pose
> information to make social interaction judgments, which is absent in most AI
> vision models. To test this, we combined state-of-the-art pose and depth
> estimation algorithms to extract 3D joint positions of people in short video
> clips depicting everyday human actions and compared their ability to predict
> human social interaction judgments with current AI vision models. Strikingly,
> 3D joint positions outperformed most current AI vision models, revealing that
> key social information is available in explicit body position but not in the
> learned features of most vision models, including even the layer-wise
> embeddings of the pose models used to extract joint positions. To uncover the
> critical pose features humans use to make social judgments, we derived a
> compact set of 3D social pose features describing only the 3D position and
> direction of faces in the videos. We found that these minimal descriptors
> matched the predictive strength of the full set of 3D joints and significantly
> improved the performance of off-the-shelf AI vision models when combined with
> their embeddings. Moreover, the degree to which 3D social pose features were
> represented in each off-the-shelf AI vision model predicted the model's ability
> to match human social judgments. Together, our findings provide strong evidence
> that human social scene understanding relies on explicit representations of 3D
> pose and can be supported by simple, structured visuospatial primitives.

