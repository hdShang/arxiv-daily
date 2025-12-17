---
layout: default
title: RTGaze: Real-Time 3D-Aware Gaze Redirection from a Single Image
---

# RTGaze: Real-Time 3D-Aware Gaze Redirection from a Single Image

**arXiv**: [2511.11289v1](https://arxiv.org/abs/2511.11289) | [PDF](https://arxiv.org/pdf/2511.11289.pdf)

**作者**: Hengfei Wang, Zhongqun Zhang, Yihua Cheng, Hyung Jin Chang

---

## 💡 一句话要点

**提出RTGaze方法以实时实现3D感知的视线重定向**

**关键词**: `视线重定向` `3D感知生成` `神经渲染` `实时处理` `几何先验蒸馏`

## 📋 核心要点

1. 现有视线重定向方法在3D一致性、效率或质量方面存在不足
2. 通过可控制视线表示学习和神经渲染解码，结合3D几何先验蒸馏
3. 在多个数据集上实现实时性能、高精度和图像质量，速度提升800倍

## 📄 摘要（原文）

> Gaze redirection methods aim to generate realistic human face images with controllable eye movement. However, recent methods often struggle with 3D consistency, efficiency, or quality, limiting their practical applications. In this work, we propose RTGaze, a real-time and high-quality gaze redirection method. Our approach learns a gaze-controllable facial representation from face images and gaze prompts, then decodes this representation via neural rendering for gaze redirection. Additionally, we distill face geometric priors from a pretrained 3D portrait generator to enhance generation quality. We evaluate RTGaze both qualitatively and quantitatively, demonstrating state-of-the-art performance in efficiency, redirection accuracy, and image quality across multiple datasets. Our system achieves real-time, 3D-aware gaze redirection with a feedforward network (~0.06 sec/image), making it 800x faster than the previous state-of-the-art 3D-aware methods.

