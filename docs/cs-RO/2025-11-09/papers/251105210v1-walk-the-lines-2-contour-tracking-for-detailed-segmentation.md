---
layout: default
title: Walk the Lines 2: Contour Tracking for Detailed Segmentation
---

# Walk the Lines 2: Contour Tracking for Detailed Segmentation

**arXiv**: [2511.05210v1](https://arxiv.org/abs/2511.05210) | [PDF](https://arxiv.org/pdf/2511.05210.pdf)

**作者**: André Peter Kelm, Max Braeschke, Emre Gülsoylu, Simone Frintrop

---

## 💡 一句话要点

**提出Walk the Lines 2轮廓跟踪算法，用于红外和RGB图像的详细分割**

**关键词**: `轮廓跟踪` `详细分割` `红外图像` `RGB图像` `非极大值抑制替代` `对象轮廓检测`

## 📋 核心要点

1. 核心问题：标准非极大值抑制在生成闭合轮廓时细节不足，影响分割质量
2. 方法要点：通过轮廓跟踪细化对象轮廓，生成1像素宽闭合形状，可二值化分割
3. 实验或效果：在红外和RGB对象分割中，实现高IoU和细节保留，优于现有轮廓方法

## 📄 摘要（原文）

> This paper presents Walk the Lines 2 (WtL2), a unique contour tracking
> algorithm specifically adapted for detailed segmentation of infrared (IR) ships
> and various objects in RGB.1 This extends the original Walk the Lines (WtL)
> [12], which focused solely on detailed ship segmentation in color. These
> innovative WtLs can replace the standard non-maximum suppression (NMS) by using
> contour tracking to refine the object contour until a 1-pixel-wide closed shape
> can be binarized, forming a segmentable area in foreground-background
> scenarios. WtL2 broadens the application range of WtL beyond its original
> scope, adapting to IR and expanding to diverse objects within the RGB context.
> To achieve IR segmentation, we adapt its input, the object contour detector, to
> IR ships. In addition, the algorithm is enhanced to process a wide range of RGB
> objects, outperforming the latest generation of contour-based methods when
> achieving a closed object contour, offering high peak Intersection over Union
> (IoU) with impressive details. This positions WtL2 as a compelling method for
> specialized applications that require detailed segmentation or high-quality
> samples, potentially accelerating progress in several niche areas of image
> segmentation.

