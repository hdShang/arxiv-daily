---
layout: default
title: Learning Neural Parametric 3D Breast Shape Models for Metrical Surface Reconstruction From Monocular RGB Videos
---

# Learning Neural Parametric 3D Breast Shape Models for Metrical Surface Reconstruction From Monocular RGB Videos

**arXiv**: [2510.13540v1](https://arxiv.org/abs/2510.13540) | [PDF](https://arxiv.org/pdf/2510.13540.pdf)

**作者**: Maximilian Weiherer, Antonia von Riedheim, Vanessa Brébant, Bernhard Egger, Christoph Palm

---

## 💡 一句话要点

**提出局部隐式神经参数3D乳房形状模型，用于从单目RGB视频重建度量准确表面**

**关键词**: `3D乳房重建` `隐式神经表示` `单目视频处理` `参数化形状模型` `度量表面重建`

## 📋 核心要点

1. 核心问题：现有3D乳房扫描方案昂贵或依赖专用硬件，难以低成本获取准确几何。
2. 方法要点：结合运动恢复结构和局部隐式神经SDF模型，分解乳房区域以提升重建细节。
3. 实验或效果：重建误差小于2毫米，速度快于6分钟，模型开源可用。

## 📄 摘要（原文）

> We present a neural parametric 3D breast shape model and, based on this
> model, introduce a low-cost and accessible 3D surface reconstruction pipeline
> capable of recovering accurate breast geometry from a monocular RGB video. In
> contrast to widely used, commercially available yet prohibitively expensive 3D
> breast scanning solutions and existing low-cost alternatives, our method
> requires neither specialized hardware nor proprietary software and can be used
> with any device that is able to record RGB videos. The key building blocks of
> our pipeline are a state-of-the-art, off-the-shelf Structure-from-motion
> pipeline, paired with a parametric breast model for robust and metrically
> correct surface reconstruction. Our model, similarly to the recently proposed
> implicit Regensburg Breast Shape Model (iRBSM), leverages implicit neural
> representations to model breast shapes. However, unlike the iRBSM, which
> employs a single global neural signed distance function (SDF), our approach --
> inspired by recent state-of-the-art face models -- decomposes the implicit
> breast domain into multiple smaller regions, each represented by a local neural
> SDF anchored at anatomical landmark positions. When incorporated into our
> surface reconstruction pipeline, the proposed model, dubbed liRBSM (short for
> localized iRBSM), significantly outperforms the iRBSM in terms of
> reconstruction quality, yielding more detailed surface reconstruction than its
> global counterpart. Overall, we find that the introduced pipeline is able to
> recover high-quality 3D breast geometry within an error margin of less than 2
> mm. Our method is fast (requires less than six minutes), fully transparent and
> open-source, and -- together with the model -- publicly available at
> https://rbsm.re-mic.de/local-implicit.

