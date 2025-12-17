---
layout: default
title: MedSapiens: Taking a Pose to Rethink Medical Imaging Landmark Detection
---

# MedSapiens: Taking a Pose to Rethink Medical Imaging Landmark Detection

**arXiv**: [2511.04255v1](https://arxiv.org/abs/2511.04255) | [PDF](https://arxiv.org/pdf/2511.04255.pdf)

**作者**: Marawan Elbatel, Anbang Wang, Keyuan Liu, Kaouther Mouheb, Enrique Almar-Munoz, Lizhuo Lin, Yanqi Yang, Karim Lekadir, Xiaomeng Li

---

## 💡 一句话要点

**提出MedSapiens，将人体姿态基础模型适配于医学影像解剖标志检测**

**关键词**: `医学影像分析` `解剖标志检测` `基础模型适配` `姿态估计` `多数据集预训练` `少样本学习`

## 📋 核心要点

1. 核心问题：医学影像解剖标志检测依赖领域特定模型，未充分利用人体中心基础模型潜力。
2. 方法要点：通过多数据集预训练，将Sapiens模型适配到医学影像，优化空间定位。
3. 实验或效果：在多个数据集上实现SDR最高21.81%提升，并在少样本设置中表现优异。

## 📄 摘要（原文）

> This paper does not introduce a novel architecture; instead, it revisits a
> fundamental yet overlooked baseline: adapting human-centric foundation models
> for anatomical landmark detection in medical imaging. While landmark detection
> has traditionally relied on domain-specific models, the emergence of
> large-scale pre-trained vision models presents new opportunities. In this
> study, we investigate the adaptation of Sapiens, a human-centric foundation
> model designed for pose estimation, to medical imaging through multi-dataset
> pretraining, establishing a new state of the art across multiple datasets. Our
> proposed model, MedSapiens, demonstrates that human-centric foundation models,
> inherently optimized for spatial pose localization, provide strong priors for
> anatomical landmark detection, yet this potential has remained largely
> untapped. We benchmark MedSapiens against existing state-of-the-art models,
> achieving up to 5.26% improvement over generalist models and up to 21.81%
> improvement over specialist models in the average success detection rate (SDR).
> To further assess MedSapiens adaptability to novel downstream tasks with few
> annotations, we evaluate its performance in limited-data settings, achieving
> 2.69% improvement over the few-shot state of the art in SDR. Code and model
> weights are available at https://github.com/xmed-lab/MedSapiens .

