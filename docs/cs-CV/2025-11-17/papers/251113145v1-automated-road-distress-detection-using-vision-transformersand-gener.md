---
layout: default
title: Automated Road Distress Detection Using Vision Transformersand Generative Adversarial Networks
---

# Automated Road Distress Detection Using Vision Transformersand Generative Adversarial Networks

**arXiv**: [2511.13145v1](https://arxiv.org/abs/2511.13145) | [PDF](https://arxiv.org/pdf/2511.13145.pdf)

**作者**: Cesar Portocarrero Rodriguez, Laura Vandeweyen, Yosuke Yamamoto

---

## 💡 一句话要点

**提出结合GAN生成数据和MaskFormer模型以提升道路病害分割性能**

**关键词**: `道路病害检测` `生成对抗网络` `视觉变换器` `图像分割` `合成数据增强`

## 📋 核心要点

1. 核心问题：美国道路基础设施状况差，传统检测方法成本高、效率低。
2. 方法要点：使用GAN生成合成数据，并应用CNN和MaskFormer进行道路病害分割。
3. 实验或效果：GAN数据提升模型性能，MaskFormer在mAP50和IoU指标上优于CNN。

## 📄 摘要（原文）

> The American Society of Civil Engineers has graded Americas infrastructure condition as a C, with the road system receiving a dismal D. Roads are vital to regional economic viability, yet their management, maintenance, and repair processes remain inefficient, relying on outdated manual or laser-based inspection methods that are both costly and time-consuming. With the increasing availability of real-time visual data from autonomous vehicles, there is an opportunity to apply computer vision (CV) methods for advanced road monitoring, providing insights to guide infrastructure rehabilitation efforts. This project explores the use of state-of-the-art CV techniques for road distress segmentation. It begins by evaluating synthetic data generated with Generative Adversarial Networks (GANs) to assess its usefulness for model training. The study then applies Convolutional Neural Networks (CNNs) for road distress segmentation and subsequently examines the transformer-based model MaskFormer. Results show that GAN-generated data improves model performance and that MaskFormer outperforms the CNN model in two metrics: mAP50 and IoU.

