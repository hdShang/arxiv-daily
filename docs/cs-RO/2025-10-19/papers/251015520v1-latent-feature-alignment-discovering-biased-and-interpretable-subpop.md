---
layout: default
title: Latent Feature Alignment: Discovering Biased and Interpretable Subpopulations in Face Recognition Models
---

# Latent Feature Alignment: Discovering Biased and Interpretable Subpopulations in Face Recognition Models

**arXiv**: [2510.15520v1](https://arxiv.org/abs/2510.15520) | [PDF](https://arxiv.org/pdf/2510.15520.pdf)

**作者**: Ignacio Serna

---

## 💡 一句话要点

**提出潜在特征对齐方法，以无属性标签方式发现人脸识别模型中的偏见子群。**

**关键词**: `人脸识别` `偏见检测` `潜在特征对齐` `无监督学习` `模型审计`

## 📋 核心要点

1. 人脸识别模型存在系统性偏见，影响特定子群，传统方法依赖昂贵预定义属性。
2. LFA利用潜在方向识别子群，实现语义一致分组和可解释方向发现。
3. 在多个模型和基准测试中，LFA在语义一致性和可解释性上优于k-means和最近邻搜索。

## 📄 摘要（原文）

> Modern face recognition models achieve high overall accuracy but continue to
> exhibit systematic biases that disproportionately affect certain
> subpopulations. Conventional bias evaluation frameworks rely on labeled
> attributes to form subpopulations, which are expensive to obtain and limited to
> predefined categories. We introduce Latent Feature Alignment (LFA), an
> attribute-label-free algorithm that uses latent directions to identify
> subpopulations. This yields two main benefits over standard clustering: (i)
> semantically coherent grouping, where faces sharing common attributes are
> grouped together more reliably than by proximity-based methods, and (ii)
> discovery of interpretable directions, which correspond to semantic attributes
> such as age, ethnicity, or attire. Across four state-of-the-art recognition
> models (ArcFace, CosFace, ElasticFace, PartialFC) and two benchmarks (RFW,
> CelebA), LFA consistently outperforms k-means and nearest-neighbor search in
> intra-group semantic coherence, while uncovering interpretable latent
> directions aligned with demographic and contextual attributes. These results
> position LFA as a practical method for representation auditing of face
> recognition models, enabling practitioners to identify and interpret biased
> subpopulations without predefined attribute annotations.

