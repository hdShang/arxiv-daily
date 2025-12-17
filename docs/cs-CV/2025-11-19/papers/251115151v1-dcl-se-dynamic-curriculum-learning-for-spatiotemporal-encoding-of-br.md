---
layout: default
title: DCL-SE: Dynamic Curriculum Learning for Spatiotemporal Encoding of Brain Imaging
---

# DCL-SE: Dynamic Curriculum Learning for Spatiotemporal Encoding of Brain Imaging

**arXiv**: [2511.15151v1](https://arxiv.org/abs/2511.15151) | [PDF](https://arxiv.org/pdf/2511.15151.pdf)

**作者**: Meihua Zhou, Xinyu Tong, Jiarui Zhao, Min Cheng, Li Yang, Lei Tian, Nan Wan

---

## 💡 一句话要点

**提出动态课程学习框架DCL-SE，以提升脑成像时空编码的准确性和鲁棒性。**

**关键词**: `脑成像分析` `动态课程学习` `时空编码` `近似秩池化` `医学图像分类` `脑疾病诊断`

## 📋 核心要点

1. 高维脑成像分析面临时空保真度不足和通用模型适应性差的问题。
2. 使用近似秩池化编码三维脑数据，结合动态课程学习策略逐步训练解码器。
3. 在多个公开数据集上验证，DCL-SE在精度、鲁棒性和可解释性方面优于现有方法。

## 📄 摘要（原文）

> High-dimensional neuroimaging analyses for clinical diagnosis are often constrained by compromises in spatiotemporal fidelity and by the limited adaptability of large-scale, general-purpose models. To address these challenges, we introduce Dynamic Curriculum Learning for Spatiotemporal Encoding (DCL-SE), an end-to-end framework centered on data-driven spatiotemporal encoding (DaSE). We leverage Approximate Rank Pooling (ARP) to efficiently encode three-dimensional volumetric brain data into information-rich, two-dimensional dynamic representations, and then employ a dynamic curriculum learning strategy, guided by a Dynamic Group Mechanism (DGM), to progressively train the decoder, refining feature extraction from global anatomical structures to fine pathological details. Evaluated across six publicly available datasets, including Alzheimer's disease and brain tumor classification, cerebral artery segmentation, and brain age prediction, DCL-SE consistently outperforms existing methods in accuracy, robustness, and interpretability. These findings underscore the critical importance of compact, task-specific architectures in the era of large-scale pretrained networks.

