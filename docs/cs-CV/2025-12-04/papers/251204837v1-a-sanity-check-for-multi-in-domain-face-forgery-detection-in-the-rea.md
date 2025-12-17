---
layout: default
title: A Sanity Check for Multi-In-Domain Face Forgery Detection in the Real World
---

# A Sanity Check for Multi-In-Domain Face Forgery Detection in the Real World

**arXiv**: [2512.04837v1](https://arxiv.org/abs/2512.04837) | [PDF](https://arxiv.org/pdf/2512.04837.pdf)

**作者**: Jikang Cheng, Renye Yan, Zhiyuan Yan, Yaozhong Gan, Xueyi Zhang, Zhongyuan Wang, Wei Peng, Ling Liang

---

## 💡 一句话要点

**提出DevDet框架以解决多域人脸伪造检测中域差异主导特征空间的问题**

**关键词**: `人脸伪造检测` `多域学习` `特征空间优化` `模型泛化` `真实世界应用`

## 📋 核心要点

1. 现有方法在训练数据有限时难以泛化至完全未见的变化，多域训练虽可行但域差异掩盖真伪差异
2. 提出模型无关框架DevDet，包含FFDev和DAFT，放大真伪差异使其主导特征空间
3. 实验显示在MID-FFD场景下提升真伪预测能力，同时保持对未见数据的泛化能力

## 📄 摘要（原文）

> Existing methods for deepfake detection aim to develop generalizable detectors. Although "generalizable" is the ultimate target once and for all, with limited training forgeries and domains, it appears idealistic to expect generalization that covers entirely unseen variations, especially given the diversity of real-world deepfakes. Therefore, introducing large-scale multi-domain data for training can be feasible and important for real-world applications. However, within such a multi-domain scenario, the differences between multiple domains, rather than the subtle real/fake distinctions, dominate the feature space. As a result, despite detectors being able to relatively separate real and fake within each domain (i.e., high AUC), they struggle with single-image real/fake judgments in domain-unspecified conditions (i.e., low ACC). In this paper, we first define a new research paradigm named Multi-In-Domain Face Forgery Detection (MID-FFD), which includes sufficient volumes of real-fake domains for training. Then, the detector should provide definitive real-fake judgments to the domain-unspecified inputs, which simulate the frame-by-frame independent detection scenario in the real world. Meanwhile, to address the domain-dominant issue, we propose a model-agnostic framework termed DevDet (Developer for Detector) to amplify real/fake differences and make them dominant in the feature space. DevDet consists of a Face Forgery Developer (FFDev) and a Dose-Adaptive detector Fine-Tuning strategy (DAFT). Experiments demonstrate our superiority in predicting real-fake under the MID-FFD scenario while maintaining original generalization ability to unseen data.

