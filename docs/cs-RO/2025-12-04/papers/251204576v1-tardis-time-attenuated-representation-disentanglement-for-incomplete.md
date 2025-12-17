---
layout: default
title: TARDis: Time Attenuated Representation Disentanglement for Incomplete Multi-Modal Tumor Segmentation and Classification
---

# TARDis: Time Attenuated Representation Disentanglement for Incomplete Multi-Modal Tumor Segmentation and Classification

**arXiv**: [2512.04576v1](https://arxiv.org/abs/2512.04576) | [PDF](https://arxiv.org/pdf/2512.04576.pdf)

**作者**: Zishuo Wan, Qinqin Kang, Yi Huang, Yun Bian, Dawei Ding, Ke Yan

---

## 💡 一句话要点

**提出TARDis框架，通过时间衰减表示解耦解决不完整多模态肿瘤分割与分类问题。**

**关键词**: `多模态医学影像` `表示解耦` `时间衰减曲线` `肿瘤分割` `条件变分自编码器` `缺失模态处理`

## 📋 核心要点

1. 核心问题：CT多期相扫描中缺失模态忽略血流动力学时间连续性，影响肿瘤分割与诊断。
2. 方法要点：将缺失模态视为时间衰减曲线上的缺失点，解耦特征为静态解剖和动态灌注成分。
3. 实验或效果：在私有和公共数据集上显著优于现有方法，在极端数据稀疏场景下保持稳健性能。

## 📄 摘要（原文）

> Tumor segmentation and diagnosis in contrast-enhanced Computed Tomography (CT) rely heavily on the physiological dynamics of contrast agents. However, obtaining a complete multi-phase series is often clinically unfeasible due to radiation concerns or scanning limitations, leading to the "missing modality" problem. Existing deep learning approaches typically treat missing phases as absent independent channels, ignoring the inherent temporal continuity of hemodynamics. In this work, we propose Time Attenuated Representation Disentanglement (TARDis), a novel physics-aware framework that redefines missing modalities as missing sample points on a continuous Time-Attenuation Curve. TARDis explicitly disentangles the latent feature space into a time-invariant static component (anatomy) and a time-dependent dynamic component (perfusion). We achieve this via a dual-path architecture: a quantization-based path using a learnable embedding dictionary to extract consistent anatomical structures, and a probabilistic path using a Conditional Variational Autoencoder to model dynamic enhancement conditioned on the estimated scan time. This design allows the network to hallucinate missing hemodynamic features by sampling from the learned latent distribution. Extensive experiments on a large-scale private abdominal CT dataset (2,282 cases) and two public datasets demonstrate that TARDis significantly outperforms state-of-the-art incomplete modality frameworks. Notably, our method maintains robust diagnostic performance even in extreme data-sparsity scenarios, highlighting its potential for reducing radiation exposure while maintaining diagnostic precision.

