---
layout: default
title: A Training-Free Framework for Open-Vocabulary Image Segmentation and Recognition with EfficientNet and CLIP
---

# A Training-Free Framework for Open-Vocabulary Image Segmentation and Recognition with EfficientNet and CLIP

**arXiv**: [2510.19333v1](https://arxiv.org/abs/2510.19333) | [PDF](https://arxiv.org/pdf/2510.19333.pdf)

**作者**: Ying Dai, Wei Yu Chen

---

## 💡 一句话要点

**提出无需训练框架，结合EfficientNet和CLIP实现开放词汇图像分割与识别**

**关键词**: `开放词汇图像分割` `无监督分割` `跨模态对齐` `EfficientNet` `CLIP模型` `图像识别`

## 📋 核心要点

1. 核心问题：开放词汇图像分割与识别，无需额外训练数据。
2. 方法要点：两阶段流程，先无监督分割，后跨模态对齐识别。
3. 实验效果：在COCO等基准上，实现SOTA性能，验证泛化能力。

## 📄 摘要（原文）

> This paper presents a novel training-free framework for open-vocabulary image
> segmentation and object recognition (OVSR), which leverages EfficientNetB0, a
> convolutional neural network, for unsupervised segmentation and CLIP, a
> vision-language model, for open-vocabulary object recognition. The proposed
> framework adopts a two stage pipeline: unsupervised image segmentation followed
> by segment-level recognition via vision-language alignment. In the first stage,
> pixel-wise features extracted from EfficientNetB0 are decomposed using singular
> value decomposition to obtain latent representations, which are then clustered
> using hierarchical clustering to segment semantically meaningful regions. The
> number of clusters is adaptively determined by the distribution of singular
> values. In the second stage, the segmented regions are localized and encoded
> into image embeddings using the Vision Transformer backbone of CLIP. Text
> embeddings are precomputed using CLIP's text encoder from category-specific
> prompts, including a generic something else prompt to support open set
> recognition. The image and text embeddings are concatenated and projected into
> a shared latent feature space via SVD to enhance cross-modal alignment.
> Recognition is performed by computing the softmax over the similarities between
> the projected image and text embeddings. The proposed method is evaluated on
> standard benchmarks, including COCO, ADE20K, and PASCAL VOC, achieving
> state-of-the-art performance in terms of Hungarian mIoU, precision, recall, and
> F1-score. These results demonstrate the effectiveness, flexibility, and
> generalizability of the proposed framework.

