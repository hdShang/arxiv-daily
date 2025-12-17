---
layout: default
title: Neural B-Frame Coding: Tackling Domain Shift Issues with Lightweight Online Motion Resolution Adaptation
---

# Neural B-Frame Coding: Tackling Domain Shift Issues with Lightweight Online Motion Resolution Adaptation

**arXiv**: [2511.18724v1](https://arxiv.org/abs/2511.18724) | [PDF](https://arxiv.org/pdf/2511.18724.pdf)

**作者**: Sang NguyenQuang, Xiem HoangVan, Wen-Hsiao Peng

---

## 💡 一句话要点

**提出轻量级分类器以解决B帧编码中域偏移问题，实现在线运动分辨率自适应。**

**关键词**: `B帧编码` `域偏移` `运动估计` `轻量级分类器` `分辨率自适应` `计算复杂度优化`

## 📋 核心要点

1. 核心问题：B帧编码域偏移源于训练与测试GOP大小不匹配，导致大运动估计不准确。
2. 方法要点：设计二进制、多类和协同分类器，利用帧状态信号预测下采样因子。
3. 实验或效果：性能接近穷举搜索，显著降低计算复杂度，无需重新训练编解码器。

## 📄 摘要（原文）

> Learned B-frame codecs with hierarchical temporal prediction often encounter the domain-shift issue due to mismatches between the Group-of-Pictures (GOP) sizes for training and testing, leading to inaccurate motion estimates, particularly for large motion. A common solution is to turn large motion into small motion by downsampling video frames during motion estimation. However, determining the optimal downsampling factor typically requires costly rate-distortion optimization. This work introduces lightweight classifiers to predict downsampling factors. These classifiers leverage simple state signals from current and reference frames to balance rate-distortion performance with computational cost. Three variants are proposed: (1) a binary classifier (Bi-Class) trained with Focal Loss to choose between high and low resolutions, (2) a multi-class classifier (Mu-Class) trained with novel soft labels based on rate-distortion costs, and (3) a co-class approach (Co-Class) that combines the predictive capability of the multi-class classifier with the selective search of the binary classifier. All classifier methods can work seamlessly with existing B-frame codecs without requiring codec retraining. Experimental results show that they achieve coding performance comparable to exhaustive search methods while significantly reducing computational complexity. The code is available at: https://github.com/NYCU-MAPL/Fast-OMRA.git.

