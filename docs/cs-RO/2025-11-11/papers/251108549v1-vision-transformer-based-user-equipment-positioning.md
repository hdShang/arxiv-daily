---
layout: default
title: Vision Transformer Based User Equipment Positioning
---

# Vision Transformer Based User Equipment Positioning

**arXiv**: [2511.08549v1](https://arxiv.org/abs/2511.08549) | [PDF](https://arxiv.org/pdf/2511.08549.pdf)

**作者**: Parshwa Shah, Dhaval K. Patel, Brijesh Soni, Miguel López-Benítez, Siddhartan Govindasamy

---

## 💡 一句话要点

**提出基于视觉变换器的用户设备定位方法，利用角度延迟配置文件提升精度。**

**关键词**: `用户设备定位` `视觉变换器` `信道状态信息` `角度延迟配置文件` `深度学习` `定位误差`

## 📋 核心要点

1. 现有深度学习模型对输入数据分配相同注意力，且不适用于非序列数据如瞬时信道状态信息。
2. 采用注意力机制的视觉变换器架构，聚焦信道状态信息矩阵中的角度延迟配置文件。
3. 在DeepMIMO和ViWi数据集上验证，室内外定位误差显著降低，优于现有方法约38%。

## 📄 摘要（原文）

> Recently, Deep Learning (DL) techniques have been used for User Equipment (UE) positioning. However, the key shortcomings of such models is that: i) they weigh the same attention to the entire input; ii) they are not well suited for the non-sequential data e.g., when only instantaneous Channel State Information (CSI) is available. In this context, we propose an attention-based Vision Transformer (ViT) architecture that focuses on the Angle Delay Profile (ADP) from CSI matrix. Our approach, validated on the `DeepMIMO' and `ViWi' ray-tracing datasets, achieves an Root Mean Squared Error (RMSE) of 0.55m indoors, 13.59m outdoors in DeepMIMO, and 3.45m in ViWi's outdoor blockage scenario. The proposed scheme outperforms state-of-the-art schemes by $\sim$ 38\%. It also performs substantially better than other approaches that we have considered in terms of the distribution of error distance.

