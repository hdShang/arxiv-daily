---
layout: default
title: Radiance-Field Reinforced Pretraining: Scaling Localization Models with Unlabeled Wireless Signals
---

# Radiance-Field Reinforced Pretraining: Scaling Localization Models with Unlabeled Wireless Signals

**arXiv**: [2512.07309v1](https://arxiv.org/abs/2512.07309) | [PDF](https://arxiv.org/pdf/2512.07309.pdf)

**作者**: Guosheng Wang, Shen Wang, Lei Yang

---

## 💡 一句话要点

**提出Radiance-Field Reinforced Pretraining，利用无标签无线信号提升室内定位模型的跨场景泛化能力。**

**关键词**: `室内定位` `自监督学习` `射频信号处理` `跨场景泛化` `神经辐射场`

## 📋 核心要点

1. 核心问题：现有基于深度学习的室内定位模型依赖场景特定标签数据，跨场景泛化能力不足。
2. 方法要点：采用非对称自编码器架构，结合定位模型和神经射频辐射场，通过重构射频谱进行自监督预训练。
3. 实验或效果：在100个场景的大规模数据上验证，预训练模型相比无预训练模型定位误差降低超40%，优于监督预训练。

## 📄 摘要（原文）

> Radio frequency (RF)-based indoor localization offers significant promise for applications such as indoor navigation, augmented reality, and pervasive computing. While deep learning has greatly enhanced localization accuracy and robustness, existing localization models still face major challenges in cross-scene generalization due to their reliance on scene-specific labeled data. To address this, we introduce Radiance-Field Reinforced Pretraining (RFRP). This novel self-supervised pretraining framework couples a large localization model (LM) with a neural radio-frequency radiance field (RF-NeRF) in an asymmetrical autoencoder architecture. In this design, the LM encodes received RF spectra into latent, position-relevant representations, while the RF-NeRF decodes them to reconstruct the original spectra. This alignment between input and output enables effective representation learning using large-scale, unlabeled RF data, which can be collected continuously with minimal effort. To this end, we collected RF samples at 7,327,321 positions across 100 diverse scenes using four common wireless technologies--RFID, BLE, WiFi, and IIoT. Data from 75 scenes were used for training, and the remaining 25 for evaluation. Experimental results show that the RFRP-pretrained LM reduces localization error by over 40% compared to non-pretrained models and by 21% compared to those pretrained using supervised learning.

