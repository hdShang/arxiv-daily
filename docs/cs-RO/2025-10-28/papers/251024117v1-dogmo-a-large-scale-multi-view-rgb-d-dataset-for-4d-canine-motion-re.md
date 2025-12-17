---
layout: default
title: DogMo: A Large-Scale Multi-View RGB-D Dataset for 4D Canine Motion Recovery
---

# DogMo: A Large-Scale Multi-View RGB-D Dataset for 4D Canine Motion Recovery

**arXiv**: [2510.24117v1](https://arxiv.org/abs/2510.24117) | [PDF](https://arxiv.org/pdf/2510.24117.pdf)

**作者**: Zan Wang, Siyu Chen, Luya Mo, Xinfeng Gao, Yuxin Shen, Lebin Ding, Wei Liang

---

## 💡 一句话要点

**提出DogMo数据集与优化方法以解决犬类运动恢复中的多视角与3D数据不足问题**

**关键词**: `犬类运动恢复` `多视角RGB-D数据集` `SMAL模型拟合` `实例特定优化` `运动序列基准`

## 📋 核心要点

1. 核心问题：现有犬类运动数据集缺乏多视角、真实3D数据，且规模和多样性有限
2. 方法要点：引入三阶段实例特定优化流程，通过粗对齐、密集对应监督和时间正则化拟合SMAL模型
3. 实验或效果：建立四个运动恢复基准，支持单目/多视角、RGB/RGB-D输入的系统评估

## 📄 摘要（原文）

> We present DogMo, a large-scale multi-view RGB-D video dataset capturing
> diverse canine movements for the task of motion recovery from images. DogMo
> comprises 1.2k motion sequences collected from 10 unique dogs, offering rich
> variation in both motion and breed. It addresses key limitations of existing
> dog motion datasets, including the lack of multi-view and real 3D data, as well
> as limited scale and diversity. Leveraging DogMo, we establish four motion
> recovery benchmark settings that support systematic evaluation across monocular
> and multi-view, RGB and RGB-D inputs. To facilitate accurate motion recovery,
> we further introduce a three-stage, instance-specific optimization pipeline
> that fits the SMAL model to the motion sequences. Our method progressively
> refines body shape and pose through coarse alignment, dense correspondence
> supervision, and temporal regularization. Our dataset and method provide a
> principled foundation for advancing research in dog motion recovery and open up
> new directions at the intersection of computer vision, computer graphics, and
> animal behavior modeling.

