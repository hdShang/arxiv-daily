---
layout: default
title: HIDISC: A Hyperbolic Framework for Domain Generalization with Generalized Category Discovery
---

# HIDISC: A Hyperbolic Framework for Domain Generalization with Generalized Category Discovery

**arXiv**: [2510.17188v1](https://arxiv.org/abs/2510.17188) | [PDF](https://arxiv.org/pdf/2510.17188.pdf)

**作者**: Vaibhav Rathore, Divyam Gupta, Biplab Banerjee

---

## 💡 一句话要点

**提出HIDISC双曲框架以解决域泛化与广义类别发现问题**

**关键词**: `域泛化` `广义类别发现` `双曲表示学习` `扩散增强` `切线插值` `对比学习`

## 📋 核心要点

1. 核心问题：域泛化与广义类别发现结合，需在未见域中分类已知和未知类别
2. 方法要点：使用双曲表示学习、GPT引导扩散增强和切线空间插值
3. 实验或效果：在PACS等数据集上优于现有方法，实现高效泛化

## 📄 摘要（原文）

> Generalized Category Discovery (GCD) aims to classify test-time samples into
> either seen categories** -- available during training -- or novel ones, without
> relying on label supervision. Most existing GCD methods assume simultaneous
> access to labeled and unlabeled data during training and arising from the same
> domain, limiting applicability in open-world scenarios involving distribution
> shifts. Domain Generalization with GCD (DG-GCD) lifts this constraint by
> requiring models to generalize to unseen domains containing novel categories,
> without accessing targetdomain data during training. The only prior DG-GCD
> method, DG2CD-Net, relies on episodic training with multiple synthetic domains
> and task vector aggregation, incurring high computational cost and error
> accumulation. We propose HIDISC, a hyperbolic representation learning framework
> that achieves domain and category-level generalization without episodic
> simulation. To expose the model to minimal but diverse domain variations, we
> augment the source domain using GPT-guided diffusion, avoiding overfitting
> while maintaining efficiency. To structure the representation space, we
> introduce Tangent CutMix, a curvature-aware interpolation that synthesizes
> pseudo-novel samples in tangent space, preserving manifold consistency. A
> unified loss -- combining penalized Busemann alignment, hybrid hyperbolic
> contrastive regularization, and adaptive outlier repulsion -- **facilitates
> compact, semantically structured embeddings. A learnable curvature parameter
> further adapts the geometry to dataset complexity. HIDISC achieves
> state-of-the-art results on PACS , Office-Home , and DomainNet, consistently
> outperforming the existing Euclidean and hyperbolic (DG)-GCD baselines.

