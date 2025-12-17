---
layout: default
title: SegTrans: Transferable Adversarial Examples for Segmentation Models
---

# SegTrans: Transferable Adversarial Examples for Segmentation Models

**arXiv**: [2510.08922v1](https://arxiv.org/abs/2510.08922) | [PDF](https://arxiv.org/pdf/2510.08922.pdf)

**作者**: Yufei Song, Ziqi Zhou, Qi Lu, Hangtao Zhang, Yifan Hu, Lulu Xue, Shengshan Hu, Minghui Li, Leo Yu Zhang

---

## 💡 一句话要点

**提出SegTrans框架以提升分割模型间对抗样本的可迁移性**

**关键词**: `分割模型` `对抗攻击` `可迁移性` `语义重映射` `扰动优化`

## 📋 核心要点

1. 分割模型在对抗攻击中可迁移性差，源于上下文依赖和特征分布差异
2. 方法将输入划分为局部区域并重映射语义，生成多样增强样本优化扰动
3. 实验在PASCAL VOC和Cityscapes数据集上，显著提高迁移成功率与效率

## 📄 摘要（原文）

> Segmentation models exhibit significant vulnerability to adversarial examples
> in white-box settings, but existing adversarial attack methods often show poor
> transferability across different segmentation models. While some researchers
> have explored transfer-based adversarial attack (i.e., transfer attack) methods
> for segmentation models, the complex contextual dependencies within these
> models and the feature distribution gaps between surrogate and target models
> result in unsatisfactory transfer success rates. To address these issues, we
> propose SegTrans, a novel transfer attack framework that divides the input
> sample into multiple local regions and remaps their semantic information to
> generate diverse enhanced samples. These enhanced samples replace the original
> ones for perturbation optimization, thereby improving the transferability of
> adversarial examples across different segmentation models. Unlike existing
> methods, SegTrans only retains local semantic information from the original
> input, rather than using global semantic information to optimize perturbations.
> Extensive experiments on two benchmark datasets, PASCAL VOC and Cityscapes,
> four different segmentation models, and three backbone networks show that
> SegTrans significantly improves adversarial transfer success rates without
> introducing additional computational overhead. Compared to the current
> state-of-the-art methods, SegTrans achieves an average increase of 8.55% in
> transfer attack success rate and improves computational efficiency by more than
> 100%.

