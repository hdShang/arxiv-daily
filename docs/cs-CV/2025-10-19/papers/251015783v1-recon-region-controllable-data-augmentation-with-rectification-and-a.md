---
layout: default
title: ReCon: Region-Controllable Data Augmentation with Rectification and Alignment for Object Detection
---

# ReCon: Region-Controllable Data Augmentation with Rectification and Alignment for Object Detection

**arXiv**: [2510.15783v1](https://arxiv.org/abs/2510.15783) | [PDF](https://arxiv.org/pdf/2510.15783.pdf)

**作者**: Haowei Zhu, Tianxiang Pan, Rui Qin, Jun-Hai Yong, Bin Wang

---

## 💡 一句话要点

**提出ReCon框架以解决目标检测中生成数据的内容位置不匹配和语义泄漏问题**

**关键词**: `目标检测` `数据增强` `生成模型` `扩散模型` `语义对齐` `区域控制`

## 📋 核心要点

1. 核心问题：生成模型用于数据增强时易出现内容位置不匹配和语义泄漏
2. 方法要点：集成区域引导校正和区域对齐交叉注意力，提升语义一致性和图像保真度
3. 实验或效果：在多个数据集和骨干网络上实现性能提升，增强生成数据的质量和可训练性

## 📄 摘要（原文）

> The scale and quality of datasets are crucial for training robust perception
> models. However, obtaining large-scale annotated data is both costly and
> time-consuming. Generative models have emerged as a powerful tool for data
> augmentation by synthesizing samples that adhere to desired distributions.
> However, current generative approaches often rely on complex post-processing or
> extensive fine-tuning on massive datasets to achieve satisfactory results, and
> they remain prone to content-position mismatches and semantic leakage. To
> overcome these limitations, we introduce ReCon, a novel augmentation framework
> that enhances the capacity of structure-controllable generative models for
> object detection. ReCon integrates region-guided rectification into the
> diffusion sampling process, using feedback from a pre-trained perception model
> to rectify misgenerated regions within diffusion sampling process. We further
> propose region-aligned cross-attention to enforce spatial-semantic alignment
> between image regions and their textual cues, thereby improving both semantic
> consistency and overall image fidelity. Extensive experiments demonstrate that
> ReCon substantially improve the quality and trainability of generated data,
> achieving consistent performance gains across various datasets, backbone
> architectures, and data scales. Our code is available at
> https://github.com/haoweiz23/ReCon .

