---
layout: default
title: FSP-DETR: Few-Shot Prototypical Parasitic Ova Detection
---

# FSP-DETR: Few-Shot Prototypical Parasitic Ova Detection

**arXiv**: [2510.09583v1](https://arxiv.org/abs/2510.09583) | [PDF](https://arxiv.org/pdf/2510.09583.pdf)

**作者**: Shubham Trehan, Udhav Ramachandran, Akash Rao, Ruth Scimeca, Sathyanarayanan N. Aakur

---

## 💡 一句话要点

**提出FSP-DETR框架以解决生物医学中少样本检测和开放集识别问题**

**关键词**: `少样本目标检测` `原型学习` `开放集识别` `生物医学图像分析` `DETR框架`

## 📋 核心要点

1. 核心问题：生物医学目标检测中标注数据稀缺和新类别频繁出现
2. 方法要点：基于类无关DETR构建原型，使用增强视图和轻量解码器学习嵌入空间
3. 实验或效果：在多个任务中显著优于现有方法，尤其在少样本和开放集场景

## 📄 摘要（原文）

> Object detection in biomedical settings is fundamentally constrained by the
> scarcity of labeled data and the frequent emergence of novel or rare
> categories. We present FSP-DETR, a unified detection framework that enables
> robust few-shot detection, open-set recognition, and generalization to unseen
> biomedical tasks within a single model. Built upon a class-agnostic DETR
> backbone, our approach constructs class prototypes from original support images
> and learns an embedding space using augmented views and a lightweight
> transformer decoder. Training jointly optimizes a prototype matching loss, an
> alignment-based separation loss, and a KL divergence regularization to improve
> discriminative feature learning and calibration under scarce supervision.
> Unlike prior work that tackles these tasks in isolation, FSP-DETR enables
> inference-time flexibility to support unseen class recognition, background
> rejection, and cross-task adaptation without retraining. We also introduce a
> new ova species detection benchmark with 20 parasite classes and establish
> standardized evaluation protocols. Extensive experiments across ova, blood
> cell, and malaria detection tasks demonstrate that FSP-DETR significantly
> outperforms prior few-shot and prototype-based detectors, especially in
> low-shot and open-set scenarios.

