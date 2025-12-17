---
layout: default
title: Adaptive transfer learning for surgical tool presence detection in laparoscopic videos through gradual freezing fine-tuning
---

# Adaptive transfer learning for surgical tool presence detection in laparoscopic videos through gradual freezing fine-tuning

**arXiv**: [2510.15372v1](https://arxiv.org/abs/2510.15372) | [PDF](https://arxiv.org/pdf/2510.15372.pdf)

**作者**: Ana Davila, Jacinto Colan, Yasuhisa Hasegawa

---

## 💡 一句话要点

**提出渐进冻结微调方法以解决手术视频中工具检测数据稀缺问题**

**关键词**: `手术工具检测` `自适应迁移学习` `渐进冻结微调` `内窥镜视频分析` `深度学习优化`

## 📋 核心要点

1. 核心问题：手术场景中标注数据有限，影响深度学习模型鲁棒性。
2. 方法要点：采用线性探测和渐进冻结阶段，动态减少可微调层数。
3. 实验或效果：在Cholec80数据集上mAP达96.4%，并在CATARACTS数据集验证泛化性。

## 📄 摘要（原文）

> Minimally invasive surgery can benefit significantly from automated surgical
> tool detection, enabling advanced analysis and assistance. However, the limited
> availability of annotated data in surgical settings poses a challenge for
> training robust deep learning models. This paper introduces a novel staged
> adaptive fine-tuning approach consisting of two steps: a linear probing stage
> to condition additional classification layers on a pre-trained CNN-based
> architecture and a gradual freezing stage to dynamically reduce the
> fine-tunable layers, aiming to regulate adaptation to the surgical domain. This
> strategy reduces network complexity and improves efficiency, requiring only a
> single training loop and eliminating the need for multiple iterations. We
> validated our method on the Cholec80 dataset, employing CNN architectures
> (ResNet-50 and DenseNet-121) pre-trained on ImageNet for detecting surgical
> tools in cholecystectomy endoscopic videos. Our results demonstrate that our
> method improves detection performance compared to existing approaches and
> established fine-tuning techniques, achieving a mean average precision (mAP) of
> 96.4%. To assess its broader applicability, the generalizability of the
> fine-tuning strategy was further confirmed on the CATARACTS dataset, a distinct
> domain of minimally invasive ophthalmic surgery. These findings suggest that
> gradual freezing fine-tuning is a promising technique for improving tool
> presence detection in diverse surgical procedures and may have broader
> applications in general image classification tasks.

