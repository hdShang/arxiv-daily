---
layout: default
title: Refracting Reality: Generating Images with Realistic Transparent Objects
---

# Refracting Reality: Generating Images with Realistic Transparent Objects

**arXiv**: [2511.17340v1](https://arxiv.org/abs/2511.17340) | [PDF](https://arxiv.org/pdf/2511.17340.pdf)

**作者**: Yue Yin, Enze Tao, Dylan Campbell

---

## 💡 一句话要点

**提出基于折射定律的图像生成方法，以解决透明物体渲染不准确的问题。**

**关键词**: `图像生成` `透明物体渲染` `折射模拟` `光学约束` `像素同步`

## 📋 核心要点

1. 核心问题：生成模型在透明物体渲染中折射效果差，未充分学习光学规律。
2. 方法要点：使用斯涅尔折射定律同步像素，结合全景图像恢复不可见表面。
3. 实验或效果：生成图像在光学合理性上显著提升，符合物理约束。

## 📄 摘要（原文）

> Generative image models can produce convincingly real images, with plausible shapes, textures, layouts and lighting. However, one domain in which they perform notably poorly is in the synthesis of transparent objects, which exhibit refraction, reflection, absorption and scattering. Refraction is a particular challenge, because refracted pixel rays often intersect with surfaces observed in other parts of the image, providing a constraint on the color. It is clear from inspection that generative models have not distilled the laws of optics sufficiently well to accurately render refractive objects. In this work, we consider the problem of generating images with accurate refraction, given a text prompt. We synchronize the pixels within the object's boundary with those outside by warping and merging the pixels using Snell's Law of Refraction, at each step of the generation trajectory. For those surfaces that are not directly observed in the image, but are visible via refraction or reflection, we recover their appearance by synchronizing the image with a second generated image -- a panorama centered at the object -- using the same warping and merging procedure. We demonstrate that our approach generates much more optically-plausible images that respect the physical constraints.

