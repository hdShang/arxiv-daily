---
layout: default
title: Your VAR Model is Secretly an Efficient and Explainable Generative Classifier
---

# Your VAR Model is Secretly an Efficient and Explainable Generative Classifier

**arXiv**: [2510.12060v1](https://arxiv.org/abs/2510.12060) | [PDF](https://arxiv.org/pdf/2510.12060.pdf)

**作者**: Yi-Chung Chen, David I. Inouye, Jing Gao

---

## 💡 一句话要点

**提出基于视觉自回归模型的高效可解释生成分类器，提升分类准确性与推理速度。**

**关键词**: `生成分类器` `视觉自回归模型` `可解释性` `类增量学习` `推理效率`

## 📋 核心要点

1. 扩散模型生成分类器计算成本高，限制可扩展性。
2. 利用视觉自回归模型构建新生成分类器，实现高效推理。
3. 实验显示高准确率、可解释性和抗灾难性遗忘能力。

## 📄 摘要（原文）

> Generative classifiers, which leverage conditional generative models for
> classification, have recently demonstrated desirable properties such as
> robustness to distribution shifts. However, recent progress in this area has
> been largely driven by diffusion-based models, whose substantial computational
> cost severely limits scalability. This exclusive focus on diffusion-based
> methods has also constrained our understanding of generative classifiers. In
> this work, we propose a novel generative classifier built on recent advances in
> visual autoregressive (VAR) modeling, which offers a new perspective for
> studying generative classifiers. To further enhance its performance, we
> introduce the Adaptive VAR Classifier$^+$ (A-VARC$^+$), which achieves a
> superior trade-off between accuracy and inference speed, thereby significantly
> improving practical applicability. Moreover, we show that the VAR-based method
> exhibits fundamentally different properties from diffusion-based methods. In
> particular, due to its tractable likelihood, the VAR-based classifier enables
> visual explainability via token-wise mutual information and demonstrates
> inherent resistance to catastrophic forgetting in class-incremental learning
> tasks.

