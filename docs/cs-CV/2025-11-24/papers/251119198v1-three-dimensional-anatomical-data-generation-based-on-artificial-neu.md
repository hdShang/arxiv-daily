---
layout: default
title: Three-Dimensional Anatomical Data Generation Based on Artificial Neural Networks
---

# Three-Dimensional Anatomical Data Generation Based on Artificial Neural Networks

**arXiv**: [2511.19198v1](https://arxiv.org/abs/2511.19198) | [PDF](https://arxiv.org/pdf/2511.19198.pdf)

**作者**: Ann-Sophia Müller, Moonkwang Jeong, Meng Zhang, Jiyuan Tian, Arkadiusz Miernik, Stefanie Speidel, Tian Qiu

---

## 💡 一句话要点

**提出基于物理模型和3D GAN的自动化3D解剖数据生成工作流，以解决手术规划中数据获取瓶颈。**

**关键词**: `3D解剖数据生成` `生成对抗网络` `医学图像分割` `手术规划` `超声成像` `物理模型仿真`

## 📋 核心要点

1. 核心问题：手术规划依赖3D解剖模型，但真实患者数据获取面临法律、伦理和技术挑战，尤其对低对比度软组织器官如前列腺。
2. 方法要点：使用物理器官模型和3D GAN生成3D数据，训练神经网络分割超声图像，并重建3D网格模型。
3. 实验或效果：在人工前列腺模型上验证，神经网络分割的IoU优于传统计算机视觉方法，并提供性能反馈。

## 📄 摘要（原文）

> Surgical planning and training based on machine learning requires a large amount of 3D anatomical models reconstructed from medical imaging, which is currently one of the major bottlenecks. Obtaining these data from real patients and during surgery is very demanding, if even possible, due to legal, ethical, and technical challenges. It is especially difficult for soft tissue organs with poor imaging contrast, such as the prostate. To overcome these challenges, we present a novel workflow for automated 3D anatomical data generation using data obtained from physical organ models. We additionally use a 3D Generative Adversarial Network (GAN) to obtain a manifold of 3D models useful for other downstream machine learning tasks that rely on 3D data. We demonstrate our workflow using an artificial prostate model made of biomimetic hydrogels with imaging contrast in multiple zones. This is used to physically simulate endoscopic surgery. For evaluation and 3D data generation, we place it into a customized ultrasound scanner that records the prostate before and after the procedure. A neural network is trained to segment the recorded ultrasound images, which outperforms conventional, non-learning-based computer vision techniques in terms of intersection over union (IoU). Based on the segmentations, a 3D mesh model is reconstructed, and performance feedback is provided.

