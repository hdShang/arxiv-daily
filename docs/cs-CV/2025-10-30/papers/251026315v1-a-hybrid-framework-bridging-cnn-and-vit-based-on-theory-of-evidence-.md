---
layout: default
title: A Hybrid Framework Bridging CNN and ViT based on Theory of Evidence for Diabetic Retinopathy Grading
---

# A Hybrid Framework Bridging CNN and ViT based on Theory of Evidence for Diabetic Retinopathy Grading

**arXiv**: [2510.26315v1](https://arxiv.org/abs/2510.26315) | [PDF](https://arxiv.org/pdf/2510.26315.pdf)

**作者**: Junlai Qiu, Yunzhu Chen, Hao Zheng, Yawen Huang, Yuexiang Li

---

## 💡 一句话要点

**提出基于证据理论的CNN与ViT混合框架以提升糖尿病视网膜病变分级性能**

**关键词**: `糖尿病视网膜病变分级` `CNN与ViT融合` `证据理论` `特征融合` `自适应模型` `医学图像分析`

## 📋 核心要点

1. 糖尿病视网膜病变分级中，单一CNN或ViT模型性能受限，需融合局部与全局特征。
2. 使用证据理论将不同主干网络特征转化为支持证据，自适应融合以增强模型能力。
3. 在公开数据集上验证，模型在准确性和可解释性方面优于现有方法。

## 📄 摘要（原文）

> Diabetic retinopathy (DR) is a leading cause of vision loss among middle-aged
> and elderly people, which significantly impacts their daily lives and mental
> health. To improve the efficiency of clinical screening and enable the early
> detection of DR, a variety of automated DR diagnosis systems have been recently
> established based on convolutional neural network (CNN) or vision Transformer
> (ViT). However, due to the own shortages of CNN / ViT, the performance of
> existing methods using single-type backbone has reached a bottleneck. One
> potential way for the further improvements is integrating different kinds of
> backbones, which can fully leverage the respective strengths of them
> (\emph{i.e.,} the local feature extraction capability of CNN and the global
> feature capturing ability of ViT). To this end, we propose a novel paradigm to
> effectively fuse the features extracted by different backbones based on the
> theory of evidence. Specifically, the proposed evidential fusion paradigm
> transforms the features from different backbones into supporting evidences via
> a set of deep evidential networks. With the supporting evidences, the
> aggregated opinion can be accordingly formed, which can be used to adaptively
> tune the fusion pattern between different backbones and accordingly boost the
> performance of our hybrid model. We evaluated our method on two publicly
> available DR grading datasets. The experimental results demonstrate that our
> hybrid model not only improves the accuracy of DR grading, compared to the
> state-of-the-art frameworks, but also provides the excellent interpretability
> for feature fusion and decision-making.

