---
layout: default
title: Beyond Real Faces: Synthetic Datasets Can Achieve Reliable Recognition Performance without Privacy Compromise
---

# Beyond Real Faces: Synthetic Datasets Can Achieve Reliable Recognition Performance without Privacy Compromise

**arXiv**: [2510.17372v1](https://arxiv.org/abs/2510.17372) | [PDF](https://arxiv.org/pdf/2510.17372.pdf)

**作者**: Paweł Borsukiewicz, Fadi Boutros, Iyiola E. Olatunji, Charles Beumier, Wendkûuni C. Ouedraogo, Jacques Klein, Tegawendé F. Bissyandé

---

## 💡 一句话要点

**提出合成人脸数据集以解决隐私问题并实现可靠识别性能**

**关键词**: `合成人脸数据` `隐私保护` `人脸识别` `数据集评估` `偏见缓解` `身份分离`

## 📋 核心要点

1. 核心问题：真实人脸数据集收集引发隐私和伦理问题，需隐私保护替代方案。
2. 方法要点：系统评估合成数据集，关注身份泄漏预防、变异性等七项隐私要求。
3. 实验或效果：合成数据集VariFace和VIGFace准确率超95%，优于部分真实数据集。

## 📄 摘要（原文）

> The deployment of facial recognition systems has created an ethical dilemma:
> achieving high accuracy requires massive datasets of real faces collected
> without consent, leading to dataset retractions and potential legal liabilities
> under regulations like GDPR. While synthetic facial data presents a promising
> privacy-preserving alternative, the field lacks comprehensive empirical
> evidence of its viability. This study addresses this critical gap through
> extensive evaluation of synthetic facial recognition datasets. We present a
> systematic literature review identifying 25 synthetic facial recognition
> datasets (2018-2025), combined with rigorous experimental validation. Our
> methodology examines seven key requirements for privacy-preserving synthetic
> data: identity leakage prevention, intra-class variability, identity
> separability, dataset scale, ethical data sourcing, bias mitigation, and
> benchmark reliability. Through experiments involving over 10 million synthetic
> samples, extended by a comparison of results reported on five standard
> benchmarks, we provide the first comprehensive empirical assessment of
> synthetic data's capability to replace real datasets. Best-performing synthetic
> datasets (VariFace, VIGFace) achieve recognition accuracies of 95.67% and
> 94.91% respectively, surpassing established real datasets including
> CASIA-WebFace (94.70%). While those images remain private, publicly available
> alternatives Vec2Face (93.52%) and CemiFace (93.22%) come close behind. Our
> findings reveal that they ensure proper intra-class variability while
> maintaining identity separability. Demographic bias analysis shows that, even
> though synthetic data inherits limited biases, it offers unprecedented control
> for bias mitigation through generation parameters. These results establish
> synthetic facial data as a scientifically viable and ethically imperative
> alternative for facial recognition research.

