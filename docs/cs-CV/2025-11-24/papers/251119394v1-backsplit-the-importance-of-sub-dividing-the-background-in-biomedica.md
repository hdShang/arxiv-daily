---
layout: default
title: BackSplit: The Importance of Sub-dividing the Background in Biomedical Lesion Segmentation
---

# BackSplit: The Importance of Sub-dividing the Background in Biomedical Lesion Segmentation

**arXiv**: [2511.19394v1](https://arxiv.org/abs/2511.19394) | [PDF](https://arxiv.org/pdf/2511.19394.pdf)

**作者**: Rachit Saluja, Asli Cihangir, Ruining Deng, Johannes C. Paetzold, Fengbei Liu, Mert R. Sabuncu

---

## 💡 一句话要点

**提出BackSplit方法，通过细分背景提升医学图像小病灶分割性能。**

**关键词**: `医学图像分割` `背景细分` `小病灶检测` `Fisher信息` `辅助标签` `优化稳定性`

## 📋 核心要点

1. 核心问题：传统方法将非病灶像素归为单一背景类，忽略解剖异质性。
2. 方法要点：使用细粒度标签细分背景，无需增加推理成本。
3. 实验效果：多数据集验证，BackSplit稳定提升小病灶分割精度。

## 📄 摘要（原文）

> Segmenting small lesions in medical images remains notoriously difficult. Most prior work tackles this challenge by either designing better architectures, loss functions, or data augmentation schemes; and collecting more labeled data. We take a different view, arguing that part of the problem lies in how the background is modeled. Common lesion segmentation collapses all non-lesion pixels into a single "background" class, ignoring the rich anatomical context in which lesions appear. In reality, the background is highly heterogeneous-composed of tissues, organs, and other structures that can now be labeled manually or inferred automatically using existing segmentation models.
>   In this paper, we argue that training with fine-grained labels that sub-divide the background class, which we call BackSplit, is a simple yet powerful paradigm that can offer a significant performance boost without increasing inference costs. From an information theoretic standpoint, we prove that BackSplit increases the expected Fisher Information relative to conventional binary training, leading to tighter asymptotic bounds and more stable optimization. With extensive experiments across multiple datasets and architectures, we empirically show that BackSplit consistently boosts small-lesion segmentation performance, even when auxiliary labels are generated automatically using pretrained segmentation models. Additionally, we demonstrate that auxiliary labels derived from interactive segmentation frameworks exhibit the same beneficial effect, demonstrating its robustness, simplicity, and broad applicability.

