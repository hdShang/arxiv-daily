---
layout: default
title: Analyzing Image Beyond Visual Aspect: Image Emotion Classification via Multiple-Affective Captioning
---

# Analyzing Image Beyond Visual Aspect: Image Emotion Classification via Multiple-Affective Captioning

**arXiv**: [2511.23115v1](https://arxiv.org/abs/2511.23115) | [PDF](https://arxiv.org/pdf/2511.23115.pdf)

**作者**: Zibo Zhou, Zhengjun Zhai, Huimin Chen, Wei Dai, Hansen Yang

---

## 💡 一句话要点

**提出基于多情感描述的图像情感分类方法，以解决情感鸿沟问题。**

**关键词**: `图像情感分类` `情感鸿沟` `多情感描述` `对比学习` `语言模型`

## 📋 核心要点

1. 核心问题：图像情感分类受情感鸿沟限制，预训练视觉模型知识应用受限。
2. 方法要点：通过层次化对比损失检测情感概念，结合情感属性链式推理生成描述，利用语言模型分类。
3. 实验或效果：在多个基准测试中取得优异结果，有效桥接情感鸿沟。

## 📄 摘要（原文）

> Image emotion classification (IEC) is a longstanding research field that has received increasing attention with the rapid progress of deep learning. Although recent advances have leveraged the knowledge encoded in pre-trained visual models, their effectiveness is constrained by the "affective gap" , limits the applicability of pre-training knowledge for IEC tasks. It has been demonstrated in psychology that language exhibits high variability, encompasses diverse and abundant information, and can effectively eliminate the "affective gap". Inspired by this, we propose a novel Affective Captioning for Image Emotion Classification (ACIEC) to classify image emotion based on pure texts, which effectively capture the affective information in the image. In our method, a hierarchical multi-level contrastive loss is designed for detecting emotional concepts from images, while an emotional attribute chain-of-thought reasoning is proposed to generate affective sentences. Then, a pre-trained language model is leveraged to synthesize emotional concepts and affective sentences to conduct IEC. Additionally, a contrastive loss based on semantic similarity sampling is designed to solve the problem of large intra-class differences and small inter-class differences in affective datasets. Moreover, we also take the images with embedded texts into consideration, which were ignored by previous studies. Extensive experiments illustrate that our method can effectively bridge the affective gap and achieve superior results on multiple benchmarks.

