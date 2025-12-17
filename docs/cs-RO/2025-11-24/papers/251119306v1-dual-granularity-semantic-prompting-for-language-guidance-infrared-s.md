---
layout: default
title: Dual-Granularity Semantic Prompting for Language Guidance Infrared Small Target Detection
---

# Dual-Granularity Semantic Prompting for Language Guidance Infrared Small Target Detection

**arXiv**: [2511.19306v1](https://arxiv.org/abs/2511.19306) | [PDF](https://arxiv.org/pdf/2511.19306.pdf)

**作者**: Zixuan Wang, Haoran Sun, Jiaming Lu, Wenxuan Wang, Zhongling Huang, Dingwen Zhang, Xuelin Qian, Junwei Han

---

## 💡 一句话要点

**提出DGSPNet以解决红外小目标检测中特征表示不足和背景干扰问题**

**关键词**: `红外小目标检测` `语义提示` `语言引导` `注意力机制` `端到端框架`

## 📋 核心要点

1. 核心问题：红外小目标检测因特征表示有限和背景干扰严重导致性能不佳
2. 方法要点：集成双粒度语义提示，包括粗粒度文本先验和细粒度视觉到文本映射
3. 实验或效果：在三个基准数据集上显著提升检测精度，达到最先进水平

## 📄 摘要（原文）

> Infrared small target detection remains challenging due to limited feature representation and severe background interference, resulting in sub-optimal performance. While recent CLIP-inspired methods attempt to leverage textual guidance for detection, they are hindered by inaccurate text descriptions and reliance on manual annotations. To overcome these limitations, we propose DGSPNet, an end-to-end language prompt-driven framework. Our approach integrates dual-granularity semantic prompts: coarse-grained textual priors (e.g., 'infrared image', 'small target') and fine-grained personalized semantic descriptions derived through visual-to-textual mapping within the image space. This design not only facilitates learning fine-grained semantic information but also can inherently leverage language prompts during inference without relying on any annotation requirements. By fully leveraging the precision and conciseness of text descriptions, we further introduce a text-guide channel attention (TGCA) mechanism and text-guide spatial attention (TGSA) mechanism that enhances the model's sensitivity to potential targets across both low- and high-level feature spaces. Extensive experiments demonstrate that our method significantly improves detection accuracy and achieves state-of-the-art performance on three benchmark datasets.

