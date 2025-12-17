---
layout: default
title: Acquisition of interpretable domain information during brain MR image harmonization for content-based image retrieval
---

# Acquisition of interpretable domain information during brain MR image harmonization for content-based image retrieval

**arXiv**: [2510.14535v1](https://arxiv.org/abs/2510.14535) | [PDF](https://arxiv.org/pdf/2510.14535.pdf)

**作者**: Keima Abe, Hayato Muraki, Shuhei Tomoshige, Kenichi Oishi, Hitoshi Iyatomi

---

## 💡 一句话要点

**提出PL-SE-ADA框架以解决脑MR图像领域偏移和可解释性问题**

**关键词**: `脑MR图像` `领域协调` `可解释表示学习` `对抗训练` `图像重建` `疾病分类`

## 📋 核心要点

1. 脑MR图像因扫描器和协议差异存在领域偏移，影响机器学习性能
2. 使用双编码器分离领域不变和特定特征，通过对抗训练和图像重建实现领域协调
3. 在图像重建、疾病分类和领域识别中表现优异，并提供可视化可解释性

## 📄 摘要（原文）

> Medical images like MR scans often show domain shifts across imaging sites
> due to scanner and protocol differences, which degrade machine learning
> performance in tasks such as disease classification. Domain harmonization is
> thus a critical research focus. Recent approaches encode brain images
> $\boldsymbol{x}$ into a low-dimensional latent space $\boldsymbol{z}$, then
> disentangle it into $\boldsymbol{z_u}$ (domain-invariant) and
> $\boldsymbol{z_d}$ (domain-specific), achieving strong results. However, these
> methods often lack interpretability$-$an essential requirement in medical
> applications$-$leaving practical issues unresolved. We propose
> Pseudo-Linear-Style Encoder Adversarial Domain Adaptation (PL-SE-ADA), a
> general framework for domain harmonization and interpretable representation
> learning that preserves disease-relevant information in brain MR images.
> PL-SE-ADA includes two encoders $f_E$ and $f_{SE}$ to extract
> $\boldsymbol{z_u}$ and $\boldsymbol{z_d}$, a decoder to reconstruct the image
> $f_D$, and a domain predictor $g_D$. Beyond adversarial training between the
> encoder and domain predictor, the model learns to reconstruct the input image
> $\boldsymbol{x}$ by summing reconstructions from $\boldsymbol{z_u}$ and
> $\boldsymbol{z_d}$, ensuring both harmonization and informativeness. Compared
> to prior methods, PL-SE-ADA achieves equal or better performance in image
> reconstruction, disease classification, and domain recognition. It also enables
> visualization of both domain-independent brain features and domain-specific
> components, offering high interpretability across the entire framework.

