---
layout: default
title: ADPretrain: Advancing Industrial Anomaly Detection via Anomaly Representation Pretraining
---

# ADPretrain: Advancing Industrial Anomaly Detection via Anomaly Representation Pretraining

**arXiv**: [2511.05245v1](https://arxiv.org/abs/2511.05245) | [PDF](https://arxiv.org/pdf/2511.05245.pdf)

**作者**: Xincheng Yao, Yan Luo, Zefeng Qian, Chongyang Zhang

---

## 💡 一句话要点

**提出ADPretrain框架，通过异常表示预训练提升工业异常检测性能**

**关键词**: `异常检测` `表示学习` `对比学习` `工业图像` `预训练框架` `特征优化`

## 📋 核心要点

1. 核心问题：ImageNet预训练特征与异常检测目标不匹配，且存在数据分布偏移问题。
2. 方法要点：设计角度和范数对比损失，最大化正常与异常特征差异，使用大规模AD数据集预训练。
3. 实验或效果：在五个数据集和骨干网络上，替换特征后均显示优越性，代码已开源。

## 📄 摘要（原文）

> The current mainstream and state-of-the-art anomaly detection (AD) methods
> are substantially established on pretrained feature networks yielded by
> ImageNet pretraining. However, regardless of supervised or self-supervised
> pretraining, the pretraining process on ImageNet does not match the goal of
> anomaly detection (i.e., pretraining in natural images doesn't aim to
> distinguish between normal and abnormal). Moreover, natural images and
> industrial image data in AD scenarios typically have the distribution shift.
> The two issues can cause ImageNet-pretrained features to be suboptimal for AD
> tasks. To further promote the development of the AD field, pretrained
> representations specially for AD tasks are eager and very valuable. To this
> end, we propose a novel AD representation learning framework specially designed
> for learning robust and discriminative pretrained representations for
> industrial anomaly detection. Specifically, closely surrounding the goal of
> anomaly detection (i.e., focus on discrepancies between normals and anomalies),
> we propose angle- and norm-oriented contrastive losses to maximize the angle
> size and norm difference between normal and abnormal features simultaneously.
> To avoid the distribution shift from natural images to AD images, our
> pretraining is performed on a large-scale AD dataset, RealIAD. To further
> alleviate the potential shift between pretraining data and downstream AD
> datasets, we learn the pretrained AD representations based on the
> class-generalizable representation, residual features. For evaluation, based on
> five embedding-based AD methods, we simply replace their original features with
> our pretrained representations. Extensive experiments on five AD datasets and
> five backbones consistently show the superiority of our pretrained features.
> The code is available at https://github.com/xcyao00/ADPretrain.

