---
layout: default
title: A Framework for Low-Effort Training Data Generation for Urban Semantic Segmentation
---

# A Framework for Low-Effort Training Data Generation for Urban Semantic Segmentation

**arXiv**: [2510.11567v1](https://arxiv.org/abs/2510.11567) | [PDF](https://arxiv.org/pdf/2510.11567.pdf)

**作者**: Denis Zavadski, Damjan Kalšan, Tim Küchler, Haebom Lee, Stefan Roth, Carsten Rother

---

## 💡 一句话要点

**提出基于扩散模型的框架，以低代价生成高保真城市语义分割训练数据**

**关键词**: `城市语义分割` `扩散模型` `域适应` `合成数据生成` `训练数据增强`

## 📋 核心要点

1. 核心问题：合成数据与真实图像存在域差距，影响城市语义分割模型性能
2. 方法要点：使用不完美伪标签适配扩散模型，生成目标域对齐图像并过滤优化
3. 实验或效果：在多个数据集上，分割性能提升达8.0% mIoU，超越现有翻译方法

## 📄 摘要（原文）

> Synthetic datasets are widely used for training urban scene recognition
> models, but even highly realistic renderings show a noticeable gap to real
> imagery. This gap is particularly pronounced when adapting to a specific target
> domain, such as Cityscapes, where differences in architecture, vegetation,
> object appearance, and camera characteristics limit downstream performance.
> Closing this gap with more detailed 3D modelling would require expensive asset
> and scene design, defeating the purpose of low-cost labelled data. To address
> this, we present a new framework that adapts an off-the-shelf diffusion model
> to a target domain using only imperfect pseudo-labels. Once trained, it
> generates high-fidelity, target-aligned images from semantic maps of any
> synthetic dataset, including low-effort sources created in hours rather than
> months. The method filters suboptimal generations, rectifies image-label
> misalignments, and standardises semantics across datasets, transforming weak
> synthetic data into competitive real-domain training sets. Experiments on five
> synthetic datasets and two real target datasets show segmentation gains of up
> to +8.0%pt. mIoU over state-of-the-art translation methods, making rapidly
> constructed synthetic datasets as effective as high-effort, time-intensive
> synthetic datasets requiring extensive manual design. This work highlights a
> valuable collaborative paradigm where fast semantic prototyping, combined with
> generative models, enables scalable, high-quality training data creation for
> urban scene understanding.

