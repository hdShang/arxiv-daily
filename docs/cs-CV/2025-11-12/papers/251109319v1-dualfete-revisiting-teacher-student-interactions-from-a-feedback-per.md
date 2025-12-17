---
layout: default
title: DualFete: Revisiting Teacher-Student Interactions from a Feedback Perspective for Semi-supervised Medical Image Segmentation
---

# DualFete: Revisiting Teacher-Student Interactions from a Feedback Perspective for Semi-supervised Medical Image Segmentation

**arXiv**: [2511.09319v1](https://arxiv.org/abs/2511.09319) | [PDF](https://arxiv.org/pdf/2511.09319.pdf)

**作者**: Le Yi, Wei Huang, Lei Zhang, Kefu Zhao, Yan Wang, Zizhou Wang

---

## 💡 一句话要点

**提出反馈机制的双教师模型以解决半监督医学图像分割中的错误传播问题**

**关键词**: `半监督学习` `医学图像分割` `教师-学生框架` `反馈机制` `双教师模型` `错误传播`

## 📋 核心要点

1. 核心问题：教师-学生框架在医学图像分割中易受图像模糊性影响，导致错误监督和自我强化偏差
2. 方法要点：引入反馈机制，学生提供反馈使教师优化伪标签，包括反馈归因器和接收器组件
3. 实验或效果：在三个医学图像基准测试中验证方法有效减少错误传播，提升分割性能

## 📄 摘要（原文）

> The teacher-student paradigm has emerged as a canonical framework in semi-supervised learning. When applied to medical image segmentation, the paradigm faces challenges due to inherent image ambiguities, making it particularly vulnerable to erroneous supervision. Crucially, the student's iterative reconfirmation of these errors leads to self-reinforcing bias. While some studies attempt to mitigate this bias, they often rely on external modifications to the conventional teacher-student framework, overlooking its intrinsic potential for error correction. In response, this work introduces a feedback mechanism into the teacher-student framework to counteract error reconfirmations. Here, the student provides feedback on the changes induced by the teacher's pseudo-labels, enabling the teacher to refine these labels accordingly. We specify that this interaction hinges on two key components: the feedback attributor, which designates pseudo-labels triggering the student's update, and the feedback receiver, which determines where to apply this feedback. Building on this, a dual-teacher feedback model is further proposed, which allows more dynamics in the feedback loop and fosters more gains by resolving disagreements through cross-teacher supervision while avoiding consistent errors. Comprehensive evaluations on three medical image benchmarks demonstrate the method's effectiveness in addressing error propagation in semi-supervised medical image segmentation.

