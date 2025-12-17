---
layout: default
title: FOUND: Fourier-based von Mises Distribution for Robust Single Domain Generalization in Object Detection
---

# FOUND: Fourier-based von Mises Distribution for Robust Single Domain Generalization in Object Detection

**arXiv**: [2511.10352v1](https://arxiv.org/abs/2511.10352) | [PDF](https://arxiv.org/pdf/2511.10352.pdf)

**作者**: Mengzhu Wang, Changyuan Deng, Shanshan Wang, Nan Yin, Long Lan, Liang Yang

---

## 💡 一句话要点

**提出FOUND框架以增强单域泛化目标检测的鲁棒性**

**关键词**: `单域泛化` `目标检测` `傅里叶变换` `vMF分布` `CLIP引导` `鲁棒特征`

## 📋 核心要点

1. 单域泛化目标检测在单一源域训练，需泛化到未知目标域
2. 结合vMF分布和傅里叶变换，建模特征方向并扰动频域模拟域偏移
3. 在天气驾驶基准上实验，性能优于现有最优方法

## 📄 摘要（原文）

> Single Domain Generalization (SDG) for object detection aims to train a model on a single source domain that can generalize effectively to unseen target domains. While recent methods like CLIP-based semantic augmentation have shown promise, they often overlook the underlying structure of feature distributions and frequency-domain characteristics that are critical for robustness. In this paper, we propose a novel framework that enhances SDG object detection by integrating the von Mises-Fisher (vMF) distribution and Fourier transformation into a CLIP-guided pipeline. Specifically, we model the directional features of object representations using vMF to better capture domain-invariant semantic structures in the embedding space. Additionally, we introduce a Fourier-based augmentation strategy that perturbs amplitude and phase components to simulate domain shifts in the frequency domain, further improving feature robustness. Our method not only preserves the semantic alignment benefits of CLIP but also enriches feature diversity and structural consistency across domains. Extensive experiments on the diverse weather-driving benchmark demonstrate that our approach outperforms the existing state-of-the-art method.

