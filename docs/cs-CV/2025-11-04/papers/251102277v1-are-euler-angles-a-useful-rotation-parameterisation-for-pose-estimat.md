---
layout: default
title: Are Euler angles a useful rotation parameterisation for pose estimation with Normalizing Flows?
---

# Are Euler angles a useful rotation parameterisation for pose estimation with Normalizing Flows?

**arXiv**: [2511.02277v1](https://arxiv.org/abs/2511.02277) | [PDF](https://arxiv.org/pdf/2511.02277.pdf)

**作者**: Giorgos Sfikas, Konstantina Nikolaidou, Foteini Papadopoulou, George Retsinas, Anastasios L. Kesidis

---

## 💡 一句话要点

**评估欧拉角作为归一化流姿态估计参数化的有效性**

**关键词**: `姿态估计` `归一化流` `欧拉角` `概率模型` `3D计算机视觉`

## 📋 核心要点

1. 核心问题：欧拉角是否适合作为概率姿态估计的参数化方法
2. 方法要点：使用归一化流模型，比较欧拉角与复杂参数化的表现
3. 实验或效果：未知具体结果，但探讨欧拉角在特定场景下的潜在优势

## 📄 摘要（原文）

> Object pose estimation is a task that is of central importance in 3D Computer
> Vision. Given a target image and a canonical pose, a single point estimate may
> very often be sufficient; however, a probabilistic pose output is related to a
> number of benefits when pose is not unambiguous due to sensor and projection
> constraints or inherent object symmetries. With this paper, we explore the
> usefulness of using the well-known Euler angles parameterisation as a basis for
> a Normalizing Flows model for pose estimation. Isomorphic to spatial rotation,
> 3D pose has been parameterized in a number of ways, either in or out of the
> context of parameter estimation. We explore the idea that Euler angles, despite
> their shortcomings, may lead to useful models in a number of aspects, compared
> to a model built on a more complex parameterisation.

