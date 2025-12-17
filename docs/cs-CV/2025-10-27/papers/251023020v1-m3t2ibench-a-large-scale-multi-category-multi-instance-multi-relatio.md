---
layout: default
title: M$^{3}$T2IBench: A Large-Scale Multi-Category, Multi-Instance, Multi-Relation Text-to-Image Benchmark
---

# M$^{3}$T2IBench: A Large-Scale Multi-Category, Multi-Instance, Multi-Relation Text-to-Image Benchmark

**arXiv**: [2510.23020v1](https://arxiv.org/abs/2510.23020) | [PDF](https://arxiv.org/pdf/2510.23020.pdf)

**作者**: Huixuan Zhang, Xiaojun Wan

---

## 💡 一句话要点

**提出M³T2IBench基准和AlignScore指标以评估多实例文本-图像对齐问题。**

**关键词**: `文本-图像生成` `多实例评估` `图像-文本对齐` `基准数据集` `目标检测指标`

## 📋 核心要点

1. 核心问题：现有文本-图像模型在多实例、多类别提示下图像-文本对齐不佳。
2. 方法要点：引入大规模多类别、多实例、多关系基准及基于目标检测的AlignScore指标。
3. 实验或效果：提出Revise-Then-Enforce方法，在扩散模型中提升对齐效果。

## 📄 摘要（原文）

> Text-to-image models are known to struggle with generating images that
> perfectly align with textual prompts. Several previous studies have focused on
> evaluating image-text alignment in text-to-image generation. However, these
> evaluations either address overly simple scenarios, especially overlooking the
> difficulty of prompts with multiple different instances belonging to the same
> category, or they introduce metrics that do not correlate well with human
> evaluation. In this study, we introduce M$^3$T2IBench, a large-scale,
> multi-category, multi-instance, multi-relation along with an
> object-detection-based evaluation metric, $AlignScore$, which aligns closely
> with human evaluation. Our findings reveal that current open-source
> text-to-image models perform poorly on this challenging benchmark.
> Additionally, we propose the Revise-Then-Enforce approach to enhance image-text
> alignment. This training-free post-editing method demonstrates improvements in
> image-text alignment across a broad range of diffusion models. \footnote{Our
> code and data has been released in supplementary material and will be made
> publicly available after the paper is accepted.}

