---
layout: default
title: Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event Streams
---

# Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event Streams

**arXiv**: [2510.11717v1](https://arxiv.org/abs/2510.11717) | [PDF](https://arxiv.org/pdf/2510.11717.pdf)

**作者**: Takuya Nakabayashi, Navami Kairanda, Hideo Saito, Vladislav Golyanik

---

## 💡 一句话要点

**提出Ev4DGS方法，从单目事件流渲染非刚性物体的新视角**

**关键词**: `事件相机` `新视角渲染` `非刚性物体` `3D高斯泼溅` `单目事件流`

## 📋 核心要点

1. 核心问题：现有方法需额外RGB输入，限制了非刚性物体新视角渲染的实用性
2. 方法要点：通过损失函数和粗3D变形模型，回归可变形3D高斯泼溅表示
3. 实验或效果：在合成和真实数据集上验证有效性，优于多个基线方法

## 📄 摘要（原文）

> Event cameras offer various advantages for novel view rendering compared to
> synchronously operating RGB cameras, and efficient event-based techniques
> supporting rigid scenes have been recently demonstrated in the literature. In
> the case of non-rigid objects, however, existing approaches additionally
> require sparse RGB inputs, which can be a substantial practical limitation; it
> remains unknown if similar models could be learned from event streams only.
> This paper sheds light on this challenging open question and introduces Ev4DGS,
> i.e., the first approach for novel view rendering of non-rigidly deforming
> objects in the explicit observation space (i.e., as RGB or greyscale images)
> from monocular event streams. Our method regresses a deformable 3D Gaussian
> Splatting representation through 1) a loss relating the outputs of the
> estimated model with the 2D event observation space, and 2) a coarse 3D
> deformation model trained from binary masks generated from events. We perform
> experimental comparisons on existing synthetic and newly recorded real datasets
> with non-rigid objects. The results demonstrate the validity of Ev4DGS and its
> superior performance compared to multiple naive baselines that can be applied
> in our setting. We will release our models and the datasets used in the
> evaluation for research purposes; see the project webpage:
> https://4dqv.mpi-inf.mpg.de/Ev4DGS/.

