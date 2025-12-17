---
layout: default
title: Enhancing CLIP Robustness via Cross-Modality Alignment
---

# Enhancing CLIP Robustness via Cross-Modality Alignment

**arXiv**: [2510.24038v1](https://arxiv.org/abs/2510.24038) | [PDF](https://arxiv.org/pdf/2510.24038.pdf)

**作者**: Xingyu Zhu, Beier Zhu, Shuo Wang, Kesen Zhao, Hanwang Zhang

---

## 💡 一句话要点

**提出COLA框架以解决CLIP在对抗扰动下的跨模态特征失准问题**

**关键词**: `跨模态对齐` `对抗鲁棒性` `最优传输` `零样本分类` `特征投影`

## 📋 核心要点

1. 核心问题：CLIP的图像与文本特征在对抗扰动下严重失准，导致分类性能下降
2. 方法要点：使用最优传输优化跨模态对齐，包括子空间投影和局部结构一致性增强
3. 实验或效果：在14个基准测试中平均提升6.7%对抗鲁棒性，且保持干净样本高精度

## 📄 摘要（原文）

> Vision-language models (VLMs) such as CLIP demonstrate strong generalization
> in zero-shot classification but remain highly vulnerable to adversarial
> perturbations. Existing methods primarily focus on adversarial fine-tuning or
> prompt optimization; they often overlook the gaps in CLIP's encoded features,
> which is shown as the text and image features lie far apart from each other.
> This misalignment is significantly amplified under adversarial perturbations,
> leading to severe degradation in classification performance. To address this
> problem, we propose Cross-modality Alignment, dubbed COLA, an optimal
> transport-based framework that explicitly addresses adversarial misalignment by
> restoring both global image-text alignment and local structural consistency in
> the feature space. (1) COLA first projects adversarial image embeddings onto a
> subspace spanned by class text features, effectively filtering out non-semantic
> distortions while preserving discriminative information. (2) It then models
> images and texts as discrete distributions over multiple augmented views and
> refines their alignment via OT, with the subspace projection seamlessly
> integrated into the cost computation. This design ensures stable cross-modal
> alignment even under adversarial conditions. COLA is training-free and
> compatible with existing fine-tuned models. Extensive evaluations across 14
> zero-shot classification benchmarks demonstrate the effectiveness of COLA,
> especially with an average improvement of 6.7% on ImageNet and its variants
> under PGD adversarial attacks, while maintaining high accuracy on clean
> samples.

