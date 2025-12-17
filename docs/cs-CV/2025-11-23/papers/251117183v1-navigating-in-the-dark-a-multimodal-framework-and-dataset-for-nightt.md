---
layout: default
title: Navigating in the Dark: A Multimodal Framework and Dataset for Nighttime Traffic Sign Recognition
---

# Navigating in the Dark: A Multimodal Framework and Dataset for Nighttime Traffic Sign Recognition

**arXiv**: [2511.17183v1](https://arxiv.org/abs/2511.17183) | [PDF](https://arxiv.org/pdf/2511.17183.pdf)

**作者**: Aditya Mishra, Akshay Agarwal, Haroon Lone

---

## 💡 一句话要点

**提出LENS-Net和INTSD数据集以解决夜间交通标志识别挑战**

**关键词**: `夜间交通标志识别` `多模态学习` `图像增强` `数据集构建` `图卷积网络` `跨模态注意力`

## 📋 核心要点

1. 核心问题：夜间交通标志识别因视觉噪声和数据集稀缺而困难，现有方法在低光照下不鲁棒。
2. 方法要点：LENS-Net集成自适应图像增强检测器和多模态CLIP-GCNN分类器，提升识别鲁棒性。
3. 实验或效果：在INTSD数据集上评估，LENS-Net超越现有框架，消融研究验证组件有效性。

## 📄 摘要（原文）

> Traffic signboards are vital for road safety and intelligent transportation systems, enabling navigation and autonomous driving. Yet, recognizing traffic signs at night remains challenging due to visual noise and scarcity of public nighttime datasets. Despite advances in vision architectures, existing methods struggle with robustness under low illumination and fail to leverage complementary mutlimodal cues effectively. To overcome these limitations, firstly, we introduce INTSD, a large-scale dataset comprising street-level night-time images of traffic signboards collected across diverse regions of India. The dataset spans 41 traffic signboard classes captured under varying lighting and weather conditions, providing a comprehensive benchmark for both detection and classification tasks. To benchmark INTSD for night-time sign recognition, we conduct extensive evaluations using state-of-the-art detection and classification models. Secondly, we propose LENS-Net, which integrates an adaptive image enhancement detector for joint illumination correction and sign localization, followed by a structured multimodal CLIP-GCNN classifier that leverages cross-modal attention and graph-based reasoning for robust and semantically consistent recognition. Our method surpasses existing frameworks, with ablation studies confirming the effectiveness of its key components. The dataset and code for LENS-Net is publicly available for research.

