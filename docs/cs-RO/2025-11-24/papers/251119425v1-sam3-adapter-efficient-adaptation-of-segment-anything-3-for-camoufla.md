---
layout: default
title: SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation
---

# SAM3-Adapter: Efficient Adaptation of Segment Anything 3 for Camouflage Object Segmentation, Shadow Detection, and Medical Image Segmentation

**arXiv**: [2511.19425v1](https://arxiv.org/abs/2511.19425) | [PDF](https://arxiv.org/pdf/2511.19425.pdf)

**作者**: Tianrun Chen, Runlong Cao, Xinda Yu, Lanyun Zhu, Chaotao Ding, Deyi Ji, Cheng Chen, Qi Zhu, Chunyan Xu, Papa Mao, Ying Zang

---

## 💡 一句话要点

**提出SAM3-Adapter以高效适配Segment Anything 3，提升伪装物体分割、阴影检测和医学图像分割性能**

**关键词**: `图像分割` `适配器框架` `伪装物体检测` `阴影检测` `医学图像分割` `基础模型适配`

## 📋 核心要点

1. 核心问题：基础模型在细粒度分割任务如伪装物体检测和医学图像分割中表现不足
2. 方法要点：设计适配器框架，降低计算开销并增强任务适应性和分割精度
3. 实验或效果：在多个下游任务中超越先前方法，实现新的最优结果

## 📄 摘要（原文）

> The rapid rise of large-scale foundation models has reshaped the landscape of image segmentation, with models such as Segment Anything achieving unprecedented versatility across diverse vision tasks. However, previous generations-including SAM and its successor-still struggle with fine-grained, low-level segmentation challenges such as camouflaged object detection, medical image segmentation, cell image segmentation, and shadow detection. To address these limitations, we originally proposed SAM-Adapter in 2023, demonstrating substantial gains on these difficult scenarios. With the emergence of Segment Anything 3 (SAM3)-a more efficient and higher-performing evolution with a redesigned architecture and improved training pipeline-we revisit these long-standing challenges. In this work, we present SAM3-Adapter, the first adapter framework tailored for SAM3 that unlocks its full segmentation capability. SAM3-Adapter not only reduces computational overhead but also consistently surpasses both SAM and SAM2-based solutions, establishing new state-of-the-art results across multiple downstream tasks, including medical imaging, camouflaged (concealed) object segmentation, and shadow detection. Built upon the modular and composable design philosophy of the original SAM-Adapter, SAM3-Adapter provides stronger generalizability, richer task adaptability, and significantly improved segmentation precision. Extensive experiments confirm that integrating SAM3 with our adapter yields superior accuracy, robustness, and efficiency compared to all prior SAM-based adaptations. We hope SAM3-Adapter can serve as a foundation for future research and practical segmentation applications. Code, pre-trained models, and data processing pipelines are available.

