---
layout: default
title: TreeFedDG: Alleviating Global Drift in Federated Domain Generalization for Medical Image Segmentation
---

# TreeFedDG: Alleviating Global Drift in Federated Domain Generalization for Medical Image Segmentation

**arXiv**: [2510.18268v1](https://arxiv.org/abs/2510.18268) | [PDF](https://arxiv.org/pdf/2510.18268.pdf)

**作者**: Yucheng Song, Chenxi Li, Haokang Ding, Zhining Liao, Zhifang Liao

---

## 💡 一句话要点

**提出TreeFedDG框架以解决联邦域泛化中的全局漂移问题**

**关键词**: `联邦学习` `域泛化` `医学图像分割` `树状拓扑` `参数聚合` `风格混合`

## 📋 核心要点

1. 核心问题：联邦学习中全局漂移导致模型泛化性能下降
2. 方法要点：基于树状拓扑的参数聚合与风格混合增强鲁棒性
3. 实验或效果：在公开数据集上优于现有域泛化方法

## 📄 摘要（原文）

> In medical image segmentation tasks, Domain Generalization (DG) under the
> Federated Learning (FL) framework is crucial for addressing challenges related
> to privacy protection and data heterogeneity. However, traditional federated
> learning methods fail to account for the imbalance in information aggregation
> across clients in cross-domain scenarios, leading to the Global Drift (GD)
> problem and a consequent decline in model generalization performance. This
> motivates us to delve deeper and define a new critical issue: global drift in
> federated domain generalization for medical imaging (FedDG-GD). In this paper,
> we propose a novel tree topology framework called TreeFedDG. First, starting
> from the distributed characteristics of medical images, we design a
> hierarchical parameter aggregation method based on a tree-structured topology
> to suppress deviations in the global model direction. Second, we introduce a
> parameter difference-based style mixing method (FedStyle), which enforces
> mixing among clients with maximum parameter differences to enhance robustness
> against drift. Third, we develop a a progressive personalized fusion strategy
> during model distribution, ensuring a balance between knowledge transfer and
> personalized features. Finally, during the inference phase, we use feature
> similarity to guide the retrieval of the most relevant model chain from the
> tree structure for ensemble decision-making, thereby fully leveraging the
> advantages of hierarchical knowledge. We conducted extensive experiments on two
> publicly available datasets. The results demonstrate that our method
> outperforms other state-of-the-art domain generalization approaches in these
> challenging tasks and achieves better balance in cross-domain performance.

