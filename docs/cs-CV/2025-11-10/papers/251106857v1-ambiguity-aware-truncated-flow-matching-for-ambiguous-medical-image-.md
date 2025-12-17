---
layout: default
title: Ambiguity-aware Truncated Flow Matching for Ambiguous Medical Image Segmentation
---

# Ambiguity-aware Truncated Flow Matching for Ambiguous Medical Image Segmentation

**arXiv**: [2511.06857v1](https://arxiv.org/abs/2511.06857) | [PDF](https://arxiv.org/pdf/2511.06857.pdf)

**作者**: Fanding Li, Xiangyu Li, Xianghe Su, Xingyu Qiu, Suyu Dong, Wei Wang, Kuanquan Wang, Gongning Luo, Shuo Li

---

## 💡 一句话要点

**提出ATFM以解决模糊医学图像分割中精度与多样性权衡问题**

**关键词**: `模糊医学图像分割` `截断流匹配` `高斯截断表示` `数据分层推理` `分割流匹配`

## 📋 核心要点

1. 核心问题：模糊医学图像分割中精度与多样性存在固有权衡，现有方法预测保真度和合理性不足
2. 方法要点：引入数据分层推理、高斯截断表示和分割流匹配，分别增强精度、多样性和预测合理性
3. 实验或效果：在LIDC和ISIC3数据集上优于SOTA方法，GED和HM-IoU提升最高达12%和7.3%

## 📄 摘要（原文）

> A simultaneous enhancement of accuracy and diversity of predictions remains a
> challenge in ambiguous medical image segmentation (AMIS) due to the inherent
> trade-offs. While truncated diffusion probabilistic models (TDPMs) hold strong
> potential with a paradigm optimization, existing TDPMs suffer from entangled
> accuracy and diversity of predictions with insufficient fidelity and
> plausibility. To address the aforementioned challenges, we propose
> Ambiguity-aware Truncated Flow Matching (ATFM), which introduces a novel
> inference paradigm and dedicated model components. Firstly, we propose
> Data-Hierarchical Inference, a redefinition of AMIS-specific inference
> paradigm, which enhances accuracy and diversity at data-distribution and
> data-sample level, respectively, for an effective disentanglement. Secondly,
> Gaussian Truncation Representation (GTR) is introduced to enhance both fidelity
> of predictions and reliability of truncation distribution, by explicitly
> modeling it as a Gaussian distribution at $T_{\text{trunc}}$ instead of using
> sampling-based approximations.Thirdly, Segmentation Flow Matching (SFM) is
> proposed to enhance the plausibility of diverse predictions by extending
> semantic-aware flow transformation in Flow Matching (FM). Comprehensive
> evaluations on LIDC and ISIC3 datasets demonstrate that ATFM outperforms SOTA
> methods and simultaneously achieves a more efficient inference. ATFM improves
> GED and HM-IoU by up to $12\%$ and $7.3\%$ compared to advanced methods.

