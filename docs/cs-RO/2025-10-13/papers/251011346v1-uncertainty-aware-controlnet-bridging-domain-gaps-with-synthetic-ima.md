---
layout: default
title: Uncertainty-Aware ControlNet: Bridging Domain Gaps with Synthetic Image Generation
---

# Uncertainty-Aware ControlNet: Bridging Domain Gaps with Synthetic Image Generation

**arXiv**: [2510.11346v1](https://arxiv.org/abs/2510.11346) | [PDF](https://arxiv.org/pdf/2510.11346.pdf)

**作者**: Joshua Niemeijer, Jan Ehrhardt, Heinz Handels, Hristina Uzunova

---

## 💡 一句话要点

**提出不确定性感知ControlNet，利用未标注数据生成合成图像以弥合领域差距**

**关键词**: `ControlNet` `不确定性控制` `合成图像生成` `领域适应` `语义分割` `视网膜OCT`

## 📋 核心要点

1. 核心问题：ControlNet生成图像时易复制原训练分布，限制合成数据对下游任务（如分割）的增强效果
2. 方法要点：引入不确定性控制机制，结合未标注和标注数据训练，生成高不确定性目标域标注图像
3. 实验或效果：在视网膜OCT和交通场景实验中，显著提升分割性能，无需额外监督

## 📄 摘要（原文）

> Generative Models are a valuable tool for the controlled creation of
> high-quality image data. Controlled diffusion models like the ControlNet have
> allowed the creation of labeled distributions. Such synthetic datasets can
> augment the original training distribution when discriminative models, like
> semantic segmentation, are trained. However, this augmentation effect is
> limited since ControlNets tend to reproduce the original training distribution.
>   This work introduces a method to utilize data from unlabeled domains to train
> ControlNets by introducing the concept of uncertainty into the control
> mechanism. The uncertainty indicates that a given image was not part of the
> training distribution of a downstream task, e.g., segmentation. Thus, two types
> of control are engaged in the final network: an uncertainty control from an
> unlabeled dataset and a semantic control from the labeled dataset. The
> resulting ControlNet allows us to create annotated data with high uncertainty
> from the target domain, i.e., synthetic data from the unlabeled distribution
> with labels. In our scenario, we consider retinal OCTs, where typically
> high-quality Spectralis images are available with given ground truth
> segmentations, enabling the training of segmentation networks. The recent
> development in Home-OCT devices, however, yields retinal OCTs with lower
> quality and a large domain shift, such that out-of-the-pocket segmentation
> networks cannot be applied for this type of data. Synthesizing annotated images
> from the Home-OCT domain using the proposed approach closes this gap and leads
> to significantly improved segmentation results without adding any further
> supervision. The advantage of uncertainty-guidance becomes obvious when
> compared to style transfer: it enables arbitrary domain shifts without any
> strict learning of an image style. This is also demonstrated in a traffic scene
> experiment.

