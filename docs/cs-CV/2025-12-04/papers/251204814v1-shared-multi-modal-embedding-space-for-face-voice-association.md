---
layout: default
title: Shared Multi-modal Embedding Space for Face-Voice Association
---

# Shared Multi-modal Embedding Space for Face-Voice Association

**arXiv**: [2512.04814v1](https://arxiv.org/abs/2512.04814) | [PDF](https://arxiv.org/pdf/2512.04814.pdf)

**作者**: Christopher Simic, Korbinian Riedhammer, Tobias Bocklet

---

## 💡 一句话要点

**提出共享多模态嵌入空间方法，结合自适应角边距损失，在FAME 2026挑战中实现人脸-语音关联任务领先性能。**

**关键词**: `人脸-语音关联` `多模态嵌入空间` `自适应角边距损失` `多语言测试` `特征提取`

## 📋 核心要点

1. 核心问题：解决人脸-语音关联任务，并在多语言设置下测试未训练语言。
2. 方法要点：采用独立单模态处理流程，提取通用特征并补充年龄-性别特征，投影至共享嵌入空间。
3. 实验或效果：在FAME 2026挑战中排名第一，平均等错误率为23.99%。

## 📄 摘要（原文）

> The FAME 2026 challenge comprises two demanding tasks: training face-voice associations combined with a multilingual setting that includes testing on languages on which the model was not trained. Our approach consists of separate uni-modal processing pipelines with general face and voice feature extraction, complemented by additional age-gender feature extraction to support prediction. The resulting single-modal features are projected into a shared embedding space and trained with an Adaptive Angular Margin (AAM) loss. Our approach achieved first place in the FAME 2026 challenge, with an average Equal-Error Rate (EER) of 23.99%.

