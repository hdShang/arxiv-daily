---
layout: default
title: Bi-Encoder Contrastive Learning for Fingerprint and Iris Biometrics
---

# Bi-Encoder Contrastive Learning for Fingerprint and Iris Biometrics

**arXiv**: [2510.22937v1](https://arxiv.org/abs/2510.22937) | [PDF](https://arxiv.org/pdf/2510.22937.pdf)

**作者**: Matthew So, Judah Goldfeder, Mark Lis, Hod Lipson

---

## 💡 一句话要点

**提出双编码器对比学习以验证指纹和虹膜生物特征相关性**

**关键词**: `双编码器网络` `对比学习` `生物特征验证` `指纹匹配` `虹膜匹配` `跨模态匹配`

## 📋 核心要点

1. 核心问题：测试个体生物特征统计独立性的历史假设
2. 方法要点：使用ResNet-50和Vision Transformer训练双编码器，最小化同个体图像对比损失
3. 实验或效果：虹膜匹配ROC AUC达91%，指纹结果与先前一致，跨模态匹配接近随机

## 📄 摘要（原文）

> There has been a historic assumption that the biometrics of an individual are
> statistically uncorrelated. We test this assumption by training Bi-Encoder
> networks on three verification tasks, including fingerprint-to-fingerprint
> matching, iris-to-iris matching, and cross-modal fingerprint-to-iris matching
> using 274 subjects with $\sim$100k fingerprints and 7k iris images. We trained
> ResNet-50 and Vision Transformer backbones in Bi-Encoder architectures such
> that the contrastive loss between images sampled from the same individual is
> minimized. The iris ResNet architecture reaches 91 ROC AUC score for
> iris-to-iris matching, providing clear evidence that the left and right irises
> of an individual are correlated. Fingerprint models reproduce the positive
> intra-subject suggested by prior work in this space. This is the first work
> attempting to use Vision Transformers for this matching. Cross-modal matching
> rises only slightly above chance, which suggests that more data and a more
> sophisticated pipeline is needed to obtain compelling results. These findings
> continue challenge independence assumptions of biometrics and we plan to extend
> this work to other biometrics in the future. Code available:
> https://github.com/MatthewSo/bio_fingerprints_iris.

