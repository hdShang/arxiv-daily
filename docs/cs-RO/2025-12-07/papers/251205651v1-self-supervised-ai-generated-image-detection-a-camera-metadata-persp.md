---
layout: default
title: Self-Supervised AI-Generated Image Detection: A Camera Metadata Perspective
---

# Self-Supervised AI-Generated Image Detection: A Camera Metadata Perspective

**arXiv**: [2512.05651v1](https://arxiv.org/abs/2512.05651) | [PDF](https://arxiv.org/pdf/2512.05651.pdf)

**作者**: Nan Zhong, Mian Zou, Yiran Xu, Zhenxing Qian, Xinpeng Zhang, Baoyuan Wu, Kede Ma

---

## 💡 一句话要点

**提出基于相机元数据的自监督方法，以检测AI生成图像并提升跨模型泛化能力。**

**关键词**: `AI生成图像检测` `自监督学习` `相机元数据` `EXIF标签` `跨模型泛化` `多媒体取证`

## 📋 核心要点

1. 核心问题：现有AI生成图像检测器依赖特定生成模型内部假设，限制跨模型适用性。
2. 方法要点：利用EXIF标签自监督学习数字摄影固有特征，通过分类和排序任务训练特征提取器。
3. 实验或效果：在多种生成模型上验证，EXIF诱导检测器显著提升性能，对野外样本和图像扰动具有强泛化性和鲁棒性。

## 📄 摘要（原文）

> The proliferation of AI-generated imagery poses escalating challenges for multimedia forensics, yet many existing detectors depend on assumptions about the internals of specific generative models, limiting their cross-model applicability. We introduce a self-supervised approach for detecting AI-generated images that leverages camera metadata -- specifically exchangeable image file format (EXIF) tags -- to learn features intrinsic to digital photography. Our pretext task trains a feature extractor solely on camera-captured photographs by classifying categorical EXIF tags (\eg, camera model and scene type) and pairwise-ranking ordinal and continuous EXIF tags (\eg, focal length and aperture value). Using these EXIF-induced features, we first perform one-class detection by modeling the distribution of photographic images with a Gaussian mixture model and flagging low-likelihood samples as AI-generated. We then extend to binary detection that treats the learned extractor as a strong regularizer for a classifier of the same architecture, operating on high-frequency residuals from spatially scrambled patches. Extensive experiments across various generative models demonstrate that our EXIF-induced detectors substantially advance the state of the art, delivering strong generalization to in-the-wild samples and robustness to common benign image perturbations.

